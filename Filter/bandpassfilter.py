from scipy.signal import butter, lfilter
import numpy as np
import math
from threading import Thread, Event
from multiprocessing import Queue
import time

class BandPassFilter(Thread):
    i = 0
    
    def __init__(self, q, data, chunksize=1024, lowcut=200.0, highcut=1000.0, fs=5000.0, order=5, sleeptime=0.2):
        """This class takes in a complete signal, splits it and
        puts filtered chunks in a shared queue object
        """        
        # Shared queue object        
        self.q = q
        
        # Split data in chunks
        n = len(data)
        self.chunks = math.ceil(n/chunksize)
        self.data = self.splitData(data, self.chunks)
        
        
        self.lowcut = lowcut
        self.highcut = highcut
        self.fs = fs
        self.order = order
        
        # Get filter coefficients
        self.b, self.a = self.butter_bandpass(order)

        self.sleeptime = sleeptime
        Thread.__init__(self)
        
    def run(self):
        """ Iterate over the blocks of data.
        Every block is filtered and added to the shared queue        
        """
        while self.i < self.chunks:
            filtered = self.butter_bandpass_filter(self.data[self.i])
            self.q.put(filtered)
            
            self.i = self.i + 1
            print("Filtering chunk nr: ", self.i)
            
            # RESET
            """if self.i >= self.chunks:
                self.i = 0
            """
            
            time.sleep(self.sleeptime)
    
    
    def butter_bandpass_filter(self, data, order=5):
        """ Returns an array of filtered values"""
        #b, a = self.butter_bandpass(order)
        y = lfilter(self.b, self.a, data)
        return y
        
        
    def butter_bandpass(self, order=5):
        nyq = 0.5 * self.fs
        low = self.lowcut / nyq
        high = self.highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a
        
    def splitData(self, data, chunks):
        return np.array_split(data, chunks)
        
    
    
    def show(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.signal import freqz
        
        # Sample rate and desired cutoff frequencies (in Hz).
        fs = 5000.0
        lowcut = 500.0
        highcut = 1250.0
        order = 5
        
        bpf = BandPassFilter(lowcut, highcut, fs, order)
        
        # Plot the frequency response for a few different orders.
        plt.figure(1)
        plt.clf()
        for order in [3, 6, 9]:
            b, a = bpf.butter_bandpass(order)
            w, h = freqz(b, a, worN=2000)
            plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)
        
        plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)], '--', label='sqrt(0.5)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.legend(loc='best')
        
        
        # Filter a noisy signal.
        T = 0.05
        nsamples = T * fs
        t = np.linspace(0, T, nsamples, endpoint=False)
        a = 0.02
        f0 = 600.0
        x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
        x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
        x += a * np.cos(2 * np.pi * f0 * t + .11)
        x += 0.03 * np.cos(2 * np.pi * 2000 * t)
        
        """
        wf = wave.open('../Alarm01.wav', 'rb')
        signal = wf.readframes(1024)
        signal = np.fromstring(signal, dtype=np.int16)
        x = signal[0::2]
        right = signal[1::2]
        """
        
        y = bpf.butter_bandpass_filter(x, order)
        
        plt.figure(2)
        plt.clf()
        plt.plot(t, x, label='Noisy signal')
        plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
        plt.xlabel('time (seconds)')
        plt.hlines([-a, a], 0, T, linestyles='--')
        plt.grid(True)
        plt.axis('tight')
        plt.legend(loc='upper left')
        
        plt.show()
