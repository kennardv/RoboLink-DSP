import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

sndA = pygame.mixer.Sound("buzzer.wav")
sndB = pygame.mixer.Sound("clap.wav")
sndC = pygame.mixer.Sound("laugh.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print "Sampler Ready."

while True:
    #soundChannelA.play(sndA)
    #soundChannelB.play(sndB)
    soundChannelC.play(sndC)
    sleep(.01)
