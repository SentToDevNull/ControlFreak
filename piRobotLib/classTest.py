#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
#from pwm import PWM
#from talonsrx import TalonSRX
#from robotbase import RobotBase

# Constants for the pins the colored LEDs are connected to.
GREEN_LED = 18

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins we're going to use to for output.  This is
# necessary if using simple output to pull pins high or low, and
# also when using PWM.
GPIO.setup(GREEN_LED, GPIO.OUT)

# Create the PWM objects.  First param is the pin.  Second param is
# frequency in Hz.
# Note this is a software based implementation of PWM, which is not
# as accurate as hardware PWM.

# with freq of 50Hz, the cycle is 20ms
pwm1 = GPIO.PWM(GREEN_LED, 50)

print(pwm1)
# Cleanup
#pwm1.stop()
GPIO.cleanup()
