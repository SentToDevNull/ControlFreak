#!/usr/bin/env python
import time
import hal
import wpilib
#from talonsrx import TalonSRX
#import piRobotLib
import logging
from pprint import pprint

# Constants for the pins the motors are connected to.
MOTOR1 = 0


try:
    print('starting test')
    #pprint(vars(hal))
    m1 = wpilib.TalonSRX(MOTOR1)
    print(m1)
    pprint(vars(m1))
    loopTime = hal.getLoopTiming()/(wpilib.SensorBase.kSystemClockTicksPerMicrosecond*1e3)
    print ('loopTime: ', loopTime)
    # set the speed of the motor - speed is between -1 and 1
    for i in range(-10, 11):
        m1.setSpeed(i/10.0)
    time.sleep(10)

except KeyboardInterrupt:
	pass
