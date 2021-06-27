# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics

class ExampleSubsystem(pyMobileRobotics.SubsystemBase):

    def periodic(self):
        pyMobileRobotics.logging.debug('DEBUG')