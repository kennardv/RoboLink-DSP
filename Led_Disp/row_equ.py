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

def set_row1(data, data12A1):
    data = int(data)
    
    if data == 1:
        data12A1 = (~16 & data12A1 & 0xFF)
        print bin(data12A1)
    #bus.write_byte_data(addressU1,0x12,data)
    elif data == 2 :
        data12A1 = (~24 & data12A1 & 0xFF)
        print bin(data12A1)
    #bus.write_byte_data(addressU1,0x12,data)
    elif data == 3 :
        data12A1 = (~28 & data12A1 & 0xFF)
        print bin(data12A1)
    #bus.write_byte_data(addressU1,0x12,data)
    elif data == 4 :
        data12A1 = (~30 & data12A1 & 0xFF)
        print bin(data12A1)
    #bus.write_byte_data(addressU1,0x12,data)
    elif data >= 5 :
        data12A1 = (~31 & data12A1 & 0xFF)
        print ("row1", bin(data12A1))
#bus.write_byte_data(addressU1,0x12,data)
    return (data12A1)

def set_row2(data, data12A1, data13A1):
    data = int(data)
    
    if data == 1:
        data13A1 = (~2 & data13A1 & 0xFF)
        print bin(data12A1)
    #bus.write_byte_data(addressU1,0x12,data)
    elif data == 2 :
        data13A1 = (~3 & data13A1 & 0xFF)
        print bin(data12A1)
    #bus.write_byte_data(addressU1,0x12,data)
    elif data == 3 :
        data12A1 = (~128 & data12A1 & 0xFF)
        data13A1 = (~3 & data13A1 & 0xFF)
        print bin(data12A1)
    #bus.write_byte_data(addressU1,0x12,data)
    elif data == 4 :
        data13A1 = (~3 & data13A1 & 0xFF)
        #data13A1 = (~1 & data13A1 & 0xFF)
        print ('row2b', bin(data13A1))
        #bus.write_byte_data(addressU1,0x13,data)
        data12A1 = (~192 & data12A1 & 0xFF)
        print ("row2", bin(data12A1))
        #bus.write_byte_data(addressU1,0x12,data)
    elif data >= 5 :
        data13A1 = (~3 & data13A1 & 0xFF)
        print bin(data13A1)
        #bus.write_byte_data(addressU1,0x13,data)
        data12A1 = (~224 & data12A1 & 0xFF)
        print bin(data13A1)
        #bus.write_byte_data(addressU1,0x12,data)
    return (data12A1, data13A1)

def set_row3(data, data13A1):
    data = int(data)
    
    if data == 1:
        data13A1 = (~192 & data13A1 & 0xFF)
        print bin(data13A1)
    #bus.write_byte_data(addressU1,0x13,data)
    elif data == 2 :
        data13A1 = (~224 & data13A1 & 0xFF)
        print bin(data13A1)
    #bus.write_byte_data(addressU1,0x13,data)
    elif data == 3 :
        data13A1 = (~240 & data13A1 & 0xFF)
        print bin(data13A1)
    #bus.write_byte_data(addressU1,0x13,data)
    elif data == 4 :
        data13A1 = (~248 & data13A1 & 0xFF)
        print bin(data13A1)
    #bus.write_byte_data(addressU1,0x13,data)
    elif data >= 5 :
        data13A1 = (~252 & data13A1 & 0xFF)
        print bin(data13A1)
#bus.write_byte_data(addressU1,0x13,data)
    return (data13A1)

def set_row4(data, data12A2):
    data = int(data)

    if data == 1:
        data12A2 = (~16 & data12A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x12,data)
    elif data == 2 :
        data12A2 = (~24 & data12A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x12,data)
    elif data == 3 :
        data12A2 = (~28 & data12A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x12,data)
    elif data == 4 :
        data12A2 = (~30 & data12A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x12,data)
    elif data >= 5 :
        data12A2 = (~31 & data12A2 & 0xFF)
        print ('row4', bin(data12A2))
#bus.write_byte_data(addressU2,0x12,data)
    return (data12A2)

def set_row5(data, data12A2, data13A2):
    data = int(data)

    if data == 1:
        data13A2 = (~2 & data13A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x12,data)
    elif data == 2 :
        data13A2 = (~3 & data13A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x12,data)
    elif data == 3 :
        data12A2 = (~128 & data12A2 & 0xFF)
        data13A2 = (~3 & data13A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x12,data)
    elif data == 4 :
        data13A2 = (~3 & data13A2 & 0xFF)
        #bus.write_byte_data(addressU2,0x13,data)
        data12A2 = (~192 & data12A2 & 0xFF)
        #bus.write_byte_data(addressU2,0x12,data)
    elif data >= 5 :
        data13A2 = (~3 & data13A2 & 0xFF)
        #bus.write_byte_data(addressU2,0x13,data)
        data12A2 = (~224 & data12A2 & 0xFF)
#bus.write_byte_data(addressU2,0x12,data)
    return (data12A2, data13A2)

def set_row6(data, data13A2):
    data = int(data)

    if data == 1:
        data13A2 = (~192 & data13A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x13,data)
    elif data == 2 :
        data13A2 = (~224 & data13A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x13,data)
    elif data == 3 :
        data13A2 = (~240 & data13A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x13,data)
    elif data == 4 :
        data13A2 = (~248 & data13A2 & 0xFF)
    #bus.write_byte_data(addressU2,0x13,data)
    elif data >= 5 :
        data13A2 = (~252 & data13A2 & 0xFF)
#bus.write_byte_data(addressU2,0x13,data)
    return (data13A2)

delay = 0.1
row1 = 0
row2 = 0
row3 = 0
row4 = 0
row5 = 0
row6 = 0

exit = False
while not exit:
    r = raw_input('Enter something, "q" to quit"')
    print(r)
    row1 = r
    bus.write_byte_data(addressU1,0x12,0xFF)
    bus.write_byte_data(addressU2,0x12,0xFF)
    bus.write_byte_data(addressU1,0x13,0xFF)
    bus.write_byte_data(addressU2,0x13,0xFF)
    
    data12A1 = 0xFF
    data12A2 = 0xFF
    data13A1 = 0xFF
    data13A2 = 0xFF
    """
    data12A1 = set_row1(row1, data12A1)
    data12A1, data13A1 = set_row2(row2, data12A1, data13A1)
    print('data12A1', bin(data12A1))
    data13A1 = set_row3(row3, data13A1)
    data12A2 = set_row4(row4, data12A2)
    data12A2, data13A2 = set_row5(row5, data12A2, data13A2)
    data13A2 =  set_row6(row6, data13A2)
    """
    #print bin(data12A1)
    #print bin(data12A2)
    #print bin(data13A1)
    #print bin(data13A2)
    """
    bus.write_byte_data(addressU1,0x12,data12A1)
    bus.write_byte_data(addressU2,0x12,data12A2)
    bus.write_byte_data(addressU1,0x13,data13A1)
    bus.write_byte_data(addressU2,0x13,data13A2)
    """
    bus.write_byte_data(addressU1,0x12,0b11001110)
    bus.write_byte_data(addressU1,0x13,0b11011110)
    bus.write_byte_data(addressU2,0x12,0b11010111)
    bus.write_byte_data(addressU2,0x13,0b10111010)

    time.sleep(delay)
    
    row6 = row5
    row5 = row4
    row4 = row3
    row3 = row2
    row2 = row1
    
    if r=='q':
        bus.write_byte_data(addressU1,0x12,0xFF)
        bus.write_byte_data(addressU2,0x12,0xFF)
        bus.write_byte_data(addressU1,0x13,0xFF)
        bus.write_byte_data(addressU2,0x13,0xFF)
        exit=True
if __name__ == "__main__":
    main()
