# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:05:57 2015

@author: Kennard
"""

import serial
import numpy as np
from array import array
from threading import Thread, Event
from multiprocessing import Queue
import time

class SerialReceiver(Thread):
    
    def __init__(self, qs, qc, portname, readlength, baudrate=115200, timeout=1.0):
        """Constantly polls the serial port for data and adds it to the queue object"""        
        self.qs = qs
        self.qc = qc
        self.readlength = readlength
        self.port = serial.Serial(portname,
                                  baudrate,
                                  parity = serial.PARITY_NONE,
                                  stopbits = serial.STOPBITS_ONE,
                                  bytesize = serial.EIGHTBITS,
                                  timeout=timeout
                                  )
        self.port.open()
        Thread.__init__(self)
        
    def __del__(self):
        self.port.close()
        
    def run(self):
        data = self.port.read(self.readlength)
        
        # Sender converted to bytearray so convert back        
        data = array('i', data)
        # Create numpy array from data
        data = np.fromstring(data, dtype=np.int16)
        #data = map(int, data)
        
        # Add received data
        self.qs.put(data)
        
        # Optional: example
        #evt = Event()
        #self.qs.put(data, evt)
        
        # Wait for consumer to process the item
        #evt.wait()
        
        
class SerialSender(Thread):
    
    def __init__(self, q, portname, readlength, baudrate=115200, timeout=1.0):
        self.q = q
        self.readlength = readlength
        self.port = serial.Serial(portname,
                                  baudrate,
                                  parity = serial.PARITY_NONE,
                                  stopbits = serial.STOPBITS_ONE,
                                  bytesize = serial.EIGHTBITS,
                                  timeout=timeout
                                  )
        self.port.open()
        Thread.__init__(self)
        
        
    def run(self):
        if not self.q.empty():
            # Get an array of values from the queue and convert to bytes
            data = self.q.get()
            databytes = array('B', data)    # faster than bytearray
            
            # Iterate over array, convert to hex and send
            i = 0
            for i in range(len(databytes)):
                bytetosend = hex(databytes[i])
                #print("Sending: ", bytetosend)
                self.port.write(bytetosend)
                
        time.sleep(0.5)
        
        
    def __del__(self):
        self.port.close()
