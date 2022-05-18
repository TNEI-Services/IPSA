class IscUnbalancedLoad:
    """
    The IscUnbalancedLoad class provides access to the three phase unbalanced load components
    to get and set data values.
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

    def GetTotalMeanMVA(self) -> float:
        """
        Returns the mean load power across all 3 phases in MVA.

        :return: The mean load power across all 3 phases in MVA.
        :rtype: float
        """
        pass

    def GetTotalMeankVA(self) -> float:
        """
        Returns the mean load power across all 3 phases in kVA.

        :return: The mean load power across all 3 phases in kVA.
        :rtype: float
        """
        pass

    def GetRealMeanMW(self) -> float:
        """
        Returns the mean load power across all 3 phases in MW.

        :return: The mean load power across all 3 phases in MW.
        :rtype: float
        """
        pass

    def GetRealMeankW(self) -> float:
        """
        Returns the mean load power across all 3 phases in kW.

        :return: The mean load power across all 3 phases in kW.
        :rtype: float
        """
        pass

    def GetReactiveMeanMVAr(self) -> float:
        """
        Returns the mean load power across all 3 phases in MVAr.

        :return: The mean load power across all 3 phases in MVAr.
        :rtype: float
        """
        pass

    def GetReactiveMeankVAr(self) -> float:
        """
        Returns the mean load power across all 3 phases in kVAr.

        :return: The mean load power across all 3 phases in kVAr.
        :rtype: float
        """
        pass

    def GetTotalMaxMVA(self) -> float:
        """
        Returns the highest load power across all 3 phases in MVA.

        :return: The highest load power across all 3 phases in MVA.
        :rtype: float
        """
        pass

    def GetTotalMaxkVA(self) -> float:
        """
        Returns the highest load power across all 3 phases in kVA.

        :return: The highest load power across all 3 phases in kVA.
        :rtype: float
        """
        pass

    def GetRealMaxMW(self) -> float:
        """
        Returns the highest load power across all 3 phases in MW.

        :return: The highest load power across all 3 phases in MW.
        :rtype: float
        """
        pass

    def GetRealMaxkW(self) -> float:
        """
        Returns the highest load power across all 3 phases in kW.

        :return: The highest load power across all 3 phases in kW.
        :rtype: float
        """
        pass

    def GetReactiveMaxMVAr(self) -> float:
        """
        Returns the highest load power across all 3 phases in MVAr.

        :return: The highest load power across all 3 phases in MVAr.
        :rtype: float
        """
        pass

    def GetReactiveMaxkVAr(self) -> float:
        """
        Returns the highest load power across all 3 phases in kVAr.

        :return: The highest load power across all 3 phases in kVAr.
        :rtype: float
        """
        pass

    def GetRealPowerAMW(self) -> float:
        """
        Returns the A phase power for the load in MW.

        :return: The A phase power for the load in MW.
        :rtype: float
        """
        pass

    def GetRealPowerBMW(self) -> float:
        """
        Returns the B phase power for the load in MW.

        :return: The B phase power for the load in MW.
        :rtype: float
        """
        pass

    def GetRealPowerCMW(self) -> float:
        """
        Returns the C phase power for the load in MW.

        :return: The C phase power for the load in MW.
        :rtype: float
        """
        pass

    def GetRealPowerAkW(self) -> float:
        """
        Returns the A phase power for the load in kW.

        :return: The A phase power for the load in kW.
        :rtype: float
        """
        pass

    def GetRealPowerBkW(self) -> float:
        """
        Returns the B phase power for the load in kW.

        :return: The B phase power for the load in kW.
        :rtype: float
        """
        pass

    def GetRealPowerCkW(self) -> float:
        """
        Returns the C phase power for the load in kW.

        :return: The C phase power for the load in kW.
        :rtype: float
        """
        pass

    def GetRealPowerAMVAr(self) -> float:
        """
        Returns the A phase power for the load in MVAr.

        :return: The A phase power for the load in MVAr.
        :rtype: float
        """
        pass

    def GetRealPowerBMVAr(self) -> float:
        """
        Returns the B phase power for the load in MVAr.

        :return: The B phase power for the load in MVAr.
        :rtype: float
        """
        pass

    def GetRealPowerCMVAr(self) -> float:
        """
        Returns the C phase power for the load in MVAr.

        :return: The C phase power for the load in MVAr.
        :rtype: float
        """
        pass

    def GetRealPowerAkVAr(self) -> float:
        """
        Returns the A phase power for the load in kVAr.

        :return: The A phase power for the load in kVAr.
        :rtype: float
        """
        pass

    def GetRealPowerBkVAr(self) -> float:
        """
        Returns the B phase power for the load in kVAr.

        :return: The B phase power for the load in kVAr.
        :rtype: float
        """
        pass

    def GetRealPowerCkVAr(self) -> float:
        """
        Returns the C phase power for the load in kVAr.

        :return: The C phase power for the load in kVAr.
        :rtype: float
        """
        pass
