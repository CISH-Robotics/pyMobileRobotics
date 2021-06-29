from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
import logging


class DigitalInput():
    """數位輸入"""

    __channel = None
    __channelMode = vmxpi.DigitalInput
    __res_handle = None

    def __init__(self, channel: int):
        self.__channel = channel
        __dio_config = vmxpi.DIOConfig();
        success, self.__res_handle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(self.__channel, self.__channelMode), __dio_config)
        if not(success):
            logging.error("Error Activating Singlechannel Resource DigitalInput for Channel index %d." % (self.__channel))
            HAL.DisplayVMXError(vmxerr)

    def get(self) -> bool:
        """
        獲取數位輸入數值

        Returns:
            bool: Value
        """
        success, high, vmxerr = HAL.getVMX().getIO().DIO_Get(self.__res_handle)
        if not(success):
            logging.error("Error Reading Digital Input value for Resource Index %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr);
        else:
            return high