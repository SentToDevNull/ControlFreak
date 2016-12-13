#!/usr/bin/env python
import time
import hal
import wpilib
import logging

# Constants for the pins the motors are connected to.
MOTOR1 = 12

try:
    logger = logging.getLogger('hal')
    logger.setLevel(logging.INFO)
    logger.info('starting test')
    m1 = wpilib.VictorSP(MOTOR1)
    
    while True:
        speed = float(input('enter speed between -1.0 and 1.0: '))
        m1.set(speed)

except KeyboardInterrupt:
	pass
