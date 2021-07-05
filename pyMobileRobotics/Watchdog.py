from pyMobileRobotics.timer import Timer
import logging
import threading


class Watchdog():

    __enabled = False
    __epochs = {}
    __minPrintPeriod = 1

    def __init__(self, timeout, callback):
        self.__timeout = timeout
        self.__callback = callback
        threading.Thread(target=self.__schedulerFunc).start()

    def __getTime(self):
        return Timer.now(os=True)

    def addEpoch(self, epochName: str):
        self.__epochs[epochName] = self.__getTime()

    def reset(self):
        self.enable()

    def enable(self):
        self.__startTime = self.__getTime()
        self.__epochs = {}
        self.__enabled = True

    #TODO 應改為多線程呼叫，應改為私有。
    def __schedulerFunc(self):
        __lastTime = self.__getTime()
        while True:
            if self.__enabled:
                __timedOut = False
                epochs = self.__epochs.copy()
                startTime = self.__startTime
                for epoch in epochs:
                    if epochs[epoch] - startTime > self.__timeout:
                        __timedOut = True
                        break
                if __timedOut:
                    logging.warning('========================================')
                    logging.warning('Watchdog not fed within ' + str(self.__timeout))
                    for epoch in epochs:
                        logging.warning('   ' + epoch + ': '
                                        + str('{:.6f}'.format(epochs[epoch] - startTime))
                                        + 's')
                    logging.warning('========================================')
                    self.__callback()
                    __lastTime = self.__getTime()
