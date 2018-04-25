from pyfrc.physics import drivetrains

class PhysicsEngine(object):
    first_run: bool

    def __init__(self, physics_controller):
        self.first_run = True
        self.physics_controller = physics_controller
        self.drivetrain = drivetrains.TwoMotorDrivetrain()

    def update_sim(self, hal_data, now, tm_diff):
        if self.first_run:
            hal_data.setdefault('custom', {})['encoder 10'] = '---'
            hal_data.setdefault('custom', {})['encoder 11'] = '---'
            self.first_run = False

        l_motor = hal_data['CAN'][11]['value']
        r_motor = hal_data['CAN'][10]['value']

        speed, rotation = self.drivetrain.get_vector(l_motor, r_motor)
        self.physics_controller.drive(speed, rotation, tm_diff)

        hal_data['custom']['encoder 10'] = self.drivetrain.l_speed * tm_diff
        hal_data['custom']['encoder 11'] = self.drivetrain.r_speed * tm_diff
