from pyMobileRobotics.command.subsystem import Subsystem
from pyMobileRobotics.command.command_scheduler import CommandScheduler

class SubsystemBase(Subsystem):

    def __init__(self):
        self.__name = super().getName()
        CommandScheduler.getInstance().registerSubsystem(self)

    def getName(self):
        return self.__name