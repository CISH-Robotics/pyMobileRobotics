from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
import logging



class DigitalOutput():
    """數位輸出"""

    __channel = None
    __channelMode = vmxpi.DigitalOutput
    __res_handle = None

    def __init__(self, channel: int):
        self.__channel = channel
        __dio_config = vmxpi.DIOConfig(vmxpi.DIOConfig.PUSHPULL);
        success, self.__res_handle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(self.__channel, self.__channelMode), __dio_config)
        if not(success):
            logging.error("Error Activating Singlechannel Resource DigitalOutput for Channel index %d." % (self.__channel))
            HAL.DisplayVMXError(vmxerr)

    def set(self, value: bool):
        """
        設置數位輸出的數值

        Args:
            value (bool): Value
        """
        success, vmxerr = HAL.getVMX().getIO().DIO_Set(self.__res_handle, value)
        if not(success):
            logging.error("Error Setting Digital Output value for Resource Index %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr);