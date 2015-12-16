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

def set_row1(data):
    data = int(data)
    print bin(data)
    if data == 1:
        data = (~1 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data == 2 :
        data = (~3 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data == 3 :
        data = (~7 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data == 4 :
        data = (~15 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data >= 5 :
        data = (~31 & 0xE0)
        bus.write_byte_data(addressU1,0x12,data)

def set_row2(data):
    data = int(data)
    print bin(data)
    if data == 1:
        data = (~32 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data == 2 :
        data = (~96 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data == 3 :
        data = (~224 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data == 4 :
        data = (~1 & 0xFF)
        bus.write_byte_data(addressU1,0x13,data)
        data = (~224 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)
    elif data >= 5 :
        data = (~3 & 0xFF)
        bus.write_byte_data(addressU1,0x13,data)
        data = (~224 & 0xFF)
        bus.write_byte_data(addressU1,0x12,data)

def set_row3(data):
    data = int(data)
    print bin(data)
    if data == 1:
        data = (~4 & 0xFF)
        bus.write_byte_data(addressU1,0x13,data)
    elif data == 2 :
        data = (~12 & 0xFF)
        bus.write_byte_data(addressU1,0x13,data)
    elif data == 3 :
        data = (~28 & 0xFF)
        bus.write_byte_data(addressU1,0x13,data)
    elif data == 4 :
        data = (~60 & 0xFF)
        bus.write_byte_data(addressU1,0x13,data)
    elif data >= 5 :
        data = (~124 & 0xFF)
        bus.write_byte_data(addressU1,0x13,data)

def set_row4(data):
    data = int(data)
    print bin(data)
    if data == 1:
        data = (~1 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data == 2 :
        data = (~3 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data == 3 :
        data = (~7 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data == 4 :
        data = (~15 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data >= 5 :
        data = (~31 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)

def set_row5(data):
    data = int(data)
    print bin(data)
    if data == 1:
        data = (~32 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data == 2 :
        data = (~96 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data == 3 :
        data = (~224 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data == 4 :
        data = (~1 & 0xFF)
        bus.write_byte_data(addressU2,0x13,data)
        data = (~224 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)
    elif data >= 5 :
        data = (~3 & 0xFF)
        bus.write_byte_data(addressU2,0x13,data)
        data = (~224 & 0xFF)
        bus.write_byte_data(addressU2,0x12,data)

def set_row6(data):
    data = int(data)
    print bin(data)
    if data == 1:
        data = (~4 & 0xFF)
        bus.write_byte_data(addressU2,0x13,data)
    elif data == 2 :
        data = (~12 & 0xFF)
        bus.write_byte_data(addressU2,0x13,data)
    elif data == 3 :
        data = (~28 & 0xFF)
        bus.write_byte_data(addressU2,0x13,data)
    elif data == 4 :
        data = (~60 & 0xFF)
        bus.write_byte_data(addressU2,0x13,data)
    elif data >= 5 :
        data = (~124 & 0xFF)
        bus.write_byte_data(addressU2,0x13,data)

delay = 0.1

exit = False
while not exit:
    r = raw_input('Enter something, "q" to quit"')
    print(r)
    row1 = r
    bus.write_byte_data(addressU1,0x12,0xFF)
    bus.write_byte_data(addressU2,0x12,0xFF)
    bus.write_byte_data(addressU1,0x13,0xFF)
    bus.write_byte_data(addressU2,0x13,0xFF)
    time.sleep(delay)
    
    set_row1(r)
    set_row2(r)
    set_row3(r)
    set_row4(r)
    set_row5(r)
    set_row6(r)
    
    time.sleep(delay)

    if r=='q':
        bus.write_byte_data(addressU1,0x12,0xFF)
        bus.write_byte_data(addressU2,0x12,0xFF)
        bus.write_byte_data(addressU1,0x13,0xFF)
        bus.write_byte_data(addressU2,0x13,0xFF)
        exit=True
if __name__ == "__main__":
   main()
