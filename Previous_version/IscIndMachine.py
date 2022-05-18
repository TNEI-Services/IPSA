class IscIndMachine:
    """
    The IscIndMachine class provides access to an Ipsa induction machine,
    to set and get data values and to retrieve load flow and fault level results.
    """
    def SetName(self, strName: str) -> bool:
        """
        Sets the name as a string.

        :param strName: The selected string name.
        :type strName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDValue(self, nFieldIndex: int) -> float:
        """
        Returns a double value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: str
        """
        pass

    def GetBValue(self, nFieldIndex: int) -> bool:
        """
        Returns a boolean value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The boolean value.
        :rtype: bool
        """
        pass

    def SetIValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the value for the enumerated field from an integer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetDValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the value for the enumerated field from a double.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetSValue(self, nFieldIndex: int, strValue: int) -> bool:
        """
        Sets the value for the enumerated field from a string.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetBValue(self, nFieldIndex: int, bValue: bool) -> bool:
        """
        Sets the value for the enumerated field from boolean.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param bValue: The given boolean value.
        :type bValue: bool
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetStatorPowerMagnitudeMVA(self) -> float:
        """
        Returns stator power in MVA.

        :return: The stator power in MVA.
        :rtype: float
        """
        pass

    def GetStatorPowerMagnitudekVA(self) -> float:
        """
        Returns stator power in kVA.

        :return: The stator power in kVA.
        :rtype: float
        """
        pass

    def GetStatorRealPowerMW(self) -> float:
        """
        Returns stator power in MW.

        :return: The stator power in MW.
        :rtype: float
        """
        pass

    def GetStatorReactivePowerMVAr(self) -> float:
        """
        Returns stator power in MVAr.

        :return: The stator power in MVAr.
        :rtype: float
        """
        pass

    def GetStatorRealPowerkW(self) -> float:
        """
        Returns stator power in kW.

        :return: The stator power in kW.
        :rtype: float
        """
        pass

    def GetStatorReactivePowerkVAr(self) -> float:
        """
        Returns stator power in kVAr.

        :return: The stator power in kVAr.
        :rtype: float
        """
        pass

    def GetRotorPowerMagnitudeMVA(self) -> float:
        """
        Returns rotor power in MVA.

        :return: The rotor power in MVA.
        :rtype: float
        """
        pass

    def GetRotorPowerMagnitudekVA(self) -> float:
        """
        Returns rotor power in kVA.

        :return: The rotor power in kVA.
        :rtype: float
        """
        pass

    def GetRotorRealPowerMW(self) -> float:
        """
        Returns rotor power in MW.

        :return: The rotor power in MW.
        :rtype: float
        """
        pass

    def GetRotorReactivePowerMVAr(self) -> float:
        """
        Returns rotor power in MVAr.

        :return: The rotor power in MVAr.
        :rtype: float
        """
        pass

    def GetRotorRealPowerkW(self) -> float:
        """
        Returns rotor power in kW.

        :return: The rotor power in kW.
        :rtype: float
        """
        pass

    def GetRotorReactivePowerkVAr(self) -> float:
        """
        Returns rotor power in kVAr.

        :return: The rotor power in kVAr.
        :rtype: float
        """
        pass

    def GetMechanicalRealPowerMW(self) -> float:
        """
        Returns mechanical shaft power in MW.

        :return: The mechanical shaft power in MW.
        :rtype: float
        """
        pass

    def GetMechanicalRealPowerkW(self) -> float:
        """
        Returns mechanical shaft power in kW.

        :return: The mechanical shaft power in kW.
        :rtype: float
        """
        pass

    def GetSlipPU(self) -> float:
        """
        Returns the motor slip in per unit where 0.0 is synchronous speed, -1.0 if stationary.

        :return: The motor slip in per unit.
        :rtype: float
        """
        pass

    def GetSlipPC(self) -> float:
        """
        Returns the motor slip in percent where 0% is synchronous speed, -100% if stationary.

        :return: The motor slip in percent.
        :rtype: float
        """
        pass

    def GetEfficiencyPC(self) -> float:
        """
        Returns the motor efficiency in percent.

        :return: The motor efficiency in percent.
        :rtype: float
        """
        pass

    def GetPowerFactor(self) -> float:
        """
        Returns the operating power factor.

        :return: The operating power factor.
        :rtype: float
        """
        pass

    def GetCurrentkA(self) -> float:
        """
        Returns the total current in kA.

        :return: The total current in kA.
        :rtype: float
        """
        pass

    def GetCurrentA(self) -> float:
        """
        Returns the total current in Amps.

        :return: The total current in Amps.
        :rtype: float
        """
        pass

    def GetTorqueMNm(self) -> float:
        """
        Returns the shaft torque in MNm.

        :return: The shaft torque in MNm.
        :rtype: float
        """
        pass

    def GetTorquekNm(self) -> float:
        """
        Returns the shaft torque in kNm.

        :return: The shaft torque in kNm.
        :rtype: float
        """
        pass

    def GetFaultRedComponentMVA(self) -> float:
        """
        Returns the red phase component of fault level in MVA.

        :return: The red phase component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentMVA(self) -> float:
        """
        Returns the yellow phase component of fault level in MVA.

        :return: The yellow phase component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentMVA(self) -> float:
        """
        Returns the blue phase component of fault level in MVA.

        :return: The blue phase component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentMVA(self) -> float:
        """
        Returns the positive sequence component of fault level in MVA.

        :return: The positive sequence component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentMVA(self) -> float:
        """
        Returns the negative sequence component of fault level in MVA.

        :return: The negative sequence component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentMVA(self) -> float:
        """
        Returns the zero sequence component of fault level in MVA.

        :return: The zero sequence component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetCurrentMagnitude(self, dOrder: float) -> float:
        """
        Returns the current magnitude in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The current magnitude in per unit.
        :rtype: float
        """
        pass

    def GetCurrentAngle(self, dOrder: float) -> float:
        """
        Returns the current angle in radians for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The current angle in radians.
        :rtype: float
        """
        pass
