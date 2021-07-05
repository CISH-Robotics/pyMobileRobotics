# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics as mb
import time

class ExampleSubsystem(mb.SubsystemBase):

    def __init__(self):
        # 必須要先呼叫父類建構式，以進行各種初始化並註冊子系統。
        super().__init__()
        self.__io = mb.DigitalInput(8)

    __lastTime = mb.Timer.now()
    def periodic(self):
        # time.sleep(5)
        high = self.__io.get()
        if high:
            mb.RobotState.setAutonomous()
        else:
            mb.RobotState.setDisabled()
        mb.NetworkVariables.setValue('periodic', mb.Timer.now() - self.__lastTime)
        # mb.logging.debug("periodic=" + str(mb.Timer.now() - self.__lastTime))
        self.__lastTime = mb.Timer.now()