from pyMobileRobotics.util import Util
from pyMobileRobotics.robot_state import RobotState
import logging


class CommandScheduler():


    __disabled = False
    __instance = None
    __subsystems = set()
    __scheduledCommands = {}
    __requirements = {}
    __inRunLoop = False
    __toSchedule = set()
    __toCancel = set()

    @staticmethod
    def getInstance():
        if CommandScheduler.__instance == None:
            CommandScheduler.__instance = CommandScheduler()
        return CommandScheduler.__instance

    def __init__(self):
        pass

    def __initCommand(self, command, interruptible: bool, requirements: set):
        """
        始化命令一個指定命令，添加其需要至清單中，並初始化該動作

        Args:
            command (Command): 需要初始化的命令
            interruptible (bool): 該命令是否支持打斷
            requirements (set[SubSystem]): 該令命的需要
        """
        command.initialize()
        self.__scheduledCommands[command] = {'interruptible': interruptible}
        for subsystem in requirements:
            self.__requirements[subsystem] = command

    def schedule(self, command, interruptible=True):
        """
        調度執行命令。 如果命令已被調度，則不執行任何操作。 如果命令的要求不可用，
        則只有當前使用這些要求的所有命令都被安排為可打斷時才會啟動。
        如果是這種情況，它們將被打斷並且命令將被調度。

        Args:
            command (Command): 要調度的命令
            interruptible (bool, optional): 該命令是否可以打斷。Defaults to True.

        Raises:
            ValueError: 不能獨立調度屬於命令組的命令
        """
        if self.__inRunLoop:
            self.__toSchedule.add(command)
            return

        from pyMobileRobotics.command.command_group_base import CommandGroupBase
        if command in CommandGroupBase.getGroupedCommands():
            raise ValueError('A command that is part of a command group cannot be independently scheduled')

        # 如果調度器被禁用，機器人被禁用並且命令在禁用時不運行，
        # 或者命令已經被調度，則不執行任何操作。
        if (self.__disabled
            or (RobotState.isDisabled() and not(command.runsWhenDisabled()))
            or command in self.__scheduledCommands.keys()):
            return

        __requirements = command.getRequirements()

        # 如果當前未使用要求，則安排命令。
        if not(Util.listsDisjoint(self.__requirements.keys(), list(__requirements))):
            self.__initCommand(command, interruptible, __requirements)
        else:
            # 否則檢查正在使用的需求是否都有可中斷的命令，
            # 如果有，則中斷這些命令並調度新命令。
            for subsystem in __requirements:
                if (subsystem in self.__requirements.keys()
                    and not(self.__scheduledCommands[self.__requirements[subsystem]]['interruptible'])):
                    return
            for subsystem in __requirements:
                self.cancel(self.__requirements[subsystem])
            self.__initCommand(command, interruptible, __requirements)

    def run(self):
        # 如果調度器為禁用則跳過
        if self.__disabled:
            return

        # 運行已註冊的子系統
        for subsystem in self.__subsystems:
            subsystem.periodic()

        # 上鎖
        self.__inRunLoop = True
        # 操作已註冊的命令
        __scheduledCommands = self.__scheduledCommands.copy()
        for command, scheduledCommand in self.__scheduledCommands.items():
            interruptible = scheduledCommand['interruptible']

            # 如果命令不支持在禁用狀態下運行且當前機器人為禁用狀態，則取消註冊並中斷該命令
            if not(command.runsWhenDisabled()) and RobotState.isDisabled():
                command.end(True)
                __requirements = self.__requirements.copy()
                for reqSubsystem, reqCommand in self.__requirements.items():
                    if reqCommand == command:
                        del __requirements[reqSubsystem]
                self.__requirements = __requirements
                del __scheduledCommands[command]
                continue

            # 運行命令
            command.execute()

            # 如果命令已完成則終止
            if command.isFinished():
                command.end(False)
                __requirements = self.__requirements.copy()
                for reqSubsystem, reqCommand in self.__requirements.items():
                    if reqCommand == command:
                        del __requirements[reqSubsystem]
                self.__requirements = __requirements
                del __scheduledCommands[command]
        self.__scheduledCommands = __scheduledCommands
        # 解鎖
        self.__inRunLoop = False

        # 初始緩存中待初始化的命令
        for toInitCommand in self.__toSchedule:
            self.initCommand(toInitCommand)

        # 取消緩存中待取消的命令
        for toCancelCommand in self.__toCancel:
            self.cancel(toCancelCommand) 

        # 清除緩存
        self.__toSchedule.clear()
        self.__toCancel.clear()

    def registerSubsystem(self, *subsystems):
        """
        註冊子系統

        Args:
            subsystems... (Subsystem): 要註冊的子系統
        """
        self.__subsystems.update(subsystems)

    def unregisterSubsystem(self, *subsystems):
        """
        取消註冊子系統

        Args:
            subsystems... (Subsystem): 要取消註冊的子系統
        """
        for subsystem in subsystems:
            self.__subsystems.remove(subsystem)

    def cancel(self, *commands):
        """
        取消命令

        Args:
            commands... (Command): 要取消的命令
        """
        if self.__inRunLoop:
            for command in commands:
                self.__toCancel.add(command)
            return

        for command in commands:
            if not(command in self.__scheduledCommands.keys()):
                continue

            command.end(True)
            __requirements = command.getRequirements()
            for subsystem in __requirements:
                del self.__requirements[subsystem]

            del self.__scheduledCommands[command]

    def cancelAll(self):
        """
        取消所有已註冊的命令
        """
        for command in self.__scheduledCommands.value():
            self.cancel(command)

    def disable(self):
        self.__disabled = True

    def enable(self):
        self.__disabled = False