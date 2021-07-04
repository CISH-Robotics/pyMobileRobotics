# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
import time

class ExampleCommand2(pyMobileRobotics.CommandBase):

    def __init__(self):
        super().__init__()
        from ExampleRobot.robot_container import exampleSubsystem
        super().addRequirements(exampleSubsystem)

    def initialize(self):
        pass

    def execute(self):
        pass

    def end(self, interrupted: bool):
        if interrupted:
            pyMobileRobotics.logging.debug('command2 interrupted')
        pass

    def isFinished(self):
        return False