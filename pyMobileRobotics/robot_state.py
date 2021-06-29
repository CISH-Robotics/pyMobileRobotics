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
    __mode = Mode.kNone
    __simulation = False

    @staticmethod
    def getMode():
        return RobotState.__mode

    @staticmethod
    def getEnabled():
        return True if RobotState.getMode() != Mode.kNone and RobotState.getMode() != Mode.kDisabled else False

    @staticmethod
    def isDisabled():
        return not(RobotState.getEnabled())

    @staticmethod
    def isEnabled():
        return RobotState.getEnabled()

    @staticmethod
    def isSimulation():
        return RobotState.__simulation

    @staticmethod
    def isTeleoperation():
        return True if RobotState.__mode == Mode.kTeleop else False

    @staticmethod
    def isAutonomous():
        return True if RobotState.__mode == Mode.kAutonomous else False

    @staticmethod
    def isTest():
        return True if RobotState.__mode == Mode.kTest else False

    @staticmethod
    def __setMode(mode: Mode):
        RobotState.__mode = mode

    @staticmethod
    def setDisabled():
        RobotState.__setMode(Mode.kDisabled)

    @staticmethod
    def setTeleoperation():
        RobotState.__setMode(Mode.kTeleop)

    @staticmethod
    def setAutonomous():
        RobotState.__setMode(Mode.kAutonomous)

    @staticmethod
    def setTest():
        RobotState.__setMode(Mode.kTest)

    @staticmethod
    def setSimulation(enable: bool):
        RobotState.__simulation = enable