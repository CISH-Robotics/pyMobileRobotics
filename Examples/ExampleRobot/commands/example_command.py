# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
import time

class ExampleCommand(pyMobileRobotics.CommandBase):

    def initialize(self):
        pyMobileRobotics.logging.debug('hello from command')
        pass

    def execute(self):
        pass

    def end(self, interrupted: bool):
        pass

    def isFinished(self):
        return False