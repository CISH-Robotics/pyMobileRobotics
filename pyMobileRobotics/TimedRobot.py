from .IterativeRobotBase import IterativeRobotBase
from oclock import Timer
import time


class TimedRobot(IterativeRobotBase):

    def __init__(self, period=0.02):
        self.__period = period
        super().__init__(period)

    def getPeriod(self):
        return self.__period

    def startCompetition(self):
        self.robotInit()

        if self.isSimulation():
            self.simulationInit()

        __expirationTime = 0
        timer = Timer(interval=self.__period)
        while True:
            __expirationTime += self.__period
            self.loopFunc()
            timer.checkpt()
