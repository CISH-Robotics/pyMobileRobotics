from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
import logging

class Encoder():
    """編碼器"""

    __channelA = None
    __channelB = None
    __channelAMode = vmxpi.EncoderAInput
    __channelBMode = vmxpi.EncoderBInput
    __resHandle = None

    def __init__(self, channelA: int, channelB: int):
        self.__channelA = channelA
        self.__channelB = channelB
        __channelAInfo = vmxpi.VMXChannelInfo(channelA, vmxpi.EncoderAInput)
        __channelBInfo = vmxpi.VMXChannelInfo(channelB, vmxpi.EncoderBInput)
        __dioConfig = vmxpi.EncoderConfig(vmxpi.EncoderConfig.x4)
        success, self.__resHandle, vmxerr = HAL.getVMX().getIO().ActivateDualchannelResource(__channelAInfo, __channelBInfo, __dioConfig)
        if not(success):
            logging.error("Error Activating Dualchannel Resource Encoder for Channel indexes %d and %d." % (__channelAInfo.index, __channelBInfo.index))
            HAL.DisplayVMXError(vmxerr)

    def get(self):
        """
        獲取編碼器數值

        Returns:
            int: 編碼器數值
            bool: 編碼器旋轉方向。True為正轉，False為反轉
        """
        success1, counter, vmxerr = HAL.getVMX().getIO().Encoder_GetCount(self.__resHandle)
        success2, encoder_direction, vmxerr = HAL.getVMX().getIO().Encoder_GetDirection(self.__resHandle)
        if not(success1) or not(success2):
            logging.error("Error retrieving Encoder count.")
            HAL.DisplayVMXError(vmxerr);
        encoder_direction = True if encoder_direction == vmxpi.VMXIO.EncoderForward else False
        return counter, encoder_direction

    def reset(self):
        """
        重置編碼器數值
        """
        success, vmxerr = HAL.getVMX().getIO().Encoder_Reset(self.__resHandle)
        if not(success):
            logging.error("Error reseting Encoder count.")
            HAL.DisplayVMXError(vmxerr);