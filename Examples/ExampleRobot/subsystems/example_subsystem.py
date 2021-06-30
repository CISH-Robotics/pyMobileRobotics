# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics

class ExampleSubsystem(pyMobileRobotics.SubsystemBase):

    def __init__(self):
        # 必須要先呼叫父類建構式，以進行各種初始化並註冊子系統。
        super().__init__()
        self.__io = pyMobileRobotics.DigitalInput(8)
        self.__ai = pyMobileRobotics.AnalogInput(22)
        pyMobileRobotics.CAN.sendMessage(0x20C006A, bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]), periodMS=50)
        self.canReceiver = pyMobileRobotics.CANReceiver(0x20C0A2A, 0xFFFFFFF, 1)


    def periodic(self):
        high = self.__io.get()
        voltage = self.__ai.getVoltage()
        numMsgRead, messageID, messageDataSize, messageData, _ = self.canReceiver.readMessage()
        pyMobileRobotics.logging.debug("ID=" + hex(messageID) + "/Size=" + str(messageDataSize) + "/Message=" + str(messageData))
        if high:
            pyMobileRobotics.RobotState.setAutonomous()
        else:
            pyMobileRobotics.RobotState.setDisabled()