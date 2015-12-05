# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:27:41 2015

@author: Kennard
"""

import sounddevice as sd
from threading import Thread
from queue import Queue

class MusicPlayer(Thread):
    def __init__(self, q, minimumblocks=20):
        self.q = q
        self.minblocks = minimumblocks
        Thread.__init__(self)
        
    def run(self):
        if not self.q.empty() and self.q.qsize() > self.minblocks:
            # get removes and returns item from the queue
            sd.play(self.q.get())
        
        # Optional: example
        # Get data and event
        #data, evt = self.q.get()
        
        # Indicate completion
        #evt.set()