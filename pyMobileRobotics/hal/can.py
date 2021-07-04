from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
from enum import Enum
import logging



class CAN():
    """CAN Bus"""

    __can = None

    class Mode(Enum):
        LISTEN = vmxpi.VMXCAN.VMXCAN_LISTEN
        LOOPBACK = vmxpi.VMXCAN.VMXCAN_LOOPBACK
        NORMAL = vmxpi.VMXCAN.VMXCAN_NORMAL
        CONFIG = vmxpi.VMXCAN.VMXCAN_CONFIG
        OFF = vmxpi.VMXCAN.VMXCAN_OFF

    @staticmethod
    def getCAN():
        if CAN.__can == None:
            CAN.__can = HAL.getVMX().getCAN()
        return CAN.__can

    @staticmethod
    def getMode() -> Mode:
        success, can_mode, vmxerr = HAL.getVMX().getCAN().GetMode()
        if success:
            if can_mode == CAN.Mode.LISTEN.value:
                return CAN.Mode.LISTEN
            elif can_mode == CAN.Mode.LOOPBACK.value:
                return CAN.Mode.LOOPBACK
            elif can_mode == CAN.Mode.NORMAL.value:
                return CAN.Mode.NORMAL
            elif can_mode == CAN.Mode.CONFIG.value:
                return CAN.Mode.CONFIG
            elif can_mode == CAN.Mode.OFF.value:
                return CAN.Mode.OFF
            else:
                logging.warning("Unknown CAN Mode")
        else:
            logging.error("Error retrieving current CAN Mode")
            HAL.DisplayVMXError(vmxerr)

    """ TODO
    @staticmethod
    def getBusStatus():
        can_bus_status = vmxpi.VMXCANBusStatus()
        success, vmxerr = HAL.getVMX().getCAN().GetCANBUSStatus(can_bus_status)
        if success != True:
            logging.error("Error getting CAN BUS Status.")
            HAL.DisplayVMXError(vmxerr)
        else:
            if(can_bus_status.busWarning):
                print("CAN Bus Warning.")
            if(can_bus_status.busPassiveError):
                print("CAN Bus in Passive mode due to errors.")
            if(can_bus_status.busOffError):
                print("CAN Bus Transmitter Off due to errors.")
            if(can_bus_status.transmitErrorCount > 0):
                print("CAN Bus Tx Error Count:  %d" % can_bus_status.transmitErrorCount)
            if(can_bus_status.receiveErrorCount > 0):
                print("CAN Bus Rx Error Count:  %d" % can_bus_status.receiveErrorCount)
            if(can_bus_status.busOffCount > 0):
                print("CAN Bus Tx Off Count:  %d", can_bus_status.busOffCount)
            if(can_bus_status.txFullCount > 0):
                print("CAN Bus Tx Full Count:  %d", can_bus_status.txFullCount)
            if(can_bus_status.hwRxOverflow):
                print("CAN HW Receive Overflow detected.")
            if(can_bus_status.swRxOverflow):
                print("CAN SW Receive Overflow detected.")
            if(can_bus_status.busError):
                print("CAN Bus Error detected.")
            if(can_bus_status.wake):
                print("CAN Bus Wake occured.")
            if(can_bus_status.messageError):
                print("CAN Message Error detected.")
    """

    @staticmethod
    def directBuffer(bufferSize: int) -> vmxpi.DirectBuffer:
        return vmxpi.DirectBuffer(bufferSize)

    @staticmethod
    def sendMessage(messageID: int, data: bytearray, periodMS=0):
        msgSize = len(data)
        msg = vmxpi.VMXCANMessage()
        msg.messageID = messageID
        msg.dataSize = msgSize
        tx_data = CAN.directBuffer(msgSize)
        for x in range (0, msgSize, 1):
            tx_data.__setitem__(x, data[x])
        msg.setData(tx_data, msgSize)
        success, vmxerr = HAL.getVMX().getCAN().SendMessage(msg, periodMS)
        if success != True:
            logging.error("Error sending CAN message.")
            HAL.DisplayVMXError(vmxerr)

    @staticmethod
    def flushRxFIFO():
        success, vmxerr = HAL.getVMX().getCAN().FlushRxFIFO()
        if success != True:
            logging.error("Error Flushing CAN RX FIFO.")
            HAL.DisplayVMXError(vmxerr)

    @staticmethod
    def flushTxFIFO():
        success, vmxerr = HAL.getVMX().getCAN().FlushTxFIFO()
        if success != True:
            logging.error("Error Flushing CAN TX FIFO.")
            HAL.DisplayVMXError(vmxerr)

    @staticmethod
    def setMode(mode: Mode):
        success, vmxerr = HAL.getVMX().getCAN().SetMode(mode.value)
        if success != True:
            logging.error("Error setting CAN Mode to " + str(mode))
            HAL.DisplayVMXError(vmxerr)