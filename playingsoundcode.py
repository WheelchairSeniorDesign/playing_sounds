"""Eren Tekbas for ECE Senior Design 2025 
Playing Sound From Screen
This code is to play sound from the speakers, which are connected to the screen, which is connected to the Jetson Nano.
It will have input of a number, which decides what sound file to play."""

""""add the ros number input"""
soundNumber = 1; # change this number to play different sound files
soundVolume = 1.0; # change this number to change the volume of the sound
import pygame # import the pygame library

pygame.init()
pygame.mixer.init() #initialize the mixer module
if soundNumber==1:
    sound = pygame.mixer.Sound('alarm.mp3') #load the sound 
    soundVolume = 1;
elif soundNumber==2:
    sound = pygame.mixer.Sound('moving.mp3') #load the sound
    soundVolume = 0.5;
elif soundNumber==3:
    sound = pygame.mixer.Sound('reverse.mp3') #load the sound
    soundVolume = 0.7;

elif soundNumber==4:
    sound = pygame.mixer.Sound('idle.mp3') #load the sound
    soundVolume = 0.3;
else:
    soundVolume = 0;

sound.set_volume(soundVolume) #set the volume
sound.play()  #play the sound