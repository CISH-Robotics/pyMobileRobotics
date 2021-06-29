from pyMobileRobotics.command import command

class CommandBase(command.Command):

    __requirements = set()

    def __init__(self):
        self.__name = super().getName()

    def getName(self):
        return self.__name

    def addRequirements(self, *requirements):
        """
        添加指定的要求至命令

        Args:
            requirements... (SubSystem): 要添加的要求子系統
        """
        self.__requirements.update(requirements)

    def getRequirements(self):
        return self.__requirements