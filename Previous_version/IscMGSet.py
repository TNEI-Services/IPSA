class IscMGSet:
    """
    The IscMGSet class provides access to an Ipsa motor-generator set,
    to set and get data values and to retrieve load flow results.
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

    def GetACRealPowerMW(self) -> float:
        """
        Returns the AC real power output of the motor-generator set in MW.

        :return: The AC real power output of the motor-generator set in MW.
        :rtype: float
        """
        pass

    def GetACRealPowerkW(self) -> float:
        """
        Returns the AC real power output of the motor-generator set in kW.

        :return: The AC real power output of the motor-generator set in kW.
        :rtype: float
        """
        pass

    def GetACReactivePowerMVAr(self) -> float:
        """
        Returns the AC reactive power output of the motor-generator set in MVAr.

        :return: The AC reactive power output of the motor-generator set in MVAr.
        :rtype: float
        """
        pass

    def GetACReactivePowerkVAr(self) -> float:
        """
        Returns the AC reactive power output of the motor-generator set in kVAr.

        :return: The AC reactive power output of the motor-generator set in kVAr.
        :rtype: float
        """
        pass

    def GetACTotalPowerMVA(self) -> float:
        """
        Returns the total AC output power of the motor-generator set in MVA.

        :return: The total AC output power of the motor-generator set in MVA.
        :rtype: float
        """
        pass

    def GetACTotalPowerkVA(self) -> float:
        """
        Returns the total AC output power of the motor-generator set in kVA.

        :return: The total AC output power of the motor-generator set in kVA.
        :rtype: float
        """
        pass

    def GetACCurrentkA(self) -> float:
        """
        Returns the AC current of the motor-generator set in kA.

        :return: The AC current of the motor-generator set in kA.
        :rtype: float
        """
        pass

    def GetDCRealPowerMW(self) -> float:
        """
        Returns the DC real power output of the motor-generator set in MW.

        :return: The DC real power output of the motor-generator set in MW.
        :rtype: float
        """
        pass

    def GetDCRealPowerkW(self) -> float:
        """
        Returns the DC real power output of the motor-generator set in kW.

        :return: The DC real power output of the motor-generator set in kW.
        :rtype: float
        """
        pass

    def GetDCTotalPowerMVA(self) -> float:
        """
        Returns the total DC output power of the motor-generator set in MVA.

        :return: The total DC output power of the motor-generator set in MVA.
        :rtype: float
        """
        pass

    def GetDCTotalPowerkVA(self) -> float:
        """
        Returns the total DC output power of the motor-generator set in kVA.

        :return: The total DC output power of the motor-generator set in kVA.
        :rtype: float
        """
        pass

    def GetDCCurrentkA(self) -> float:
        """
        Returns the DC current of the motor-generator set in kA.

        :return: The DC current of the motor-generator set in kA.
        :rtype: float
        """
        pass
