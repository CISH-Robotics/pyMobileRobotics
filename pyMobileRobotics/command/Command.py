from pyMobileRobotics.command.subsystem import Subsystem
from pyMobileRobotics.command.command_scheduler import CommandScheduler


class Command():

    def initialize(self):
        """
        命令的初始程序。在命令被初始化時執行一次。
        """
        pass

    def execute(self):
        """
        命令的程式主體。在命令被調度後重複執行。
        """
        pass

    def end(self, interrupted: bool):
        """
        命令的結束程序。在命令完成時執行，
        或命令被打斷時執行。

        Args:
            interrupted (bool): 命令是否被打斷
        """
        pass

    def isFinished(self) -> bool:
        """
        命令是否已完成。當命令完成時，命令調度系統會執行end()一次，
        並取消調度該命令。

        Returns:
            bool: 命令是否已完成?
        """
        return False

    def getName(self) -> str:
        return self.__class__.__name__

    def addRequirements(self, requirements: set[Subsystem]):
        pass

    def getRequirements(self) -> set[Subsystem]:
        pass

    def runsWhenDisabled(self) -> bool:
        return False

    def schedule(self, interruptible=True):
        CommandScheduler.getInstance().schedule(self, interruptible)