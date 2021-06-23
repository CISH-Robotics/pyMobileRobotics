from . import IterativeRobotBase
from . import RobotBase
from oclock import Timer

class TimedRobot(IterativeRobotBase.IterativeRobotBase):

    def __init__(self, period=0.02):
        self.__period = period

    def getPeriod(self):
        return self.__period

    def startCompetition(self):
        self.robotInit()

        if self.isSimulation():
            self.simulationInit()

        timer = Timer(interval=self.__period)
        while True:
            self.loopFunc()
            timer.checkpt()