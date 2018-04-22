#!/usr/bin/env python3

import wpilib
from wpilib import drive
import ctre
from magicbot import MagicRobot

from robotmap import RobotMap
from components.lifter import Lifter
from components.claw import Claw


class MyRobot(MagicRobot):
    arm: Lifter
    body: Lifter
    claw: Claw
    
    def createObjects(self):
        # Initialize all wpilib HW

        self.right_drive = ctre.WPI_TalonSRX(RobotMap.drive_cfg['left_can'])
        self.left_drive = ctre.WPI_TalonSRX(RobotMap.drive_cfg['right_can'])
        self.drive = wpilib.drive.DifferentialDrive(self.right_drive, self.left_drive)

        self.arm_lifter = wpilib.DoubleSolenoid(
                RobotMap.arm_cfg['pcm_id'],
                RobotMap.arm_cfg['lift_pcm'],
                RobotMap.arm_cfg['drop_pcm'],
        )
        self.arm_position = RobotMap.arm_cfg['default_up']

        self.body_lifter = wpilib.DoubleSolenoid(
                RobotMap.body_cfg['pcm_id'],
                RobotMap.body_cfg['lift_pcm'],
                RobotMap.body_cfg['drop_pcm'],
        )
        self.body_position = RobotMap.body_cfg['default_up']

        self.claw_ram = wpilib.DoubleSolenoid(
                RobotMap.claw_cfg['ram_pcm_id'],
                RobotMap.claw_cfg['ram_fwd_pcm'],
                RobotMap.claw_cfg['ram_bwd_pcm'],
        )
        self.claw_rear_motors = wpilib.Spark(RobotMap.claw_cfg['rear_pwm'])
        self.claw_front_motors = wpilib.Talon(RobotMap.claw_cfg['front_pwm'])

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
            self.drive.arcadeDrive(
                    self.joystick.getY(wpilib.interfaces.GenericHID.Hand.kLeft), # Drive fwd/bwd
                    self.joystick.getX(wpilib.interfaces.GenericHID.Hand.kRight), # Turn left/right
            )
        except:
            self.onException()
        
        try:
            if self.joystick.getYButtonPressed():
                self.arm.toggle_position()
        except:
            self.onException()

        try:
            if self.joystick.getStartButtonPressed():
                self.body.toggle_position()
        except:
            self.onException()

        try:
            if self.joystick.getBumperPressed(wpilib.interfaces.GenericHID.Hand.kRight):
                self.claw.set_state(Claw.states['pull'])
            elif self.joystick.getXButtonPressed():
                self.claw.set_state(Claw.states['fast'])
            elif self.joystick.getBumperPressed(wpilib.interfaces.GenericHID.Hand.kLeft):
                self.claw.set_state(Claw.states['medium'])
            elif self.joystick.getTriggerAxis(wpilib.interfaces.GenericHID.Hand.kLeft) >= 0.25:
                self.claw.set_state(Claw.states['slow'])
        except:
            self.onException()





if __name__ == '__main__':
    wpilib.run(MyRobot)
