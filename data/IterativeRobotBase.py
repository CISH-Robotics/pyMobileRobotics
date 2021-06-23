from . import RobotBase
import logging
import time

"""
 IterativeRobotBase implements a specific type of robot program framework, extending the RobotBase
 class.

 <p>The IterativeRobotBase class does not implement startCompetition(), so it should not be used
 by teams directly.

 <p>This class provides the following functions which are called by the main loop,
 startCompetition(), at the appropriate times:
 *
 <p>robotInit() -- provide for initialization at robot power-on

 <p>init() functions -- each of the following functions is called once when the
 appropriate mode is entered:
   - disabledInit()   -- called each and every time disabled is entered from
                         another mode
   - autonomousInit() -- called each and every time autonomous is entered from
                         another mode
   - teleopInit()     -- called each and every time teleop is entered from
                         another mode
   - testInit()       -- called each and every time test is entered from
                         another mode

 <p>periodic() functions -- each of these functions is called on an interval:
   - robotPeriodic()
   - disabledPeriodic()
   - autonomousPeriodic()
   - teleopPeriodic()
   - testPeriodic()
"""
class IterativeRobotBase(RobotBase.RobotBase):

    __lastMode = RobotBase.mode.kNone

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

    __lastTime = time.time()
    def loopFunc(self):

        if self.isDisabled():
            if self.__lastMode != RobotBase.mode.kDisabled:
                self.disabledInit()
                self.__lastMode = RobotBase.mode.kDisabled
            self.disabledPeriodic()
        elif self.isAutonomous():
            if self.__lastMode != RobotBase.mode.kAutonomous:
                self.autonomousInit()
                self.__lastMode = RobotBase.mode.kAutonomous
            self.autonomousPeriodic()
        elif self.isTeleoperation():
            if self.__lastMode != RobotBase.mode.kTeleop:
                self.teleopInit()
                self.__lastMode = RobotBase.mode.kTeleop
            self.teleopPeriodic()
        elif self.isTest():
            if self.__lastMode != RobotBase.mode.kTest:
                self.testInit()
                self.__lastMode = RobotBase.mode.kTest
            self.testPeriodic()

        self.robotPeriodic()

        if self.isSimulation():
            self.simulationPeriodic()
