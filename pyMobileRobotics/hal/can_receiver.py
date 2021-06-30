from pyMobileRobotics.hal import vmxpi
from pyMobileRobotics.hal.hal import HAL
from pyMobileRobotics.hal.can import CAN
import logging



class CANReceiver(CAN):

    def __init__(self, messageID = 0x0000000, messageMask=0x0000000, maxMessages=100):
        success, self.__canrxhandle, vmxerr  = CAN.getCAN().OpenReceiveStream(messageID, messageMask, maxMessages)
        if not(success):
            logging.error("Error opening CAN RX Stream")
            HAL.DisplayVMXError(vmxerr)

    def readMessage(self, messagesToRead=1):
        rx_data = CAN.directBuffer(8)
        stream_msg = vmxpi.VMXCANTimestampedMessage();
        success, num_msgs_read, vmxerr = HAL.getVMX().getCAN().ReadReceiveStream(self.__canrxhandle, stream_msg, messagesToRead)
        if not(success):
            logging.error("Error invoking CAN ReadReceiveStream for stream %d" % self.__canrxhandle)
            HAL.DisplayVMXError(vmxerr)
        is_eid = True
        if (stream_msg.messageID & vmxpi.VMXCAN_IS_FRAME_11BIT) !=0:
            is_eid = False;
            stream_msg.messageID = stream_msg.messageID &(~vmxpi.VMXCAN_IS_FRAME_11BIT);
        stream_msg.messageID = stream_msg.messageID & ~(vmxpi.VMXCAN_IS_FRAME_REMOTE);
        stream_msg.getData(rx_data, stream_msg.dataSize)
        data = []
        for i in range(stream_msg.dataSize):
            data.append(rx_data[i])
        return num_msgs_read, stream_msg.messageID, stream_msg.dataSize, data, stream_msg