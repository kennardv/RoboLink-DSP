# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:13:21 2015

@author: Kennard
"""

import matplotlib.pyplot as plt
from scipy import fft, arange, signal
from numpy import pi, sqrt, linspace
from Filter import bandpassfilter

def plot_freqz_filter(Fs, lowcut, highcut, order=5):
    bpf = bandpassfilter.BandPassFilter(lowcut, highcut, Fs, order)
    
    # Plot the frequency response for a few different orders.
    plt.figure(1, (8, 5))
    for order in [3, 6, 9]:
        b, a = bpf.butter_bandpass(order)
        w, h = signal.freqz(b, a, worN=2000)
        plt.plot((Fs * 0.5 / pi) * w, abs(h), label="order = %d" % order)
    
    plt.plot([0, 0.5 * Fs], [sqrt(0.5), sqrt(0.5)], '--', label='sqrt(0.5)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    
def plotSignalAndSpectrum(y, Fs, title):
    """ Signal plot """
    n = len(y)              # Number of frames
    k = arange(n)           # Evenly spaced values within interval
    T = float(n) / Fs       # Duration
    t = linspace(0, T, n, endpoint=False)
    
    plt.figure()
    plt.suptitle(title)
    plt.subplot(211)
    plt.plot(t, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    
    """ Single-Sided Amplitude Spectrum of y(t) """
    frq = k/T                   # two sides frequency range
    frq = frq[range(n//2)]      # one side frequency range
    
    Y = fft(y)/n                # fft computing and normalization
    Y = Y[range(n//2)]
    
    plt.subplot(212)
    plt.plot(frq,abs(Y),'r')    # plotting the spectrum
    plt.xlabel('Freq (Hz)')
    plt.ylabel('|Y(freq)|')