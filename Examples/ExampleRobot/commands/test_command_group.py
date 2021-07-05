# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics as mb
from ExampleRobot.commands.example_command import ExampleCommand
from ExampleRobot.commands.example_command2 import ExampleCommand2


class TestCommandGroup(mb.SequentialCommandGroup):

    def __init__(self):
        super().__init__(
            ExampleCommand(),
            ExampleCommand2()
        )