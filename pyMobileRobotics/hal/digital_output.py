from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
import logging



class DigitalOutput():
    """數位輸出"""

    __channel = None
    __channelMode = vmxpi.DigitalOutput
    __resHandle = None

    def __init__(self, channel: int):
        """
        數位輸出

        Args:
            channel (int): 輸出腳位
        """
        self.__channel = channel
        __dioConfig = vmxpi.DIOConfig(vmxpi.DIOConfig.PUSHPULL);
        success, self.__resHandle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(self.__channel, self.__channelMode), __dioConfig)
        if not(success):
            logging.error("Error Activating Singlechannel Resource DigitalOutput for Channel index %d." % (self.__channel))
            HAL.DisplayVMXError(vmxerr)

    def set(self, value: bool):
        """
        設置數位輸出的數值

        Args:
            value (bool): Value
        """
        success, vmxerr = HAL.getVMX().getIO().DIO_Set(self.__resHandle, value)
        if not(success):
            logging.error("Error Setting Digital Output value for Resource Index %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr);

    def pulse(self, high: bool, microseconds: int):
        """
        開始一個數位輸出的定時脈衝

        **脈衝週期 <= 100 微秒是高度準確的，並且會阻塞 HighCurrDIO/CommDIO。 脈衝週期 > 100 微秒會降低計時精度，並且可能需要長達 1 毫秒才能終止，但是此調用不會阻塞。**
        Args:
            high (bool): True為高電位脈衝，False為低電位脈衝
            microseconds (int): 脈衝時間
        """
        success, vmxerr = HAL.getVMX().getIO().DIO_Pulse(self.__resHandle, high, microseconds)
        if not(success):
            logging.error("Error Setting Digital Output pulse for Resource Index %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr);