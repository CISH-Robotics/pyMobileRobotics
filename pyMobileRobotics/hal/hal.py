from pyMobileRobotics import hal
import logging


class HAL():

    __vmx = None

    @staticmethod
    def getVMX():
        if HAL.__vmx == None:
            HAL.createVMX()
        return HAL.__vmx

    @staticmethod
    def createVMX(realtime=True, ahrs_update_rate_hz=50):
        HAL.__vmx = hal.vmxpi.VMXPi(realtime, ahrs_update_rate_hz)

    @staticmethod
    def isVMXOpen() -> bool:
        return HAL.getVMX().IsOpen()

    @staticmethod
    def DisplayVMXError(vmxerr):
        err_description = hal.vmxpi.GetVMXErrorString(vmxerr)
        logging.error("VMXError %s:  " % (err_description))