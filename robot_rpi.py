# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:02:26 2015

@author: Kennard
"""

import wave
import numpy as np

from UART import serialtransceiver

# Custom plotting class
import plotter

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

chunksize = 1024
Fs = 22050

# get serial transceiver obj
stc = serialtransceiver.SerialTransceiver('/dev/ttyAMA0', 115200)


yRecvTotal = np.array([], dtype=np.int16)
i = 0
while 1:
    # Receive filtered chunk of signal via serial port
    yRecv = stc.receive(chunksize)
    yRecvTotal = np.append(yRecvTotal, yRecv)
    
    print(yRecv)




# Plot the total received signal
#plotter.plotSignalAndSpectrum(yRecvTotal, Fs, 'Filtered signal')