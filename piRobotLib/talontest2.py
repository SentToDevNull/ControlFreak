#!/usr/bin/env python
import time
import hal
import wpilib
#from talonsrx import TalonSRX
#import piRobotLib
import logging

# Constants for the pins the motors are connected to.
MOTOR1 = 0
MOTOR2 = 1

try:
    logger = logging.getLogger('hal')
    logger.setLevel(logging.INFO)
    logger.info('starting test')
    print(hal)
    m1 = wpilib.TalonSRX(MOTOR1)
    m2 = wpilib.TalonSRX(MOTOR2)
    #print(m1)
    #print(hal)
    #m1.start()
    
    while True:
        speed = float(input('enter speed between -1.0 and 1.0: '))
        m1.set(speed)
        m2.set(speed)

except KeyboardInterrupt:
	pass
