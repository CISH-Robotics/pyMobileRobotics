from pyMobileRobotics.command.subsystem import SubSystem
from pyMobileRobotics.command.command_scheduler import CommandScheduler

class SubSystemBase(SubSystem):

    def __init__(self):
        self.__name = super().getName()
        CommandScheduler.getInstance().registerSubsystem(self)

    def getName(self):
        return self.__name