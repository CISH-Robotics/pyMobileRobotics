


class CommandScheduler():

    __instance = None

    @staticmethod
    def getInstance():
        if CommandScheduler.__instance == None:
            CommandScheduler.__instance = CommandScheduler()
        return CommandScheduler.__instance

    def __init(self):
        pass