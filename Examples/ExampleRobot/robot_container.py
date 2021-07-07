# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
from .subsystems.example_subsystem import ExampleSubsystem
from .subsystems.servo_test import ServoTest
from .subsystems.drivetrain import DriveTrain
from .commands.test_command_group import TestCommandGroup


exampleSubsystem = ExampleSubsystem()
servoTest = ServoTest()
drivetrain = DriveTrain()
testCommandGroup = TestCommandGroup()

def getAutonomousCommand():
    return testCommandGroup