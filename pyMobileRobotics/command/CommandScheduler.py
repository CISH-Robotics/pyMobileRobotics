from command.Command import Command
from command.CommandState import CommandState
from command.SubSystem import SubSystem


class CommandScheduler():

    __instance = None
    __scheduledCommands = {}
    __requirements = {}

    @staticmethod
    def getInstance():
        if CommandScheduler.__instance == None:
            CommandScheduler.__instance = CommandScheduler()
        return CommandScheduler.__instance

    def __init__(self):
        pass

    def __initCommand(self, command: Command, interruptible: bool, requirements: set):
        """initCommand 初始化命令一個指定命令，添加其需要至清單中，並初始化該動作

        Args:
            command (Command): 需要初始化的命令
            interruptible (bool): 該命令是否支持打斷
            requirements (set): 該令命的需要
        """
        __commandName = self.__getCommandName(command)
        command.initialize()
        scheduledCommand = CommandState(interruptible)
        self.__scheduledCommands[__commandName] = CommandState
        for requirement in requirements:
            __requirementName = self.__getSubSystemName(requirement)
            self.__requirements[__requirementName] = command

    def __schedule(self, interruptible: bool, command: Command):
        if self.__inRunLoop:
            __commandName = self.__getCommandName(command)
            self.__toSchedule[__commandName] = interruptible
            return

        if 

    @staticmethod
    def __getCommandName(command: Command):
        return command.__class__.__name__

    @staticmethod
    def __getSubSystemName(subsystem: SubSystem):
        return subsystem.__class__.__name__