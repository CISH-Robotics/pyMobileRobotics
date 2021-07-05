from pyMobileRobotics.command.command_group_base import CommandGroupBase


class SequentialCommandGroup(CommandGroupBase):

    __commands = []
    __currentCommandIndex = -1
    __runWhenDisabled = True

    def __init__(self, *commands):
        self.addCommands(commands)

    def addCommands(self, commands: tuple):
        CommandGroupBase.requireUngrouped(commands)

        if self.__currentCommandIndex != -1:
            raise ValueError('Commands cannot be added to a CommandGroup while the group is running')

        CommandGroupBase.registerGroupedCommands(commands)

        for command in commands:
            self.__commands.append(command)
            for subsystem in command.getRequirements():
                self.addRequirements(subsystem)
            self.__runWhenDisabled &= command.runsWhenDisabled()

    def initialize(self):
        self.__currentCommandIndex = 0

        if len(self.__commands) != 0:
            self.__commands[0].initialize()

    def execute(self):
        if len(self.__commands) == 0:
            return

        currentCommand = self.__commands[self.__currentCommandIndex]

        currentCommand.execute()
        if currentCommand.isFinished():
            currentCommand.end(False)
            self.__currentCommandIndex += 1
            if self.__currentCommandIndex < len(self.__commands):
                self.__commands[self.__currentCommandIndex].initialize()

    def end(self, interrupted: bool):
        if (interrupted and len(self.__commands) != 0 and self.__currentCommandIndex > -1
            and self.__currentCommandIndex < len(self.__commands)):
            self.__commands[self.__currentCommandIndex].end(True)
        self.__currentCommandIndex = -1

    def isFinished(self) -> bool:
        return True if self.__currentCommandIndex >= len(self.__commands) else False

    def runsWhenDisabled(self) -> bool:
        return self.__runWhenDisabled