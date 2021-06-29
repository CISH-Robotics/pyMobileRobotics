from pyMobileRobotics.robot_state import RobotState
from pyMobileRobotics.hal.hal import HAL
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
    def startRobot(robot, simulation=False):
        """
        啟動機器人

        Args:
            robot (RobotBase): 機器人程序
            simulation (bool, optional): 啟用模擬。 Defaults to False.
        """
        RobotState.setSimulation(simulation)
        if not(simulation):
            logging.info('********* VMX-HAL library starting *********')
            HAL.getVMX()
        logging.info('********** Robot program starting **********')
        robot.startCompetition()