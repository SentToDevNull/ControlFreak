#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import hal
import time
from pprint import pprint
import traceback
from networktables import NetworkTables


# Constants for the pins the motors are connected to.
# Note the new Raspberry pi HAL uses BOARD rather than BCM numbering

MOTOR1 = 0
MOTOR2 = 1
SOLENOID = 13

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        traceback.print_stack()
        
        m1 = wpilib.TalonSRX(MOTOR1)
        m2 = wpilib.TalonSRX(MOTOR2)
        self.robot_drive = wpilib.RobotDrive(m1, m2)
        self.stick = wpilib.Joystick(0)
        print(self.stick)
        #pprint (vars(self.stick))
        #self.button1 = wpilib.buttons.JoystickButton(self.stick, 0)
        self.s1 = wpilib.DigitalOutput(SOLENOID)
        self.CannonIsFiring = False
    
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        
        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(.1, 0) # Drive forwards
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)    #Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        # check if the button has been pushed and if we're already in the firing state
        if (self.stick.getButton(0)):
            if not self.CannonIsFiring:
                print('Fire!')
                self.s1.set(True)
            self.CannonIsFiring = True
        else:
            if self.CannonIsFiring:
                # button is no longer pressed, so turn off the solenoid
                self.s1.set(False)
            self.CannonIsFiring = False
        print("testing")
        #print('test if safety functions kill an unresponsive robot')
        #time.sleep(10)
        self.robot_drive.arcadeDrive(self.stick)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    print('rtest.py starting')
    hal.HALInitialize()
    #pprint(vars(hal))
    #print(MyRobot)
    wpilib.run(MyRobot)
    #robot = MyRobot()
    #robot.robotInit()
    #hal.observeUserProgramStarting()
    #while True:
        #hal.observeUserProgramTeleop()
    #    robot.teleopPeriodic()
    #print('test program terminating')
