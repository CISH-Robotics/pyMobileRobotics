# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics as mb
import ExampleRobot.robot_container as container

class ExampleCommand(mb.CommandBase):

    def __init__(self):
        # 必須要先運行父類的建構式，以進行基本初始化及註冊
        super().__init__()
        # 添加需求子系統
        super().addRequirements(container.drivetrain)
        self._timer = mb.Timer()

    def initialize(self):
        container.drivetrain.setMotorSpeed(0, 0)
        self._timer.start()
        pass

    def execute(self):
        container.drivetrain.setMotorSpeed(0, 480)
        pass

    def end(self, interrupted: bool):
        container.drivetrain.setMotorSpeed(0, 0)
        self._timer.stop()
        pass

    def isFinished(self):
        return True if self._timer.get() > 3 else False