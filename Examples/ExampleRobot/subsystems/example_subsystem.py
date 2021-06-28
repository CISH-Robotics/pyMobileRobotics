# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics

class ExampleSubsystem(pyMobileRobotics.SubsystemBase):

    def __init__(self):
        self.__io = pyMobileRobotics.DigitalInput(8)

    def periodic(self):
        pyMobileRobotics.logging.debug(self.__io.get())