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
    # Specify end of line char
    eol = b'\r'
    leneol = len(eol)
    
    exitFlag = 0
    
    # Array to hold incoming values
    data = np.array([])
    buffer = bytearray()
    
    
    def __init__(self, qs, qc, chunksize, portname, baudrate=115200, timeout=1):
        """Constantly polls the serial port for data and adds it to the queue object"""        
        self.qs = qs
        self.qc = qc
        self.chunksize = chunksize
        self.port = serial.Serial(portname,
                                  baudrate,
                                  parity = serial.PARITY_NONE,
                                  stopbits = serial.STOPBITS_ONE,
                                  bytesize = serial.EIGHTBITS,
                                  timeout=timeout
                                  )
        
        Thread.__init__(self)
        
    def run(self):
        while not self.exitFlag:
            # Custom readline function
            arr = self.__readline()
            
            line = ''
            for i in range(len(arr)):
                line = arr[i].decode()
                try:
                    # Parse to a float
                    val = np.float64(line)
                    self.data = np.append(self.data, val)
                    
                    #print("Added: ", type(val))                
                    #print(self.data)
                except ValueError:
                    print("Not a float!", line)
            
            
            if len(self.data) >= self.chunksize:
                # Add data array to queue
                self.qs.put(self.data)
                
                print("Size queue: ", self.qs.qsize())
                print("Length data: ", len(self.data))
                print(self.data)
                
                # Clear array
                self.data = np.array([])
                
                time.sleep(0.3)
            
            # Optional: example
            #evt = Event()
            #self.qs.put(data, evt)
            
            # Wait for consumer to process the item
            #evt.wait()
            
    
    def _readline(self):
        """Custom serial readline function.
        Data is read from the serial port until an end-of-line character is found.
        The received string is returned in encoded form.        
        """
        line = bytearray()
        while True:
            c = self.port.read(1)
            if c:
                line += c
                if line[-self.leneol:] == self.eol:
                    # Cut off eol char
                    line = line[:-self.leneol]
                    break
            else:
                break
        return bytes(line)
        
    
    def __readline(self):
        """Custom serial readline function.
        Data is read from the serial port until an end-of-line character is found.
        The received string is returned in encoded form.        
        """
        valarr = []
        while True:
            # Read from serial port
            c = self.port.read(100)
            if c:
                self.buffer += c
                
                i = 0
                while i < len(self.buffer):
                    # From i to i+length of eol
                    if self.buffer[i:i+self.leneol] == self.eol:
                        # Get value from line
                        val = self.buffer[:i]
                        # Add found val to list
                        valarr.append(val)
                        
                        # Cut off just found value + eol
                        self.buffer = self.buffer[i+self.leneol:]
                        i = 0
                    
                    i += 1
                    
            else:
                break
            
        
        return bytes(valarr)
        
        
class SerialSender(Thread):
    # Specify end of line char
    eol = b'\r'
    leneol = len(eol)
    
    exitFlag = 0
        
    def __init__(self, q, chunksize, portname, baudrate=115200, timeout=1.0):        
        self.q = q
        self.chunksize = chunksize
        self.port = serial.Serial(portname,
                                  baudrate,
                                  parity = serial.PARITY_NONE,
                                  stopbits = serial.STOPBITS_ONE,
                                  bytesize = serial.EIGHTBITS,
                                  timeout=timeout
                                  )
        # WINDOWS        
        #self.port.open()
        Thread.__init__(self)
        
        
    def run(self):
        while not self.exitFlag:
            #if not self.q.empty():
            data = self.q.get()

            i = 0
            for i in range(len(data)):
                val = data[i]
                line = str(val)
                byteline = line.encode() + self.eol
                self.port.write(byteline)
                
            time.sleep(0.5)