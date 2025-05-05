"""Eren Tekbas for ECE Senior Design 2025 
Playing Sound From Screen
This code is to play sound from the speakers, which are connected to the screen, which is connected to the Jetson Nano.
It will have input of two numbers, first one to select the sound file (1-4) and the second one to choose volume (0.0-1.0)."""

import pygame # import the pygame library
import rclpy
from rclpy.node import Node
from wheelchair_sensor_msgs.msg import Sounds
import playing_sounds.playingsoundcode 
import os

pygame.init()
pygame.mixer.init() #initialize the mixer module
sound_dir = os.path.join(os.getcwd(), 'src', 'playing_sounds', 'playing_sounds')

def soundPlay(soundNumber, soundVolume, playing):

    if playing==False:
        volume = 0;
    elif soundNumber==1:

        sound = pygame.mixer.Sound(os.path.join(sound_dir, 'Air Raid Siren Sound Effect.wav')) #load the sound 
        volume = soundVolume;
    elif soundNumber==2:
        sound = pygame.mixer.Sound(os.path.join(sound_dir, 'Tesla reversing sound.wav')) #load the sound
        volume = 0.5*soundVolume;
    elif soundNumber==3:
        sound = pygame.mixer.Sound(os.path.join(sound_dir, 'Truck reverse sound effect.wav')) #load the sound
        volume = 0.7*soundVolume;
    elif soundNumber==4:
        sound = pygame.mixer.Sound(os.path.join(sound_dir, 'Supercar Engine Revving.wav')) #load the sound
        volume = 0.3*soundVolume;
    else:
        volume = 0;
    sound.set_volume(volume) #set the volume
    sound.play()  #play the sound   
    pygame.time.wait(2000)  # Wait for 2 seconds (sound duration)

