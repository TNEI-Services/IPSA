from typing import List


class IscAnalysis:
    """
    There are separate classes for each analysis type, e.g. load flow, fault level and harmonic analysis.
    The IscNetwork class provides functions to obtain an IscAnalysis instance for each analysis type,
    for example GetAnalysisLF() returns an IscAnalysisLF object.
    Motor start analysis options are provided under the fault level analysis class.
    """
    def GetIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The integer value for the field.
        :rtype: int
        """
        pass

    def GetDValue(self, nFieldIndex: int) -> float:
        """
        Returns a float value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The float value for the field.
        :rtype: float
        """
        pass

    def GetSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The string value for the field.
        :rtype: str
        """
        pass

    def GetBValue(self, nFieldIndex: int) -> bool:
        """
        Returns a boolean value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The boolean value for the field.
        :rtype: bool
        """
        pass

    def SetIValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the integer value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :param nValue: The integer value that will be set.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetDValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the float value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :param dValue: The float value that will be set.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetSValue(self, nFieldIndex: int, strValue: str) -> bool:
        """
        Sets the string value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :param strValue: The string value that will be set.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetBValue(self, nFieldIndex: int, bValue: bool) -> bool:
        """
        Sets the integer value for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :param bValue: The boolean value that will be set.
        :type bValue: bool
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetFieldType(self, nFieldIndex: int) -> str:
        """
        Returns the field type as a string for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The field type.
        :rtype: str
        """
        pass

    def GetFieldName(self, nFieldIndex: int) -> str:
        """
        Returns the field name as a string for the enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The field name.
        :rtype: str
        """
        pass

    def SetBusesToFault(self, nUIDs: List[int]) -> None:
        """
        Specifies which busbars will be faulted as defined by the list of busbar UIDs.
        Only applicable when the FaultStudyType is set to FaultSelectedBusbars.

        :param nUIDs: The list of busbar UIDs which will be faulted.
        :type nUIDs: list(int)
        """
        pass

    def GetBusesToFault(self) -> List[int]:
        """
        Returns a list of busbar UIDs representing the busbars that have been selected to be faulted.

        :return: The list of faulted busbars.
        :rtype: list(int)
        """
        pass