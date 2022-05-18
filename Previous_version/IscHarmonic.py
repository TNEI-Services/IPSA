from typing import Dict


class IscHarmonic:
    """
    The IscHarmonic class provides access to an Ipsa harmonic source.
    Individual harmonic orders are indexed using an integer number.
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

    def SetOrder(self, nOrderIndex: int, h: float) -> None:
        """
        Sets the harmonic order index to the selected harmonic order.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :param nOrderIndex: The selected harmonic order.
        :type nOrderIndex: float
        """
        pass

    def GetOrder(self, nOrderIndex: int) -> float:
        """
        Returns the harmonic order for the order index.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :return: The harmonic order.
        :rtype: float
        """
        pass

    def GetMagnitudePU(self, nOrderIndex: int) -> float:
        """
        Gets the current or voltage magnitude for the order index.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :return: The current or voltage magnitude.
        :rtype: float
        """
        pass

    def SetMagnitudePU(self, nOrderIndex: int, dMagnitude: float) -> None:
        """
        Sets the current or voltage magnitude for the order index.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :param dMagnitude: The current or voltage magnitude.
        :type dMagnitude: float
        """
        pass

    def SetAngleDeg(self, nOrderIndex: int, dAngleDeg: float) -> None:
        """
        Sets the current or voltage angle in degrees for the order index.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :param dAngleDeg: The current or voltage angle in degrees.
        :type dAngleDeg: float
        """
        pass

    def GetAngleRad(self, nOrderIndex: int) -> float:
        """
        Gets the current or voltage angle in radians for the order index.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :return: The current or voltage angle in radians.
        :rtype: float
        """
        pass

    def SetAngleRad(self, nOrderIndex: int, dAngleRad: float) -> None:
        """
        Sets the current or voltage angle in radians for the order index.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :param dAngleRad: The current or voltage angle in radians.
        :type dAngleRad: float
        """
        pass

    def GetHarmonicR(self) -> Dict[int, float]:
        """
        Returns a dictionary of harmonic resistances.
        The dictionary key values are the order indexes and the values are the harmonic resistances in per unit.

        :return: A dictionary of harmonic resistances.
        :rtype: dict(int, float)
        """
        pass

    def GetHarmonicX(self) -> Dict[int, float]:
        """
        Returns a dictionary of harmonic reactances.
        The dictionary key values are the order indexes and the values are the harmonic reactances in per unit.

        :return: A dictionary of harmonic reactances.
        :rtype: dict(int, float)
        """
        pass

    def SetHarmonicR(self, dicHarmonic: Dict[int, float]) -> None:
        """
        Sets the harmonic resistances from a dictionary.
        The dictionary key values are the order indexes and the values are the harmonic resistances in per unit.

        :param dicHarmonic: The harmonic resistances.
        :type dicHarmonic: dict(int,float)
        """
        pass

    def SetHarmonicX(self, dicHarmonic: Dict[int, float]) -> None:
        """
        Sets the harmonic reactances from a dictionary.
        The dictionary key values are the order indexes and the values are the harmonic reactances in per unit.

        :param dicHarmonic: The harmonic reactances.
        :type dicHarmonic: dict(int,float)
        """
        pass

