from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
import logging


class DigitalInput():

    __channel = None
    __channelMode = vmxpi.DigitalInput
    __res_handle = None

    def __init__(self, channel):
        __dio_config = vmxpi.DIOConfig();
        success, self.__res_handle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(channel, self.__channelMode), __dio_config)
        if not(success):
            logging.error("Error Activating Singlechannel Resource DigitalInput for Channel index %d." % (self.__channel))
            HAL.DisplayVMXError(vmxerr)

    def get(self):
        success, high, vmxerr = HAL.getVMX().getIO().DIO_Get(self.__res_handle)
        if not(success):
            print("Error Reading Digital Input value for Resource Index %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr);
        else:
            return high