from enum import Enum

class Mode(Enum):
    """機器人模式"""
    kNone = 0
    kDisabled = 1
    kAutonomous = 2
    kTeleop = 3
    kTest = 4

class RobotState():
    """保存機器人狀態和模式的類"""

    __enabled = False

    @staticmethod
    def getMode():
        return Mode.kNone

    @staticmethod
    def getEnabled():
        return RobotState.__enabled

    @staticmethod
    def isDisabled():
        return not(RobotState.getEnabled())

    @staticmethod
    def isEnabled():
        return RobotState.getEnabled()

    @staticmethod
    def isSimulation():
        return False

    @staticmethod
    def isTeleoperation():
        return RobotState.getMode() == Mode.kTeleop

    @staticmethod
    def isAutonomous():
        return RobotState.getMode() == Mode.kAutonomous

    @staticmethod
    def isTest():
        return RobotState.getMode() == Mode.kTest