from pyMobileRobotics.timer import Timer

class CommandState():
    """保存命令調度狀態的類。"""

    __startTime = -1

    def __init__(self, interruptible: bool):
        self.__interruptible = interruptible
        self.startTiming()
        self.startRunning()

    def startTiming(self):
        self.__startTime = Timer.getTime()

    def startRunning(self):
        self.__startTime = -1

    def isInterrupted(self):
        return self.__interruptible

    def timeSinceInitialized(self):
        return Timer.getTime() - self.__startTime if self.__startTime != -1 else -1