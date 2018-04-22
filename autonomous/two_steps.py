
from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.lifter import Lifter
                    
class TwoSteps(AutonomousStateMachine):

    MODE_NAME = 'Two Steps'
    DEFAULT = True
    
    arm: Lifter
    body: Lifter

    @timed_state(duration=2, next_state='invert', first=True)
    def nana(self):
        pass

    @timed_state(duration=2, next_state='uninvert')
    def invert(self):
        self.arm.set_lift(False)
        self.body.set_lift(True)

    @timed_state(duration=5)
    def uninvert(self):
        self.arm.set_lift(True)
        self.body.set_lift(False)
