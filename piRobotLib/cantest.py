#!/usr/bin/env python
import time
import hal
import wpilib
#from talonsrx import TalonSRX
#import piRobotLib
import logging

# Constants for the pins the motors are connected to.
MOTOR1 = 12
MOTOR2 = 11

try:
    logger = logging.getLogger('hal')
    logger.setLevel(logging.INFO)
    logger.info('starting test')
    print(hal)
    m1 = wpilib.CANTalon(MOTOR1)
    m2 = wpilib.CANTalon(MOTOR2)
    #print(m1)
    #print(hal)
    #m1.start()
    
    while True:
        speed = float(input('enter speed between -1.0 and 1.0: '))
        m1.set(speed)
        m2.set(speed)

except KeyboardInterrupt:
	pass
