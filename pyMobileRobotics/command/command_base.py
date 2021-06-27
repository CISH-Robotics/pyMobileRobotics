from pyMobileRobotics.command.command import Command
from pyMobileRobotics.command.subsystem import SubSystem

class CommandBase(Command):

    __requirements = {}

    def __init__(self):
        self.__name = super().getName()

    def getName(self):
        return self.__name

    def addRequirements(self, requirements: set[SubSystem]):
        """
        添加指定的要求至命令

        Args:
            requirements (set[SubSystem]): 要添加的要求
        """
        self.__requirements.update(requirements)

    def getRequirements(self):
        return self.__requirements