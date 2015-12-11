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
    data = np.array([])
    
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
        
        Thread.__init__(self)
        
    def run(self):
        while True:
            rcv = self.port.readline()
            try:
                val = np.float64(rcv)
                self.data = np.append(self.data, val)
            except ValueError:
                print("Not a float!")
                
            
            if len(self.data) >= self.readlength:
                # Add data array to queue
                self.qs.put(self.data)
                
                # Clear array
                self.data = np.array([])
                
                time.sleep(0.3)
            
            # Optional: example
            #evt = Event()
            #self.qs.put(data, evt)
            
            # Wait for consumer to process the item
            #evt.wait()
        
        
class SerialSender(Thread):
    exitFlag = 0
    i = 0
        
    def __init__(self, q, portname, readlength, baudrate=115200, timeout=1.0):
        self.q = q
        self.readlength = readlength
        self.port = serial.Serial(portname,
                                  baudrate,
                                  parity = serial.PARITY_NONE,
                                  stopbits = serial.STOPBITS_ONE,
                                  bytesize = serial.EIGHTBITS,
                                  timeout=timeout,
                                  xonxoff = False
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
                print(val)
                val = str(val) + "\n"
                self.port.write(val.encode())
                
            time.sleep(0.5)
                
            
            """i = 0
            for i in range(len(data)):
                val = data[i]
                val = str(val)
                print(val)
                val = val.encode()
                self.port.write(val)
                time.sleep(0.5)"""
            
            """data = str(data)
            data = data.encode()
            numOfBytes = self.port.write(data)
            print(numOfBytes)
            
            time.sleep(1)"""
                
            #self.exitFlag = 1
        
    
    # WINDOWS
    #def __del__(self):
        #self.port.close()
