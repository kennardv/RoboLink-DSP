# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:07:31 2015

@author: Kennard
"""

#import RPi.GPIO as GPIO

class GPIOMapper():
    rpi = 0    
    
    def __init__(self, inputChannels, outputChannels):
        #GPIO.setmode(GPIO.BCM)          # set board mode to Broadcom
        
        GPIO.setup(inputPins, GPIO.IN)
        GPIO.setup(outputPins, GPIO.OUT)
        
    def readPin(self, channel):
        return GPIO.input(channel)
        
    def setPin(self, channel, state):
        GPIO.output(channel, state)
        
    def setPins(self, channels, state):
        GPIO.output(channels, state)
        
    def __del__(self):
        GPIO.cleanup()
            

mapper = GPIOMapper([2, 5, 8], [1, 3, 12])
        