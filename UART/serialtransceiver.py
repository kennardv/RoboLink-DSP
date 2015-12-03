# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:34:56 2015

@author: Kennard
"""

import serial
from time import sleep

class SerialTransceiver:
    
    def __init__(self, portname, baudrate=115200, timeout=1.0):
        self.port = serial.Serial(portname,
                                  baudrate,
                                  parity = serial.PARITY_NONE,
                                  stopbits = serial.STOPBITS_ONE,
                                  bytesize = serial.EIGHTBITS,
                                  timeout=timeout
                                  )
        self.port.open()
    
    def receive(self, length):
        return self.port.read(length)
        
    def send(self, data):
        databytes = data.tobytes()
        i = 0
        for i in range(len(databytes)):
            bytetosend = hex(databytes[i])
            #print("Sending: ", bytetosend)
            bytetosend = int(bytetosend, 16)
            self.port.write(bytetosend)
        
    def __del__(self):
        self.port.close()