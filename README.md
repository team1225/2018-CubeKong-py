# Team 1225 CubeKong (2018 PowerUp) (python)

## Setup:
We'll use a python [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/) for the robotpy installation:
- Start a pyenv folder should it not exist, this helps many tools find your virtualenvs
  - (Linux or Mac) `mkdir -p ~/.pyenv`
  - (Windows) `mkdir %userprofile%/.pyenv`
- Create a virtualenv with `virtualenv --python=python3.6 ~/.pyenv`
- Enter the virtualenv with:
  - (On Linux or Mac) `source ~/.pyenv/robotpy/bin/activate`
  - (On Windows) `%userprofile%\.pyenv\scripts\activate`
- Install robotpy with `pip install robotpy-installer pyfrc robotpy-ctre pygame coverage pylint`

### VSCode setup:
- Ensure that `python.venvPath` contains `"~/.pyenv/"`
- Ensure that `python.terminal.activateEnvironment` is `true`
- Open the robot project and go!
- Run the robot deploy/test/simulations in the included terminal.

### Vim/NeoVim Setup
- Whenever editing, activate the virtualenv first `source ~/.pyenv/robotpy/bin/activate`
- Install pymode's dependencies in the virtualenv `pip install pylint rope ropemode ropevim pylama pyflakes pep8 autopep8 pep257 mccabe`
- (NeoVim) Install the neovim python bindings in the virtualenv `pip install neovim`
- Install pymode for vim, see [here](https://github.com/python-mode/python-mode#how-to-install).
- Edit away! Warnings and errors will appear automatically.
- Run the robot deploy/test/simulations with `:!` to run a shell, example: `:! ./robot.py test`

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
