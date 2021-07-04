from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
import logging



class AnalogInput():
    """類比輸入"""

    __channel = None
    __channelMode = vmxpi.AccumulatorInput
    __resHandle = None

    def __init__(self, channel: int):
        self.__channel = channel
        __accum_config = vmxpi.AccumulatorConfig();
        success, self.__resHandle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(self.__channel, self.__channelMode), __accum_config)
        if not(success):
            logging.error("Error Activating Singlechannel Resource Accumulator for Channel index %d." % (self.__channel))
            HAL.DisplayVMXError(vmxerr)

    def getVoltage(self) -> float:
        """
        獲取類比輸入電壓

        Returns:
            float: 電壓 Voltage
        """
        success, an_in_voltage, vmxerr = HAL.getVMX().getIO().Accumulator_GetAverageVoltage(self.__resHandle)
        if not(success):
            logging.error("Error getting Average Voltage of analog accumulator %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr);
        else:
            return an_in_voltage

    def getValue(self) -> int:
        """
        獲取類比輸入數值

        Returns:
            int: 數值 Value
        """
        success, an_in_value, vmxerr = HAL.getVMX().getIO().Accumulator_GetAverageValue(self.__resHandle)
        if not(success):
            logging.error("Error getting Average Value of analog accumulator %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr);
        else:
            return an_in_value