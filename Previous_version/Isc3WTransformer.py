class Isc3WTransformer:
    """
    The Isc3WTransformer class provides access to an Ipsa 3-winding transformer,
    to set and get data values and to retrieve load flow and fault level results.
    In the following functions and field values the following conventions are used:

        - Primary winding = winding 1. Winding number **nWinding** = 1
        - Secondary winding = winding 2. Winding number **nWinding** = 2
        - Tertiary winding = winding 3. Winding number **nWinding** = 3
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

    def GetWindingRatingMVA(self, nWinding: int, nRatingIndex: int) -> float:
        """
        Returns the MVA rating for the 3-winding transformer for the specified rating set.

        :param nWinding: The winding number.
        :type nWinding: int
        :param nRatingIndex: The specified rating index.
        :type nRatingIndex: int
        :return: The MVA rating for the 3-winding transformer.
        :rtype: float
        """
        pass

    def SetWindingRatingMVA(self, nSection: int, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating to dRatingMVA for the specified rating set.

        :param nSection: The number of sections.
        :type nSection: int
        :param nRatingIndex: The specified rating index.
        :type nRatingIndex: int
        :param dRatingMVA: The MVA rating that is set.
        :type dRatingMVA: float
        """
        pass

    def GetLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest 3-winding transformer end power in MVA.

        :return: The highest 3-winding transformer end power in MVA.
        :rtype: float
        """
        pass

    def GetLargestPowerMagnitudekVA(self) -> float:
        """
        Returns the highest 3-winding transformer end power in kVA.

        :return: The highest 3-winding transformer end power in kVA.
        :rtype: float
        """
        pass

    def GetLargestRealPowerMW(self) -> float:
        """
        Returns the highest 3-winding transformer end power in MW.

        :return: The highest 3-winding transformer end power in MW.
        :rtype: float
        """
        pass

    def GetLargestReactivePowerMVAr(self) -> float:
        """
        Returns the highest 3-winding transformer end power in MVAr.

        :return: The highest 3-winding transformer end power in MVAr.
        :rtype: float
        """
        pass

    def GetLargestRealPowerkW(self) -> float:
        """
        Returns the highest 3-winding transformer end power in kW.

        :return: The highest 3-winding transformer end power in kW.
        :rtype: float
        """
        pass

    def GetLargestReactivePowerkVAr(self) -> float:
        """
        Returns the highest 3-winding transformer end power in kVAr.

        :return: The highest 3-winding transformer end power in kVAr.
        :rtype: float
        """
        pass

    def GetLossesMW(self) -> float:
        """
        Returns the 3-winding transformer losses in MW.

        :return: The 3-winding transformer losses in MW.
        :rtype: float
        """
        pass

    def GetLossesMVAr(self) -> float:
        """
        Returns the 3-winding transformer losses in MVAr.

        :return: The 3-winding transformer losses in MVAr.
        :rtype: float
        """
        pass

    def GetLosseskW(self) -> float:
        """
        Returns the 3-winding transformer losses in kW.

        :return: The 3-winding transformer losses in kW.
        :rtype: float
        """
        pass

    def GetLosseskVAr(self) -> float:
        """
        Returns the 3-winding transformer losses in kVAr.

        :return: The 3-winding transformer losses in kVAr.
        :rtype: float
        """
        pass

    def GetWindingPowerMagnitudeMVA(self, nWinding: int) -> float:
        """
        Returns the MVA power flow in the specified winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The MVA power flow in the specified winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetWindingPowerMagnitudekVA(self, nWinding: int) -> float:
        """
        Returns the kVA power flow in the specified winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The kVA power flow in the specified winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetWindingRealPowerMW(self, nWinding: int) -> float:
        """
        Returns the MW power flow in the specified winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The MW power flow in the specified winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetWindingReactivePowerMVAr(self, nWinding: int) -> float:
        """
        Returns the MVAr power flow in the specified winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The MVAr power flow in the specified winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetWindingRealPowerkW(self, nWinding: int) -> float:
        """
        Returns the kW power flow in the specified winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The kW power flow in the specified winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetWindingReactivePowerkVAr(self, nWinding: int) -> float:
        """
        Returns the kVAr power flow in the specified winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The kVAr power flow in the specified winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetFaultRedComponentMVA(self, nWinding: int) -> float:
        """
        Returns the red phase fault level component in MVA for the specified winding of the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The red phase fault level component in MVA for the specified winding of the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentMVA(self, nWinding: int) -> float:
        """
        Returns the yellow phase fault level component in MVA for the specified winding of the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The yellow phase fault level component in MVA for the specified winding of the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentMVA(self, nWinding: int) -> float:
        """
        Returns the blue phase fault level component in MVA for the specified winding of the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The blue phase fault level component in MVA for the specified winding of the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentMVA(self, nWinding: int) -> float:
        """
        Returns the positive sequence fault level component in MVA for the specified winding of the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The positive sequence fault level component in MVA for the specified winding of the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentMVA(self, nWinding: int) -> float:
        """
        Returns the negative sequence fault level component in MVA for the specified winding of the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The negative sequence fault level component in MVA for the specified winding of the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentMVA(self, nWinding: int) -> float:
        """
        Returns the zero sequence fault level component in MVA for the specified winding of the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The zero sequence fault level component in MVA for the specified winding of the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetCurrentMagnitude(self, nWinding: int, dOrder: float) -> float:
        """
        Returns the current magnitude for the specified winding in per unit on the network base for the harmonic order.

        :param nWinding: The winding number.
        :type nWinding: int
        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The current magnitude in per unit.
        :rtype: float
        """
        pass

    def GetCurrentAngle(self, nWinding: int, dOrder: float) -> float:
        """
        Returns the current angle magnitude for the specified winding in radians for the harmonic order.

        :param nWinding: The winding number.
        :type nWinding: int
        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The current angle magnitude in radians.
        :rtype: float
        """
        pass

    def GetResistance(self, nWinding: int, dOrder: float) -> float:
        """
        Returns the transformer harmonic resistance for the specified winding in per unit on the network base
        for the harmonic order.

        :param nWinding: The winding number.
        :type nWinding: int
        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The transformer harmonic resistance in per unit.
        :rtype: float
        """
        pass

    def GetReactance(self, nWinding: int, dOrder: float) -> float:
        """
        Returns the transformer harmonic reactance for the specified winding in per unit on the network base
        for the harmonic order.

        :param nWinding: The winding number.
        :type nWinding: int
        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The transformer harmonic reactance in per unit.
        :rtype: float
        """
        pass
