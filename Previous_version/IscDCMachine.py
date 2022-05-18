class IscDCMachine:
    """
    The IscDCMachine class provides access to an Ipsa DC machine,
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

    def GetRealMechanicalPowerMW(self) -> float:
        """
        Returns the mechanical output power of the DC machine in MW.

        :return: The mechanical output power of the DC machine in MW.
        :rtype: float
        """
        pass

    def GetRealMechanicalPowerkW(self) -> float:
        """
        Returns the mechanical output power of the DC machine in kW.

        :return: The mechanical output power of the DC machine in kW.
        :rtype: float
        """
        pass

    def GetRealElectricalPowerMW(self) -> float:
        """
        Returns the electrical output power of the DC machine in MW.

        :return: The electrical output power of the DC machine in MW.
        :rtype: float
        """
        pass

    def GetRealElectricalPowerkW(self) -> float:
        """
        Returns the electrical output power of the DC machine in kW.

        :return: The electrical output power of the DC machine in kW.
        :rtype: float
        """
        pass

    def GetTotalPowerMVA(self) -> float:
        """
        Returns the total output power of the DC machine in MVA.

        :return: The total output power of the DC machine in MVA.
        :rtype: float
        """
        pass

    def GetTotalPowerkVA(self) -> float:
        """
        Returns the total output power of the DC machine in kVA.

        :return: The total output power of the DC machine in kVA.
        :rtype: float
        """
        pass

    def GetPowerLossMW(self) -> float:
        """
        Returns the power loss of the DC machine in MW.

        :return: The power loss of the DC machine in MW.
        :rtype: float
        """
        pass

    def GetPowerLosskW(self) -> float:
        """
        Returns the power loss of the DC machine in kW.

        :return: The power loss of the DC machine in kW.
        :rtype: float
        """
        pass

    def GetCurrentkA(self) -> float:
        """
        Returns the DC machine injected current in kA.

        :return: The DC machine injected current in kA.
        :rtype: float
        """
        pass
