
import time
import sys
import json
import os
import pygame

main_dir = os.path.dirname(os.path.realpath(__file__)) #Locate self

#Get necessary paths
packages_path = os.path.join(main_dir, "Packages")
settings_path = os.path.join(main_dir, "settings.json")

with open(settings_path) as settings_file:
    settings = json.load(settings_file)
    right_axis = settings["Right_Axis"]
    left_axis = settings["Left_Axis"]
    front_forward = settings["Front_Forward"]
    front_reverse = settings["Front_Reverse"]
    mid_forward = settings["Mid_Forward"]
    mid_reverse = settings["Mid_Reverse"]
    dump_toggle = settings["Dump_Toggle"]
    

sys.path.append(packages_path)

#import packages
from PCA9685 import PCA9685

map_val = 250
pygame.init()
pygame.display.init()
pygame.display.set_mode((1,1))
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True
debug = True
print(sys.version)

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

joys = pygame.joystick.Joystick(0)

# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize the appended joystick (-1 means last array item)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    if debug: print ("Detected joystick "),joysticks[-1].get_name(),"'"


def drive_servo(channel, direction):
    if direction == "Forward":
        pwm.setServoPulse(channel,600)
    elif direction == "Reverse":
        pwm.setServoPulse(channel,2500)
    else:
        pwm.setServoPulse(channel, 500)

def angle_servo(channel, angle):
    pulse = 500+(2000*(angle/360))
    pwm.setServoPulse(channel, pulse)


while keepPlaying:
    clock.tick(60)
    for event in pygame.event.get():
        pass