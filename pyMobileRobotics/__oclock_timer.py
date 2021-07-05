import oclock
from pyMobileRobotics import timer


class OClockTimer(oclock.Timer):

    @staticmethod
    def now():
        return timer.Timer.now()