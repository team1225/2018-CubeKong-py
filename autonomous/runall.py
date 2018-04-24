import wpilib
from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.lifter import Lifter
from components.claw import Claw
                    
class RunAll(AutonomousStateMachine):

    MODE_NAME = 'Run All'
    DEFAULT = True
    
    drive: wpilib.drive.DifferentialDrive
    arm: Lifter
    body: Lifter
    claw: Claw

    @timed_state(duration=2, next_state='invert', first=True)
    def nada(self):
        self.drive.arcadeDrive(0.00, 0.00)

    @timed_state(duration=2, next_state='spin_left')
    def invert(self):
        self.arm.set_lift(False)
        self.body.set_lift(True)
        self.drive.arcadeDrive(0.00, 0.00)

    @timed_state(duration=1, next_state='spin_right')
    def spin_left(self):
        self.drive.arcadeDrive(0.00, -0.80)

    @timed_state(duration=1, next_state='uninvert')
    def spin_left(self):
        self.drive.arcadeDrive(0.00, 0.80)

    @timed_state(duration=5)
    def uninvert(self):
        self.arm.set_lift(True)
        self.body.set_lift(False)
