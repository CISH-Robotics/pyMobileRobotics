from pyMobileRobotics.iterative_robot_base import IterativeRobotBase
from pyMobileRobotics.__oclock_timer import OClockTimer
import time


class TimedRobot(IterativeRobotBase):

    def __init__(self, period=0.02):
        self.__period = period
        super().__init__(period)

    def getPeriod(self):
        return self.__period

    def startCompetition(self):
        self.robotInit()

        if super().isSimulation():
            self.simulationInit()

        __expirationTime = 0
        timer = OClockTimer(interval=self.__period)
        while True:
            __expirationTime += self.__period
            self.loopFunc()
            timer.checkpt()