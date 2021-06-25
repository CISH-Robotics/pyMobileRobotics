from pyMobileRobotics.timed_robot import TimedRobot
from enum import Enum
import coloredlogs
import logging


class Mode(Enum):
    kNone = 0
    kDisabled = 1
    kAutonomous = 2
    kTeleop = 3
    kTest = 4

class RobotBase():

    __enabled = False

    __LOG_FORMAT = '%(asctime)s %(hostname)s %(levelname)s %(message)s'
    coloredlogs.install('DEBUG', __LOG_FORMAT)

    def getMode(self):
        return Mode.kNone

    def getEnabled(self):
        return self.__enabled

    def isDisabled(self):
        return not(self.getEnabled())

    def isEnabled(self):
        return self.getEnabled()

    def isSimulation(self):
        return False

    def isTeleoperation(self):
        return self.getMode() == Mode.kTeleop

    def isAutonomous(self):
        return self.getMode() == Mode.kAutonomous

    def isTest(self):
        return self.getMode() == Mode.kTest

    @staticmethod
    def startRobot(robot: TimedRobot):
        """startRobot

        Args:
            robot (TimedRobot): TimedRobot
        """
        logging.info('********** Robot program starting **********')
        robot.startCompetition()