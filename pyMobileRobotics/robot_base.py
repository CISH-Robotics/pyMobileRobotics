from pyMobileRobotics.robot_state import RobotState
from enum import Enum
import coloredlogs
import logging

class RobotBase():

    __LOG_FORMAT = '%(asctime)s %(hostname)s %(levelname)s %(message)s'
    coloredlogs.install(level='DEBUG', fmt=__LOG_FORMAT)

    def getMode(self):
        return RobotState.getMode()

    def getEnabled(self):
        return RobotState.getEnabled()

    def isDisabled(self):
        return RobotState.isDisabled()

    def isEnabled(self):
        return RobotState.isEnabled()

    def isSimulation(self):
        return RobotState.isSimulation()

    def isTeleoperation(self):
        return RobotState.isTeleoperation()

    def isAutonomous(self):
        return RobotState.isSimulation()

    def isTest(self):
        return RobotState.isTest()

    @staticmethod
    def startRobot(robot):
        """
        啟動機器人

        Args:
            robot (TimedRobot): TimedRobot
        """
        logging.info('********** Robot program starting **********')
        robot.startCompetition()