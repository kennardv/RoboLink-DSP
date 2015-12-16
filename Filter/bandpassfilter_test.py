# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:49:58 2015

@author: Kennard
"""

from scipy.signal import butter, lfilter
import numpy as np
import math
import time

class BandPassFilter():
    i = 0
    
    def __init__(self, lowcut=200.0, highcut=1000.0, fs=5000.0, order=5):
        """This class takes in a complete signal, splits it and
        puts filtered chunks in a shared queue object
        """
        self.lowcut = lowcut
        self.highcut = highcut
        self.fs = fs
        self.order = order
        
    def run(self):
        """ Iterate over the blocks of data.
        Every block is filtered and added to the shared queue        
        """
        while self.i < self.chunks:
            t0 = time.clock()
            filtered = self.butter_bandpass_filter(self.data[self.i])
            self.q.put(filtered)
            
            self.i = self.i + 1
            
            print("Filtering chunk time: ", time.clock()-t0)

            
            time.sleep(self.sleeptime)
    
    
    def butter_bandpass_filter(self, data, order=5):
        """ Returns an array of filtered values.
        Return type: numpy.int16"""
        b, a = self.butter_bandpass(order)
        y = lfilter(b, a, data)
        y = [np.int32(i) for i in y]
        #print(type(y[2]))
        return y
        
        
    def butter_bandpass(self, order=5):
        nyq = 0.5 * self.fs
        low = self.lowcut / nyq
        high = self.highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a
        
    def splitData(self, data, chunks):
        return np.array_split(data, chunks)
        
    
    
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
from scipy import arange
import wave

# Sample rate and desired cutoff frequencies (in Hz).
fs = 5000.0
lowcut = 500.0
highcut = 1250.0
order = 5

bpf = BandPassFilter(lowcut, highcut, fs, order)

# Plot the frequency response for a few different orders.
plt.figure(1, figsize=(12,8))
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

"""
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

wf = wave.open('../mario_mono.wav', 'rb')
signal = wf.readframes(1000)
signal = np.fromstring(signal, dtype=np.int16)
x = signal[0::2]
right = signal[1::2]

T = wf.getsampwidth()
n = len(right)
k = arange(n)

wf.close()

y = bpf.butter_bandpass_filter(x, order)

plt.figure(2, figsize=(12, 8))
plt.clf()
plt.plot(k, x, label='Noisy signal')
plt.plot(k, y, label='Filtered signal')
plt.xlabel('nr of samples (n)')
plt.hlines([-a, a], 0, T, linestyles='--')
plt.grid(True)
plt.axis('tight')
plt.legend(loc='upper left')

plt.show()