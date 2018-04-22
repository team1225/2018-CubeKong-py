#!/usr/bin/env python3

import wpilib
from magicbot import MagicRobot

from robotmap import RobotMap
from components.lifter import Lifter


class MyRobot(MagicRobot):
    arm: Lifter
    body: Lifter
    
    def createObjects(self):
        # Initialize all wpilib HW

        self.arm_lifter = wpilib.DoubleSolenoid(
                RobotMap.arm_cfg['pcm_id'],
                RobotMap.arm_cfg['lift_pcm'],
                RobotMap.arm_cfg['drop_pcm'],
        )
        self.body_lifter = wpilib.DoubleSolenoid(
                RobotMap.body_cfg['pcm_id'],
                RobotMap.body_cfg['lift_pcm'],
                RobotMap.body_cfg['drop_pcm'],
        )
        self.arm_position = RobotMap.arm_cfg['default_up']
        self.body_position = RobotMap.body_cfg['default_up']
        self.joystick = wpilib.XboxController(0)
    
    #
    # No autonomous routine boilerplate required here, anything in the
    # autonomous folder will automatically get added to a list
    #
    
    def teleopInit(self):
        self.arm.set_lift(RobotMap.arm_cfg['default_up'])
        #super.teleopInit()

    def teleopPeriodic(self):
        # Operator Control, runs repeatedly while teleop-enabled
        
        try:
            if self.joystick.getYButtonPressed():
                self.arm.toggle_position()
        except:
            self.onException()

        try:
            if self.joystick.getXButtonPressed():
                self.body.toggle_position()
        except:
            self.onException()




if __name__ == '__main__':
    wpilib.run(MyRobot)
