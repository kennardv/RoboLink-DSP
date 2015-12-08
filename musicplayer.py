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
    
    def __init__(self, q, minimumblocks=10):
        self.q = q
        self.minblocks = minimumblocks
        Thread.__init__(self)
        
    def run(self):
        while self.i < 119:
            print("Musicplayer thread")
            # qsize() is unreliable
            if not self.q.empty() and self.q.qsize() > self.minblocks:
                sd.play(self.q.get())
                self.i = self.i + 1

            time.sleep(0.5)
        
        # Optional: example
        # Get data and event
        #data, evt = self.q.get()
        
        # Indicate completion
        #evt.set()
