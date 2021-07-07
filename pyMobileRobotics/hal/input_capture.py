from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
from enum import Enum
import logging



class InputCapture():
    """輸入擷取器"""

    class CounterClockSource(Enum):
        INTERNAL = vmxpi.InputCaptureConfig.INTERNAL
        EDGEDETECT_CH1 = vmxpi.InputCaptureConfig.EDGEDETECT_CH1
        FILTERED_CH1 = vmxpi.InputCaptureConfig.FILTERED_CH1
        FILTERED_CH2 = vmxpi.InputCaptureConfig.FILTERED_CH2

    class CounterDirection(Enum):
        DIRECTION_UP = vmxpi.InputCaptureConfig.DIRECTION_UP
        DIRECTION_DN = vmxpi.InputCaptureConfig.DIRECTION_DN

    class SlaveMode(Enum):
        SLAVEMODE_DISABLED = vmxpi.InputCaptureConfig.SLAVEMODE_DISABLED
        SLAVEMODE_RESET = vmxpi.InputCaptureConfig.SLAVEMODE_RESET
        SLAVEMODE_GATED = vmxpi.InputCaptureConfig.SLAVEMODE_GATED
        SLAVEMODE_TRIGGER = vmxpi.InputCaptureConfig.SLAVEMODE_TRIGGER
        SLAVEMODE_FILTERED_INPUT_TRIGGER = vmxpi.InputCaptureConfig.SLAVEMODE_FILTERED_INPUT_TRIGGER

    class SlaveModeTriggerSource(Enum):
        TRIGGER_EDGEDETECT_CH1 = vmxpi.InputCaptureConfig.TRIGGER_EDGEDETECT_CH1
        TRIGGER_FILTERED_CH1 = vmxpi.InputCaptureConfig.TRIGGER_FILTERED_CH1
        TRIGGER_FILTERED_CH2 = vmxpi.InputCaptureConfig.TRIGGER_FILTERED_CH2
        TRIGGER_DYNAMIC = vmxpi.InputCaptureConfig.TRIGGER_DYNAMIC

    class CaptureChannelSource(Enum):
        CAPTURE_SIGNAL_A = vmxpi.InputCaptureConfig.CAPTURE_SIGNAL_A
        CAPTURE_SIGNAL_B = vmxpi.InputCaptureConfig.CAPTURE_SIGNAL_B
        CAPTURE_SIGNAL_DYNAMIC = vmxpi.InputCaptureConfig.CAPTURE_SIGNAL_DYNAMIC

    class CaptureChannelActiveEdge(Enum):
        ACTIVE_RISING = vmxpi.InputCaptureConfig.ACTIVE_RISING
        ACTIVE_FALLING = vmxpi.InputCaptureConfig.ACTIVE_FALLING
        ACTIVE_BOTH = vmxpi.InputCaptureConfig.ACTIVE_BOTH

    class CaptureChannelPrescaler(Enum):
        x1 = vmxpi.InputCaptureConfig.x1
        x2 = vmxpi.InputCaptureConfig.x2
        x4 = vmxpi.InputCaptureConfig.x4
        x8 = vmxpi.InputCaptureConfig.x8

    class StallAction(Enum):
        ACTION_NONE = vmxpi.InputCaptureConfig.ACTION_NONE
        ACTION_CLEAR_COUNTER = vmxpi.InputCaptureConfig.ACTION_CLEAR_COUNTER

    __channel = None
    __resHandle = None

    # 兩個channel共用一個時鐘，所以必須區分channel所用的資源類型
    __resAChannels = [0, 2, 4, 6, 8, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
    __resBChannels = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]

    def __init__(self, channel: int, counterClockSource=CounterClockSource.INTERNAL,
                 counterDirection=CounterDirection.DIRECTION_UP, slaveMode=SlaveMode.SLAVEMODE_DISABLED,
                 slaveModeTriggerSource=SlaveModeTriggerSource.TRIGGER_DYNAMIC,
                 captureChannelSource=CaptureChannelSource.CAPTURE_SIGNAL_DYNAMIC,
                 captureChannelPrescaler=CaptureChannelPrescaler.x1,
                 stallAction=StallAction.ACTION_NONE,
                 captureChannelFilterNumSamples=2):
        self.__channel = channel

        if channel in InputCapture.__resAChannels:
            self.__channelMode = vmxpi.InputCaptureInput
        elif channel in InputCapture.__resBChannels:
            self.__channelMode = vmxpi.InputCaptureInput2
        else:
            raise ValueError("Incorrect channel index.")

        __dioConfig = vmxpi.InputCaptureConfig();
        __dioConfig.SetCounterClockSource(counterClockSource.value)
        __dioConfig.SetCounterDirection(counterDirection.value)
        __dioConfig.SetSlaveMode(slaveMode.value)
        __dioConfig.SetSlaveModeTriggerSource(slaveModeTriggerSource.value)
        __dioConfig.SetCaptureChannelSource(vmxpi.InputCaptureConfigBase.CH1, captureChannelSource.value)
        __dioConfig.SetCaptureChannelSource(vmxpi.InputCaptureConfigBase.CH2, captureChannelSource.value)
        if HAL.getVMX().getIO().ChannelSupportsCapability(self.__channel, self.__channelMode):
            __dioConfig.SetCaptureChannelActiveEdge(vmxpi.InputCaptureConfigBase.CH1, vmxpi.InputCaptureConfig.ACTIVE_FALLING)
            __dioConfig.SetCaptureChannelActiveEdge(vmxpi.InputCaptureConfigBase.CH2, vmxpi.InputCaptureConfig.ACTIVE_RISING)
        else:
            __dioConfig.SetCaptureChannelActiveEdge(vmxpi.InputCaptureConfigBase.CH1, vmxpi.InputCaptureConfig.ACTIVE_RISING)
            __dioConfig.SetCaptureChannelActiveEdge(vmxpi.InputCaptureConfigBase.CH2, vmxpi.InputCaptureConfig.ACTIVE_FALLING)
        __dioConfig.SetCaptureChannelPrescaler(vmxpi.InputCaptureConfigBase.CH1, captureChannelPrescaler.value)
        __dioConfig.SetCaptureChannelPrescaler(vmxpi.InputCaptureConfigBase.CH2, captureChannelPrescaler.value)
        __dioConfig.SetStallAction(stallAction.value)
        filterNumber = __dioConfig.GetClosestCaptureCaptureFilterNumSamples(captureChannelFilterNumSamples)
        __dioConfig.SetCaptureChannelFilter(vmxpi.InputCaptureConfigBase.CH1, filterNumber)
        __dioConfig.SetCaptureChannelFilter(vmxpi.InputCaptureConfigBase.CH2, filterNumber)
        # success, self.__resHandle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(self.__channel, self.__channelMode), __dioConfig)
        success, self.__resHandle, vmxerr = HAL.getVMX().getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(self.__channel, self.__channelMode), __dioConfig)
        if not(success):
            logging.error("Error Activating Singlechannel Resource InputCapture for Channel index %d." % (self.__channel))
            HAL.DisplayVMXError(vmxerr)

    def get(self):
        """
        獲取輸入領取器計數

        Returns:
            int: CH1
            int: CH2
        """
        # success, count, vmxerr = HAL.getVMX().getIO().InputCapture_GetCount(self.__resHandle)
        success, ch1_count, ch2_count, vmxerr = HAL.getVMX().getIO().InputCapture_GetChannelCounts(self.__resHandle)
        if not(success):
            logging.error("Error Reading Input Capture counts for Resource Index %d" % (self.__channel))
            HAL.DisplayVMXError(vmxerr)
        return ch1_count, ch2_count