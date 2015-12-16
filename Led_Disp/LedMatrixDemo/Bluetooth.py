"""
import bluetooth

target_name = None #"My Phone"
target_address = "00:16:53:03:65:A5"

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address

else:
    print "could not find target bluetooth device nearby"



import sys
import bluetooth
import os


server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM0 )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address

data = client_sock.recv(1024)
print "received [%s]" % data

client_sock.close()
server_sock.close()
"""
"""
import bluetooth



target_name = None #"My Phone"
target_address = "00:16:53:03:65:A5"

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address

else:
    print "could not find target bluetooth device nearby"



bd_addr = "00:16:53:03:65:A5"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

data = client_sock.recv(1024)
print "received [%s]" % data

#sock.send("hello!!")


sock.close()
"""


import serial

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )

#a = None
#while a == None:
#   try:
#       a = float( raw_input( "Please enter the first number: " ) )
#   except:
#       pass    # Ignore any errors that may occur and try again

#b = None
#while b == None:
#    try:
#        b = float( raw_input( "Please enter the second number: " ) )
#    except:
#        pass    # Ignore any errors that may occur and try again

#bluetoothSerial.write( "{0} {1}".format( a, b ) )
while 1:
    #x = bluetoothSerial.parseInt()
    try:
        print bluetoothSerial.readline()
    except:
        pass    # Ignore any errors that may occur and try again
        bluetoothSerial.close()
    




