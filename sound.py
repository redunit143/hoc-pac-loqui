#!/usr/bin/env python3
#from gpiozero import Button
#from signal import pause
import time
import random
import os
#from datetime import datetime

# Print current date

#date = datetime.now().strftime("%d_%m_%Y-%H:%M:%S")
#print(f"{date}")

# Make sure that the 'sounds' folder exists, and if it does not, create it

path = './sounds'

isExist = os.path.exists(path)

if not isExist:
  os.makedirs(path)
  print("The new directory is created!")
  os.system('chmod 777 -R ' + path)

isExist = os.path.exists(path)

if not isExist:
    print("Unable to create folder")
    exit
# Download a 'burp' sound if it does not already exist

burp = path + '/burp.wav'

isExist = os.path.exists(burp)
if not isExist:
  os.system('wget http://rpf.io/burp -O burp.wav')
  print("sound file 404!")

exit

# Setup button functions - Pin 27 = Button hold time 10 seconds.

button = Button(27, hold_time=10)

def pressed():
    global press_time
    press_time = time.time()
    print("Pressed at %s" % (press_time));

def released():
    release_time = time.time()
    pressed_for = release_time - press_time
    print("Released at %s after %.2f seconds" % (release_time, pressed_for))
    if pressed_for < button.hold_time:
        print("This is a short press")
        randomfile = random.choice(os.listdir(soundFolder))
        file = path + randomfile
        os.system('aplay ' + file)

def held():
    print("This is a long press")
    os.system('aplay ' + burp)
    #os.system('arecord --format S16_LE --duration=5 --rate 48000 -c2 /home/<username>/sounds/$(date +"%d_%m_%Y-%H_%M_%S")_voice.m4a');

button.when_pressed = pressed
button.when_released = released
button.when_held = held

pause()