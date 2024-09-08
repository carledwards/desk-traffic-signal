# SPDX-License-Identifier: MIT
# Created by Carl Edwards

import board
import digitalio
import time
import random

# Initialization (LEDs are active high)
red_light = digitalio.DigitalInOut(board.D7)
red_light.direction = digitalio.Direction.OUTPUT
red_light.value = False

yellow_light = digitalio.DigitalInOut(board.D8)
yellow_light.direction = digitalio.Direction.OUTPUT
yellow_light.value = False

green_light = digitalio.DigitalInOut(board.D9)
green_light.direction = digitalio.Direction.OUTPUT
green_light.value = False

# Startup sequence

# Snake through the LEDs
green_light.value = True
time.sleep(.4)
yellow_light.value = True
time.sleep(.4)
red_light.value = True
time.sleep(.4)
green_light.value = False
time.sleep(.4)
yellow_light.value = False
time.sleep(.4)
red_light.value = False
time.sleep(.4)

# Blink the LEDs
for i in range(1, 4):
    green_light.value = True
    yellow_light.value = True
    red_light.value = True
    time.sleep(.2)
    green_light.value = False
    yellow_light.value = False
    red_light.value = False
    time.sleep(.2)

time.sleep(2)

# Main signal simulation 
while True:
    # Green light phase (30 to 50 seconds)
    green_light.value = True
    time.sleep(random.randint(30, 50))
    green_light.value = False

    # Yellow light phase (3 to 5 seconds)
    yellow_light.value = True
    time.sleep(random.randint(3, 5))
    yellow_light.value = False
    
    # Red light phase (30 to 50 seconds)
    red_light.value = True
    time.sleep(random.randint(30, 50))
    red_light.value = False
