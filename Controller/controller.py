import RPi.GPIO as GPIO
import thread


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

  
def checkbtns(test):
	while 1:
		if(GPIO.input(17) == 0):
			print("Button up")
		if(GPIO.input(23) == 0):
			print("Button down")
		if(GPIO.input(22) == 0):
			print("Button falldown")
		if(GPIO.input(24) == 0):
			print("Button left")
		if(GPIO.input(27) == 0):
			print("Button right")
	print test


try:
   thread.start_new_thread(checkbtns, (5,))
   
except:
   print "Error: unable to start thread"
   
while 1:   
   pass
   
GPIO.cleanup()