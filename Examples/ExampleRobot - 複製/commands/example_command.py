# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
import time

class ExampleCommand(pyMobileRobotics.CommandBase):

    def __init__(self):
        # 必須要先運行父類的建構式，以進行基本初始化及註冊
        super().__init__()
        # 添加需求子系統
        from ExampleRobot.robot_container import exampleSubsystem
        super().addRequirements(exampleSubsystem)

        self.__do = pyMobileRobotics.DigitalOutput(12)

    def initialize(self):
        self.__do.set(True)
        pass

    def execute(self):
        value = True if time.time() % 0.4 < 0.2 else False
        pyMobileRobotics.logging.debug('TEST=' + str(value))
        self.__do.set(value)

    def end(self, interrupted: bool):
        self.__do.set(False)
        if interrupted:
            pyMobileRobotics.logging.debug('command1 interrupted')
        pass

    def isFinished(self):
        return False