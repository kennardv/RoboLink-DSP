#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# By Nathan Chantrell http://nathan.chantrell.net
# GNU GPL V3 

# SK Pang Electronics June 2012

import smbus
import sys
import getopt
import time 
bus = smbus.SMBus(1)

addressU1 = 0x20 # I2C address of MCP23017 1st driver
addressU2 = 0x24 # I2C address of MCP23017 2nd driver
bus.write_byte_data(0x20,0x00,0x00) # Set all of 1st driver bank A to outputs 
bus.write_byte_data(0x20,0x01,0x00) # Set all of 1st driver bank B to outputs 
bus.write_byte_data(0x24,0x00,0x00) # Set all of 2nd driver bank A to outputs 
bus.write_byte_data(0x24,0x01,0x00) # Set all of 2nd driver bank B to outputs 



def set_led(data,bank):
  data = (~data & 0xFF)
  if bank == 0:
   bus.write_byte_data(addressU1,0x12,data)
  elif bank == 1:
   bus.write_byte_data(addressU1,0x13,data)
  elif bank == 2:
   bus.write_byte_data(addressU2,0x12,data)
  else:
   bus.write_byte_data(addressU2,0x13,data)
  return

# Handle the command line arguments
def main():
   a = 0
delay = 0.1   
while True:

# Move led left  
   for x in range(0,8):
     a = 1 << x
     set_led(a,0)
     time.sleep(delay)
   set_led(0,0)

   for x in range(0,8):
     a = 1 << x
     set_led(a,1)
     time.sleep(delay)
   set_led(0,1)  

   for x in range(0,8):
     a = 1 << x
     set_led(a,2)
     time.sleep(delay)
   set_led(0,2)

   for x in range(0,8):
     a = 1 << x
     set_led(a,3)
     time.sleep(delay)
   set_led(0,3)  
 
# Move led right 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,3)
     time.sleep(delay)
   set_led(0,3)
 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,2)
     time.sleep(delay)
   set_led(0,2)

   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,1)
     time.sleep(delay)
   set_led(0,1)
 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,0)
     time.sleep(delay)
   set_led(0,0)
   
  
if __name__ == "__main__":
   main()
