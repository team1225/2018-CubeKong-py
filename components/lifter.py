import wpilib

class Lifter:
    # The lifting mechanism, will be injected in robot.py
    lifter: wpilib.DoubleSolenoid
    position: bool

    def set_lift(self, new_position):
        if new_position == True:
            self.position = True
        elif new_position == False:
            self.position = False
        else:
            raise ExpectedBool

    def toggle_position(self):
        if self.position == True:
            self.position = False
        elif self.position == False:
            self.position = True
        else:
            raise ExpectedBool

    def on_enable(self):
        # Called when the robot enters teleop or autonomous mode
        pass

    def execute(self):
        # Executes during robot runtime
        if self.position:
            self.lifter.set(wpilib.DoubleSolenoid.Value.kReverse)
        else:
            self.lifter.set(wpilib.DoubleSolenoid.Value.kForward)
