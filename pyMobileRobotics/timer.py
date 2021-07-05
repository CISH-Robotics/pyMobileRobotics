from pyMobileRobotics.hal.hal import HAL
import time


class Timer():
    """計時器"""

    __isVMX = HAL.isVMXOpen()
    _enabled = False

    def __init__(self):
        """
        創建計時器
        """
        self.reset()

    def reset(self):
        """
        重置計時器
        """
        self._startTime = Timer.now()

    def start(self):
        """
        啟動計時器
        """
        self.reset()
        self._enabled = True

    def get(self) -> float:
        """
        獲取計時器從開始至今經過的時間

        Returns:
            float: 經過時間(秒)
        """
        if self._enabled:
            return Timer.now() - self._startTime
        else:
            return 0

    def stop(self):
        """
        終止計時器
        """
        self._enabled = False

    @staticmethod
    def now(os=False):
        """獲取當前系統計時器時間

        Returns:
            time: 當前時間(秒)
        """
        if Timer.__isVMX and not(os):
            now = HAL.getVMX().getTime().GetCurrentMicroseconds()
            now *= 0.000001
        else:
            now = time.perf_counter()
        return now