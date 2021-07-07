# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics as mb
import studica
import time

class ServoTest(mb.SubsystemBase):

    def __init__(self):
        # 必須要先呼叫父類建構式，以進行各種初始化並註冊子系統。
        super().__init__()
        self.__pwm = mb.PWMGenerator(21, 50)
        self.__us = studica.Ultrasonic(13, 11)
        mb.NetworkVariables.setValue('ServoDeg', float(0.0))

    def periodic(self):
        mb.logging.debug(str(self.__us.pingCM()))
        if mb.RobotState.isEnabled():
            deg = mb.NetworkVariables.getValue('ServoDeg')
            duty = (deg / 300 * 0.1) + 0.025 if deg > 0 else 0.025
            self.__pwm.set(duty)