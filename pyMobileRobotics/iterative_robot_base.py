from pyMobileRobotics.robot_base import RobotBase
from pyMobileRobotics.robot_state import Mode
from pyMobileRobotics.watchdog import Watchdog
import logging
import time

class IterativeRobotBase(RobotBase):
    """
    IterativeRobotBase implements a specific type of robot program framework, extending the RobotBase
    class.

    The IterativeRobotBase class does not implement startCompetition(), so it should not be used
    by teams directly.

    This class provides the following functions which are called by the main loop,
    startCompetition(), at the appropriate times:

    robotInit() -- provide for initialization at robot power-on

    init() functions -- each of the following functions is called once when the
    appropriate mode is entered:
    - disabledInit()   -- called each and every time disabled is entered from
                            another mode
    - autonomousInit() -- called each and every time autonomous is entered from
                            another mode
    - teleopInit()     -- called each and every time teleop is entered from
                            another mode
    - testInit()       -- called each and every time test is entered from
                            another mode

    periodic() functions -- each of these functions is called on an interval:
    - robotPeriodic()
    - disabledPeriodic()
    - autonomousPeriodic()
    - teleopPeriodic()
    - testPeriodic()
    """

    __lastMode = Mode.kNone

    """----------- Overridable initialization code -----------------"""

    def robotInit(self):
        logging.info("Default robotInit() method... Override me!")

    def simulationInit(self):
        logging.info("Default simulationInit() method... Override me!")

    def disabledInit(self):
        logging.info("Default disabledInit() method... Override me!")

    def autonomousInit(self):
        logging.info("Default autonomousInit() method... Override me!")

    def teleopInit(self):
        logging.info("Default teleopInit() method... Override me!")

    def testInit(self):
        logging.info("Default testInit() method... Override me!")

    """----------- Overridable periodic code -----------------"""

    __rpFirstRun = True
    def robotPeriodic(self):
        if self.__rpFirstRun:
            logging.info("Default robotPeriodic() method... Override me!")
            self.__rpFirstRun = False

    __spFirstRun = True
    def simulationPeriodic(self):
        if self.__spFirstRun:
            logging.info("Default simulationPeriodic() method.. Override me!")
            self.__spFirstRun = False

    __dpFirstRun = True
    def disabledPeriodic(self):
        if self.__dpFirstRun:
            logging.info("Default disabledPeriodic() method.. Override me!")
            self.__dpFirstRun = False

    __apFirstRun = True
    def autonomousPeriodic(self):
        if self.__apFirstRun:
            logging.info("Default autonomousPeriodic() method.. Override me!")
            self.__apFirstRun

    __tpFirstRun = True
    def teleopPeriodic(self):
        if self.__tpFirstRun:
            logging.info("Default teleopPeriodic() method.. Override me!")
            self.__tpFirstRun = False

    __tmpFirstRun = True
    def testPeriodic(self):
        if self.__tmpFirstRun:
            logging.info("Default testPeriodic() method.. Override me!")
            self.__tmpFirstRun = False

    """----------- Internal functions code -----------------"""

    def __init__(self, period):
        self.__period = period
        self.__watchdog = Watchdog(period, lambda: self.__printLoopOverrunMessage())

    def loopFunc(self):
        self.__watchdog.reset()

        if self.isDisabled():
            if self.__lastMode != Mode.kDisabled:
                self.disabledInit()
                self.__lastMode = Mode.kDisabled
            self.disabledPeriodic()
            self.__watchdog.addEpoch('disabledPeriodic()')
        elif self.isAutonomous():
            if self.__lastMode != Mode.kAutonomous:
                self.autonomousInit()
                self.__lastMode = Mode.kAutonomous
            self.autonomousPeriodic()
            self.__watchdog.addEpoch('autonomousPeriodic()')
        elif self.isTeleoperation():
            if self.__lastMode != Mode.kTeleop:
                self.teleopInit()
                self.__lastMode = Mode.kTeleop
            self.teleopPeriodic()
            self.__watchdog.addEpoch('teleopPeriodic()')
        elif self.isTest():
            if self.__lastMode != Mode.kTest:
                self.testInit()
                self.__lastMode = Mode.kTest
            self.testPeriodic()
            self.__watchdog.addEpoch('testPeriodic()')

        self.robotPeriodic()
        self.__watchdog.addEpoch('robotPeriodic()')

        if self.isSimulation():
            self.simulationPeriodic()

        self.__watchdog.schedulerFunc()

    def __printLoopOverrunMessage(self):
        # logging.warning('Loop time of ' + str(self.__period) + 's overrun')
        pass