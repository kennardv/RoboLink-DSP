# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:11:51 2015

@author: Kennard
"""

import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
from Filter import bandpassfilter

# wav file
wf = wave.open('Alarm01.wav', 'rb')
# read all frames
y = wf.readframes(-1)
y = np.fromstring(y, dtype=np.int16)
# get left channel only
y = y[0::1]

# Sample rate and desired cutoff frequencies (in Hz).
fs = wf.getframerate()
lowcut = 2000
highcut = 9000
order = 5

# get bandpassfilter obj
bpf = bandpassfilter.BandPassFilter(lowcut, highcut, fs, order)


# Plot the frequency response for a few different orders.
plt.figure(1, (8, 5))
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


# Filter the sound signal.
yfiltered = bpf.butter_bandpass_filter(y, order)

T = len(y) / fs
nsamples = T * fs
t = np.linspace(0, T, nsamples, endpoint=False)

# Plot in time domain
plt.figure(2, (8, 5))
plt.clf()
plt.plot(t, y, 'b' ,label='Original signal')
plt.plot(t, yfiltered, 'r', label='Filtered signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.hlines([-a, a], 0, T, linestyles='--')
plt.grid(True)
plt.legend(loc='best')

plt.show()


# Power spectrum calculation
p = 20*np.log10(np.abs(np.fft.rfft(y)))
f = np.linspace(0, fs/2, len(p))
pfiltered = 20*np.log10(np.abs(np.fft.rfft(y)))
ffiltered = np.linspace(0, fs/2, len(p))

# Plot power spectrum
plt.figure(3, (8, 5))
plt.clf()
plt.plot(f, p, 'b-', label='Original signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.grid(True)
plt.legend(loc='best')

plt.show()

plt.figure(4, (8, 5))
plt.clf()
plt.plot(ffiltered, pfiltered, 'r-', label='Filtered signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.grid(True)
plt.legend(loc='best')

plt.show()