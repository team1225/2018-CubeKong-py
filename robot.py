#!/usr/bin/env python3

'''
Team 1225 Cube Kong program
'''

import wpilib
from wpilib import drive  # pylint: disable=unused-import
import ctre
from magicbot import MagicRobot

from robotmap import RobotMap
from components.lifter import Lifter
from components.claw import Claw


class MyRobot(MagicRobot):
    '''
    Robot Class for the 1225 Gorillas' 2018 'Cube Kong' robot
    Used in the FRC 2018 game PowerUp (C++ code used in events)
    '''
    # pylint: disable=too-many-instance-attributes
    # robots have many instance attributes
    left_drive: ctre.WPI_TalonSRX
    right_drive: ctre.WPI_TalonSRX
    drive: wpilib.drive.DifferentialDrive

    arm: Lifter
    arm_lifter: wpilib.DoubleSolenoid
    arm_position: bool

    body: Lifter
    body_lifter: wpilib.DoubleSolenoid
    body_position: bool

    claw: Claw
    claw_ram: wpilib.DoubleSolenoid
    claw_rear_motors: wpilib.Spark
    claw_front_motors: wpilib.Talon

    joystick: wpilib.XboxController

    def createObjects(self):
        '''
        Initialize all wpilib HW
        - Drive
        - Left
        - Right
        - Arm Lifter
        - Body Lifter
        - Claw
        - Joystick
        '''

        self.right_drive = ctre.WPI_TalonSRX(RobotMap.drive_cfg['left_can'])
        self.left_drive = ctre.WPI_TalonSRX(RobotMap.drive_cfg['right_can'])
        self.right_drive.setInverted(RobotMap.drive_cfg['right_invert'])
        self.left_drive.setInverted(RobotMap.drive_cfg['left_invert'])
        self.drive = wpilib.drive.DifferentialDrive(
            self.right_drive, self.left_drive)

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
        self.claw_rear_motors.setInverted(RobotMap.claw_cfg['rear_invert'])
        self.claw_front_motors.setInverted(RobotMap.claw_cfg['front_invert'])

        self.joystick = wpilib.XboxController(0)

    #
    # No autonomous routine boilerplate required here, anything in the
    # autonomous folder will automatically get added to a list
    #

    def teleopInit(self):
        '''
        Runs one time as the robot enters teleop
        '''
        self.arm.set_lift(RobotMap.arm_cfg['default_up'])
        # super.teleopInit()

    def teleopPeriodic(self):
        # Operator Control, runs repeatedly while teleop-enabled

        self.drive.arcadeDrive(
            # Drive fwd/bwd
            -0.60 * \
            self.joystick.getY(wpilib.interfaces.GenericHID.Hand.kLeft),
            # Turn left/right
            0.50 * \
            self.joystick.getX(wpilib.interfaces.GenericHID.Hand.kRight),
        )

        if self.joystick.getYButtonPressed():
            self.arm.toggle_position()

        if self.joystick.getBackButtonPressed():
            self.body.toggle_position()

        if self.joystick.getBumper(wpilib.interfaces.GenericHID.Hand.kRight):
            self.claw.set_state(Claw.states['pull'])
        elif self.joystick.getXButton():
            self.claw.set_state(Claw.states['fast'])
        elif self.joystick.getBumper(wpilib.interfaces.GenericHID.Hand.kLeft):
            self.claw.set_state(Claw.states['medium'])
        elif self.joystick.getTriggerAxis(wpilib.interfaces.GenericHID.Hand.kLeft) >= 0.25:
            self.claw.set_state(Claw.states['slow'])
        else:
            self.claw.set_state(Claw.states['hold'])


if __name__ == '__main__':
    wpilib.run(MyRobot)
