# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics as mb
import studica


class DriveTrain(mb.SubsystemBase):

    def __init__(self):
        super().__init__()
        self.__encoder = mb.Encoder(0, 1)
        self.__titan = studica.TitanQuad(titanID=42)
        self.__titan.resetEncoder(0)
        mb.NetworkVariables.setValue('M0_Speed', float(0))
        kp = mb.NetworkVariables.setValue('kp', 1.5)
        ki = mb.NetworkVariables.setValue('ki', 0.0)
        kd = mb.NetworkVariables.setValue('kd', 0.03)
        self.__pid = mb.PID(kp, ki, kd)
        self.__pid.sample_time = 0.015
        self.__pid.output_limits = (-100, 100)

    def getEncoderDeg(self, motorID: int) -> float:
        if motorID == 0:
            encVal, encDir = self.__encoder.get()
            encDeg = encVal * 0.25
            return encDeg

    def setMotorSpeed(self, motorID: int, speed: float):
        if motorID == 0:
            self.__pid.setpoint += speed * 0.015

    def setPID(self, motorID: int, Kp: float, Ki: float, Kd: float):
        if motorID == 0:
            self.__pid.Kp = Kp
            self.__pid.Ki = Ki
            self.__pid.Kd = Kd

    def periodic(self):
        kp = mb.NetworkVariables.getValue('kp')
        ki = mb.NetworkVariables.getValue('ki')
        kd = mb.NetworkVariables.getValue('kd')
        self.setPID(0, kp, ki, kd)
        speed = mb.NetworkVariables.getValue('M0_Speed')
        self.setMotorSpeed(0, speed)

        controlSpeed = self.__pid(self.getEncoderDeg(0)) / 100
        self.__titan.setSpeed(0, controlSpeed)

        if not(mb.RobotState.isDisabled()):
            self.__titan.setEnabled()
        else:
            self.__titan.setDisabled()