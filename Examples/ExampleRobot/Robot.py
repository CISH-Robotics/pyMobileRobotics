# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
import time

class Robot(pyMobileRobotics.TimedRobot):

    def __init__(self):
        super().__init__()

    def robotInit(self):
        """
        該函數將在機器人程序初次啟動時運行
        """
        pyMobileRobotics.logging.debug('TEST')

    lastTime = time.time()
    def robotPeriodic(self):
        """
        該函數將在任何模式下運行

        Tips:該函數會在各模式的迴圈之後運行
        """
        pyMobileRobotics.logging.debug('{:.3f}'.format(time.perf_counter() - self.lastTime))
        self.lastTime = time.perf_counter()

        # time.sleep(1)

    def disabledInit(self):
        """
        該函數將在機器人進入禁能狀態時運行一次
        """
        pass

    def disabledPeriodic(self):
        """
        該函數將在禁能狀態下每次運行
        """
        pass

    def autonomousInit(self):
        """
        該函數將在機器人進入自動模式時運行一次
        """
        pass

    def autonomousPeriodic(self):
        """
        該函數將在自動模式下每次運行
        """
        pass

    def teleopInit(self):
        """
        該函數將在機器人進入遙控模式時運行一次
        """
        pass

    def teleopPeriodic(self):
        """
        該函數將在遙控模式下每次運行
        """
        pass

    def testInit(self):
        """
        該函數將在機器人進入測試模式時運行一次
        """
        pass

    def testPeriodic(self):
        """
        該函數將在測試模式下每次運行
        """
        pass
