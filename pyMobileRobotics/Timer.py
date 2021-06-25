import time

class Timer():

    @staticmethod
    def getTime():
        """getTime 獲取當前系統時間

        Returns:
            time: 當前系統時間(秒)
        """
        return time.perf_counter()