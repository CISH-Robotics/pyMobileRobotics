import time
import logging


class Watchdog():

    __epochs = {}

    def __init__(self, timeout, callback):
        self.__timeout = timeout
        self.__callback = callback

    def __getTime(self):
        return time.perf_counter()

    def addEpoch(self, epochName):
        self.__epochs[epochName] = self.__getTime()

    def reset(self):
        self.enable()

    def enable(self):
        self.__startTime = self.__getTime()
        self.__epochs = {}

    #TODO 應改為多線程呼叫，應改為私有
    def schedulerFunc(self):
        __timedOut = False
        for epoch in self.__epochs:
            if self.__epochs[epoch] - self.__startTime > self.__timeout:
                __timedOut = True
                break
        if __timedOut:
            logging.warning('========================================')
            logging.warning('Watchdog not fed within ' + str(self.__timeout))
            for epoch in self.__epochs:
                logging.warning('   ' + epoch + ': ' +
                                str('{:.6f}'.format(self.__epochs[epoch] - self.__startTime)) +
                                's')
            logging.warning('========================================')
            self.__callback()
