# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
import Robot

def main():
    robot = Robot.Robot()
    pyMobileRobotics.RobotBase.startRobot(robot)

if __name__ == '__main__':
    main()