# Team 1225 CubeKong (2018 PowerUp) (python)

## Setup:
We'll use a python [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/) for the robotpy installation:
- Create a virtualenv with `virtualenv --python=python3.6 python_env`
- Enter the virtualenv with:
  - (On Linux or Mac) `source python_env/bin/activate`
  - (On Windows) `.\python_env\scripts\activate`
- Install robotpy with `sudo pip install robotpy-installer pyfrc robotpy-ctre pygame coverage`

When you're done, close the virtualenv with `deactivate`

### Prepare the robot:
- While connected to the internet:
```
robotpy-install download-robotpy
robotpy-install download-opkg python36-robotpy-ctre
```
- While connected to the robot:
```
robotpy-install install-robotpy
robotpy-install install-opkg python36-robotpy-ctre
```  

### Test the code
`./robot.py test`  

### Simulate the robot
`./robot.py sim`  

### Deploy to the robot
`./robot.py deploy`
