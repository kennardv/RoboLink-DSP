# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:02:26 2015

@author: Kennard
"""

import numpy as np
import sounddevice as sd
import wave, math
from scipy import arange
from multiprocessing import Queue

from UART import serialtransceiver
import musicplayer

# Custom plotting class
import plotter

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

chunksize = 1024
Fs = 8000

# Create the shared queues: qs = sound | qc = commands
qs = Queue()
qc = Queue()
# get serial transceiver thread obj
sr = serialtransceiver.SerialReceiver(qs, qc, chunksize, '/dev/ttyAMA0', baudrate=115200)
# get musicplayer thread obj
mp = musicplayer.MusicPlayer(qs, Fs)

sr.start()
mp.start()


# Plot the total received signal
#plotter.plotSignalAndSpectrum(yRecvTotal, Fs, 'Filtered signal')
