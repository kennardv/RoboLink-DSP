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
        self.port.flushInput()
        
        Thread.__init__(self)
        
    def run(self):
        while not self.exitFlag:
            # Custom readline function
            # List with values as strings
            #t1 = time.clock()
            arr = self._readline(1000)
            #print("Time spent reading + decoding: ", time.clock()-t1)
            #t2 = time.clock()
            line = ''
            for i in range(len(arr)):
                line = arr[i]
                try:
                    # Parse to a float
                    val = np.int32(line)
                    self.data = np.append(self.data, val)
                except ValueError:
                    print("Not a float!", line)
            #print("Time spent parsing: ", time.clock()-t2)
            
            if len(self.data) >= self.chunksize:
                # Add data array to queue
                self.qs.put(self.data)
                
                print("Size queue: ", self.qs.qsize())
                print("Length data: ", len(self.data))
                
                # Clear array
                self.data = np.array([])

                if not self.port.inWaiting():                    
                    # Wait
                    time.sleep(0.05)
            
            # Optional: example
            #evt = Event()
            #self.qs.put(data, evt)
            
            # Wait for consumer to process the item
            #evt.wait()
            
    
    def readlineSingleByte(self):
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
        
    
    def _readline(self, length=100):
        """Custom serial readline function.
        Data is read from the serial port until an end-of-line character is found.
        The received values are returned as an array of strings.        
        """
        valarr = []
        while True:
            try:
                # Read from serial port
                c = self.port.read(length)
                if c:
                    # Append to buffer
                    self.buffer += c
                    
                    i = 0
                    while i < len(self.buffer):
                        # From i to i+length of eol
                        if self.buffer[i:i+self.leneol] == self.eol:
                            # Get value from line
                            val = self.buffer[:i]       # Bytearray
                            val = bytes(val)            # To string
                            
                            # Add found val to list
                            valarr.append(val)
                            
                            # Cut off just found value + eol from buffer
                            self.buffer = self.buffer[i+self.leneol:]
                            i = 0
                        
                        i += 1
                    
                    # Break when buffer is empty
                    break
                        
                else:
                    break
            except serial.SerialException:
                print("Nothing in buffer")

        return valarr
        
        
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
            t0 = time.clock()
            #if not self.q.empty():
            data = self.q.get()

            #t1 = time.clock()
            msgparts = []
            i = 0
            for i in range(len(data)):
                val = data[i]
                line = str(val)
                line = line.encode()
                msgparts.append(line + self.eol)
                
            byteline = b"".join(msgparts)
            #print("Time spent converting + joining: ", time.clock()-t1)
            #t2 = time.clock()
            self.port.write(byteline)
            #print("Time spent writing to port: ", time.clock()-t2)
                
            print("Total time spent sending 1 chunk: ", time.clock()-t0)
            time.sleep(0.05)
