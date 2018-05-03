import wpilib

class Claw:
    # The lifting mechanism, will be injected in robot.py
    rear_motors: wpilib.Spark
    front_motors: wpilib.Talon
    ram: wpilib.DoubleSolenoid
    
    states = {
        # 'state': (motor speed, ram position)
        'pull': (-0.75, False),
        'hold': (-0.20, False),
        'slow': (0.50, False),
        'medium': (0.85, False),
        'fast': (0.00, True),
    }

    speed = states['hold'][0]
    ram_position = states['hold'][1]

    def set_state(self, new_state):
        if len(new_state) != 2:
            raise RuntimeError('Expected tuple of length 2 for new_state')
        elif type(new_state[0]) is not float:
            raise RuntimeError('Expected an int for new_state[0]')
        elif type(new_state[1]) is not bool:
            raise RuntimeError('Expected an bool for new_state[1]')
        else:
            self.speed = new_state[0]
            self.ram_position = new_state[1]

    def on_enable(self):
        # Called when the robot enters teleop or autonomous mode
        self.ram.set(wpilib.DoubleSolenoid.Value.kReverse)
        pass

    def execute(self):
        # Executes during robot runtime
        if self.ram_position:
            self.ram.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.ram.set(wpilib.DoubleSolenoid.Value.kReverse)
        self.front_motors.set(self.speed)
        self.rear_motors.set(self.speed)
