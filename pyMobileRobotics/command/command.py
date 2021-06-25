from pyMobileRobotics.command.subsystem import SubSystem


class Command():

    def initialize(self):
        pass

    def getName(self):
        return self.__class__.__name__

    def addRequirements(self, requirements: set[SubSystem]):
        pass

    def getRequirements(self) -> set[SubSystem]:
        pass