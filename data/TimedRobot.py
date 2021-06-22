from . import IterativeRobotBase
from oclock import Timer

class TimedRobot(IterativeRobotBase.IterativeRobotBase):

    def __init__(self, period=0.02):
        self.period = period

    def getPeriod(self):
        return self.period

    def startCompetition(self):
        timer = Timer(interval=0.02)  # Loops will be of total duration 2 seconds
        while True:
            super().loopFunc()
            timer.checkpt()