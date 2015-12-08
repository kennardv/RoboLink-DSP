import pygame
import wave
import sounddevice as sd

pygame.mixer.init()

file = wave.open("Alarm01.wav")
#s = pygame.mixer.Sound("Alarm01.wav")
#file.play()
sd.play(file)
