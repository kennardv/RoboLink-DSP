# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:34:56 2015

@author: Kennard
"""

import serial

class SerialTransceiver:
    
    def __init__(self, portname, baudrate=115200, timeout=3.0):
        self.port = serial.Serial(portname, baudrate, timeout)
        #self.port.close()
    
    def receive(self, length):
        return self.port.read(length)
        
    def send(self, data):
        self.port.write(data)