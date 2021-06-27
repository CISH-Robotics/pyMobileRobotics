import pyMobileRobotics
from .subsystems.example_subsystem import ExampleSubsystem
from .commands.example_command import ExampleCommand

class RobotContainer():

    exampleSubsystem = ExampleSubsystem()
    exampleCommand = ExampleCommand()