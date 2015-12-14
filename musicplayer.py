# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:27:41 2015

@author: Kennard
"""

import sounddevice as sd
from threading import Thread
from multiprocessing import Queue
import time

class MusicPlayer(Thread):
    i = 0
    
    def __init__(self, q, Fs, minimumblocks=10, sleeptime=0.1):
        self.q = q
        self.Fs = Fs
        self.sleeptime = sleeptime
        self.minblocks = minimumblocks
        
        Thread.__init__(self)
        
    def run(self):
        while self.i < 110:
            # qsize() is unreliable
            if not self.q.empty() and self.q.qsize() > self.minblocks:
                # Get all values from all chunks and put in a list
                data = []
                n = 0
                for n in range(self.minblocks):
                    # get minblocks amount of chunks
                    tmp = self.q.get()

                    n = n + 1

                    m = 0
                    for m in range(len(tmp)):
                        # append all values in chunk to data list
                        data.append(tmp[m])
                        m = m + 1

                    self.i = self.i + 1

                print("Musicplayer: Playing data with length: ", len(data))
                sd.play(data)

            time.sleep(self.sleeptime)
        
        # Optional: example
        # Get data and event
        #data, evt = self.q.get()
        
        # Indicate completion
        #evt.set()
