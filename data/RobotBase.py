import logging
from enum import Enum
from . import TimedRobot

class mode(Enum):
    kNone = 0
    kDisabled = 1
    kAutonomous = 2
    kTeleop = 3
    kTest = 4

class RobotBase():

    __enabled = False

    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    def getMode(self):
        return mode.kNone

    def getEnabled(self):
        return self.__enabled

    def isDisabled(self):
        return not(self.getEnabled)

    def isEnabled(self):
        return self.getEnabled

    def isTeleoperation(self):
        return self.getMode() == mode.kTeleop

    def isAutonomous(self):
        return self.getMode() == mode.kAutonomous

    def isTest(self):
        return self.getMode() == mode.kTest

    def startRobot(robot):
        robot.startCompetition()