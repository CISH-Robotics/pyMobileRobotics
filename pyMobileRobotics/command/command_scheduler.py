from pyMobileRobotics.command.command import Command
from pyMobileRobotics.command.command_state import CommandState
from pyMobileRobotics.command.command_group_base import CommandGroupBase
from pyMobileRobotics.command.subsystem import SubSystem
from pyMobileRobotics.robot_state import RobotState
from pyMobileRobotics.util import Util


class CommandScheduler():

    __instance = None
    __scheduledCommands = set()
    __requirements = {}
    __toCancel = set()

    @staticmethod
    def getInstance():
        if CommandScheduler.__instance == None:
            CommandScheduler.__instance = CommandScheduler()
        return CommandScheduler.__instance

    def __init__(self):
        pass

    def __initCommand(self, command: Command, interruptible: bool, requirements: set[SubSystem]):
        """__initCommand 初始化命令一個指定命令，添加其需要至清單中，並初始化該動作

        Args:
            command (Command): 需要初始化的命令
            interruptible (bool): 該命令是否支持打斷
            requirements (set[SubSystem]): 該令命的需要
        """
        __commandName = command.getName()
        command.initialize()
        scheduledCommand = CommandState(interruptible)
        # self.__scheduledCommands[__commandName] = scheduledCommand
        self.__scheduledCommands.add(command)
        for requirement in requirements:
            __requirementName = requirement.getName()
            self.__requirements[__requirementName] = command

    def schedule(self, interruptible: bool, command: Command):
        """schedule
        調度執行命令。 如果命令已被調度，則不執行任何操作。 如果命令的要求不可用，
        則只有當前使用這些要求的所有命令都被安排為可打斷時才會啟動。
        如果是這種情況，它們將被打斷並且命令將被調度。

        Args:
            interruptible (bool): 該命令是否可以打斷
            command (Command): 要調度的命令

        Raises:
            ValueError: 不能獨立調度屬於命令組的命令
        """
        __commandName = command.getName()
        if self.__inRunLoop:
            self.__toSchedule[__commandName] = interruptible
            return

        if __commandName in CommandGroupBase.getGroupedCommands():
            raise ValueError('A command that is part of a command group cannot be independently scheduled')

        # 如果調度器被禁用，機器人被禁用並且命令在禁用時不運行，
        # 或者命令已經被調度，則不執行任何操作。
        if (self.__disabled
            or (RobotState.isDisabled() and not(command.runsWhenDisabled()))
            or command in self.__scheduledCommands):
            return

        __requirements = command.getRequirements()

        # 如果當前未使用要求，則安排命令。
        if not(Util.dictsDisjoint(self.__requirements, list(__requirements))):
            self.__initCommand(command, interruptible, __requirements)
        else:
            # 否則檢查正在使用的需求是否都有可中斷的命令，
            # 如果有，則中斷這些命令並調度新命令。
            for requirement in __requirements:
                __subsystemName = requirement.getName()
                if (__subsystemName in self.__requirements.keys()
                    and not(self.__requirements[__subsystemName].isInterruptible())):
                    return
            for requirement in __requirements:
                __subsystemName = requirement.getName()
                self.cancel(self.__requirements[__subsystemName])
            self.__initCommand(command, interruptible, __requirements)

    def cancel(self, *commands: Command):
        if self.__inRunLoop:
            for command in commands:
                self.__toCancel.add(command)
            return

        for command in commands:
            __commandName = command.getName()
            if not(__commandName in self.__scheduledCommands.keys()):
                continue

            command.end(True)
            del self.__scheduledCommands[__commandName]
            __requirements = command.getRequirements()
            for requirement in __requirements:
                __subsystemName = requirement.getName()
                del self.__requirements[__subsystemName]

    def cancelAll(self):
        for command in self.__scheduledCommands:
            self.cancel(command)

    def disable(self):
        self.__disabled = True

    def enable(self):
        self.__disabled = False