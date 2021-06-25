from pyMobileRobotics.command.command_base import CommandBase
from pyMobileRobotics.command.command import Command

class CommandGroupBase(CommandBase):
    """
    CommandGroupBase 命令組的基礎。 靜態跟踪已分配給組的命令，
    以確保這些命令也不會單獨使用，這會導致命令狀態不一致和執行不可預測。
    """

    __groupedCommands = set()

    @staticmethod
    def registerGroupedCommands(*commands: Command):
        __commands = commands.set(commands)
        CommandGroupBase.__groupedCommands.append(__commands)

    @staticmethod
    def clearGroupedCommands():
        """clearGroupedCommands
        清除分組命令列表，允許再次自由使用所有命令。

        **警告：隨意使用它可能會導致意外/不良行為。 除非你完全理解你在做什麼，否則不要使用它。**
        """
        CommandGroupBase.__groupedCommands = set()

    @staticmethod
    def clearGroupedCommand(command: Command):
        """clearGroupedCommand
        從分組命令列表中刪除單個命令，使其可以再次自由使用。

        **警告：隨意使用它會導致意外/不良行為。 除非你完全理解你在做什麼，否則不要使用它。**

        Args:
            command (Command): 要從分組命令列表中刪除的命令
        """
        CommandGroupBase.__groupedCommands.remove(command)

    @staticmethod
    def requireUngrouped(*commands: Command):
        for command in commands:
            if CommandGroupBase.__groupedCommands.isdisjoint(command):
                raise ValueError("Commands cannot be added to more than one CommandGroup")

    @staticmethod
    def getGroupedCommands():
        return CommandGroupBase.__groupedCommands

    def addCommands(self, *commands: Command):
        pass

    @staticmethod
    def sequence(self, *commands: Command):
        pass

    @staticmethod
    def parallel(self, *commands: Command):
        pass

    @staticmethod
    def race(self, *commands: Command):
        pass

    @staticmethod
    def deadline(self, *commands: Command):
        pass