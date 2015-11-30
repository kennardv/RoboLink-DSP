from scipy.signal import butter, lfilter

class BandPassFilter:
    def __init__(self, lowcut=200.0, highcut=1000.0, fs=5000.0, order=5):
        self.lowcut = lowcut
        self.highcut = highcut
        self.fs = fs
        self.order = order


    def butter_bandpass(self, order=5):
        nyq = 0.5 * self.fs
        low = self.lowcut / nyq
        high = self.highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a
    
    
    def butter_bandpass_filter(self, data, order=5):
        b, a = self.butter_bandpass(order)
        y = lfilter(b, a, data)
        return y
        
    def run(self):
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