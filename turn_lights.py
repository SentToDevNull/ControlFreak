#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
# Constants for the pins the colored LEDs are connected to.
GREEN_LED = 18
# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins we're going to use to for output.  This is
# necessary if using simple output to pull pins high or low, and
# also when using PWM.
GPIO.setup(GREEN_LED, GPIO.OUT)

# Note this is a software based implementation of PWM, which is not 
# as accurate as hardware PWM.
# This should be a frequency that works with the Talon motor controller
# pwm1 = GPIO.PWM(GREEN_LED, 50)

# Start each PWM object with a duty cycle of 0 (off)
# Duty cycle is the % of the complete cycle that the pin is pulled high.
# i.e, the % of time the device is on.
# Range of duty cycle is 0.0 <= dc <= 100.0

class Light:
    def __init__(self):
      # self.CURRENT_POWER = 50
      self.running = False
    def run(self):
        self.running = True

        # Cleanup
        # pwm1.stop()
        GPIO.cleanup()
    def loop(self, latest_coords):
        if latest_coords[0] > 80:
            GPIO.output(GREEN_LED, True)
        else:
            GPIO.output(GREEN_LED, False)
    def stop(self):
        self.running = False
