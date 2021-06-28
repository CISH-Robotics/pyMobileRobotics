from pyMobileRobotics.hal import vmxpi
import logging


class HAL():

    __vmx = None

    @staticmethod
    def getVMX():
        if HAL.__vmx == None:
            HAL.__vmx = HAL()
        return HAL.__vmx

    @staticmethod
    def DisplayVMXError(vmxerr):
        err_description = vmxpi.GetVMXErrorString(vmxerr)
        logging.error("VMXError %s:  " % (err_description))

    def __init__(self, realtime=False, ahrs_update_rate_hz=50):
        HAL.__vmx = vmxpi.VMXPi(realtime, ahrs_update_rate_hz)