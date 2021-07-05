from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
import logging



class InputCapture():
    """輸入擷取器"""

    __channel = None
    __resHandle = None

    # 兩個channel共用一個時鐘，所以必須區分channel所用的資源類型
    __resAChannels = [0, 2, 4, 6, 8, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    __resBChannels = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 31, 33]

    __maxDutyCycle = 65535

    # def __init__(self, channel: int, frequency: int):
    #     self.__channel = channel

    #     if channel in PWMGenerator.__resAChannels:
    #         self.__channelMode = vmxpi.PWMGeneratorOutput
    #     elif channel in PWMGenerator.__resBChannels:
    #         self.__channelMode = vmxpi.PWMGeneratorOutput2
    #     else:
    #         raise ValueError("Incorrect channel index.")

    #     __dioConfig = vmxpi.PWMGeneratorConfig(frequency);
    #     # 設置最大佔空比(uint16)
    #     __dioConfig.SetMaxDutyCycleValue(PWMGenerator.__maxDutyCycle)
    #     success, self.__resHandle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(self.__channel, self.__channelMode), __dioConfig)
    #     if not(success):
    #         logging.error("Error Activating Singlechannel Resource PWMGenerator for Channel index %d." % (self.__channel))
    #         HAL.DisplayVMXError(vmxerr)

    # def set(self, dutyCycle: float):
    #     """
    #     設置PWM訊號產生器的佔空比

    #     Args:
    #         dutyCycle (float): 佔空比(0~1)
    #     """
    #     if dutyCycle > 1:
    #         dutyCycle = 1
    #     elif dutyCycle < 0:
    #         dutyCycle = 0
    #     dutyCycle *= PWMGenerator.__maxDutyCycle
    #     dutyCycle = int(dutyCycle)
    #     success, vmxerr = HAL.getVMX().getIO().PWMGenerator_SetDutyCycle(self.__resHandle, self.__channel, dutyCycle)
    #     if not(success):
    #         logging.error("Error Setting PWMGenerator duty cycle for Resource Index %d" % (self.__channel))
    #         HAL.DisplayVMXError(vmxerr);