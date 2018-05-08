# Team 1225 CubeKong (2018 PowerUp) (python)

## Setup:
### Install robotpy:
`sudo pip install robotpy-installer pyfrc coverage`  

### Or Install all dependencies at one time
py -3 -m pip install pyfrc wpilib coverage pynetconsole pynetworktables pytest robotpy-ctre robotpy-hal-base robotpy-hal-sim robotpy-installer robotpy-wpilib-utilities pygame

### Prepare the robot:
- While connected to the internet: `robotpy-install download-robotpy`
- While connected to the robot: `robotpy-install install-robotpy`  

### Test the code
`./robot.py test`  

### Simulate the robot
`./robot.py sim`  

### Deploy to the robot
`./robot.py deploy`
