# ----------------------------------------------------------------------------
#  Copyright (c) 2021 CISH Robotics. All Rights Reserved.
# ----------------------------------------------------------------------------

import pyMobileRobotics
from studica.titan_quad import TitanQuad
from simple_pid import PID
import time

class ExampleSubsystem(pyMobileRobotics.SubsystemBase):

    def __init__(self):
        # 必須要先呼叫父類建構式，以進行各種初始化並註冊子系統。
        super().__init__()
        self.__io = pyMobileRobotics.DigitalInput(8)
        self.__ai = pyMobileRobotics.AnalogInput(22)
        self.__encoder = pyMobileRobotics.Encoder(0, 1)
        self.__titan = TitanQuad(titanID=42, m0Frequency = 15600)
        self.__titan.resetEncoder(0)
        pyMobileRobotics.NetworkVariables.setValue('testVar', 'qwq')
        pyMobileRobotics.NetworkVariables.setValue('m0Setpoint', float(0))
        pyMobileRobotics.NetworkVariables.setValue('kp', 1.0)
        pyMobileRobotics.NetworkVariables.setValue('ki', 0.0)
        pyMobileRobotics.NetworkVariables.setValue('kd', 0.0)
        kp = pyMobileRobotics.NetworkVariables.getValue('kp')
        ki = pyMobileRobotics.NetworkVariables.getValue('ki')
        kd = pyMobileRobotics.NetworkVariables.getValue('kd')
        self.__pid = PID(kp, ki, kd)
        self.__pid.sample_time = 0.015
        self.__pid.output_limits = (-100, 100)


    __lastTime = time.time()
    __lastValue = False
    __deg = 0
    def periodic(self):
        high = self.__io.get()

        kp = pyMobileRobotics.NetworkVariables.getValue('kp')
        ki = pyMobileRobotics.NetworkVariables.getValue('ki')
        kd = pyMobileRobotics.NetworkVariables.getValue('kd')
        self.__pid.Kp = kp
        self.__pid.Ki = ki
        self.__pid.Kd = kd

        self.__deg += 11
        self.__pid.setpoint = pyMobileRobotics.NetworkVariables.getValue('m0Setpoint')
        encVal, encDir = self.__encoder.get()
        # encVal = self.__titan.getEncoderValue(0)
        encDeg = encVal * 0.25
        speed = self.__pid(encDeg)
        speed /= 100
        self.__titan.setSpeed(0, speed)
        pyMobileRobotics.NetworkVariables.setValue('ENC0_Value', encDeg)
        testVarData = pyMobileRobotics.NetworkVariables.getValue('testVar')
        # pyMobileRobotics.logging.debug("testVarData=" + str(testVarData))
        # pyMobileRobotics.logging.debug("set=" + str(self.__pid.setpoint) + "/encDeg=" + str(encDeg))
        if high != self.__lastValue:
            if high:
                pyMobileRobotics.RobotState.setAutonomous()
                self.__titan.setEnabled()
            else:
                pyMobileRobotics.RobotState.setDisabled()
                self.__titan.setDisabled()
            self.__lastValue = high
        pyMobileRobotics.NetworkVariables.setValue('periodic', time.time() - self.__lastTime)
        # pyMobileRobotics.logging.debug("periodic=" + str(time.time() - self.__lastTime))
        self.__lastTime = time.time()