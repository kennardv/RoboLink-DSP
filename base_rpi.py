# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:11:51 2015

@author: Kennard
"""

import wave
import numpy as np
from scipy import arange
import math
from queue import Queue

#import sounddevice as sd

from Filter import bandpassfilter
from UART import serialtransceiver

# Custom plotting class
import plotter

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# WAV file
wf = wave.open('Alarm01.wav', 'rb')
y = np.fromstring(wf.readframes(-1), dtype=np.int16)        # read all frames
y = y[0::2]                                                 # get left channel only

Fs = wf.getframerate()                                      # Sampling rate
"""
n = wf.getnframes()                                         # Number of frames
k = arange(n)                                               # Evenly spaced values within interval
T = n / Fs                                                  # Duration
sw = wf.getsampwidth()
"""

chunksize = 1024                                                # Chunk size
#chunks = math.ceil(n/chunksize)                                 # Number of chunks


wf.close()


#plotter.plotSignalAndSpectrum(y, Fs, 'Original signal')    # Plot original signal before splitting in chunks
#y = np.array_split(y, chunks)                               # Split signal in chunks

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Shared queue object
q = Queue()

# Filter
lowcut = 200
highcut = 2000
order = 3                   # 3 is faster

# get bandpassfilter obj
bpf = bandpassfilter.BandPassFilter(q, y, chunksize, lowcut, highcut, Fs, order)

# Plot of various filter orders
#plotter.plot_freqz_filter(Fs, lowcut, highcut, order)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# get serial transceiver obj
ss = serialtransceiver.SerialSender(q, 'COM255', 9600)

bpf.start()
ss.start()


"""
yFiltTotal = np.array([], dtype=np.int16)
i = 0
while i < chunks:
    # Filter the sound signal.
    yFilt = bpf.butter_bandpass_filter(y[i], order)
    yFiltTotal = np.append(yFiltTotal, yFilt)
    
    # Send filtered chunk of signal via serial port
    stc.send(yFilt)
    # Play filtered chunk of signal via jack
    #sd.play(yFilt)
    #sd.wait()
    
    # Plot original signal
    #plotter.plotSignalAndSpectrum(y[i], Fs, 'Original signal')
    
    # Plot filtered signal
    #plotter.plotSignalAndSpectrum(yFilt, Fs, 'Filtered signal')
    
    i = i + 1
"""

# Plot the total filtered signal to check if append works correctly
#plotter.plotSignalAndSpectrum(yFiltTotal, Fs, 'Filtered signal')