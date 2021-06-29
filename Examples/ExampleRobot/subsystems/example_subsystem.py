# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics

class ExampleSubsystem(pyMobileRobotics.SubsystemBase):

    def __init__(self):
        # 必須要先呼叫父類建構式，以進行各種初始化並註冊子系統。
        super().__init__()
        self.__io = pyMobileRobotics.DigitalInput(8)

    def periodic(self):
        high = self.__io.get()
        # pyMobileRobotics.logging.debug(high)
        if high:
            pyMobileRobotics.RobotState.setAutonomous()
        else:
            pyMobileRobotics.RobotState.setDisabled()