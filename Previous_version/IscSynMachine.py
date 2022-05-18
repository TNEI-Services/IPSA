class IscSynMachine:
    """
    The IscSynMachine class provides access to an Ipsa generator (or more specifically, a synchronous machine),
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

    def GetVoltageMagnitudePU(self) -> float:
        """
        Returns the generator voltage magnitude in per unit.

        :return: The generator voltage magnitude in per unit.
        :rtype: float
        """
        pass

    def GetVoltageAngleRad(self) -> float:
        """
        Returns the voltage angle in radians.

        :return: The voltage angle.
        :rtype: float
        """
        pass

    def GetVoltageAngleDeg(self) -> float:
        """
        Returns the voltage angle in degrees.

        :return: The voltage angle.
        :rtype: float
        """
        pass

    def GetPowerMagnitudeMVA(self) -> float:
        """
        Returns the generator output in MVA.

        :return: The generator output in MVA.
        :rtype: float
        """
        pass

    def GetPowerMagnitudekVA(self) -> float:
        """
        Returns the generator output in kVA.

        :return: The generator output in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerMW(self) -> float:
        """
        Returns the generator output in MW.

        :return: The generator output in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerMVAr(self) -> float:
        """
        Returns the generator output in MVAr.

        :return: The generator output in MVAr.
        :rtype: float
        """
        pass

    def GetRealPowerkW(self) -> float:
        """
        Returns the generator output in kW.

        :return: The generator output in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerkVAr(self) -> float:
        """
        Returns the generator output in kVAr.

        :return: The generator output in kVAr.
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

    def GetImpedanceMagnitude(self, dOrder: float) -> float:
        """
        Returns the impedance magnitude in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The impedance magnitude in per unit.
        :rtype: float
        """
        pass
