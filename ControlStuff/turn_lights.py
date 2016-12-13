#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
# Constants for the pins the colored LEDs are connected to.
GREEN_LED = 18
# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN_LED, GPIO.OUT)


class Light:
    # This will be called over and over
    # It must be in this method
    # so that the server can update the server/respond to clients
    # The only parameter is latest_coords
    # which provides the coordinates of the joystick between 0 and 100
    def loop(self, latest_coords):
        if latest_coords[0] > 80:
            GPIO.output(GREEN_LED, True)
        else:
            GPIO.output(GREEN_LED, False)
