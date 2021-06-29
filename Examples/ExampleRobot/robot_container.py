# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
from .subsystems.example_subsystem import ExampleSubsystem
from .commands.example_command import ExampleCommand
from .commands.example_command2 import ExampleCommand2


exampleSubsystem = ExampleSubsystem()
exampleCommand = ExampleCommand()
exampleCommand2 = ExampleCommand2()

def getAutonomousCommand():
    return exampleCommand