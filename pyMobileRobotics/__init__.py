# author:	CISH Robotics
# website:	https://github.com/CISH-Robotics/

# set the version number
__version__ = "0.0.1"

# import the necessary packages
import importlib
import os
import sys

from . import *
from .RobotBase import logging
from .RobotBase import RobotBase
from .IterativeRobotBase import IterativeRobotBase
from .TimedRobot import TimedRobot