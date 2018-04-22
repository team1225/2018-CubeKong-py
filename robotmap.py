# Robot Map of CubeKong (FRC 2018 "PowerUp")

# Define HW values: PWM, CAN, PCM, etc...
class RobotMap():
    pass

    drive = {
        'left_can_talon': 10,
        'right_can_talon': 11,
    }

    pcm_arm_id = 5
    pcm_body_id = 6

    claw_cfg = { # type Claw
        'rear_pwm': 0,
        'front_pwm': 1,
        'ram_pcm_id': pcm_arm_id,
        'ram_fwd_pcm': 2,
        'ram_bwd_pcm': 3,
    }

    arm_cfg = { # type Lifter
        'default_up': False,
        'pcm_id': pcm_arm_id,
        'lift_pcm': 0,
        'drop_pcm': 1,
    }

    body_cfg = { # type Lifter
        'default_up': True,
        'pcm_id': pcm_body_id,
        'lift_pcm': 0,
        'drop_pcm': 1,
    }

    # HW specific conversions
    drive_bits2inches = (4096 / 6*3.1415)
