# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import sys
import pyMobileRobotics
from . import robot


argvs = sys.argv[1:]
print(argvs)
pyMobileRobotics.RobotBase.startRobot(robot.Robot())