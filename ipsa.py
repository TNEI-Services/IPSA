from typing import Dict, List, overload, Tuple, Union


class Isc3WTransformer:
    """
    Provides access to an IPSA 3-winding transformer.
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

    def GetListDValue(self, nFieldIndex: int) -> list[float]:
        """
        Returns a list of double values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[float]
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

    def SetListDValue(self, nFieldIndex: int, lDValue: list[float]) -> bool:
        """
        Sets the value for the enumerated field from a list of doubles.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lDValue: The given list of double values.
        :type lDValue: list[float]
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

    def GetDCLFLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest 3-winding transformer end power in MVA.

        :return: The highest 3-winding transformer end power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFLargestPowerMagnitudekVA(self) -> float:
        """
        Returns the highest 3-winding transformer end power in kVA.

        :return: The highest 3-winding transformer end power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFLargestRealPowerMW(self) -> float:
        """
        Returns the highest 3-winding transformer end power in MW.

        :return: The highest 3-winding transformer end power in MW.
        :rtype: float
        """
        pass

    def GetDCLFLargestRealPowerkW(self) -> float:
        """
        Returns the highest 3-winding transformer end power in kW.

        :return: The highest 3-winding transformer end power in kW.
        :rtype: float
        """
        pass

    def GetDCLFLossesMW(self) -> float:
        """
        Returns the 3-winding transformer losses in MW.

        :return: The 3-winding transformer losses in MW.
        :rtype: float
        """
        pass

    def GetDCLFLosseskW(self) -> float:
        """
        Returns the 3-winding transformer losses in kW.

        :return: The 3-winding transformer losses in kW.
        :rtype: float
        """
        pass

    def GetDCLFWindingPowerMagnitudeMVA(self, nWinding: int) -> float:
        """
        Returns the MVA power flow in winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The MVA power flow in winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetDCLFWindingPowerMagnitudekVA(self, nWinding: int) -> float:
        """
        Returns the kVA power flow in winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The kVA power flow in winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetDCLFWindingRealPowerMW(self, nWinding: int) -> float:
        """
        Returns the MW power flow in winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The MW power flow in winding for the 3-winding transformer.
        :rtype: float
        """
        pass

    def GetDCLFWindingRealPowerkW(self, nWinding: int) -> float:
        """
        Returns the kW power flow in winding for the 3-winding transformer.

        :param nWinding: The winding number.
        :type nWinding: int
        :return: The kW power flow in winding for the 3-winding transformer.
        :rtype: float
        """
        pass

class IscAnalysisAF:
    """
    Analysis class for the ArcFlash analysis.
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

class IscAnalysisLF:
    """
    Analysis class for the load flow analysis.
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

class IscAnalysisFL:
    """
    Analysis class for the fault level analysis.
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

class IscAnalysisHM:
    """
    Analysis class for the harmonic analysis.
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

    def SetBusesToAnalyse(self, nUIDs: List[int]) -> None:
        """
        Specifies which busbars will be analysed as defined by the list of busbar UIDs.

        :param nUIDs: The list of busbar UIDs which will be analysed.
        :type nUIDs: list(int)
        """
        pass

    def GetBusesToAnalyse(self) -> List[int]:
        """
        Returns a list of busbar UIDs representing the busbars that have been selected to be analysed.

        :return: The list of analysed busbars.
        :rtype: list(int)
        """
        pass

class IscAnalysisDCLF:
    """
    Analysis class for the DC load flow analysis.
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

class IscAnnotation:
    """
    Provides access to a diagram annotation allowing annotation text to be set and cleared.
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

class IscBattery:
    """
    Provides access to an IPSA battery.
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

    def GetRealPowerMW(self) -> float:
        """
        Returns the battery output in MW.

        :return: The battery output in MW.
        :rtype: float
        """
        pass

    def GetRealPowerkW(self) -> float:
        """
        Returns the battery output in kW.

        :return: The battery output in kW.
        :rtype: float
        """
        pass

    def GetTotalPowerMVA(self) -> float:
        """
        Returns the battery produced total power in MVA.

        :return: The battery produced total power in MVA.
        :rtype: float
        """
        pass

    def GetTotalPowerkVA(self) -> float:
        """
        Returns the battery produced total power in kVA.

        :return: The battery produced total power in kVA.
        :rtype: float
        """
        pass

    def GetVoltagePU(self) -> float:
        """
        Returns the battery injected voltage in per unit.

        :return: The battery injected voltage in per unit.
        :rtype: float
        """
        pass

    def GetCurrentPU(self) -> float:
        """
        Returns the battery injected current in per unit.

        :return: The battery injected current in per unit.
        :rtype: float
        """
        pass

    def GetCurrentkA(self) -> float:
        """
        Returns the battery injected current in kA.

        :return: The battery injected current in kA.
        :rtype: float
        """
        pass

class IscBranch:
    """
    Provides access to the IPSA branch.
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

    def AddSections(self, nSections: int) -> None:
        """
        Add sections to the branch. All branches start with one section.

        :param nSections: The number of sections.
        :type nSections: int
        """
        pass

    def GetSections(self) -> int:
        """
        Returns the number of sections in the branch. All branches have at least one section.

        :return: The number of sections in the branch.
        :rtype: int
        """
        pass

    @overload
    def GetIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    @overload
    def GetIValue(self, nSection: int, nFieldIndex: int) -> int:
        """
        Returns an integer value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    @overload
    def GetDValue(self, nFieldIndex: int) -> float:
        """
        Returns a double value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    @overload
    def GetDValue(self, nSection: int, nFieldIndex: int) -> float:
        """
        Returns a double value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetDValue(self, nFieldIndex: int) -> float:
        """
        Returns a double value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    @overload
    def GetSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: str
        """
        pass

    @overload
    def GetSValue(self, nSection: int, nFieldIndex: int) -> str:
        """
        Returns a string value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: str
        """
        pass

    def GetSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: str
        """
        pass

    @overload
    def GetBValue(self, nFieldIndex: int) -> bool:
        """
        Returns a boolean value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The boolean value.
        :rtype: bool
        """
        pass

    @overload
    def GetBValue(self, nSection: int, nFieldIndex: int) -> bool:
        """
        Returns a boolean value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The boolean value.
        :rtype: bool
        """
        pass

    def GetBValue(self, nFieldIndex: int) -> bool:
        """
        Returns a boolean value for the enumerated field.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The boolean value.
        :rtype: bool
        """
        pass

    def GetListDValue(self, nFieldIndex: int) -> list[float]:
        """
        Returns a list of double values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[float]
        """
        pass

    @overload
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

    @overload
    def SetIValue(self, nSection: int, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the value for the enumerated field from an integer.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetIValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the value for the enumerated field from an integer.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    @overload
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

    @overload
    def SetDValue(self, nSection: int, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the value for the enumerated field from a double.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetDValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the value for the enumerated field from a double.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    @overload
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

    @overload
    def SetSValue(self, nSection: int, nFieldIndex: int, strValue: int) -> bool:
        """
        Sets the value for the enumerated field from a string.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetSValue(self, nFieldIndex: int, strValue: int) -> bool:
        """
        Sets the value for the enumerated field from a string.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    @overload
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

    @overload
    def SetBValue(self, nSection: int, nFieldIndex: int, bValue: bool) -> bool:
        """
        Sets the value for the enumerated field from boolean.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param bValue: The given boolean value.
        :type bValue: bool
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetBValue(self, nFieldIndex: int, bValue: bool) -> bool:
        """
        Sets the value for the enumerated field from boolean.

        :param nSection: The index of the section.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param bValue: The given boolean value.
        :type bValue: bool
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetListDValue(self, nFieldIndex: int, lDValue: list[float]) -> bool:
        """
        Sets the value for the enumerated field from a list of doubles.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lDValue: The given list of double values.
        :type lDValue: list[float]
        :return: True if successful.
        :rtype: bool
        """
        pass

    @overload
    def GetRatingMVA(self, nRatingIndex: int) -> float:
        """
        Returns the MVA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The MVA rating associated with the rating set.
        :rtype: float
        """
        pass

    @overload
    def GetRatingMVA(self, nSection: int, nRatingIndex: int) -> float:
        """
        Returns the MVA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The MVA rating associated with the rating set.
        :rtype: float
        """
        pass

    def GetRatingMVA(self, nRatingIndex: int) -> float:
        """
        Returns the MVA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The MVA rating associated with the rating set.
        :rtype: float
        """
        pass

    @overload
    def GetRatingSendkA(self, nRatingIndex: int) -> float:
        """
        Returns the send end kA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The send end kA rating associated with the rating set.
        :rtype: float
        """
        pass

    @overload
    def GetRatingSendkA(self, nSection: int, nRatingIndex: int) -> float:
        """
        Returns the send end kA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The send end kA rating associated with the rating set.
        :rtype: float
        """
        pass

    def GetRatingSendkA(self, nRatingIndex: int) -> float:
        """
        Returns the send end kA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The send end kA rating associated with the rating set.
        :rtype: float
        """
        pass

    @overload
    def GetRatingReceivekA(self, nRatingIndex: int) -> float:
        """
        Returns the receiving end kA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The receiving end kA rating associated with the rating set.
        :rtype: float
        """
        pass

    @overload
    def GetRatingReceivekA(self, nSection: int, nRatingIndex: int) -> float:
        """
        Returns the receiving end kA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The receiving end kA rating associated with the rating set.
        :rtype: float
        """
        pass

    def GetRatingReceivekA(self, nRatingIndex: int) -> float:
        """
        Returns the receiving end kA rating associated with the rating set given by the rating index.
        Set 0 for details of branch rating indices.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The receiving end kA rating associated with the rating set.
        :rtype: float
        """
        pass

    @overload
    def SetRatingMVA(self, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating to the specified rating MVA for the rating set given by the rating index.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingMVA: The rating MVA.
        :type dRatingMVA: float
        """
        pass

    @overload
    def SetRatingMVA(self, nSection: int, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating to the specified rating MVA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingMVA: The rating MVA.
        :type dRatingMVA: float
        """
        pass

    def SetRatingMVA(self, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating to the specified rating MVA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingMVA: The rating MVA.
        :type dRatingMVA: float
        """
        pass

    @overload
    def SetRatingkA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the kA rating to the specified rating kA for the rating set given by the rating index.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    @overload
    def SetRatingkA(self, nSection: int, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the kA rating to the specified rating kA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    def SetRatingkA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the kA rating to the specified rating kA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    @overload
    def SetRatingSendkA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the send end kA rating to the specified rating kA for the rating set given by the rating index.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    @overload
    def SetRatingSendkA(self, nSection: int, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the send end kA rating to the specified rating kA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    def SetRatingSendkA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the send end kA rating to the specified rating kA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    @overload
    def SetRatingReceivekA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the receiving end kA rating to the specified rating kA for the rating set given by the rating index.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    @overload
    def SetRatingReceivekA(self, nSection: int, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the receiving end kA rating to the specified rating kA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    def SetRatingReceivekA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the receiving end kA rating to the specified rating kA for the rating set given by the rating index.

        :param nSection: The index of the section.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
        """
        pass

    def PopulateByDBEntry(self, strLineDataName: str, dLength: float, nParallel: int) -> bool:
        """
        Populates the object data with database information from the first database that was loaded.

        :param strLineDataName: The name of the branch.
        :type strLineDataName: str
        :param dLength: The length of the branch.
        :type dLength: float
        :param nParallel: The number of parallel components.
        :type nParallel: int
        :return: Returns True if successful.
        :rtype: bool
        """
        pass

    def GetSendPowerMagnitudeMVA(self) -> float:
        """
        Returns the branch sending end power in MVA.

        :return: The branch sending end power in MVA.
        :rtype: float
        """
        pass

    def GetSendPowerMagnitudekVA(self) -> float:
        """
        Returns the branch sending end power in kVA.

        :return: The branch sending end power in kVA.
        :rtype: float
        """
        pass

    def GetSendRealPowerMW(self) -> float:
        """
        Returns the branch sending end power in MW.

        :return: The branch sending end power in MW.
        :rtype: float
        """
        pass

    def GetSendReactivePowerMVAr(self) -> float:
        """
        Returns the branch sending end power in MVAr.

        :return: The branch sending end power in MVAr.
        :rtype: float
        """
        pass

    def GetSendRealPowerkW(self) -> float:
        """
        Returns the branch sending end power in kW.

        :return: The branch sending end power in kW.
        :rtype: float
        """
        pass

    def GetSendReactivePowerkVAr(self) -> float:
        """
        Returns the branch sending end power in kVAr.

        :return: The branch sending end power in kVAr.
        :rtype: float
        """
        pass

    def GetReceivePowerMagnitudeMVA(self) -> float:
        """
        Returns the branch receiving end power in MVA.

        :return: The branch receiving end power in MVA.
        :rtype: float
        """
        pass

    def GetReceivePowerMagnitudekVA(self) -> float:
        """
        Returns the branch receiving end power in kVA.

        :return: The branch receiving end power in kVA.
        :rtype: float
        """
        pass

    def GetReceiveRealPowerMW(self) -> float:
        """
        Returns the branch receiving end power in MW.

        :return: The branch receiving end power in MW.
        :rtype: float
        """
        pass

    def GetReceiveReactivePowerMVAr(self) -> float:
        """
        Returns the branch receiving end power in MVAr.

        :return: The branch receiving end power in MVAr.
        :rtype: float
        """
        pass

    def GetReceiveRealPowerkW(self) -> float:
        """
        Returns the branch receiving end power in kW.

        :return: The branch receiving end power in kW.
        :rtype: float
        """
        pass

    def GetReceiveReactivePowerkVAr(self) -> float:
        """
        Returns the branch receiving end power in kVAr.

        :return: The branch receiving end power in kVAr.
        :rtype: float
        """
        pass

    @overload
    def GetLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest branch power in MVA.

        :return: The highest branch power in MVA.
        :rtype: float
        """
        pass

    @overload
    def GetLargestPowerMagnitudeMVA(self, nStudyUID: int) -> float:
        """
        Returns the highest branch power in MVA.

        :param nStudyUID: The automation or contingency study UID which the results are for
        :type nStudyUID: int
        :return: The highest branch power in MVA.
        :rtype: float
        """
        pass

    def GetLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest branch power in MVA.

        :param nStudyUID: If supplied, the automation or contingency study UID which the results are for
        :type nStudyUID: int
        :return: The highest branch power in MVA.
        :rtype: float
        """
        pass

    def GetLargestPowerMagnitudekVA(self) -> float:
        """
        Returns the highest branch power in kVA.

        :return: The highest branch power in kVA.
        :rtype: float
        """
        pass

    def GetLargestRealPowerMW(self) -> float:
        """
        Returns the highest branch power in MW.

        :return: The highest branch power in MW.
        :rtype: float
        """
        pass

    def GetLargestReactivePowerMVAr(self) -> float:
        """
        Returns the highest branch power in MVAr.

        :return: The highest branch power in MVAr.
        :rtype: float
        """
        pass

    def GetLargestRealPowerkW(self) -> float:
        """
        Returns the highest branch power in kW.

        :return: The highest branch power in kW.
        :rtype: float
        """
        pass

    def GetLargestReactivePowerkVAr(self) -> float:
        """
        Returns the highest branch power in kVAr.

        :return: The highest branch power in kVAr.
        :rtype: float
        """
        pass

    def GetLossesMW(self) -> float:
        """
        Returns the branch losses in MW.

        :return: The branch losses in MW.
        :rtype: float
        """
        pass

    def GetLossesMVAr(self) -> float:
        """
        Returns the branch losses in MVAr.

        :return: The branch losses in MVAr.
        :rtype: float
        """
        pass

    def GetLosseskW(self) -> float:
        """
        Returns the branch losses in kW.

        :return: The branch losses in kW.
        :rtype: float
        """
        pass

    def GetLosseskVAr(self) -> float:
        """
        Returns the branch losses in kVAr.

        :return: The branch losses in kVAr.
        :rtype: float
        """
        pass

    def GetCapacityHeadroomPC(self) -> float:
        """
        Returns the branch capacity headroom as a percentage.

        :return: The branch capacity headroom as a percentage.
        :rtype: float
        """
        pass

    def GetFaultRedComponentMVA(self) -> float:
        """
        Returns the red phase level component in MVA.

        :return: The red phase level component in MVA.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentMVA(self) -> float:
        """
        Returns the yellow phase fault level component in MVA.

        :return: The yellow phase fault level component in MVA.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentMVA(self) -> float:
        """
        Returns the blue phase fault level component in MVA.

        :return: The blue phase fault level component in MVA.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentMVA(self) -> float:
        """
        Returns the positive sequence fault level component in MVA.

        :return: The positive sequence fault level component in MVA.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentMVA(self) -> float:
        """
        Returns the negative sequence fault level component in MVA.

        :return: The negative sequence fault level component in MVA.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentMVA(self) -> float:
        """
        Returns the zero sequence fault level component in MVA.

        :return: The zero sequence fault level component in MVA.
        :rtype: float
        """
        pass

    def GetFaultRedComponentkA(self) -> float:
        """
        Returns the red phase component of fault current in kA.

        :return: The red phase component of fault current in kA.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentkA(self) -> float:
        """
        Returns the yellow phase component of fault current in kA.

        :return: The yellow phase component of fault current in kA.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentkA(self) -> float:
        """
        Returns the blue phase component of fault current in kA.

        :return: The blue phase component of fault current in kA.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentkA(self) -> float:
        """
        Returns the positive sequence component of fault current in kA.

        :return: The positive sequence component of fault current in kA.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentkA(self) -> float:
        """
        Returns the negative sequence component of fault current in kA.

        :return: The negative sequence component of fault current in kA.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentkA(self) -> float:
        """
        Returns the zero sequence component of fault current in kA.

        :return: The zero sequence component of fault current in kA.
        :rtype: float
        """
        pass

    def GetFaultRedComponentAngleDeg(self) -> float:
        """
        Returns the red phase component of fault angle in degrees.

        :return: The red phase component of fault angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentAngleDeg(self) -> float:
        """
        Returns the yellow phase component of fault angle in degrees.

        :return: The yellow phase component of fault angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentAngleDeg(self) -> float:
        """
        Returns the blue phase component of fault angle in degrees.

        :return: The blue phase component of fault angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentAngleDeg(self) -> float:
        """
        Returns the positive sequence component of fault angle in degrees.

        :return: The positive sequence component of fault angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentAngleDeg(self) -> float:
        """
        Returns the negative sequence component of fault angle in degrees.

        :return: The negative sequence component of fault angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentAngleDeg(self) -> float:
        """
        Returns the zero sequence component of fault angle in degrees.

        :return: The zero sequence component of fault angle in degrees.
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

    def GetResistance(self, dOrder: float) -> float:
        """
        Returns the branch harmonic resistance in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The branch harmonic resistance in per unit.
        :rtype: float
        """
        pass

    def GetReactance(self, dOrder: float) -> float:
        """
        Returns the branch harmonic reactance in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The branch harmonic reactance in per unit.
        :rtype: float
        """
        pass

    def GetSusceptance(self, dOrder: float) -> float:
        """
        Returns the branch harmonic susceptance in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The branch harmonic susceptance in per unit.
        :rtype: float
        """
        pass

    def GetProfileMinimumFlowMVA(self) -> float:
        """
        Returns the minimum branch flow in MVA from the profile study results.

        :return: The minimum branch flow in MVA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMinimumFlowkA(self) -> float:
        """
        Returns the minimum branch flow in kA from the profile study results.

        :return: The minimum branch flow in kA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMaximumFlowMVA(self) -> float:
        """
        Returns the maximum branch flow in MVA from the profile study results.

        :return: The maximum branch flow in MVA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMaximumFlowkA(self) -> float:
        """
        Returns the maximum branch flow in kA from the profile study results.

        :return: The maximum branch flow in kA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMedianFlowMVA(self) -> float:
        """
        Returns the median of the branch flow in MVA from the profile study results.

        :return: The median of the branch flow in MVA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMedianFlowkA(self) -> float:
        """
        Returns the median of the branch flow in kA from the profile study results.

        :return: The median of the branch flow in kA from the profile study results.
        :rtype: float
        """
        pass

    def GetMinimumProfileIndex(self) -> int:
        """
        Returns the category index which identifies the minimum branch flow from the profile study results.

        :return: The minimum category index.
        :rtype: int
        """
        pass

    def GetMaximumProfileIndex(self) -> int:
        """
        Returns the category index which identifies the maximum branch flow from the profile study results.

        :return: The maximum category index.
        :rtype: int
        """
        pass

    def GetDCLFSendPowerMagnitudeMVA(self) -> float:
        """
        Returns the branch sending end power in MVA.

        :return: The branch sending end power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFSendPowerMagnitudekVA(self) -> float:
        """
        Returns the branch sending end power in kVA.

        :return: The branch sending end power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFSendRealPowerMW(self) -> float:
        """
        Returns the branch sending end power in MW.

        :return: The branch sending end power in MW.
        :rtype: float
        """
        pass

    def GetDCLFSendRealPowerkW(self) -> float:
        """
        Returns the branch sending end power in kW.

        :return: The branch sending end power in kW.
        :rtype: float
        """
        pass

    def GetDCLFReceivePowerMagnitudeMVA(self) -> float:
        """
        Returns the branch receiving end power in MVA.

        :return: The branch receiving end power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFReceivePowerMagnitudekVA(self) -> float:
        """
        Returns the branch receiving end power in kVA.

        :return: The branch receiving end power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFReceiveRealPowerMW(self) -> float:
        """
        Returns the branch receiving end power in MW.

        :return: The branch receiving end power in MW.
        :rtype: float
        """
        pass

    def GetDCLFReceiveRealPowerkW(self) -> float:
        """
        Returns the branch receiving end power in kW.

        :return: The branch receiving end power in kW.
        :rtype: float
        """
        pass

    def GetDCLFLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest branch power in MVA.

        :return: The highest branch power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFLargestPowerMagnitudekVA(self) -> float:
        """
        Returns the highest branch power in kVA.

        :return: The highest branch power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFLargestRealPowerMW(self) -> float:
        """
        Returns the highest branch power in MW.

        :return: The highest branch power in MW.
        :rtype: float
        """
        pass

    def GetDCLFLargestRealPowerkW(self) -> float:
        """
        Returns the highest branch power in kW.

        :return: The highest branch power in kW.
        :rtype: float
        """
        pass

    def GetDCLFLossesMW(self) -> float:
        """
        Returns the branch losses in MW.

        :return: The branch losses in MW.
        :rtype: float
        """
        pass

    def GetDCLFLosseskW(self) -> float:
        """
        Returns the branch losses in kW.

        :return: The branch losses in kW.
        :rtype: float
        """
        pass

class IscBusbar:
    """
    Provides access to an IPSA busbar.
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

    def GetFaultDValue(self, nFaultFieldIndex: int) -> float:
        """
        Returns a float value for the circuit breaker field.
        In IPSA 2.10.2, nFaultFieldIndex should be one of FaultMakePeakkA, FaultBreakRMSkA, FaultBreakDCPC,
        FaultBreakTimemS or FaultNomCurrentkA.
        nFaultFieldIndex can also be one of the IscCircuitBreaker field indexes MakePeakkA, BreakRMSkA, BreakDCPC,
        BreakTimemS or NomCurrentkA.
        This function is used to get fault (breaker) ratings for a busbar.

        :param nFaultFieldIndex: FaultMakePeakkA, FaultBreakRMSkA, FaultBreakDCPC, FaultBreakTimemS or
            FaultNomCurrentkA.
        :type nFaultFieldIndex: int
        :return: The float value for the selected field.
        :rtype: float
        """
        pass

    def SetFaultDValue(self, nFaultFieldIndex: int) -> bool:
        """
        Sets the value for the circuit breaker field.
        In IPSA 2.10.2, nFaultFieldIndex should be one of FaultMakePeakkA, FaultBreakRMSkA, FaultBreakDCPC,
        FaultBreakTimemS or FaultNomCurrentkA.
        nFaultFieldIndex can also be one of the IscCircuitBreaker field indexes MakePeakkA, BreakRMSkA, BreakDCPC,
        BreakTimemS or NomCurrentkA.
        This function is used to set fault (breaker) ratings for a busbar.

        :param nFaultFieldIndex: FaultMakePeakkA, FaultBreakRMSkA, FaultBreakDCPC, FaultBreakTimemS or
            FaultNomCurrentkA.
        :type nFaultFieldIndex: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    @overload
    def GetVoltageMagnitudePU(self, nStudyUid: int) -> float:
        """
        Returns the voltage magnitude in per unit for the given automation or contingency study.

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :return: The voltage magnitude for the study.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageMagnitudePU(self) -> float:
        """
        Returns the voltage magnitude in per unit.

        :return: The voltage magnitude.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageMagnitudePU(self, dOrder: float) -> float:
        """
        *Deprecated in IPSA 2.10.2 instead use GetVoltageMagnitudeHarmPU*

        Returns the harmonic voltage magnitude in per unit for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The harmonic voltage magnitude in per unit.
        :rtype: float
        """
        pass

    def GetVoltageMagnitudePU(self, nStudyUid: int) -> float:
        """
        Returns the voltage magnitude in per unit.

        If a UID is provided this is for the associated automation or contingency study.

        *Deprecated. If a float dOrder is provided, this is the harmonic voltage magnitude for the given harmonic order.
        Instead, use GetVoltageMagnitudeHarmPU*

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The voltage magnitude, if a UID is provided this returns the voltage magnitude for the associated
            study. If a dOrder is provided this returns the voltage magnitude for the harmonic order.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageMagnitudekV(self, nStudyUid: int) -> float:
        """
        Returns the voltage magnitude in kV for the given automation or contingency study.

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :return: The voltage magnitude for the study.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageMagnitudekV(self) -> float:
        """
        Returns the voltage magnitude in kV.

        :return: The voltage magnitude.
        :rtype: float
        """
        pass

    def GetVoltageMagnitudekV(self, nStudyUid: int) -> float:
        """
        Returns the voltage magnitude in kV.
        If a UID is provided this is for the associated automation or contingency study.

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :return: The voltage magnitude, if a UID is provided this returns the voltage magnitude for the associated study.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageAngleRad(self) -> float:
        """
        Returns the voltage angle in radians.

        :return: The voltage angle.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageAngleRad(self, nStudyUid: int) -> float:
        """
        Returns the voltage angle in radians for the given automation or contingency study

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :return: Returns the voltage angle in radians in per unit for the study.
        :rtype: float
        """
        pass

    def GetVoltageAngleRad(self, nStudyUid: int) -> float:
        """
        Returns the voltage angle in radians.
        If a UID is provided this is for the associated automation or contingency study.

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :return: The voltage angle, if a UID is provided this returns the voltage angle for the associated study.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageAngleDeg(self) -> float:
        """
        Returns the voltage angle in degrees.

        :return: The voltage angle.
        :rtype: float
        """
        pass

    @overload
    def GetVoltageAngleDeg(self, nStudyUid: int) -> float:
        """
        Returns the voltage angle in degrees for the given automation or contingency study

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :return: Returns the voltage angle in radians in per unit for the study.
        :rtype: float
        """
        pass

    def GetVoltageAngleDeg(self, nStudyUid: int) -> float:
        """
        Returns the voltage angle in degrees.
        If a UID is provided this is for the associated automation or contingency study.

        :param nStudyUid: The UID of the study.
        :type nStudyUid: int
        :return: The voltage angle, if a UID is provided this returns the voltage angle for the associated study.
        :rtype: float
        """
        pass

    def GetRealMismatchMW(self) -> float:
        """
        Returns the load flow MW mismatch.

        :return: The load flow MW mismatch.
        :rtype: float
        """
        pass

    def GetReactiveMismatchMVAr(self) -> float:
        """
        Returns the load flow MVAr mismatch.

        :return: The load flow MVAr mismatch.
        :rtype: float
        """
        pass

    def GetRealGenerationMW(self) -> float:
        """
        Returns the total MW of generation at a busbar.

        :return: The total MW of generation at a busbar.
        :rtype: float
        """
        pass

    def GetReactiveGenerationMVAr(self) -> float:
        """
        Returns the total MVAr of generation at a busbar.

        :return: The total MVAr of generation at a busbar.
        :rtype: float
        """
        pass

    def GetRealInductionMW(self) -> float:
        """
        Returns the total MW of induction machines at a busbar.

        :return: The total MW of induction machines at a busbar.
        :rtype: float
        """
        pass

    def GetReactiveInductionMVAr(self) -> float:
        """
        Returns the total MVAr of induction machines at a busbar.

        :return: The total MVAr of induction machines at a busbar.
        :rtype: float
        """
        pass

    def GetRealLoadMW(self) -> float:
        """
        Returns the total MW of static load at a busbar.

        :return: The total MW of static load at a busbar.
        :rtype: float
        """
        pass

    def GetReactiveLoadMVAr(self) -> float:
        """
        Returns the total MVAr of static load at a busbar.

        :return: The total MVAr of static load at a busbar.
        :rtype: float
        """
        pass

    def GetRedVoltageMagnitudePU(self) -> float:
        """
        Returns the red phase voltage magnitude in per-unit.

        :return: The red phase voltage magnitude in per-unit.
        :rtype: float
        """
        pass

    def GetRedVoltageMagnitudekV(self) -> float:
        """
        Returns the red phase voltage magnitude in kV.

        :return: The red phase voltage magnitude in kV.
        :rtype: float
        """
        pass

    def GetRedVoltageAngleDeg(self) -> float:
        """
        Returns the red phase voltage angle in degrees.

        :return: The red phase voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetYellowVoltageMagnitudePU(self) -> float:
        """
        Returns the yellow phase voltage magnitude in per-unit.

        :return: The yellow phase voltage magnitude in per-unit.
        :rtype: float
        """
        pass

    def GetYellowVoltageMagnitudekV(self) -> float:
        """
        Returns the yellow phase voltage magnitude in kV.

        :return: The yellow phase voltage magnitude in kV.
        :rtype: float
        """
        pass

    def GetYellowVoltageAngleDeg(self) -> float:
        """
        Returns the yellow phase voltage angle in degrees.

        :return: The yellow phase voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetBlueVoltageMagnitudePU(self) -> float:
        """
        Returns the blue phase voltage magnitude in per-unit.

        :return: The blue phase voltage magnitude in per-unit.
        :rtype: float
        """
        pass

    def GetBlueVoltageMagnitudekV(self) -> float:
        """
        Returns the blue phase voltage magnitude in kV.

        :return: The blue phase voltage magnitude in kV.
        :rtype: float
        """
        pass

    def GetBlueVoltageAngleDeg(self) -> float:
        """
        Returns the blue phase voltage angle in degrees.

        :return: The blue phase voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultACComponentMVA(self) -> float:
        """
        Returns the AC component of fault level in MVA.

        :return: The AC component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFaultDCComponentMVA(self) -> float:
        """
        Returns the DC component of fault level in MVA.

        :return: The DC component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFault2HComponentMVA(self) -> float:
        """
        Returns the second harmonic component of fault level in MVA.

        :return: The second harmonic component of fault level in MVA.
        :rtype: float
        """
        pass

    def GetFaultDCTheveninX(self) -> float:
        """
        Returns the inductive/capacitive component of the DC X/R ratio.

        :return: The inductive/capacitive component of the DC X/R ratio.
        :rtype: float
        """
        pass

    def GetFaultDCTheveninR(self) -> float:
        """
        Returns the resistive component of the DC X/R ratio.

        :return: The resistive component of the DC X/R ratio.
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

    def GetFaultRedComponentAngleDeg(self) -> float:
        """
        Returns the red phase component of fault angle in degrees.

        :return: The red phase component of fault angle in degrees.
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

    def GetFaultYellowComponentAngleDeg(self) -> float:
        """
        Returns the yellow phase component of fault angle in degrees.

        :return: The yellow phase component of fault angle in degrees.
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

    def GetFaultBlueComponentAngleDeg(self) -> float:
        """
        Returns the blue phase component of fault angle in degrees.

        :return: The blue phase component of fault angle in degrees.
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

    def GetFaultPositiveComponentAngleDeg(self) -> float:
        """
        Returns the positive sequence component of fault angle in degrees.

        :return: The positive sequence component of fault angle in degrees.
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

    def GetFaultNegativeComponentAngleDeg(self) -> float:
        """
        Returns the negative sequence component of fault angle in degrees.

        :return: The negative sequence component of fault angle in degrees.
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

    def GetFaultZeroComponentAngleDeg(self) -> float:
        """
        Returns the zero sequence component of fault angle in degrees.

        :return: The zero sequence component of fault angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultACComponentkA(self) -> float:
        """
        Returns the AC component of fault level in kA.

        :return: The AC component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultDCComponentkA(self) -> float:
        """
        Returns the DC component of fault level in kA.

        :return: The DC component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFault2HComponentkA(self) -> float:
        """
        Returns the second harmonic component of fault level in kA.

        :return: The second harmonic component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultRedComponentkA(self) -> float:
        """
        Returns the red phase component of fault level in kA.

        :return: The red phase component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentkA(self) -> float:
        """
        Returns the yellow phase component of fault level in kA.

        :return: The yellow phase component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentkA(self) -> float:
        """
        Returns the blue phase component of fault level in kA.

        :return: The blue phase component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentkA(self) -> float:
        """
        Returns the positive sequence component of fault level in kA.

        :return: The positive sequence component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentkA(self) -> float:
        """
        Returns the negative sequence component of fault level in kA.

        :return: The negative sequence component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentkA(self) -> float:
        """
        Returns the zero sequence component of fault level in kA.

        :return: The zero sequence component of fault level in kA.
        :rtype: float
        """
        pass

    def GetFaultRedVoltagePU(self) -> float:
        """
        Returns the red phase fault voltage in per unit.

        :return: The red phase fault voltage in per unit.
        :rtype: float
        """
        pass

    def GetFaultRedVoltageAngleDeg(self) -> float:
        """
        Returns the red phase fault voltage angle in degrees.

        :return: The red phase fault voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultYellowVoltagePU(self) -> float:
        """
        Returns the yellow phase fault voltage in per unit.

        :return: The yellow phase fault voltage in per unit.
        :rtype: float
        """
        pass

    def GetFaultYellowVoltageAngleDeg(self) -> float:
        """
        Returns the yellow phase fault voltage angle in degrees.

        :return: The yellow phase fault voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultBlueVoltagePU(self) -> float:
        """
        Returns the blue phase fault voltage in per unit.

        :return: The blue phase fault voltage in per unit.
        :rtype: float
        """
        pass

    def GetFaultBlueVoltageAngleDeg(self) -> float:
        """
        Returns the blue phase fault voltage angle in degrees.

        :return: The blue phase fault voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultPositiveVoltagePU(self) -> float:
        """
        Returns the positive sequence component of fault voltage in per unit.

        :return: The positive sequence component of fault voltage in per unit.
        :rtype: float
        """
        pass

    def GetFaultPositiveVoltageAngleDeg(self) -> float:
        """
        Returns the positive sequence component of fault voltage angle in degrees.

        :return: The positive sequence component of fault voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultNegativeVoltagePU(self) -> float:
        """
        Returns the negative sequence component of fault voltage in per unit.

        :return: The negative sequence component of fault voltage in per unit.
        :rtype: float
        """
        pass

    def GetFaultNegativeVoltageAngleDeg(self) -> float:
        """
        Returns the negative sequence component of fault voltage angle in degrees.

        :return: The negative sequence component of fault voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultZeroVoltagePU(self) -> float:
        """
        Returns the zero sequence component of fault voltage in per unit.

        :return: The zero sequence component of fault voltage in per unit.
        :rtype: float
        """
        pass

    def GetFaultZeroVoltageAngleDeg(self) -> float:
        """
        Returns the zero sequence component of fault voltage angle in degrees.

        :return: The zero sequence component of fault voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetFaultIEC909InitialSymRMSMVA(self) -> float:
        """
        Returns the initial symmetrical RMS fault level in MVA for IEC60909 analysis.

        :return: The initial symmetrical RMS fault level in MVA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909PeakMVA(self) -> float:
        """
        Returns the peak fault level in MVA for IEC60909 analysis.

        :return: The peak fault level in MVA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909AsymmetricBreakMVA(self) -> float:
        """
        Returns the asymmetric break fault level in MVA for IEC60909 analysis.

        :return: The asymmetric break fault level in MVA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909SymmetricBreakMVA(self) -> float:
        """
        Returns the symmetric break fault level in MVA for IEC60909 analysis.

        :return: The symmetric break fault level in MVA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909DCMagnitudeMVA(self) -> float:
        """
        Returns the DC fault level magnitude in MVA for IEC60909 analysis.

        :return: The DC fault level magnitude in MVA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909SteadyStateMVA(self) -> float:
        """
        Returns the steady state fault level in MVA for IEC60909 analysis.

        :return: The steady state fault level in MVA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909DCXoverR(self) -> float:
        """
        Returns the X/R ratio for IEC60909 analysis.

        :return: The X/R ratio for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909DCXoverRBreak(self) -> float:
        """
        Returns the X/R ratio at break time for IEC60909 analysis.

        :return: The X/R ratio at break time for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909InitialSymRMSkA(self) -> float:
        """
        Returns the initial symmetrical RMS fault level in kA for IEC60909 analysis.

        :return: The initial symmetrical RMS fault level in kA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909PeakkA(self) -> float:
        """
        Returns the peak fault level in kA for IEC60909 analysis.

        :return: The peak fault level in kA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909AsymmetricBreakkA(self) -> float:
        """
        Returns the asymmetric break fault level in kA for IEC60909 analysis.

        :return: The asymmetric break fault level in kA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909SymmetricBreakkA(self) -> float:
        """
        Returns the symmetric break fault level in kA for IEC60909 analysis.

        :return: The symmetric break fault level in kA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909DCMagnitudekA(self) -> float:
        """
        Returns the DC fault level magnitude in kA for IEC60909 analysis.

        :return: The DC fault level magnitude in kA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetFaultIEC909SteadyStatekA(self) -> float:
        """
        Returns the steady state fault level in kA for IEC60909 analysis.

        :return: The steady state fault level in kA for IEC60909 analysis.
        :rtype: float
        """
        pass

    def GetVoltageOrders(self) -> List[float]:
        """
        Returns a list of all harmonic orders at a busbar.
        These harmonic orders can then be used to access busbar results at a specific harmonic order.

        :return: All harmonic orders at a busbar.
        :rtype: list(float)
        """
        pass

    def GetVoltageMagnitudeHarmPU(self, dOrder: float) -> float:
        """
        Returns the harmonic voltage magnitude in per unit for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The harmonic voltage magnitude in per unit.
        :rtype: float
        """
        pass

    def GetVoltageMagnitudePC(self, dOrder: float) -> float:
        """
        Returns the harmonic voltage magnitude in percent for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The harmonic voltage magnitude in percent.
        :rtype: float
        """
        pass

    def GetVoltageAngle(self, dOrder: float) -> float:
        """
        Returns the harmonic voltage angle in radians for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The harmonic voltage angle in radians.
        :rtype: float
        """
        pass

    def GetImpedanceOrders(self) -> List[float]:
        """
        Returns a list of all harmonic impedance orders at a busbar.
        These harmonic orders can then be used to access busbar results at a specific harmonic order.

        :return: All harmonic impedance orders at a busbar.
        :rtype: list[float]
        """
        pass

    def GetImpedanceMagnitude(self, dOrder: float) -> float:
        """
        Returns the harmonic impedance magnitude in per unit for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The harmonic impedance magnitude in per unit.
        :rtype: float
        """
        pass

    def GetImpedanceAngle(self, dOrder: float) -> float:
        """
        Returns the harmonic impedance angle in radians for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The harmonic impedance angle in radians.
        :rtype: float
        """
        pass

    def GetImpedanceReal(self, dOrder: float) -> float:
        """
        Returns the real part of the harmonic impedance in per unit for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The real part of the harmonic impedance in per unit.
        :rtype: float
        """
        pass

    def GetImpedanceImaginary(self, dOrder: float) -> float:
        """
        Returns the imaginary part of the harmonic impedance in per unit for harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The imaginary part of the harmonic impedance in per unit.
        :rtype: float
        """
        pass

    def GetTotalHarmonicDistortion(self) -> float:
        """
        Returns the total harmonic distortion at a busbar in percent.

        :return: The total harmonic distortion at a busbar in percent.
        :rtype: float
        """
        pass

    def GetHarmonicDistortion(self, dOrder: float) -> float:
        """
        Returns the harmonic distortion at a busbar in percent for order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The harmonic distortion at a busbar in percent.
        :rtype: float
        """
        pass

    def GetMaximumDistortion(self) -> List[float]:
        """
        Returns a list of reals for harmonic order with the highest distortion. The distortion is in percent.

        :return: A list of reals for harmonic order with the highest distortion.
        :rtype: list[float]
        """
        pass

    def GetResonances(self) -> List[float]:
        """
        Returns a list containing all the resonances found at a busbar.
        Each list gives the lower and upper resonance orders for each resonance found.

        :return: A list containing all the resonances found at a busbar.
        :rtype: list[float]
        """
        pass

    def GetVoltageSum(self) -> float:
        """
        Returns the arithmetic sum of all harmonic voltages at a busbar in per unit.

        :return: The arithmetic sum of all harmonic voltages at a busbar in per unit.
        :rtype: float
        """
        pass

    def GetAverageInterruptionHours(self) -> float:
        """
        Returns the average interruption time in hours from the reliability study results.

        :return: The average interruption time in hours from the reliability study results.
        :rtype: float
        """
        pass

    def GetAnnualInterruptionHours(self) -> float:
        """
        Returns the total annual interruption time in hours from the reliability study results.

        :return: The total annual interruption time in hours from the reliability study results.
        :rtype: float
        """
        pass

    def GetAnnualInterruptionFrequency(self) -> float:
        """
        Returns the number of interruptions per year from the reliability study results.

        :return: The number of interruptions per year from the reliability study results.
        :rtype: float
        """
        pass

    def GetProfileMinimumVoltagePU(self) -> float:
        """
        Returns the minimum voltage in per unit from the profile study results.

        :return: The minimum voltage in per unit from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMaximumVoltagePU(self) -> float:
        """
        Returns the maximum voltage in per unit from the profile study results.

        :return: The maximum voltage in per unit from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMedianVoltagePU(self) -> float:
        """
        Returns the median of the voltage in per unit from the profile study results.

        :return: The median of the voltage in per unit from the profile study results.
        :rtype: float
        """
        pass

    def GetMinimumProfileIndex(self) -> int:
        """
        Returns the category index which identifies the minimum busbar voltage result from the profile study results.

        :return: The minimum category index.
        :rtype: int
        """
        pass

    def GetMaximumProfileIndex(self) -> int:
        """
        Returns the category index which identifies the maximum busbar voltage result from the profile study results.

        :return: The maximum category index.
        :rtype: int
        """
        pass

    def GetDCLFVoltageAngleDeg(self) -> float:
        """
        Returns the voltage angle in degrees.

        :return: The voltage angle in degrees.
        :rtype: float
        """
        pass

    def GetDCLFVoltageAngleRad(self) -> float:
        """
        Returns the voltage angle in radians.

        :return: The voltage angle in radians.
        :rtype: float
        """
        pass

    def GetDCLFRealGenerationMW(self) -> float:
        """
        Returns the total MW of generation at a busbar.

        :return: The total MW of generation at a busbar.
        :rtype: float
        """
        pass

    def GetDCLFRealGenerationkW(self) -> float:
        """
        Returns the total kW of generation at a busbar.

        :return: The total kW of generation at a busbar.
        :rtype: float
        """
        pass

    def GetDCLFRealLoadMW(self) -> float:
        """
        Returns the total MW of static load at a busbar.

        :return: The total MW of static load at a busbar.
        :rtype: float
        """
        pass

    def GetDCLFRealLoadkW(self) -> float:
        """
        Returns the total kW of static load at a busbar.

        :return: The total kW of static load at a busbar.
        :rtype: float
        """
        pass

    def GetDCLFTransmissionLossFactor(self) -> float:
        """
        Returns transmission losses factor for the busbar.

        :return: Transmission losses factor for the busbar.
        :rtype: float
        """
        pass

    def GetArcBusbarConfiguration(self) -> int:
        """
        Returns the specific busbar configuration for this bus according to the definitions penned out by IEEE-1584
        standard:

            - 0 = Unknown
            - 1 = VCB (vertical closed box)
            - 2 = VCBB (vertical closed bolted box)
            - 3 = HCB (horizontal closed box)
            - 4 = VOA (vertical open air box)
            - 5 = HOA (horizontal open air box)

        :return: The specific busbar configuration.
        :rtype: int
        """
        pass
    
    def GetArcEnclosureHeightMM(self) -> float:
        """
        Returns the height of the busbar enclosure for the arcflash in mm.

        :return: The height of the busbar enclosure for the arcflash in mm.
        :rtype: float
        """
        pass

    def GetArcEnclosureWidthMM(self) -> float:
        """
        Returns the width of the busbar enclosure for the arcflash in mm.

        :return: The width of the busbar enclosure for the arcflash in mm.
        :rtype: float
        """
        pass

    def GetArcEnclosureDepthMM(self) -> float:
        """
        Returns the depth of the busbar enclosure for the arcflash in mm.

        :return: The depth of the busbar enclosure for the arcflash in mm.
        :rtype: float
        """
        pass

    def GetArcConductorGapMM(self) -> float:
        """
        Returns the air gap between the conductors that the arc flash jumps across in mm.

        :return: The air gap between the conductors in mm.
        :rtype: float
        """
        pass

    def GetArcWorkingDistanceMM(self) -> float:
        """
        Returns the working distance for the bus container in mm.

        :return: The working distance for the bus container in mm.
        :rtype: float
        """
        pass

    def SetArcBusbarConfiguration(self, nConfig: int) -> bool:
        """
        Sets the specific busbar configuration for this bus according to the definitions penned out by IEEE-1584
        standard:

            - 0 = Unknown
            - 1 = VCB (vertical closed box)
            - 2 = VCBB (vertical closed bolted box)
            - 3 = HCB (horizontal closed box)
            - 4 = VOA (vertical open air box)
            - 5 = HOA (horizontal open air box)

        :param nConfig: The specific busbar configuration.
        :type nConfig: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetArcEnclosureHeightMM(self, dHeight: float) -> bool:
        """
        Sets the height of the busbar enclosure for the arcflash in mm.

        :param dHeight: The height of the busbar enclosure for the arcflash in mm.
        :type dHeight: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetArcEnclosureWidthMM(self, dWidth: float) -> bool:
        """
        Sets the width of the busbar enclosure for the arcflash in mm.

        :param dWidth: The width of the busbar enclosure for the arcflash in mm.
        :type dWidth: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetArcEnclosureDepthMM(self, dDepth: float) -> bool:
        """
        Sets the depth of the busbar enclosure for the arcflash in mm.

        :param dDepth: The depth of the busbar enclosure for the arcflash in mm.
        :type dDepth: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetArcConductorGapMM(self, dConductorGap: float) -> bool:
        """
        Returns the air gap between the conductors that the arc flash jumps across in mm.

        :param dConductorGap: The air gap between the conductors in mm.
        :type dConductorGap: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetArcWorkingDistanceMM(self, dWorkingDistance: float) -> bool:
        """
        Returns the working distance for the bus container in mm.

        :param dWorkingDistance: The working distance for the bus container in mm.
        :type dWorkingDistance: float
        :return: True if successful.
        :rtype: bool
        """
        pass

class IscChopper:
    """
    Provides access to a DC/DC Converter.
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

    def GetLineIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the line associated with this chopper.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The line associated with this chopper.
        :rtype: int
        """
        pass

    def GetLineDValue(self, nFieldIndex: int) -> float:
        """
        Returns a float value for the line associated with this chopper.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The line associated with this chopper.
        :rtype: float
        """
        pass

    def GetLineSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the line associated with this chopper.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The line associated with this chopper.
        :rtype: str
        """
        pass

    def SetLineIValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets an integer value for the line associated with this chopper.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The integer value for the line.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetLineDValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets a float value for the line associated with this chopper.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The float value for the line.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetLineSValue(self, nFieldIndex: int, strValue: str) -> bool:
        """
        Sets a string value for the line associated with this chopper.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The string value for the line.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetRatingskA(self, nRatingIndex: int, dSendRatingkA: float, dRecieveRatingkA: float) -> None:
        """
        Sets the sending and receiving end current ratings in kA for the chopper.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :param dSendRatingkA: The sending end current ratings in kA.
        :type dSendRatingkA: float
        :param dRecieveRatingkA: The receiving end current ratings in kA.
        :type dRecieveRatingkA: float
        """
        pass

    def SetRatingMVA(self, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating for the chopper.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :param dRatingMVA: The MVA rating.
        :type dRatingMVA: float
        """
        pass

    def GetRatingSendkA(self, nRatingIndex: int) -> float:
        """
        Returns the sending end current ratings in kA for the chopper.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The sending end current ratings in kA.
        :rtype: float
        """
        pass

    def GetRatingReceivekA(self, nRatingIndex: int) -> float:
        """
        Returns the receiving end current ratings in kA for the chopper.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The receiving end current ratings in kA.
        :rtype: float
        """
        pass

    def GetRatingMVA(self, nRatingIndex: int) -> float:
        """
        Returns the MVA rating for the chopper.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The MVA rating.
        :rtype: float
        """
        pass

    def GetSendRealPowerMW(self) -> float:
        """
        Returns the chopper sending end power in MW.

        :return: The chopper sending end power in MW.
        :rtype: float
        """
        pass

    def GetSendRealPowerkW(self) -> float:
        """
        Returns the chopper sending end power in kW.

        :return: The chopper sending end power in kW.
        :rtype: float
        """
        pass

    def GetSendRealCurrentkA(self) -> float:
        """
        Returns the chopper sending end current in kA.

        :return: The chopper sending end current in kA.
        :rtype: float
        """
        pass

    def GetReceiveRealPowerMW(self) -> float:
        """
        Returns the chopper receiving end power in MW.

        :return: The chopper receiving end power in MW.
        :rtype: float
        """
        pass

    def GetReceiveRealPowerkW(self) -> float:
        """
        Returns the chopper receiving end power in kW.

        :return: The chopper receiving end power in kW.
        :rtype: float
        """
        pass

    def GetReceiveRealCurrentkA(self) -> float:
        """
        Returns the chopper receiving end current in kA.

        :return: The chopper receiving end current in kA.
        :rtype: float
        """
        pass

    def GetLargestRealPowerMW(self) -> float:
        """
        Returns the highest chopper end power in MW.

        :return: The highest chopper end power in MW.
        :rtype: float
        """
        pass

    def GetLargestRealPowerkW(self) -> float:
        """
        Returns the highest chopper end power in kW.

        :return: The highest chopper end power in kW.
        :rtype: float
        """
        pass

    def GetLargestRealCurrentkA(self) -> float:
        """
        Returns the highest chopper end current in kA.

        :return: The highest chopper end current in kA.
        :rtype: float
        """
        pass

    def GetLossesMW(self) -> float:
        """
        Returns the chopper losses in MW.

        :return: The chopper losses in MW.
        :rtype: float
        """
        pass

    def GetLosseskW(self) -> float:
        """
        Returns the chopper losses in kW.

        :return: The chopper losses in kW.
        :rtype: float
        """
        pass

    def GetChopperEfficiency(self) -> float:
        """
        Returns the efficiency of the chopper in percent.

        :return: The efficiency of the chopper in percent.
        :rtype: float
        """
        pass

    def GetLoadRatio(self) -> float:
        """
        Returns the ratio of the internal resistance to the load of the chopper for clearer visualization of buck-boost
        losses (fractional value).

        :return: The ratio of the internal resistance to the load of the chopper.
        :rtype: float
        """
        pass

class IscCircuitBreaker:
    """
    Provides access to an IPSA circuit breaker.
    """
    def GetBranchUID(self) -> int:
        """
        Returns the UID of the branch which the breaker is located on.

        :return: The UID of the branch which the breaker is located on.
        :rtype: int
        """
        pass

    def GetBusbarUID(self) -> int:
        """
        Returns the UID of the busbar that the breaker is connected to.
        If the breaker is located on the sending end of a branch, then the UID of the sending end busbar is returned.

        :return: The UID of the busbar that the breaker is connected to.
        :rtype: int
        """
        pass

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

    def PopulateByDBEntry(self, strBreakerDataName: str) -> bool:
        """
        Populates the object data with database information from the first database that was loaded.

        :param strBreakerDataName: The break data name.
        :type strBreakerDataName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

class IscConverter:
    """
    Provides access to an AC/DC Converter.
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
        Returns the AC real power output of the converter in MW.

        :return: The AC real power output of the converter in MW.
        :rtype: float
        """
        pass

    def GetACRealPowerkW(self) -> float:
        """
        Returns the AC real power output of the converter in kW.

        :return: The AC real power output of the converter in kW.
        :rtype: float
        """
        pass

    def GetACReactivePowerMVAr(self) -> float:
        """
        Returns the AC reactive power output of the converter in MVAr.

        :return: The AC reactive power output of the converter in MVAr.
        :rtype: float
        """
        pass

    def GetACReactivePowerkVAr(self) -> float:
        """
        Returns the AC reactive power output of the converter in kVAr.

        :return: The AC reactive power output of the converter in kVAr.
        :rtype: float
        """
        pass

    def GetACTotalPowerMVA(self) -> float:
        """
        Returns the total AC output power of the converter in MVA.

        :return: The total AC output power of the converter in MVA.
        :rtype: float
        """
        pass

    def GetACTotalPowerkVA(self) -> float:
        """
        Returns the total AC output power of the converter in kVA.

        :return: The total AC output power of the converter in kVA.
        :rtype: float
        """
        pass

    def GetACCurrentkA(self) -> float:
        """
        Returns the AC current of the converter in kA.

        :return: The AC current of the converter in kA.
        :rtype: float
        """
        pass

    def GetDCRealPowerMW(self) -> float:
        """
        Returns the DC real power output of the converter in MW.

        :return: The DC real power output of the converter in MW.
        :rtype: float
        """
        pass

    def GetDCRealPowerkW(self) -> float:
        """
        Returns the DC real power output of the converter in kW.

        :return: The DC real power output of the converter in kW.
        :rtype: float
        """
        pass

    def GetDCTotalPowerMVA(self) -> float:
        """
        Returns the total DC output power of the converter in MVA.

        :return: The total DC output power of the converter in MVA.
        :rtype: float
        """
        pass

    def GetDCTotalPowerkVA(self) -> float:
        """
        Returns the total DC output power of the converter in kVA.

        :return: The total DC output power of the converter in kVA.
        :rtype: float
        """
        pass

    def GetDCCurrentkA(self) -> float:
        """
        Returns the DC current of the converter in kA.

        :return: The DC current of the converter in kA.
        :rtype: float
        """
        pass

    def GetTapPC(self) -> float:
        """
        Returns the operating tap setting of the converter transformer in percentage of nominal.

        :return: The operating tap setting of the converter transformer in percentage of nominal.
        :rtype: float
        """
        pass

    def GetFundamentalEMFMagnitude(self) -> float:
        """
        Returns the fundamental EMF magnitude of the converter.

        :return: The fundamental EMF magnitude of the converter.
        :rtype: float
        """
        pass

    def GetFundamentalEMFAngle(self) -> float:
        """
        Returns the fundamental EMF angle of the converter.

        :return: The fundamental EMF angle of the converter.
        :rtype: float
        """
        pass

    def GetModulationIndex(self) -> float:
        """
        Returns the modulation index of the converter.

        :return: The modulation index of the converter.
        :rtype: float
        """
        pass

class IscDCMachine:
    """
    Provides access to an IPSA DC machine.
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

class IscDiagram:
    """
    The ``IscDiagram`` class provides access to graphical data on a single IPSA diagram.
    These functions allow network components to be drawn, display options to be set and deleted.

    The creation of items on the diagram also creates the associated network components.
    The parameters of these components can then be set using the functions described for the particular component types.

    The origin for the co-ordinates is normally the top left corner of the diagram.
    Positive values of X are to the right whilst positive values of Y are down below the origin.
    """
    def GetName(self) -> str:
        """
        Returns the name of the diagram.

        :return: The name of the diagram.
        :rtype: str
        """
        pass

    def SetName(self, strName: str) -> None:
        """
        Sets the name of the diagram.

        :param strName: The name of the diagram.
        :type strName: str
        """
        pass

    def GetUID(self) -> int:
        """
        Returns the unique diagram ID.

        :return: The ID of the diagram.
        :rtype: int
        """
        pass

    def CreateBusbarPoint(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        A point busbar symbol is a small dot which does not resize as the diagram zoom level is changed.

        :param strName: The busbar name.
        :type strName: str
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def CreateBusbarJunction(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        A junction busbar symbol is the circular junction symbol.

        :param strName: The busbar name.
        :type strName: str
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def CreateBusbarHexagonal(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        A hexagonal busbar symbol has six sides.

        :param strName: The busbar name.
        :type strName: str
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def CreateBusbarCircular(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        A circular busbar symbol is a circle.

        :param strName: The busbar name.
        :type strName: str
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def CreateBusbarRectangular(self, strName: str, bHorizontal: bool, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        The rectangular symbol is the standard horizontal or vertical busbar.

        :param strName: The busbar name.
        :type strName: str
        :param bHorizontal: True draws a horizontal rectangular busbar, while False draws a vertical busbar.
        :type bHorizontal: bool
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def DrawBusbarPoint(self, nUID: int, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        A point busbar symbol is displayed as a small dot which does not resize as the diagram zoom level is changed.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarJunction(self, nUID: int, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        A junction busbar symbol is the solid circular junction symbol.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarHexagonal(self, nUID: int, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        The hexagonal symbol is the standard filled hexagonal busbar.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarRectangular(self, nUID: int, bHorizontal: bool, dSize: float, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        The rectangular symbol is the standard horizontal or vertical busbar.

        :param nUID: The busbar UID.
        :type nUID: int
        :param bHorizontal: True draws a horizontal rectangular busbar, while False draws a vertical busbar.
        :type bHorizontal: bool
        :param dSize: The length of the busbar symbol.
        :type dSize: float
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarCircular(self, nUID: int, dSize: float, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        The circular symbol is the larger unfilled circle.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dSize: The radius of the busbar symbol.
        :type dSize: float
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def CreateLine(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        *Deprecated in Ipsa 2.10.2.* Instead, use CreateBranch.

        Creates a new branch component on the diagram.

        :param strName: The branch name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new branch.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    # Fixing gaps in documentation EL 11/2023
    def CreateBranch(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        Creates a new branch component on the diagram.

        :param strName: The branch name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new branch.
            If the branch cannot be drawn, the return value is 0.
        :rtype: int
        """
        pass

    def DrawLine(self, nUID: int) -> bool:
        """
        Draws the symbol for the line identified by the unique ID.
        The line is drawn as a single segment between two busbars.
        The line must have been created using one of the following first:

            - IscDiagram.CreateLine
            - IscNetwork.CreateBranch
            - IscNetwork.CreateTransformer

        :param nUID: The line UID.
        :type nUID: int
        :return: Boolean denoting whether the line was drawn.
        :rtype: bool
        """
        pass

    def CreateBreaker(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new circuit breaker on the diagram.
        Note branch has to have already been drawn.

        :param strName: The breaker name.
        :type strName: str
        :param dX: The x coordinate of the circuit breaker.
        :type dX: float
        :param dY: The y coordinate of the circuit breaker.
        :type dY: float
        :return: The unique positive ID of the new circuit breaker.
            If the breaker cannot be drawn, the return value is 0.
        :rtype: int
        """
        pass

    def DrawBreaker(self, nBreakerUID: int, dX: float, dY: float) -> bool:
        """
        Draws the symbol for the breaker identified by the unique ID nBreakerUID at the location dX,dY.

        :param nBreakerUID: The breaker UID.
        :type nBreakerUID: int
        :param dX: The x coordinate of the circuit breaker.
        :type dX: float
        :param dY: The y coordinate of the circuit breaker.
        :type dY: float
        :return: The function returns True if the breaker was drawn
        :rtype: bool
        """
        pass

    def CreateTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        *Deprecated in Ipsa 2.10.2.* Instead, use Create2WTransformer.

        Creates a new transformer component on the diagram.

        :param strName: The branch name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new transformer.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    # Fixing gaps in documentation EL 11/2023
    def Create2WTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        Creates a new transformer component on the diagram.

        :param strName: The transformer name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the transformer starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the transformer starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the transformer ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the transformer ends.
        :type dYTo: float
        :return: The unique positive ID of the new transformer.
            If the transformer cannot be drawn, the return value is 0.
        :rtype: int
        """
        pass

    def DrawTransformer(self, nUID: int) -> bool:
        """
        Draws the symbol for the transformer identified by the unique ID.
        The line is drawn as a single segment between two busbars.
        The line must have been created using the following first:

            - IscNetwork.CreateTransformer

        :param nUID: The transformer UID.
        :type nUID: int
        :return: Boolean denoting whether the line was drawn.
        :rtype: bool
        """
        pass

    def CreateUnbalancedLine(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        *Deprecated in Ipsa 2.10.2.* Instead, use CreateUnbalancedBranch.

        Creates a new unbalanced line component on the diagram.

        :param strName: The unbalanced line name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new unbalanced line component.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    # Fixing gaps in documentation EL 11/2023
    def CreateUnbalancedBranch(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        Creates a new unbalanced line component on the diagram.

        :param strName: The unbalanced line name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the unbalanced line starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the unbalanced line starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the unbalanced line ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the unbalanced line ends.
        :type dYTo: float
        :return: The unique positive ID of the new unbalanced line component.
            If the unbalanced line cannot be drawn, the return value is 0.
        :rtype: int
        """
        pass

    def CreateUnbalancedTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        *Deprecated in Ipsa 2.10.2.* Instead, use CreateUnbalanced2WTransformer.

        Creates a new unbalanced transformer component on the diagram.

        :param strName: The unbalanced transformer name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new unbalanced transformer component.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    # Fixing gaps in documentation EL 11/2023
    def CreateUnbalanced2WTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float,
                                      dYTo: float) -> int:
        """
        Creates a new unbalanced transformer component on the diagram.

        :param strName: The unbalanced transformer name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the unbalanced transformer starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the unbalanced transformer starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the unbalanced transformer ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the unbalanced transformer ends.
        :type dYTo: float
        :return: The unique positive ID of the new unbalanced transformer component.
            If the unbalanced transformer cannot be drawn, the return value is 0.
        :rtype: int
        """
        pass

    def AddPointToLine(self, nLineUID: int, dX: float, dY: float, bFromEnd: bool, bRefreshLine: bool) -> bool:
        """
        Adds a knee point to the line identified by the unique ID. By default, this function will fully redraw the line
        the knee point has been added to. This can be disabled by setting bRefreshLine to False.

        *Deprecated in IPSA 2.10.3 instead use AddKneepoint*

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param dX: The knee point x coordinate.
        :type dX: float
        :param dY: The knee point y coordinate.
        :type dY: float
        :param bFromEnd: If True then the knee point is added to the last segment, i.e. furthest from the From end.
            If False then the knee point is added to the first segment.
        :type bFromEnd: float
        :param bRefreshLine: Defaults to True. If True, the line is fully redrawn when the knee point is added.
        :type bRefreshLine: bool
        :return: Boolean denoting whether the knee point was added.
        :rtype: bool
        """
        pass

    def AddKneepoint(self, nLineUID: int, dX: float, dY: float, bFromEnd: bool, bRefreshLine: bool) -> bool:
        """
        Adds a knee point to the line identified by the unique ID. By default, this function will fully redraw the line
        the knee point has been added to. This can be disabled by setting bRefreshLine to False.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param dX: The knee point x coordinate.
        :type dX: float
        :param dY: The knee point y coordinate.
        :type dY: float
        :param bFromEnd: If True then the knee point is added to the last segment, i.e. furthest from the From end.
            If False then the knee point is added to the first segment.
        :type bFromEnd: float
        :param bRefreshLine: Defaults to True. If True, the line is fully redrawn when the knee point is added.
        :type bRefreshLine: bool
        :return: Boolean denoting whether the knee point was added.
        :rtype: bool
        """
        pass

    def AddKneepoints(self, nLineUID: int, listX: list[float], listY: list[float], bFromEnd: bool,
                      bRefreshLine: bool) -> bool:
        """
        Adds multiple knee points to the line identified by the unique ID. By default, this function will fully redraw
        the line the knee point has been added to. This can be disabled by setting bRefreshLine to False.

        If listX and listY are not of the same length, no kneepoints will be added.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param listX: A list of x coordinates for each knee point to be added.
        :type listX: list(float)
        :param listY: A corresponding list of y coordinates for each knee point to be added.
        :type listY: list(float)
        :param bFromEnd: If True then the knee point is added to the last segment, i.e. furthest from the From end.
            If False then the knee point is added to the first segment.
        :type bFromEnd: float
        :param bRefreshLine: Defaults to True. If True, the line is fully redrawn when the knee point is added.
        :type bRefreshLine: bool
        :return: Boolean denoting whether the knee points were added.
        :rtype: bool
        """
        pass

    def DeleteKneepoint(self, nLineUID: int, dX: float, dY: float, bRefreshLine: bool) -> bool:
        """
        Deletes a specific knee point from the line identified by the unique ID. If no kneepoint is found at the
        provided coordinates, nothing will occur. By default, this function will fully redraw the line the knee point
        has been deleted from. This can be disabled by setting bRefreshLine to False.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param dX: The knee point x coordinate.
        :type dX: float
        :param dY: The knee point y coordinate.
        :type dY: float
        :param bRefreshLine: Defaults to True. If True, the line is fully redrawn when the knee point is added.
        :type bRefreshLine: bool
        :return: Boolean denoting whether the knee point was added.
        :rtype: bool
        """
        pass

    def DeleteAllKneepoints(self, nLineUID: int, bRefreshLine: bool) -> bool:
        """
        Deletes all the knee points from the line identified by the unique ID. By default, this function will fully
        redraw the line the knee point has been deleted from. This can be disabled by setting bRefreshLine to False.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param bRefreshLine: Defaults to True. If True, the line is fully redrawn when the knee point is added.
        :type bRefreshLine: bool
        :return: Boolean denoting whether the knee point was added.
        :rtype: bool
        """
        pass

    def RefreshLine(self, nLineUID: int) -> None:
        """
        Redraws the line identified by the line UID after knee points have been added.

        :param nLineUID: The line UID.
        :type nLineUID: int
        """
        pass

    def SplitBranch(self, nLineUID: int, nSection: int, dRatio: float, strName: str) -> int:
        """
        *Deprecated. Instead, use IscNetwork.SplitBranch.*
        Splits a branch into two sections connected by a new busbar.
        This will only act if the branch is only drawn in this IscDiagram instance.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param nSection: Specifies which section of a multi-section branch is split.
            For branches with only one section then nSection should be set to 0.
        :type nSection: int
        :param dRatio: Specifies how the branch impedances are divided between the new branches.
            A value of 0.0 sets the split position to be at the “From” end whilst a value of 1.0 specifies the “To” end.
            Values between 0.0 and 1.0 split the branch in proportion.
            For multi-section branches dRatio splits the section identified by nSection.
        :type dRatio: float
        :param strName: The name of the busbar.
        :type strName: str
        :return: The UID of the new branch if it is greater than 0. ) if the branch has not been split.
            This is because there is a circuit breaker on the branch or the branch is drawn on more than one diagram.
        :rtype: int
        """
        pass

    def DrawUndrawnItemsAttachedToBusbar(self, nBusbarUID: int) -> None:
        """
        Draws items attached to the busbar identified by the busbar UID if they are not already drawn on the diagram.
        Note that this will draw branch items as well.

        :param nBusbarUID: The busbar UID.
        :type nBusbarUID: int
        """
        pass

    def DeleteItem(self, nUID: int) -> bool:
        """
        Deletes the graphic item identified by the UID. This may be a line, radial component or busbar.

        :param nUID: The graphical item UID.
        :type nUID: int
        :return: ``True`` if deletion is successful.
        :rtype: bool
        """
        pass

    @overload
    def GetLineLength(self, nUID: int) -> float:
        """
        Returns the component length for the graphic symbol on the current diagram.
        On geographic diagrams this function returns the actual line length,
        assuming that the diagram is correctly scaled.

        :param nUID: The line UID.
        :type nUID: int
        :return: The component length for the graphic symbol.
        :rtype: float
        """
        pass

    @overload
    def GetLineLength(self, pComponent) -> float:
        """
        Returns the component length for the graphic symbol on the current diagram.
        On geographic diagrams this function returns the actual line length,
        assuming that the diagram is correctly scaled.

        :param pComponent: The line IscBranch instance.
        :type pComponent: IscBranch
        :return: The component length for the graphic symbol.
        :rtype: float
        """
        pass

    def GetLineLength(self, pComponent) -> float:
        """
        Returns the component length for the graphic symbol on the current diagram.
        On geographic diagrams this function returns the actual line length,
        assuming that the diagram is correctly scaled.

        :param nUID: The line UID.
        :type nUID: int
        :param pComponent: The line IscBranch instance.
        :type pComponent: IscBranch
        :return: The component length for the graphic symbol.
        :rtype: float
        """
        pass

    def SetItemPenColour(self, nUID: int, nRed: int, nGreen: int, nBlue: int, nAlpha: int) -> bool:
        """
        Sets the outline colour of the diagram object.
        The colour is set by the RGB parameters.
        All colour parameters should be between 0 and 255.

        :param nUID: The diagram object UID.
        :type nUID: int
        :param nRed: The red colour.
        :type nRed: int
        :param nGreen: The green colour.
        :type nGreen: int
        :param nBlue: The blue colour.
        :type nBlue: int
        :param nAlpha: The transparency of the colour.
        :type nAlpha: int
        :return: Denoting whether the colour is set.
        :rtype: bool
        """
        pass

    def SetItemBrushColour(self, nUID: int, nRed: int, nGreen: int, nBlue: int, nAlpha: int) -> bool:
        """
        Sets the fill colour of the diagram object.
        The colour is set by the RGB parameters.
        All colour parameters should be between 0 and 255.

        :param nUID: The diagram object UID.
        :type nUID: int
        :param nRed: The red colour.
        :type nRed: int
        :param nGreen: The green colour.
        :type nGreen: int
        :param nBlue: The blue colour.
        :type nBlue: int
        :param nAlpha: The transparency of the colour.
        :type nAlpha: int
        :return: Denoting whether the colour is set.
        :rtype: bool
        """
        pass

    def MapToLatLong(self, fScreenX: float, fScreenY: float) -> List[float]:
        """
        Returns the latitude and longitude in decimal degrees of the screen position.
        The diagram is the one referenced by the IscDiagram object that the function is called on.
        The fScreenX and fScreenY parameters are relative to the nominal centre point of the screen,
        therefore calling this function with fScreenX = 0.0 and fScreenY = 0.0 returns the centre point of
        the background map in degrees.
        Note that the screen X is north/south and screen y is east/west.

        :param fScreenX: The x coordinate of the screen position.
        :type fScreenX: float
        :param fScreenX: The y coordinate of the screen position.
        :type fScreenX: float
        :return: The latitude and longitude of the screen position.
        :rtype: list(float)
        """
        pass

    def LatLongToMap(self, fN: float, fE: float) -> List[float]:
        """
        Returns the screen X and Y coordinates of the latitude and longitude.
        The fScreenX and fScreenY coordinates are relative to the nominal centre point of the screen
        which can be found by the MapToLatLong function.
        Note that the screen X is north/south and screen y is east/west.

        :param fN: The latitude.
        :type fN: float
        :param fE: The longitude.
        :type fE: float
        :return: The screen X and Y coordinates.
        :rtype: list(float)
        """
        pass

    def GetUIDFromCoordinates(self, dX: float, dY: float) -> int:
        """
        Returns the UID of a component at coordinates  (dX, dY).
        The screen coordinates are relative to the nominal centre point of the screen.

        :param dX: The screen X coordinate.
        :type dX: float
        :param dY: The screen Y coordinate.
        :type dY: float
        :return: The UID of the component located.
            Returns 0, if the component cannot be found,
        :rtype: int
        """
        pass

    def GetBusbarUIDFromCoordinates(self, dX: float, dY: float) -> int:
        """
        Returns the UID of a busbar at coordinates (dX, dY).
        The screen coordinates are relative to the nominal centre point of the screen.

        :param dX: The screen X coordinate.
        :type dX: float
        :param dY: The screen Y coordinate.
        :type dY: float
        :return: The UID of the component located.
            Returns 0, if the component cannot be found,
        :rtype: int
        """
        pass

    def GetItemX(self, nUID: int) -> float:
        """
        Returns the screen X coordinate of the busbar.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The busbar UID.
        :type nUID: int
        :return: The screen X coordinate.
        :rtype: float
        """
        pass

    def GetItemY(self, nUID: int) -> float:
        """
        Returns the screen Y coordinate of the busbar.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The busbar UID.
        :type nUID: int
        :return: The screen Y coordinate.
        :rtype: float
        """
        pass

    def GetItemFromXPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen X coordinates of the FROM busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the FROM end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen X coordinates.
        :rtype: float
        """
        pass

    def GetItemFromYPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen Y coordinates of the FROM busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the FROM end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen Y coordinates.
        :rtype: float
        """
        pass

    def GetItemToXPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen X coordinates of the TO busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the TO end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen X coordinates.
        :rtype: float
        """
        pass

    def GetItemToYPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen Y coordinates of the TO busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the TO end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen Y coordinates.
        :rtype: float
        """
        pass

    def CreateAnnotation(self, strName: str, strAnnotationText: str, dX: float, dY: float) -> int:
        """
        Creates a new diagram annotation.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param strName: The strName is not used and can be an empty string.
        :type strName: str
        :param strAnnotationText: The text to be displayed on the diagram.
            The text string can include simple html for text formatting.
        :type strAnnotationText: str
        :param dX: The x coordinate of the diagram.
        :type dX: float
        :param dY: The y coordinate of the diagram.
        :type dY: float
        :return: The diagram annotation.
        :rtype: int
        """
        pass

    def PrintPDF(self, strFileName: str, bRefreshDiagram: bool = True ) -> None:
        """
        Print the diagram to a PDF format file with name strFileName.

        :param strFileName: The path and filename where the PDF should be saved (including the .pdf extension).
        :type strFileName: str
        :param bRefreshDiagram: If True, calls RefreshDiagram before saving, so the diagram is up-to-date with any
            changes made in scripting.
        :type bRefreshDiagram: bool
        """
        pass

    def SetLabelCharacteristics(self, nUID: int, bShowLabel: bool, bFixedSize: bool) -> bool:
        """
        Sets whether the label for the component identified by the given UID is visible, and
        whether it scales with zoom.
        This can also be set from Data Display Styles.

        :param nUID: The UID of the component with the label to be modified.
        :type nUID: int
        :param bShowLabel: True if the label should be visible.
        :type bShowLabel: bool
        :param bFixedSize: True if the label has a fixed size on scaling.
        :type bFixedSize: bool
        :return: Returns True if the values have been set.
        :rtype: bool
        """
        pass

    def SetBackgroundColour(self, strHexColour: str) -> None:
        """
        Sets the diagram background colour to the specified hex colour.
        strHexColour can either be set as a hex colour code or as one of the SVG color keyword names.

        :param strHexColour: The hex colour to set the diagram background to.
        :type strHexColour: str
        """
        pass

    def SetBackgroundImage(self, dOpacity: float, strImageFile: str, dWidth: float, dHeight: float,
                           bKeepAspectRatio: bool) -> None:
        """
        Sets the background image of a diagram to the image found in strImageFile. The background image is displayed
        with the opacity defined by dOpacity, and the image size defined by dWidth and dHeight. If bKeepAspectRatio is
        set to True, dHeight is ignored, and the image is displayed with the width determined by dWidth and a height
        automatically calculated to maintain the image aspect ratio.

        Note, if strImageFile is not a valid image path, the background image will be cleared.

        :param dOpacity: The opacity of the background image in the range 0-1.
        :type dOpacity: float
        :param strImageFile: The path to the new background image.
        :type strImageFile: str
        :param dWidth: The pixel width the background image will be displayed with.
        :type dWidth: float
        :param dHeight: The pixel height the background image will be displayed with.
        :type dHeight: float
        :param bKeepAspectRatio: If True, dHeight is auto-calculated to maintain the provided image aspect ratio.
        :type bKeepAspectRatio: bool
        """
        pass

    def RefreshDiagram(self) -> None:
        """
        Refreshes the diagram to ensure that the diagram window is up to date with the data held in IPSA.

        """
        pass

class IscFilter:
    """
    Provides access to an IPSA harmonic filter.
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

    def GetPowerMagnitudeMVA(self) -> float:
        """
        Returns the filter absorbed power in MVA.

        :return: The filter absorbed power in MVA.
        :rtype: float
        """
        pass

    def GetPowerMagnitudekVA(self) -> float:
        """
        Returns the filter absorbed power in kVA.

        :return: The filter absorbed power in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerMW(self) -> float:
        """
        Returns the filter absorbed power in MW.

        :return: The filter absorbed power in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerMVAr(self) -> float:
        """
        Returns the filter absorbed power in MVAr.

        :return: The filter absorbed power in MVAr.
        :rtype: float
        """
        pass

    def GetRealPowerkW(self) -> float:
        """
        Returns the filter absorbed power in kW.

        :return: The filter absorbed power in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerkVAr(self) -> float:
        """
        Returns the filter absorbed power in kVAr.

        :return: The filter absorbed power in kVAr.
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

    def GetDCLFRealPowerMW(self) -> float:
        """
        Returns the generator output in MW.

        :return: The generator output in MW.
        :rtype: float
        """
        pass

    def GetDCLFRealPowerkW(self) -> float:
        """
        Returns the generator output in kW.

        :return: The generator output in kW.
        :rtype: float
        """
        pass

class IscGridInfeed:
    """
    Provides access to an IPSA grid infeed.
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

    def SetHarmonicR(self, dictHarmonicData: Dict[float, float]) -> None:
        """
        Sets the values for the harmonic resistance of the grid infeed.

        :param dictHarmonicData: Dictionary in the following format:
            **{double dHarmonicOrder:double dHarmonicImpedance, …}** where dHarmonicImpedance is a value specifying the
            harmonic resistance at the frequency given by the harmonic order dHarmonicOrder. Up to 120 different orders
            may be specified in each grid infeed.
        :type dictHarmonicData: dict(float,float)
        """
        pass

    def SetHarmonicX(self, dictHarmonicData: Dict[float, float]) -> None:
        """
        Sets the values for the harmonic reactance of the grid infeed.

        :param dictHarmonicData: Dictionary in the following format:
            **{double dHarmonicOrder:double dHarmonicImpedance, …}** where dHarmonicImpedance is a value specifying the
            harmonic resistance at the frequency given by the harmonic order dHarmonicOrder. Up to 120 different orders
            may be specified in each grid infeed.
        :type dictHarmonicData: dict(float,float)
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

    def GetDCLFRealPowerMW(self) -> float:
        """
        Returns the generator output in MW.

        :return: The generator output in MW.
        :rtype: float
        """
        pass

    def GetDCLFRealPowerkW(self) -> float:
        """
        Returns the generator output in kW.

        :return: The generator output in kW.
        :rtype: float
        """
        pass

from typing import List


class IscGroup:
    """
    The IscGroup class provides access to an IPSA group to set and get group members.
    Note the extension functions will only work for general groups and may not function for other groups e.g., areas, transformer
    groups.
    """
    def GetUID(self) -> int:
        """
        Returns the UID of the group.

        :return: The group UID.
        :rtype: int
        """
        pass

    def GetName(self) -> str:
        """
        Returns the user defined group name as a string.

        :return: The user defined group name.
        :rtype: str
        """
        pass

    def SetName(self, strName: str) -> None:
        """
        Sets the name as a string.

        :param strName: The selected string name.
        :type strName: str
        """
        pass

    def GetGroupType(self) -> int:
        """
        Returns the type of the group where:

            - 0 = No group type
            - 1 = Area type group – contains all busbars in an area
            - 2 = Mixed item group
            - 3 = Load scaling group
            - 4 = Load transfer group
            - 5 = Protection device group
            - 8 = Generator scaling group
            - 9 = Region group
            - 10 = Transformer group (master slave operation)

        :return: The group type.
        :rtype: int
        """
        pass

    def GetMembers(self) -> List[int]:
        """
        Returns a list containing the UIDs of the components in the group.

        :return: The UIDs of the components in the group.
        :rtype: list(int)
        """
        pass

    def SetMembers(self, nUIDs: List[int]) -> None:
        """
        Overwrites the current list of group members with the given list of component UIDs.
        This replaces any existing members with the supplied list of UIDs.

        :param nUIDs: List of component integers.
        :type nUIDs: list(int)
        """
        pass

    def ClearMembers(self) -> None:
        """
        Sets the group members to an empty list.
        This clears any existing members.
        """
        pass

    def AddMember(self, nUID: int) -> None:
        """
        Appends the component with the given UID to the list of component UIDs if the UID is not present.
        All existing group member UIDs are unaffected.

        :param nUID: Component UID.
        :type nUID: int
        """
        pass

    def RemoveMember(self, nUID: int) -> None:
        """
        Removes the component with the given UID from the list of component UIDs if the UID is present.
        All other existing group member UIDs are unaffected.

        :param nUID: Component UID.
        :type nUID: int
        """
        pass

    def IsMember(self, nUID: int) -> bool:
        """
        Checks whether the component with the given UID is present in the list of component UIDs.
        The list of group member UIDs will be unaffected.

        :param nUID: Component UID.
        :type nUID: int
        :return: True if nUID is present in list of member UIDs.
        :rtype: bool
        """
        pass

    def CompareGroups(self, nGroupUID: int, bUseIntersection: bool = False) -> List[int]:
        """
        Compares the current group with the group with UID given by nGroupUID.
        By default, will perform a difference operation returning a list of component UIDs present in the current group
        but not present in the group with UID given by nGroupUID.
        If bUseIntersection is True it will return a list of component UIDs present in both lists.
        Both lists of group member UIDs will be unaffected.

        :param nGroupUID: UID of the group to compare with.
        :type nGroupUID: int
        :param bUseIntersection: If True performs an intersection, if False a difference operation.
        :type bUseIntersection: bool
        :return: The list of UIDs that make up the difference (default) or intersection of the two groups.
        :rtype: list(int)
        """
        pass

    def MergeGroups(self, nGroupUID: int, bDeleteGroup: bool = False) -> None:
        """
        Appends the list of component UIDs from the group with the given UID onto the current group's UID list.
        By default the group with the given UID will be unnaffected, unless bDeleteGroup is True, in which case it will be deleted.

        :param nGroupUID: UID of the group to merge with.
        :type nGroupUID: int
        :param bDeleteGroup: If True deletes the group with nGroupUID, otherwise the group is unnaffected.
        :type bDeleteGroup: bool
        """
        pass

    def GetLoadScalingReal(self) -> float:
        """
        Returns the per unit scaling factor for the active power load.

        :return: The per unit scaling factor for the active power load.
        :rtype: float
        """
        pass

    def GetLoadScalingReactive(self) -> float:
        """
        Returns the per unit scaling factor for the reactive power load.

        :return: The per unit scaling factor for the reactive power load.
        :rtype: float
        """
        pass

    def SetLoadScaling(self, fMW: float, fMVAr: float) -> bool:
        """
        Sets the per unit scaling factors for the active and reactive parts of the load.

        :param fMW: The active part of the load.
        :type fMW: float
        :param fMVAr: The reactive part of the load.
        :type fMVAr: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def AddDataExtension(self, strName: str, default: Union[int,float,str, bool]) -> int:
        """
        Adds an integer/float/string/double extension data field and returns the new field index.
        Sets the default value.

        This only has to be called once per component type - not for every instance of the component!

        **Note: The variable of the function is not called default.**

        You can use either nDefault, dDefault, strDefault or bDefault to specify the default value depending on the
        type of data extension being added.

        :param strName: The name of the field.
        :type strName: str
        :param nDefault: The integer default value.
        :type nDefault: int
        :param dDefault: The float default value.
        :type dDefault: float
        :param strDefault: The string default value.
        :type strDefault: str
        :param bDefault: The bool default value.
        :type bDefault: bool
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListIntDataExtension(self, strName: str) -> int:
        """
        Adds a data field for a list of integers and returns the new field index.
        Sets the default value to an empty list.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListDblDataExtension(self, strName: str) -> int:
        """
        Adds a data field for a list of doubles and returns the new field index.
        Sets the default value to an empty list.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListStrDataExtension(self, strName: str) -> int:
        """
        Adds a data field for a list of strings and returns the new field index.
        Sets the default value to an empty list.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    @overload
    def DeleteDataExtensionField(self, nFieldIndex: int) -> bool:
        """
        Deletes the extension field identified by the index nFieldIndex. This will delete the data in this extension
        field from this group and all other groups of the same type.
        It is advised to call NonDefaultExtensionInstanceCount prior to deleting the data extension field to ensure the
        expected amount of data shall be deleted.

        This only has to be called once per component type - not for every instance of the component!

        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: True if the field is deleted successfully.
        :rtype: bool
        """
        pass

    @overload
    def DeleteDataExtensionField(self, strName: str) -> bool:
        """
        Deletes the extension field identified by the name strName. This will delete the data in this extension field
        from this group and all other groups of the same type.
        It is advised to call NonDefaultExtensionInstanceCount prior to deleting the data extension field to ensure the
        expected amount of data shall be deleted.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: True if the field is deleted successfully.
        :rtype: bool
        """
        pass

    def DeleteDataExtensionField(self, strName: str) -> bool:
        """
        Deletes the extension field identified by the name strName or index nFieldIndex. This will delete the data in
        this extension field from this group and all other groups of the same type.
        It is advised to call NonDefaultExtensionInstanceCount prior to deleting the data extension field to ensure the
        expected amount of data shall be deleted.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: True if the field is deleted successfully.
        :rtype: bool
        """
        pass

    @overload
    def NonDefaultExtensionField(self, nFieldIndex: int) -> int:
        """
        Returns the number of groups of the same type where the extension field identified by nFieldIndex is set to
        a non-default value. That is, the count of the components where data will be destroyed by calling
        DeleteDataExtensionField.

        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: The number of components with a non-default value in the extension field.
        :rtype: int
        """
        pass

    @overload
    def NonDefaultExtensionField(self, strName: str) -> int:
        """
        Returns the number of groups of the same type where the extension field identified by strName is set to
        a non-default value. That is, the count of the components where data will be destroyed by calling
        DeleteDataExtensionField.

        :param strName: The name of the field.
        :type strName: str
        :return: The number of components with a non-default value in the extension field.
        :rtype: int
        """
        pass

    def NonDefaultExtensionField(self, strName: str) -> int:
        """
        Returns the number of groups of the same type where the extension field identified by strName or nFieldIndex is
        set to a non-default value. That is, the count of the components where data will be destroyed by calling
        DeleteDataExtensionField.

        :param strName: The name of the field.
        :type strName: str
        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: The number of components with a non-default value in the extension field.
        :rtype: int
        """
        pass

    def GetIntExtensionValue(self, nFieldIndex: int) -> int:
        """
        Get the integer value from the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The element value.
        :rtype: int
        """
        pass

    def GetDblExtensionValue(self, nFieldIndex: int) -> float:
        """
        Get the float value from the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The element value.
        :rtype: float
        """
        pass

    def GetStrExtensionValue(self, nFieldIndex: int) -> str:
        """
        Get the string value from the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The element value.
        :rtype: str
        """
        pass

    def GetBoolExtensionValue(self, nFieldIndex: int) -> bool:
        """
        Get the boolean value from the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The element value.
        :rtype: bool
        """
        pass

    def GetListIntExtensionValue(self, nFieldIndex: int, nIndex: int) -> int:
        """
        Get a single integer value from the list within the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: int
        """
        pass

    def GetListDblExtensionValue(self, nFieldIndex: int, nIndex: int) -> float:
        """
        Get a single float value from the list within the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: float
        """
        pass

    def GetListStrExtensionValue(self, nFieldIndex: int, nIndex: int) -> str:
        """
        Get a single string value from the list within the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: str
        """
        pass

    def GetListIntSize(self, nFieldIndex: int) -> int:
        """
        Gets the size of the list of integers for the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def GetListDblSize(self, nFieldIndex: int) -> int:
        """
        Gets the size of the list of doubles for the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def GetListStrSize(self, nFieldIndex: int) -> int:
        """
        Gets the size of the list of strings for the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def SetIntExtensionValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Set the integer value for the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The selected value.
        :type nValue: int
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetDblExtensionValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Set the float value for the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The selected value.
        :type dValue: float
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetStrExtensionValue(self, nFieldIndex: int, sValue: str) -> bool:
        """
        Set the string value for the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param sValue: The selected value.
        :type sValue: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetBoolExtensionValue(self, nFieldIndex: int, bValue: bool) -> bool:
        """
        Set the boolean value for the given extension field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param bValue: The selected value.
        :type bValue: bool
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetListIntExtensionValue(self, nFieldIndex: int, nIndex: int, nValue: int) -> bool:
        """
        Sets the value of a specified element in a list of integers within the given enumerated field.

        Note the index within the list, nIndex, must already exist - that is, the size of the list (i.e.,
        GetListIntSize) must be larger than nIndex.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param nValue: The selected value.
        :type nValue: int
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetListDblExtensionValue(self, nFieldIndex: int, nIndex: int, dValue: float) -> bool:
        """
        Sets the value of a specified element in a list of doubles within the given enumerated field.

        Note the index within the list, nIndex, must already exist - that is, the size of the list (i.e.,
        GetListDblSize) must be larger than nIndex.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param dValue: The selected value.
        :type dValue: float
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetListStrExtensionValue(self, nFieldIndex: int, nIndex: int, strValue: str) -> bool:
        """
        Sets the value of a specific element in a list of strings within the given enumerated field.

        Note the index within the list, nIndex, must already exist - that is, the size of the list (i.e.,
        GetListStrSize) must be larger than nIndex.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param strValue: The selected value.
        :type strValue: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListIntExtensionValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Adds an item with the given value to the end of a list of integers within the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The selected value.
        :type nValue: int
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListDblExtensionValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Adds an item with the given value to the end of a list of doubles within the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The selected value.
        :type dValue: float
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListStrExtensionValue(self, nFieldIndex: int, strValue: str) -> bool:
        """
        Adds an item with the given value to the end of a list of strings within the given enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The selected value.
        :type strValue: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def GetExtensionFieldIndex(self, strName: str) -> int:
        """
        Returns the field index for the extended data field of a specified name.

        :param strName: The name of the extended data field.
        :type strName: str
        :return: The field index.
        :rtype: int
        """
        pass

    def GetExtensionNames(self) -> Dict[int,str]:
        """
        Returns a dictionary of extension field indexes and field names.
        The dictionary keys are integers representing all the extended data fields.
        The dictionary values are the field names of the individual extended data fields.
        Each extended data field is therefore represented by {nIndex:strName}, where integer nIndex is the field index
        and string strName is the field name.

        :return: Dictionary of extension field indexes and field names.
        :rtype: dict(int, str)
        """
        pass

class IscHarmonic:
    """
    Provides access to an IPSA harmonic source.
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

    def GetListDValue(self, nFieldIndex: int) -> list[float]:
        """
        Returns a list of double values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[float]
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

    def SetListDValue(self, nFieldIndex: int, lDValue: list[float]) -> bool:
        """
        Sets the value for the enumerated field from a list of doubles.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lDValue: The given list of double values.
        :type lDValue: list[float]
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

    def GetAngleDeg(self, nOrderIndex: int) -> float:
        """
        Gets the current or voltage angle in degrees for the order index.

        :param nOrderIndex: The order index.
        :type nOrderIndex: int
        :return: The current or voltage angle in degrees.
        :rtype: float
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

class IscIndMachine:
    """
    Provides access to an IPSA induction machine.
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

    def PopulateByDBEntry(self, strIMachineDataName: str, nParallel: int) -> bool:
        """
        Populates the object data with database information from the first database that was loaded.

        :param strIMachineDataName: The name of the induction machine.
        :type strIMachineDataName: str
        :param nParallel: The number of parallel components.
        :type nParallel: int
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

    def GetDCLFStatorPowerMagnitudeMVA(self) -> float:
        """
        Returns stator power in MVA.

        :return: The stator power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFStatorPowerMagnitudekVA(self) -> float:
        """
        Returns stator power in kVA.

        :return: The stator power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFStatorRealPowerMW(self) -> float:
        """
        Returns stator power in MW.

        :return: The stator power in MW.
        :rtype: float
        """
        pass

    def GetDCLFStatorRealPowerkW(self) -> float:
        """
        Returns stator power in kW.

        :return: The stator power in kW.
        :rtype: float
        """
        pass

    def GetDCLFEfficiencyPC(self) -> float:
        """
        Returns the motor efficiency in percent.

        :return: The motor efficiency in percent.
        :rtype: float
        """
        pass

    def GetDCLFCurrentkA(self) -> float:
        """
        Returns the total current in kA.

        :return: The total current in kA.
        :rtype: float
        """
        pass

    def GetDCLFCurrentA(self) -> float:
        """
        Returns the total current in Amps.

        :return: The total current in Amps.
        :rtype: float
        """
        pass

class IscInterface:
    """
    The main interface class used to access all other IPSA objects and functions.
    """
    def ReadFile(self, strName: str):
        """
        Opens an IPSA i2f file strName and returns an IscNetwork instance for that file.

        :param strName: The IPSA i2f file that is going to be opened.
        :type strName: str
        :return: The IscNetwork instance for the strName file
        :rtype: IscNetwork
        """
        pass

    def ReadIpsa1File(self, strName: str):
        """
        Imports an IPSA 1 (\*.iif) file strName and returns an IscNetwork instance for that file.

        :param strName: The IPSA i2f file that is going to be imported.
        :type strName: str
        :return: The IscNetwork instance for the strName file
        :rtype: IscNetwork
        """
        pass

    def GetNetwork(self):
        """
        Returns an IscNetwork instance for the current IPSA network.

        :return: The IscNetwork instance of the IPSA network.
        :rtype: IscNetwork
        """
        pass

    def CloseNetwork(self) -> bool:
        """
        Closes the current network. Returns False if the network can’t be closed, e.g. if there is unsaved data.

        :return: Boolean denoting whether the network is closed.
        :rtype: bool
        """
        pass

    @overload
    def GetDiagram(self, network, strName: str):
        """
        Returns an IscDiagram instance for the diagram with name strName contained in the identified network.

        :param network: The IscNetwork instance of the IPSA network.
        :type network: IscNetwork
        :param strName: The name of the diagram.
        :type strName: str
        :return: The diagram of the IPSA network.
        :rtype: IscDiagram
        """
        pass

    @overload
    def GetDiagram(self, network, nUID: int):
        """
        Returns an IscDiagram instance for the diagram with ID nUID contained the identified network.

        :param network: The IscNetwork instance of the Ipsa network.
        :type network: IscNetwork
        :param nUID: The diagram ID.
        :type nUID: int
        :return: The diagram of the Ipsa network.
        :rtype: IscDiagram
        """
        pass

    def GetDiagram(self, network, strName: str):
        """
        Returns an IscDiagram instance for the diagram with name strName or ID nUID contained in the identified network.

        :param network: The IscNetwork instance of the Ipsa network.
        :type network: IscNetwork
        :param strName: The name of the diagram.
        :type strName: str
        :param nUID: The diagram ID.
        :type nUID: int
        :return: The diagram of the Ipsa network.
        :rtype: IscDiagram
        """
        pass

    def CreateNewNetwork(
            self,
            dSystemBaseMVA: float,
            dFrequencyHz: float,
            bWithDiagram: bool,
            bIsDiagramSingleLine: bool,
            dGeoSceneScale: float,
            nSceneMeasurementUnit: int
    ) -> bool:
        """
        Creates a new IPSA network based on the supplied parameters. Returns False if the network can’t be created.

        :param dSystemBaseMVA: The network base MVA.
        :type dSystemBaseMVA: float
        :param dFrequencyHz: The nominal network frequency in hertz.
        :type dFrequencyHz: float
        :param bWithDiagram: Denoting whether the diagram is required.
        :type bWithDiagram: bool
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :return: Boolean denoting whether a network can be created.
        :rtype: bool
        """
        pass

    def MergeFile(self, sMergeName: str) -> bool:
        """
        Merges the IPSA I2F file sMergeName into the current network.

        :param sMergeName: The name of the file being merged.
        :type sMergeName: str
        :return: Returns True if successful, False on merge failure.
        :rtype: bool
        """
        pass

    def ValidatedMergeFile(self, sMergeName: str) -> bool:
        """
        Performs a consistency check to determine if the IPSA I2F file sMergeName can be merged into
        the current network. Use the GetFilingErrors() function to get details of the merge errors.

        :param sMergeName: The name of the file being merged.
        :type sMergeName: str
        :return: True if successful, False on merge failure.
        :rtype: bool
        """
        pass

    def GetFilingMessages(self) -> List[str]:
        """
        Returns a list of strings detailing the successful merge operations that occurred as a result of
        the ValidatedMergeFile function.

        :return: List of successful merge operations.
        :rtype: list(str)
        """
        pass

    def GetFilingErrors(self) -> List[str]:
        """
        Returns a list of strings detailing the failed merge operations that occurred as a result of
        the ValidatedMergeFile function.

        :return: List of failed merge operations.
        :rtype: list(str)
        """
        pass

# Fixing gaps in documentation EL 11/2023
    def WriteFile(self, strName: str) -> bool:
        """
        Saves the IscNetwork instance as a new IPSA i2f network file with the file name strName.
        The file is saved in the current working directory unless the path is defined in the file name.
        The file name should include the .i2f extension

        :param strName: The name of the output file containing the i2f network.
        :type strName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def WriteArea(self, nAreaUID: int, strName: str) -> bool:
        """
        Saves the area group specified by the UID, nAreaUID, as a new IPSA i2f network file with the file name strName.
        The integer nAreaUID can be obtained using the IscGroup functions.
        The file is saved in the current working directory unless the path is defined in the file name.
        The file name should include the .i2f extension

        :param nAreaUID: The area group UID.
        :type nAreaUID: int
        :param strName: The name of the output file containing the i2f network.
        :type strName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetAllDiagrams(self, network):
        """
        Returns a tuple of IscDiagram instances for the identified network.

        :param network: The IPSA network.
        :type network: IscNetwork
        :return: The network diagram.
        :rtype: tuple(IscDiagram)
        """
        pass

    def GetAllDiagramsNames(self, network) -> List[str]:
        """
        Returns a list of all the diagram names for the identified network.

        :param network: The IPSA network.
        :type network: IscNetwork
        :return: List of diagram names.
        :rtype: list(str)
        """
        pass

    def GetAllDiagramsUIDs(self, network):
        """
        Returns a dictionary of diagrams for the identified network. The keys are the Diagram IDs.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :return: Dictionary of diagrams for the network.
        :rtype: dict(int, IscDiagram)
        """
        pass

    @overload
    def AddDiagram(self, network,
                   strSceneTitle: str,
                   bIsDiagramSingleLine: bool,
                   dGeoSceneScale: float,
                   nSceneMeasurementUnit: int):
        """
        Creates a new diagram for the identified network based on the supplied parameters.
        Returns an IscDiagram object corresponding to the new diagram.
        Note that this function causes IPSA to rebuild the IscDiagram data maps.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :param strSceneTitle: The name of the new diagram.
        :type strSceneTitle: str
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :return: The IscDiagram object for the newly created diagram.
        :rtype: IscDiagram
        """
        pass

    @overload
    def AddDiagram(self, network,
                   strSceneTitle: str,
                   bIsDiagramSingleLine: bool,
                   dGeoSceneScale: float,
                   nSceneMeasurementUnit: int,
                   nCopyWhat: int,
                   pDiagramToCopy: IscDiagram):
        """
        Creates a new diagram for the identified network based on the supplied parameters.
        Returns an IscDiagram object corresponding to the new diagram.
        Note that this function causes IPSA to rebuild the IscDiagram data maps.
        pDiagramToCopy provides a reference diagram, which this new diagram is based upon.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :param strSceneTitle: The name of the new diagram.
        :type strSceneTitle: str
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :param nCopyWhat: Determines what is copied from the provided diagram pDiagramToCopy

            * 0 if copy nothing
            * 1 if copy the busbars as they are
            * 2 if copy the busbars as junctions
            * 3 if copy everything
        :type nCopyWhat: int
        :param pDiagramToCopy: The IscDiagram object that any components may be copied from.
        :type pDiagramToCopy: IscDiagram
        :return: The IscDiagram object for the newly created diagram.
        :rtype: IscDiagram
        """
        pass

    def AddDiagram(self, network,
                   strSceneTitle: str,
                   bIsDiagramSingleLine: bool,
                   dGeoSceneScale: float,
                   nSceneMeasurementUnit: int,
                   nCopyWhat: int,
                   pDiagramToCopy: IscDiagram):
        """
        Creates a new diagram for the identified network based on the supplied parameters.
        Returns an IscDiagram object corresponding to the new diagram.
        Note that this function causes IPSA to rebuild the IscDiagram data maps.

        If nCopy what and pDiagramToCopy are provided, they provide a reference diagram and determine what is copied
        from that diagram into the new diagram.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :param strSceneTitle: The name of the new diagram.
        :type strSceneTitle: str
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :param nCopyWhat: Determines what is copied from the provided diagram pDiagramToCopy

            * 0 if copy nothing
            * 1 if copy the busbars as they are
            * 2 if copy the busbars as junctions
            * 3 if copy everything
        :type nCopyWhat: int
        :param pDiagramToCopy: The IscDiagram object that any components may be copied from.
        :type pDiagramToCopy: IscDiagram
        :return: The IscDiagram object for the newly created diagram.
        :rtype: IscDiagram
        """
        pass

    @overload
    def DeleteDiagram(self, network, pDiagram: IscDiagram)-> None:
        """
        Deletes the diagram associated with the IscDiagram object from the identified network.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :param pDiagram: The diagram to be deleted.
        :type pDiagram: IscDiagram
        """
        pass

    @overload
    def DeleteDiagram(self, network, nUID: int) -> None:
        """
        Deletes the diagram identified by ID nUID from the identified network.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :param nUID: The diagram ID to be deleted.
        :type nUID: int
        """
        pass

    @overload
    def DeleteDiagram(self, network, strName: str) -> None:
        """
        Deletes the diagram identified by name strName from the identified network.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :param strName: The name of the diagram to be deleted.
        :type strName: str
        """
        pass

    def DeleteDiagram(self, network, strName: str) -> None:
        """
        Deletes the diagram identified by name strName, ID nUID or IscDiagram pDiagram from the identified network.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :param strName: The name of the diagram to be deleted.
        :type strName: str
        :param nUID: The diagram ID to be deleted.
        :type nUID: int
        :param pDiagram: The diagram to be deleted.
        :type pDiagram: IscDiagram
        """
        pass

    def PrintPDF(self, diagram, strFileName) -> None:
        """
        Print the IscDiagram instance to a PDF format file with name strFileName.

        :param diagram: The diagram of the IPSA network.
        :type diagram: IscDiagram
        :param strFileName: The name of the pdf file.
        :type strFileName: str
        """
        pass

    def MessageBox(self, strDialogTitle: str, strMessage: str) -> bool:
        """
        Display a message box with title specified by strDialogTitle and a message specified by strMessage.
        An OK button is provided for the user to dismiss the dialog.

        :param strDialogTitle: The title of the message box.
        :type strDialogTitle: str
        :param strMessage: The message displayed on the message box.
        :type strMessage: str
        :return: Boolean denoting whether a message box is created.
        :rtype: bool
        """
        pass

    def AskQuestion(self, strDialogTitle: str, strQuestion: str) -> bool:
        """
        Display a message box with a title and a question as shown below.

        :param strDialogTitle: The title of the message box.
        :type strDialogTitle: str
        :param strQuestion: The question displayed on the message box.
        :type strQuestion: str
        :return: True when the user clicks Yes, otherwise False.
        :rtype: bool
        """
        pass

    def AllowStackBarUpdates(self, bAllow: bool) -> None:
        """
        Setting bAllow to True prevents the IPSA stack bar from updating during script execution.
        This can provide speed improvements since redrawing the stack bar is prevented.

        :param bAllow: Deciding whether the IPSA stack bar can be updated during script execution.
        :type bAllow: bool
        """
        pass

    def GetDate(self) -> str:
        """
        Returns the date and time that IPSA was launched, e.g. 06 Nov 2012 22:53:17.

        :return: The date in a string format.
        :rtype: str
        """
        pass

    def GetUser(self) -> str:
        """
        Returns the name of the current logged on user.

        :return: The name of the current logged on user.
        :rtype: str
        """
        pass

    def GetHost(self) -> str:
        """
        Returns the host name of the PC.

        :return: The host name of the PC.
        :rtype: str
        """
        pass

    def GetOrganisation(self) -> str:
        """
        Returns the company organisation data as set in network properties.

        :return: The company organisation data.
        :rtype: str
        """
        pass

    def GetNetworkTitle(self) -> str:
        """
        Returns the network title as set in network properties.

        :return: The network title.
        :rtype: str
        """
        pass

    def GetNetworkFileName(self) -> str:
        """
        Returns the filename of the current network.

        :return: The filename of the current network.
        :rtype: str
        """
        pass

    def GetFileName(self, strDialogTitle: str, strFileTypes: str) -> str:
        """
        Display the operating system File Open dialog to prompt the user to select a file.

        :param strDialogTitle: The title of the dialog itself.
        :type strDialogTitle: str
        :param strFileTypes: The file type filter.
        :type strFileTypes: str
        :return: String containing the file name and path selected by the user.
        :rtype: str
        """
        pass

    def GetDirectoryName(self, strDialogTitle: str) -> str:
        """
        Display the operating system Folder Selection dialog to prompt the user to select a folder.

        :param strDialogTitle: The title of the dialog itself.
        :type strDialogTitle: str
        :return: String containing the path selected by the user.
        :rtype: str
        """
        pass

    def GetVersion(self) -> str:
        """
        Returns the version number of IPSA software.

        :return: The version number.
        :rtype: str
        """
        pass

    def HasLoadFlow(self) -> bool:
        """
        Returns True if a load flow license is present.

        :return: Boolean denoting whether a load flow license is presented.
        :rtype: bool
        """
        pass

    def HasFaultLevel(self) -> bool:
        """
        Returns True if a fault level license is present.

        :return: Boolean denoting whether a fault level license is presented.
        :rtype: bool
        """
        pass

    def HasTransient(self) -> bool:
        """
        Returns True if a transient stability license is present.

        :return: Boolean denoting whether a transient stability license is presented.
        :rtype: bool
        """
        pass

    def HasProtection(self) -> bool:
        """
        Returns True if a protection analysis license is present.

        :return: Boolean denoting whether a protection analysis license is presented.
        :rtype: bool
        """
        pass

    def HasHarmonics(self) -> bool:
        """
        Returns True if a harmonics analysis license is present.

        :return: Boolean denoting whether a harmonics analysis license is presented.
        :rtype: bool
        """
        pass

    def HasUDM(self) -> bool:
        """
        Returns True if a UDM (User Defined Modelling) license is present.

        :return: Boolean denoting whether a UDM license is presented.
        :rtype: bool
        """
        pass

    def HasDC(self) -> bool:
        """
        Returns True if a DC component license is present.

        :return: Boolean denoting whether a DC component license is presented.
        :rtype: bool
        """
        pass

    def HasStaticCon(self) -> bool:
        """
        Returns True if a static converter license is present.

        :return: Boolean denoting whether a static converter license is presented.
        :rtype: bool
        """
        pass

    def HasTandemGen(self) -> bool:
        """
        Returns True if a tandem generator license is present.

        :return: Boolean denoting whether a tandem generator license is presented.
        :rtype: bool
        """
        pass

    def HasNonLinDevs(self) -> bool:
        """
        Returns True if a non-linear devices license is present.

        :return: Boolean denoting whether a non-linear devices license is presented.
        :rtype: bool
        """
        pass

    def HasAutomation(self) -> bool:
        """
        Returns True if an automation analysis license is present.

        :return: Boolean denoting whether an automation analysis license is presented.
        :rtype: bool
        """
        pass

    def IsLimitedSize(self) -> bool:
        """
        Returns True if the current license imposes a limit on the maximum number of busbars.

        :return: Boolean denoting whether the current license imposes a limit on the maximum number of busbars.
        :rtype: bool
        """
        pass

    def GetMaxBusbars(self) -> int:
        """
        Returns the maximum number of busbars if it is a limited busbar version, returns 0 if unlimited.

        :return: The maximum number of busbars if in limited busbar version, else 0.
        :rtype: int
        """
        pass

    def DisplayResultsTable(self, nTableType: int) -> None:
        """
        Displays the IPSA results table which will contain the results of the last analysis.

        :param nTableType: Specify the type of table displayed:

            - ipsa.IscInterface.BusbarLF = busbar load flow results
            - ipsa.IscInterface.GeneratorLF = generator load flow results
            - ipsa.IscInterface.GridInfeedLF = grid infeed load flow results
            - ipsa.IscInterface.LoadLF = load object load flow results
            - ipsa.IscInterface.IMachineLF = motor load flow results
            - ipsa.IscInterface.StaticVCLF = SVC load flow results
            - ipsa.IscInterface.MechSwCapLF = switched capacitor load flow results
            - ipsa.IscInterface.UMachineLF = universal machine load flow results
            - ipsa.IscInterface.FilterLF = harmonic filter load flow results
            - ipsa.IscInterface.LineLF = branch load flow results
            - ipsa.IscInterface.TransformerLF = transformer load flow results
            - ipsa.IscInterface.ThreeWindingTransformerLF = 3 winding transformer load flow results
            - ipsa.IscInterface.BatteryLF = DC battery load flow results
            - ipsa.IscInterface.DCMachineLF = DC machine load flow results
            - ipsa.IscInterface.ConverterLF = AC-DC converter load flow results
            - ipsa.IscInterface.ChopperLF = DC-DC converter load flow results
            - ipsa.IscInterface.MGSetLF = motor-generator set load flow results
            - ipsa.IscInterface.BusbarFL = busbar fault level results
            - ipsa.IscInterface.GeneratorFL = generator fault level results
            - ipsa.IscInterface.GridInfeedFL = grid infeed fault level results
            - ipsa.IscInterface.LoadFL = load object fault level results
            - ipsa.IscInterface.IMachineFL = motor fault level results
            - ipsa.IscInterface.LineFL = branch fault level results
            - ipsa.IscInterface.TransformerFL = transformer fault level results
            - ipsa.IscInterface.ThreeWindingTransformerFL = 3 winding transformer fault level results
            - ipsa.IscInterface.UniversalMachineFL = universal machine fault level results
            - ipsa.IscInterface.BusbarHM = busbar harmonic analysis results
            - ipsa.IscInterface.GeneratorHM = generator harmonic analysis results
            - ipsa.IscInterface.LoadHM = load object harmonic analysis results
            - ipsa.IscInterface.IMachineHM = motor harmonic analysis results
            - ipsa.IscInterface.FilterHM = filter harmonic analysis results
            - ipsa.IscInterface.LineHM = branch harmonic analysis results
            - ipsa.IscInterface.TransformerHM = transformer harmonic analysis results
            - ipsa.IscInterface.ThreeWindingTransformerHM = 3 winding transformer harmonic analysis results
        :type: int
        """
        pass

    def GetResultsTableText(self, nTableType: int) -> str:
        """
        Returns the data contained in the results' table as a comma delimited string
        which can be pasted directly into a spreadsheet.

        :param nTableType: The type defined for the DisplayResultsTable function.
        :type nTableType: int
        :return: Data contained in the results' table.
        :rtype: str
        """
        pass

    def CloseResultsTable(self, nTableType: int) -> None:
        """
        Closes the results' table nTableType which is as defined for the DisplayResultsTable function.

        :param nTableType: The type defined for the DisplayResultsTable function.
        :type nTableType: int
        """
        pass

    def GetLogFileName(self) -> str:
        """
        Get the name of log file.

        :return: The name of the log file.
        :rtype: str
        """
        pass

    def DbgSetLogFileName(self, strName: str) -> None:
        """
        Set the name of the load flow log file to strName.
        If no file path is specified then the file is created in the IPSA bin directory.

        :param strName: The name of the load flow log file.
        :type strName: str
        """
        pass

    def IsLogging(self) -> bool:
        """
        Checks whether a logging is in progress.

        :return: Returns True if logging is in progress.
        :rtype: bool
        """
        pass

    def DbgStartLogging(self) -> None:
        """Start logging of all analysis engine calls."""
        pass

    def DbgStopLogging(self) -> None:
        """Stop logging of all analysis engine calls."""
        pass

    def OpenDBFromFile(self, strFilename: str) -> bool:
        """
        Opens the database from file.

        :param strFilename: The path name of the file to be opened.
        :type strFilename: str
        :return: Returns True if the database is opened successfully.
        :rtype: bool
        """
        pass

    def CloseDBFromFile(self, strFilename: str) -> bool:
        """
        Closes the specified database file.

        :param strFilename: The path name of the file to be closed.
        :type strFilename: str
        :return: Returns True if the database is closed successfully.
        :rtype: bool
        """
        pass

    def CloseAllDB(self) -> bool:
        """
        Close all the databases.

        :return: Returns True if databases are closed.
        :rtype: bool
        """
        pass

    def GetDBNames(self) -> List[str]:
        """
        Returns all filenames of the databases that have been loaded.

        :return: Returns list of the databases' filenames.
        :rtype: list(str)
        """
        pass

    def GetDBBranchNames(self, strFilename: str) -> List[str]:
        """
        Returns all branch names in a database.

        :param strFilename: The path name of the database.
        :type strFilename: str
        :return: Returns list of the branch names.
        :rtype: list(str)
        """
        pass

    def GetDBTransformerNames(self, strFilename: str) -> List[str]:
        """
        Returns all transformer names in a database.

        :param strFilename: The path name of the database.
        :type strFilename: str
        :return: Returns list of the transformer names.
        :rtype: list(str)
        """
        pass

    def GetDBGeneratorNames(self, strFilename: str) -> List[str]:
        """
        Returns all generator names in a database.

        :param strFilename: The path name of the database.
        :type strFilename: str
        :return: Returns list of the generator names.
        :rtype: list(str)
        """
        pass

    def GetDBIndMachineNames(self, strFilename: str) -> List[str]:
        """
        Returns all induction machine names in a database.

        :param strFilename: The path name of the database.
        :type strFilename: str
        :return: Returns list of the induction machine names.
        :rtype: list(str)
        """
        pass

    def GetDBCircuitBreakerNames(self, strFilename: str) -> List[str]:
        """
        Returns all circuit breaker names in a database.

        :param strFilename: The path name of the database.
        :type strFilename: str
        :return: Returns list of the circuit breaker names.
        :rtype: list(str)
        """
        pass

    def GetReportType(self) -> int:
        """
        The nReport type of the most recently generated report, matching those in e.g.,
        :meth:`IscNetwork.GetStudies(nReportType)`.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        *Note this number only updates if a report has been generated from the IPSA UI.*

        :return: The nReport type of the most recently generated report.
        :rtype: int
        """
        pass

    def GetUndoActive(self) -> bool:
        """
        Returns a boolean determining whether Undo is currently active.

        :return: Returns True if Undo is active.
        :rtype: bool
        """
        pass

    def SetUndoActive(self, bSetActive: bool):
        """
        Sets the boolean determining whether Undo is currently active.

        :param bSetActive: True if undo should be active.
        :type bSetActive: bool
        """
        pass

    def HasPSSEIO(self) -> bool:
        """
        *Deprecated.*
        Returns True if a PSSE analysis license is present.

        :return: Boolean denoting whether a PSSE analysis license is presented.
        :rtype: bool
        """
        pass

    def GetIpsa1Mode(self) -> bool:
        """
        *Deprecated.*
        Returns the IPSA 1 mode - note, this is currently not used anywhere so does nothing.

        :return: The boolean of the Ipsa1 mode.
        :rtype: bool
        """
        pass

    def SetIpsa1Mode(self, bIpsa1) -> bool:
        """
        *Deprecated.*
        Sets the IPSA 1 mode - note, this is currently not used anywhere so does nothing.

        :param bIpsa1: The boolean of the Ipsa1 mode.
        :type bIpsa1: bool
        """
        pass

    def WriteJsonFile(self, strName: str) -> bool:
        """
        *Deprecated.*
        Saves the graphical information, name and UID for every component in the network as a json file.
        The file is saved in the current working directory unless the path is defined in the file name.
        The file name should include the .json extension

        :param strName: The name of the output file.
        :type strName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def WriteCSVItemFile(self, strName: str) -> bool:
        """
        *Deprecated.*
        Saves the UID, component type and name for every component in the network as a csv file.
        The file is saved in the current working directory unless the path is defined in the file name.
        The file name should include the .csv extension

        :param strName: The name of the output file.
        :type strName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

class IscIntertrip:
    """
    Provides access to an IPSA intertrip object.
    """
    def GetUID(self) -> str:
        """
        Gets the unique ID of the intertrip

        :return: The UID of the intertrip.
        :rtype: str
        """
        pass

    def GetName(self) -> str:
        """
        Gets the python name as a string.

        :return: The name of the intertrip.
        :rtype: str
        """
        pass

    def SetName(self, strName: str) -> bool:
        """
        Sets the name of the intertrip to the specified name.

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

    def GetListIValue(self, nFieldIndex: int) -> list[int]:
        """
        Returns a list of integer values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[int]
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

    def SetListIValue(self, nFieldIndex: int, lIValue: list[int]) -> bool:
        """
        Sets the value for the enumerated field from a list of integers.

        Note: Setting the Masters/Slaves will set the list to be the provided list, removing any circuit breakers that
        are in a different intertrip, or in the current intertrip in the opposite role.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lIValue: The given list of values.
        :type lIValue:  list[int]
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetMembers(self) -> List[int]:
        """
        Returns a list containing the UIDs of the breakers in the intertrip.

        :return: The UIDs of the breakers in the intertrip.
        :rtype: list(int)
        """
        pass

    def GetMasters(self) -> List[int]:
        """
        Returns a list containing the UIDs of the master breakers in the intertrip.

        :return: The UIDs of the masters in the intertrip.
        :rtype: list(int)
        """
        pass

    def GetSlaves(self) -> List[int]:
        """
        Returns a list containing the UIDs of the slave breakers in the intertrip.

        :return: The UIDs of the slaves in the intertrip.
        :rtype: list(int)
        """
        pass

    def AddMaster(self, nUID: int) -> bool:
        """
        Appends the circuit breaker identified by the nUID to the intertrip as a master.
        If the circuit breaker already exists in another IscIntertrip object, or as a slave, the intertrip is
        unchanged.

        :param nUID: The UID of the specified circuit breaker.
        :type nUID: int
        :return: True if the circuit breaker is added to the intertrip as a master.
        :rtype: bool
        """
        pass

    def AddSlave(self, nUID: int) -> bool:
        """
        Appends the circuit breaker identified by the nUID to the intertrip as a slave.
        If the circuit breaker already exists in another IscIntertrip object, or as a master, the intertrip is
        unchanged.

        :param nUID: The UID of the specified circuit breaker.
        :type nUID: int
        :return: True if the circuit breaker is added to the intertrip as a slave.
        :rtype: bool
        """
        pass

    def SwitchMasterSlave(self, nUID: int) -> bool:
        """
        If nUID identifies a master within the intertrip, converts it to a slave.
        Otherwise, if it identifies a slave, converts it to a master.

        :param nUID: The UID of the specified circuit breaker.
        :type nUID: int
        :return: True if the role of the circuit breaker is successfully switched.
        :rtype: bool
        """
        pass

    def RemoveMember(self, nUID: int):
        """
        Removes the circuit breaker identified by  nUID from the intertrip.

        :param nUID: The UID of the specified circuit breaker.
        :type nUID: int
        """
        pass

    def IsMember(self, nUID: int) -> bool:
        """
        Checks if the breaker identified by the UID is in the intertrip.

        :param nUID: The UID of the specified circuit breaker.
        :type nUID: int
        :return: True if circuit breaker is a member of the intertrip.
        :rtype: bool
        """
        pass

    def IsMaster(self, nUID: int) -> bool:
        """
        Checks if the breaker identified by the UID is a master in the intertrip.

        :param nUID: The UID of the specified circuit breaker.
        :type nUID: int
        :return: True if circuit breaker is a master in the intertrip.
        :rtype: bool
        """
        pass

    def IsSlave(self, nUID: int) -> bool:
        """
        Checks if the breaker identified by the UID is a slave in the intertrip.

        :param nUID: The UID of the specified circuit breaker.
        :type nUID: int
        :return: True if circuit breaker is a slave in the intertrip.
        :rtype: bool
        """
        pass

    def ClearMembers(self):
        """
        Removes all the member circuit breakers from the intertrip.
        """
        pass

    def ClearMasters(self):
        """
        Removes all the master circuit breakers from the intertrip.
        """
        pass

    def ClearSlaves(self):
        """
        Removes all the slave circuit breakers from the intertrip.
        """
        pass

class IscLoad:
    """
    Provides access to an IPSA load.
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

    def GetPowerMagnitudeMVA(self) -> float:
        """
        Returns the load in MVA.

        :return: The load in MVA.
        :rtype: float
        """
        pass

    def GetPowerMagnitudekVA(self) -> float:
        """
        Returns the load in kVA.

        :return: The load in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerMW(self) -> float:
        """
        Returns the load in MW.

        :return: The load in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerMVAr(self) -> float:
        """
        Returns the load in MVAr.

        :return: The load in MVAr.
        :rtype: float
        """
        pass

    def GetRealPowerkW(self) -> float:
        """
        Returns the load in kW.

        :return: The load in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerkVAr(self) -> float:
        """
        Returns the load in kVAr.

        :return: The load in kVAr.
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

    def GetDCLFPowerMagnitudeMVA(self) -> float:
        """
        Returns the load in MVA.

        :return: The load in MVA.
        :rtype: float
        """
        pass

    def GetDCLFPowerMagnitudekVA(self) -> float:
        """
        Returns the load in kVA.

        :return: The load in kVA.
        :rtype: float
        """
        pass

    def GetDCLFRealPowerMW(self) -> float:
        """
        Returns the load in MW.

        :return: The load in MW.
        :rtype: float
        """
        pass

    def GetDCLFRealPowerkW(self) -> float:
        """
        Returns the load in kW.

        :return: The load in kW.
        :rtype: float
        """
        pass

class IscMechSwCapacitor:
    """
    Provides access to an IPSA mechanical switched capacitor.
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

    def GetFinalPosition(self) -> int:
        """
        Returns the position of the MSC after a load flow.
        Positive values represent capacitor steps and negative values are inductive steps.
        See also **ContinuousOutputMVAr** for the output in continuous mode.

        :return: The position of the MSC after a load flow.
        :rtype: int
        """
        pass

class IscMGSet:
    """
    Provides access to an IPSA motor-generator set.
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

class IscNetComponent:
    """
    The base class for all IPSA components.
    """
    def GetUID(self) -> int:
        """
        Returns the unique ID of the component.

        :return: The unique ID of the component.
        :rtype: int
        """
        pass

    def GetName(self) -> str:
        """
        Gets the name as a string - this is the name Python knows the object by
        (only identical to the IPSA name for busbars).

        :return: The name of the component.
        :rtype: str
        """
        pass

    def SetName(self, strName: str) -> None:
        """
        Sets the name to the component to the specified name.

        :param strName: The component name.
        :type strName: str
        """
        pass

    def GetRealName(self, strName: str) -> str:
        """
        Gets the user defined component name as a string for the specified component name.

        :param strName: The component Python name.
        :type strName: str
        :return: Returns the IPSA component name.
        :rtype: str
        """
        pass

    def SetRealName(self, strName: str) -> None:
        """
        Sets the user defined IPSA component name.

        :param strName: The IPSA component name.
        :type strName: str
        """
        pass

    def GetFieldType(self, nFieldIndex: int) -> str:
        """
        Returns the field type as a string for the given enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: Returns ‘String’, ‘Integer’, ‘Float’ or ‘Boolean’.
        :rtype: str
        """
        pass

    def GetFieldName(self, nFieldIndex: int) -> str:
        """
        Returns the field name as a string for the given enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The field name.
        :rtype: str
        """
        pass

    def GetFromBusbarUID(self) -> int:
        """
        Returns the FROM busbar UID of the component. For busbars this will return 0.

        :return: The FROM busbar UID.
        :rtype: int
        """
        pass

    def GetToBusbarUID(self, nBranchUID: int) -> int:
        """
        Returns the TO busbar UID of the component. For busbars and radials this will return 0, for shunts,
        this value will match the from busbar UID.

        :return: The TO busbar UID.
        :rtype: int
        """
        pass

    def GetType(self) -> int:
        """
        Returns an integer that matches one of the class field indices (e.g., IscNetComponent.Busbar).

        :return: The integer that matches one of the class' field indices.
        :rtype: int
        """
        pass

    def AddDataExtension(self, strName: str, default: Union[int, float, str, bool]) -> int:
        """
        Adds an integer/float/string/double extension data field and returns the new field index.
        Sets the default value.

        This only has to be called once per component type - not for every instance of the component!

        **Note: The variable of the function is not called default.**

        You can use either nDefault, dDefault, strDefault or bDefault to specify the default value depending on the
        type of data extension being added.

        :param strName: The name of the field.
        :type strName: str
        :param nDefault: The integer default value.
        :type nDefault: int
        :param dDefault: The float default value.
        :type dDefault: float
        :param strDefault: The string default value.
        :type strDefault: str
        :param bDefault: The bool default value.
        :type bDefault: bool
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListIntDataExtension(self, strName: str) -> int:
        """
        Adds a list of integers data field and returns the new field index.
        Sets the default value to an empty list.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListDblDataExtension(self, strName: str) -> int:
        """
        Adds a list of doubles data field and returns the new field index.
        Sets the default value to an empty list.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListStrDataExtension(self, strName: str) -> int:
        """
        Adds a list of strings data field and returns the new field index.
        Sets the default value to an empty list.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    @overload
    def DeleteDataExtensionField(self, nFieldIndex: int) -> bool:
        """
        Deletes the extension field identified by the index nFieldIndex. This will delete the data in this extension
        field from this component and all other components of the same type.
        It is advised to call NonDefaultExtensionInstanceCount prior to deleting the data extension field to ensure the
        expected amount of data shall be deleted.

        This only has to be called once per component type - not for every instance of the component!

        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: True if the field is deleted successfully.
        :rtype: bool
        """
        pass

    @overload
    def DeleteDataExtensionField(self, strName: str) -> bool:
        """
        Deletes the extension field identified by the name strName. This will delete the data in this extension field
        from this component and all other components of the same type.
        It is advised to call NonDefaultExtensionInstanceCount prior to deleting the data extension field to ensure the
        expected amount of data shall be deleted.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :return: True if the field is deleted successfully.
        :rtype: bool
        """
        pass

    def DeleteDataExtensionField(self, strName: str) -> bool:
        """
        Deletes the extension field identified by the name strName or index nFieldIndex. This will delete the data in
        this extension field from this component and all other components of the same type.
        It is advised to call NonDefaultExtensionInstanceCount prior to deleting the data extension field to ensure the
        expected amount of data shall be deleted.

        This only has to be called once per component type - not for every instance of the component!

        :param strName: The name of the field.
        :type strName: str
        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: True if the field is deleted successfully.
        :rtype: bool
        """
        pass

    @overload
    def NonDefaultExtensionField(self, nFieldIndex: int) -> int:
        """
        Returns the number of components of the same type where the extension field identified by nFieldIndex is set to
        a non-default value. That is, the count of the components where data will be destroyed by calling
        DeleteDataExtensionField.

        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: The number of components with a non-default value in the extension field.
        :rtype: int
        """
        pass

    @overload
    def NonDefaultExtensionField(self, strName: str) -> int:
        """
        Returns the number of components of the same type where the extension field identified by strName is set to
        a non-default value. That is, the count of the components where data will be destroyed by calling
        DeleteDataExtensionField.

        :param strName: The name of the field.
        :type strName: str
        :return: The number of components with a non-default value in the extension field.
        :rtype: int
        """
        pass

    def NonDefaultExtensionField(self, strName: str) -> int:
        """
        Returns the number of components of the same type where the extension field identified by strName or nFieldIndex is
        set to a non-default value. That is, the count of the components where data will be destroyed by calling
        DeleteDataExtensionField.

        :param strName: The name of the field.
        :type strName: str
        :param nFieldIndex: The index of the field.
        :type nFieldIndex: int
        :return: The number of components with a non-default value in the extension field.
        :rtype: int
        """
        pass

    def GetListIntExtensionValue(self, nFieldIndex: int, nIndex: int) -> int:
        """
        Get a single integer value from the list for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: int
        """
        pass

    def GetListDblExtensionValue(self, nFieldIndex: int, nIndex: int) -> float:
        """
        Get a single float value from the list for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: float
        """
        pass

    def GetListStrExtensionValue(self, nFieldIndex: int, nIndex: int) -> str:
        """
        Get a single string value from the list for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: str
        """
        pass

    def GetListIntSize(self, nFieldIndex: int) -> int:
        """
        Get size of the list of integers for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def GetListDblSize(self, nFieldIndex: int) -> int:
        """
        Get size of the list of doubles for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def GetListStrSize(self, nFieldIndex: int) -> int:
        """
        Get size of the list of strings for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def SetListIntExtensionValue(self, nFieldIndex: int, nIndex: int, nValue: int) -> bool:
        """
        Sets the value of an element in a list of integers for the enumerated field at given position to given value.

        Note the index within the list, nIndex, must already exist - that is, the size of the list (i.e.,
        GetListIntSize) must be larger than nIndex.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param nValue: The selected value.
        :type nValue: int
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetListDblExtensionValue(self, nFieldIndex: int, nIndex: int, dValue: float) -> bool:
        """
        Sets the value of an element in a list of doubles for the enumerated field at given position to given value.

        Note the index within the list, nIndex, must already exist - that is, the size of the list (i.e.,
        GetListDblSize) must be larger than nIndex.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param dValue: The selected value.
        :type dValue: float
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetListStrExtensionValue(self, nFieldIndex: int, nIndex: int, strValue: str) -> bool:
        """
        Sets the value of an element in a list of strings for the enumerated field at given position to given value.

        Note the index within the list, nIndex, must already exist - that is, the size of the list (i.e.,
        GetListStrSize) must be larger than nIndex.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param strValue: The selected value.
        :type strValue: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListIntExtensionValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Adds an item to the end of a list of integers for the enumerated field with the given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The selected value.
        :type nValue: int
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListDblExtensionValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Adds an item to the end of a list of doubles for the enumerated field with the given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The selected value.
        :type dValue: float
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListStrExtensionValue(self, nFieldIndex: int, strValue: str) -> bool:
        """
        Adds an item to the end of a list of strings for the enumerated field with the given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The selected value.
        :type strValue: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def GetExtensionFieldIndex(self, strName: str) -> int:
        """
        Returns the field index for the extended data field.

        :param strName: The name of the extended data field.
        :type strName: str
        :return: The field index.
        :rtype: int
        """
        pass

    def GetExtensionNames(self) -> Dict[int,str]:
        """
        Returns a dictionary of extension field indexes and field names.
        The dictionary keys are integers representing all the extended data fields.
        The dictionary values are the field names of the individual extended data fields.
        Each extended data field is therefore represented by {nIndex:strName}, where integer nIndex is the field index
        and string strName is the field name.

        :return: Dictionary of extension field indexes and field names.
        :rtype: dict(int, str)
        """
        pass

    def GetNumberOfDataComponents(self) -> int:
        """
        *Deprecated.*
        Returns the number of data components within the IscNetComponent object.
        For most IscNetComponents this will return 1. To obtain the number of sections in a branch the function
        :meth:`IscBranch.GetSections()` should instead be used

        :return: Number of data components in the IscNetComponent object.
        :rtype: int
        """
        pass

class IscNetwork:
    """
    Class providing the main access to an IPSA network.
    """
    def SetBusbarSlack(self, strBusbar: str) -> None:
        """
        Sets the busbar as the slack busbar for a particular part of the network.

        :param strBusbar: The Python busbar name which is returned by IscNetComponent.GetName().
        :type strBusbar: str
        """
        pass

    def RefreshSystem(self) -> None:
        """
        Forces IPSA to rebuild its internal component data maps.
        This function can be used if the network has been modified outside of scripting while a script is running.
        """
        pass

    def WriteFile(self, strName: str) -> bool:
        """
        Saves the current network file at the path and the file name.

        :param strName: The file name.
        :type strName: str
        :return: Denoting whether the file is saved.
        :rtype: bool
        """
        pass

    def WriteArea(self, nAreaUID: int, strName: str) -> bool:
        """
        Saves the area group UID as a new IPSA i2f network file.
        The file is saved in the current working directory.
        The file name should include the .i2f extension.

        :param nAreaUID: The area group UID. nAreaUID can be obtained using the IscGroup functions.
        :type strName: int
        :param strName: The file name.
        :type strName: str
        :return: Denoting whether the file is saved.
        :rtype: bool
        """
        pass

    def MergeFile(self, strMergeName: str) -> bool:
        """
        Merges the file into the current network file.

        :param strMergeName: The merged file name.
        :type strMergeName: str
        :return: Denoting whether the file is successfully saved.
        :rtype: bool
        """
        pass

    def ValidatedMergeFile(self, strMergeName: str) -> bool:
        """
        Performs a consistency check to determine if the IPSA I2F file can be merged into the current network.
        Use the GetFilingErrors() function to get details of the merge errors.

        :param strMergeName: The merged file name.
        :type strMergeName: str
        :return: Denoting whether the file is successfully saved.
        :rtype: bool
        """
        pass

    def CommitVersion(self, strVersionName: str) -> int:
        """
        Creates a new network version which includes all non-versioned network changes.

        :param strVersionName: The new network version name.
        :type strVersionName: str
        :return: An integer representing the version ID.
        :rtype: int
        """
        pass

    def GetVersionUuid(self, nVersion: int) -> str:
        """
        Returns a unique string (UUID) representing the version name for the given version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: The version name.
        :rtype: str
        """
        pass

    def SetToVersion(self, nVersion: int) -> bool:
        """
        Selects the version of the current network.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: Denoting whether the version is successfully set or whether it does not exist.
        :rtype: bool
        """
        pass

    def CreateChangeFile(self, nVersion: int, strMergeName: str) -> bool:
        """
        Creates an IPSA merge file based on the network differences between the given version and the current version.

        :param nVersion: The selected version.
        :type nVersion: int
        :param strMergeName: The merged file name.
        :type strMergeName: str
        :return: Denoting whether the file is successfully created.
        :rtype: bool
        """
        pass

    def GetCurrentVersion(self) -> int:
        """
        Returns the current working version. Any changes to the network are made to this version.

        :return: The current version.
        :rtype: int
        """
        pass

    def GetParentVersion(self, nVersion: int) -> int:
        """
        Returns the parent version for the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: The parent version.
        :rtype: int
        """
        pass

    def GetVersionDiffAdded(self, nVersion: int) -> List[int]:
        """
        Returns a list of component UIDs which have been added to the network in the current selected version and
        that were not in the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: List of component UIDs.
        :rtype: int
        """
        pass

    def GetVersionDiffChanged(self, nVersion: int) -> List[int]:
        """
        Returns a list of component UIDs which have been edited in the current selected version compared to
        the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: List of component UIDs.
        :rtype: int
        """
        pass

    def GetVersionDiffDeleted(self, nVersion: int) -> List[int]:
        """
        Returns a list of component UIDs which have been deleted from the network in the current selected version and
        that were in the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: List of component UIDs.
        :rtype: int
        """
        pass

    def ResetResults(self) -> None:
        """Reset all analysis results."""
        pass

    def GetSystemBaseMVA(self) -> float:
        """
        Returns the current system MVA defined for the IPSA network
        Default: 100 MVA

        :return: Network system MVA value
        :rtype: float
        """
        pass

    def GetNumberOfIslands(self) -> int:
        """
        Returns the number of islands.

        :return: The number of islands.
        :rtype: int
        """
        pass

    def GetIslandsUIDs(self) -> Dict[str, List[int]]:
        """
        Returns a dictionary of integer busbar nUIDs belonging to the islands.
        The keys are the island slack busbar names or the first busbar names if no slack busbar is set for that island.

        :return: The busbars belonging to each island.
        :rtype: dict(str,list(int))
        """
        pass

    def GetNoSlackIslandsUIDs(self) -> Dict[str, List[int]]:
        """
        Returns a dictionary of integer busbar UIDs belonging to islands with no slack busbars.
        The keys are the first busbar names.

        :return: The busbars with no slack belonging to each island.
        :rtype: dict(str,list(int))
        """
        pass

    def GetNoGeneratorIslandsUIDs(self) -> Dict[str, List[int]]:
        """
        Returns a dictionary of integer busbar UIDs belonging to the islands with no generators or grid infeeds.
        The keys are the island slack busbar names or the first busbar names if no slack busbar is set for that island.

        :return: The busbars with no generators or grid infeeds belonging to each island.
        :rtype: dict(str,list(int))
        """
        pass

    def GetBusbars(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of busbars. The keys are the busbar names.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of busbars.
        :rtype: dict(str,IscBusbar)
        """
        pass

    def GetBusbarsOrderedByVoltage(self, bFetchFromSystem: bool = True) -> Tuple[int]:
        """
        Returns a tuple of busbar UIDs, sorted in ascending order of voltage and then by busbar name.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of busbars UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedBranches(self, nBusbarUID: int, bFetchFromSystem: bool = True) -> Tuple[int]:
        """
        Returns a tuple of branch UIDs attached to the busbar specified by busbar UID.
        Only branches are returned, not transformers.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of busbars UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedTransformers(self, nBusbarUID: int, bFetchFromSystem: bool = True) -> Tuple[int]:
        """
        Returns a tuple of transformer UIDs attached to the busbar specified by busbar UID.
        Only transformers are returned, not branches or 3W transformers.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttached3WTransformers(self, nBusbarUID: int, bFetchFromSystem: bool = True) -> Tuple[int]:
        """
        Returns a tuple of 3-winding transformer UIDs attached to the busbar specified by busbar UID.
        Only 3-winding transformers are returned, not 2-winding transformers or branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of 3-winding transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedUnbalancedBranches(self, nBusbarUID: int, bFetchFromSystem: bool = True) -> Tuple[int]:
        """
        Returns a tuple of unbalanced branch UIDs attached to the busbar specified by busbar UID.
        Only unbalanced branches are returned, not unbalanced transformers.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of unbalanced branch UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedUnbalancedTransformers(self, nBusbarUID: int, bFetchFromSystem: bool = True) -> Tuple[int]:
        """
        Returns a tuple of unbalanced transformer UIDs attached to the busbar specified by busbar UID.
        Only unbalanced transformers are returned, not unbalanced branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of unbalanced transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBranches(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscBranch instances.
        Key values (sPyName) are the Python names and the associated values are IscBranch instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of branches.
        :rtype: dict(str,IscBranch)
        """
        pass

    def GetTransformers(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscTransformer instances.
        Keys (sPyName) are the Python names and the associated values are IscTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of transformers.
        :rtype: dict(str,IscTransformer)
        """
        pass

    def Get3WTransformers(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of Isc3WTransformer instances.
        Keys (sPyName) are the Python names and the associated values are Isc3WTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of 3WTransformers.
        :rtype: dict(str,Isc3WTransformer)
        """
        pass

    def GetLoads(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscLoad instances.
        Keys (sPyName) are the Python names and the associated values are IscLoad instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of loads.
        :rtype: dict(str,IscLoad)
        """
        pass

    def GetSynMachines(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscSynMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscSynMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of synchronous machines.
        :rtype: dict(str,IscSynMachine)
        """
        pass

    def GetGridInfeeds(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscGridInfeed instances.
        Keys (sPyName) are the Python names and the associated values are IscGridInfeed instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of grid infeeds.
        :rtype: dict(str,IscGridInfeed)
        """
        pass

    def GetFilters(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscFilter instances.
        Keys (sPyName) are the Python names and the associated values are IscFilter instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of filters.
        :rtype: dict(str,IscFilter)
        """
        pass

    def GetIndMachines(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscIndMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscIndMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of induction machines.
        :rtype: dict(str,IscIndMachine)
        """
        pass

    def GetMechSwCapacitors(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscMechSwCapacitor instances.
        Keys (sPyName) are the Python names and the associated values are IscMechSwCapacitor instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of mechanical switch capacitors.
        :rtype: dict(str,IscMechSwCapacitor)
        """
        pass

    def GetStaticVCs(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscStaticVC instances.
        Keys (sPyName) are the Python names and the associated values are IscStaticVC instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of static var compensators.
        :rtype: dict(str,IscStaticVC)
        """
        pass

    def GetUMachines(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscUMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscUMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of universal machines.
        :rtype: dict(str,IscUMachine)
        """
        pass

    def GetHarmonics(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscHarmonic instances.
        Keys (sPyName) are the Python names and the associated values are IscHarmonic instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of harmonics.
        :rtype: dict(str,IscHarmonic)
        """
        pass

    def GetCircuitBreakers(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscCircuitBreaker instances.
        Keys (sPyName) are the Python names and the associated values are IscCircuitBreaker instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of circuit breakers.
        :rtype: dict(str,IscCircuitBreaker)
        """
        pass

    def GetBatteries(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscBattery instances.
        Keys (sPyName) are the Python names and the associated values are IscBattery instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of batteries.
        :rtype: dict(str,IscBattery)
        """
        pass

    def GetDCMachines(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscDCMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscDCMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of DC machines.
        :rtype: dict(str,IscDCMachine)
        """
        pass

    def GetConverters(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscConverter instances.
        Keys (sPyName) are the Python names and the associated values are IscConverter instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of converters.
        :rtype: dict(str,IscConverter)
        """
        pass

    def GetChoppers(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscChopper instances.
        Keys (sPyName) are the Python names and the associated values are IscChopper instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of choppers.
        :rtype: dict(str,IscChopper)
        """
        pass

    def GetMGSets(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscMGSet instances.
        Keys (sPyName) are the Python names and the associated values are IscMGSet instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of MG sets.
        :rtype: dict(str,IscMGSet)
        """
        pass

    def GetProtectionDevices(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscProtectionDevice instances.
        Keys (sPyName) are the Python names and the associated values are IscProtectionDevice instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of protection devices.
        :rtype: dict(str,IscProtectionDevice)
        """
        pass

    def GetUnbalancedLoads(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscUnbalancedLoad instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedLoad instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced loads.
        :rtype: dict(str,IscUnbalancedLoad)
        """
        pass

    def GetUnbalancedLines(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscUnbalancedLine instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedLine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced lines.
        :rtype: dict(str,IscUnbalancedLine)
        """
        pass

    def GetUnbalancedTransformers(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscUnbalancedTransformer instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced transformers.
        :rtype: dict(str,IscUnbalancedTransformer)
        """
        pass

    def GetVoltageRegulators(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscVoltageRegulator instances.
        Keys (sPyName) are the Python names and the associated values are IscVoltageRegulator instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of voltage regulators.
        :rtype: dict(str,IscVoltageRegulator)
        """
        pass

    def GetAnnotations(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscAnnotation instances.
        Keys (sPyName) are the Python names and the associated values are IscAnnotation instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of annotations.
        :rtype: dict(str,IscAnnotation)
        """
        pass

    def GetGroups(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscGroup instances.
        Keys (sPyName) are the Python names and the associated values are IscGroup instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of groups.
        :rtype: dict(str,IscGroup)
        """
        pass

    def GetGroupsForItem(self, nUID: int, bFetchFromSystem: bool = True) -> Tuple[int]:
        """
        Returns a tuple containing the group UIDs for each group that the component UID is a member of.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :param nUID: Component UID.
        :type nUID: int
        :return: Tuple of group UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetIntertrips(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscIntertrip instances.
        Keys (sPyName) are the Python names and the associated values are IscIntertrip instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of intertrips.
        :rtype: dict(str,IscIntertrip)
        """
        pass

    def GetPlugins(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of IscPlugin instances.
        Keys (sPyName) are the Python names and the associated values are IscPlugin instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of plugins.
        :rtype: dict(str,IscPlugin)
        """
        pass

    def TraceBusbarUIDs(self, nBranchUID: int, bOpenBreakers: bool, nGroupUID: int) -> List[int]:
        """
        Performs a network trace to identify all busbars that are connected to the selected branch.
        The network trace stops when it reaches any busbar that is a member of the group of the selected group UID or
        when it reaches a transformer.

        :param nBranchUID: The selected branch UID.
        :type nBranchUID: int
        :param bOpenBreakers: If True then the trace also stops if it finds an open circuit breaker.
        :type bOpenBreakers: bool
        :param nGroupUID: The selected group UID.
        :type nGroupUID: int
        :return: List of all busbar UIDs found by the trace.
        :rtype: list(int)
        """
        pass

    def GetBusbarSlacks(self) -> List[str]:
        """
        Returns a list of all the busbar names contained in the network busbar slack list.

        :return: List of busbar names.
        :rtype: list(str)
        """
        pass

    @overload
    def GetBusbar(self, nUID: int):
        """
        Returns an IscBusbar instance for the busbar identified by the UID.

        :param nUID: The selected busbar UID.
        :type nUID: int
        :return: The busbar instance or None if such is not found.
        :rtype: IscBusbar
        """
        pass

    @overload
    def GetBusbar(self, strPythonName: str):
        """
        Returns an IscBusbar instance for the busbar identified by the Python name.

        :param strPythonName: The selected busbar name.
        :type strPythonName: str
        :return: The busbar instance or None if such is not found.
        :rtype: IscBusbar
        """
        pass

    def GetBusbar(self, strPythonName: str):
        """
        Returns an IscBusbar instance for the busbar identified by the UID or the Python name.

        You can use either nUID specifying the busbar UID, or strPythonName specifying its name.

        :param nUID: The selected busbar UID.
        :type nUID: int
        :param strPythonName: The selected busbar name.
        :type strPythonName: str
        :return: The busbar instance or None if such is not found.
        :rtype: IscBusbar
        """
        pass

    @overload
    def GetBranch(self, nUID: int):
        """
        Returns an IscBranch instance for the branch identified by the UID.

        :param nUID: The selected branch UID.
        :type nUID: int
        :return: The branch instance or None if such is not found.
        :rtype: IscBranch
        """
        pass

    @overload
    def GetBranch(self, strPythonName: str):
        """
        Returns an IscBranch instance for the branch identified by the Python name.

        :param strPythonName: The selected branch name.
        :type strPythonName: str
        :return: The branch instance or None if such is not found.
        :rtype: IscBranch
        """
        pass

    def GetBranch(self, strPythonName: str):
        """
        Returns an IscBranch instance for the branch identified by the UID or the Python name.

        You can use either nUID specifying the branch UID, or strPythonName specifying its name.

        :param nUID: The selected branch UID.
        :type nUID: int
        :param strPythonName: The selected branch name.
        :type strPythonName: str
        :return: The branch instance or None if such is not found.
        :rtype: IscBranch
        """
        pass

    @overload
    def GetTransformer(self, nUID: int):
        """
        Returns an IscTransformer instance for the transformer identified by the UID.

        :param nUID: The selected transformer UID.
        :type nUID: int
        :return: The transformer instance or None if such is not found.
        :rtype: IscTransformer
        """
        pass

    @overload
    def GetTransformer(self, strPythonName: str):
        """
        Returns an IscTransformer instance for the transformer identified by the Python name.

        :param strPythonName: The selected transformer name.
        :type strPythonName: str
        :return: The transformer instance or None if such is not found.
        :rtype: IscTransformer
        """
        pass

    def GetTransformer(self, strPythonName: str):
        """
        Returns an IscTransformer instance for the transformer identified by the UID or the Python name.

        You can use either nUID specifying the transformer UID, or strPythonName specifying its name.

        :param nUID: The selected transformer UID.
        :type nUID: int
        :param strPythonName: The selected transformer name.
        :type strPythonName: str
        :return: The transformer instance or None if such is not found.
        :rtype: IscTransformer
        """
        pass

    @overload
    def Get3WTransformer(self, nUID: int):
        """
        Returns an Isc3WTransformer instance for the three winding transformer identified by the UID.

        :param nUID: The selected three winding transformer UID.
        :type nUID: int
        :return: The three winding transformer instance or None if such is not found.
        :rtype: Isc3WTransformer
        """
        pass

    @overload
    def Get3WTransformer(self, strPythonName: str):
        """
        Returns an Isc3WTransformer instance for the three winding transformer identified by the Python name.

        :param strPythonName: The selected three winding transformer name.
        :type strPythonName: str
        :return: The three winding transformer instance or None if such is not found.
        :rtype: Isc3WTransformer
        """
        pass

    def Get3WTransformer(self, strPythonName: str):
        """
        Returns an Isc3WTransformer instance for the three winding transformer identified by the UID or the Python name.

        You can use either nUID specifying the three winding transformer UID, or strPythonName specifying its name.

        :param nUID: The selected three winding transformer UID.
        :type nUID: int
        :param strPythonName: The selected three winding transformer name.
        :type strPythonName: str
        :return: The three winding transformer instance or None if such is not found.
        :rtype: Isc3WTransformer
        """
        pass

    @overload
    def GetLoad(self, nUID: int):
        """
        Returns an IscLoad instance for the load identified by the UID.

        :param nUID: The selected load UID.
        :type nUID: int
        :return: The load instance or None if such is not found.
        :rtype: IscLoad
        """
        pass

    @overload
    def GetLoad(self, strPythonName: str):
        """
        Returns an IscLoad instance for the load identified by the Python name.

        :param strPythonName: The selected load name.
        :type strPythonName: str
        :return: The load instance or None if such is not found.
        :rtype: IscLoad
        """
        pass

    def GetLoad(self, strPythonName: str):
        """
        Returns an IscLoad instance for the load identified by the UID or the Python name.

        You can use either nUID specifying the load UID, or strPythonName specifying its name.

        :param nUID: The selected load UID.
        :type nUID: int
        :param strPythonName: The selected load name.
        :type strPythonName: str
        :return: The load instance or None if such is not found.
        :rtype: IscLoad
        """
        pass

    @overload
    def GetSynMachine(self, nUID: int):
        """
        Returns an IscSynMachine instance for the synchronous machine identified by the UID.

        :param nUID: The selected synchronous machine UID.
        :type nUID: int
        :return: The synchronous machine instance or None if such is not found.
        :rtype: IscSynMachine
        """
        pass

    @overload
    def GetSynMachine(self, strPythonName: str):
        """
        Returns an IscSynMachine instance for the synchronous machine identified by the Python name.

        :param strPythonName: The selected synchronous machine name.
        :type strPythonName: str
        :return: The synchronous machine instance or None if such is not found.
        :rtype: IscSynMachine
        """
        pass

    def GetSynMachine(self, strPythonName: str):
        """
        Returns an IscSynMachine instance for the synchronous machine identified by the UID or the Python name.

        You can use either nUID specifying the synchronous machine UID, or strPythonName specifying its name.

        :param nUID: The selected synchronous machine UID.
        :type nUID: int
        :param strPythonName: The selected synchronous machine name.
        :type strPythonName: str
        :return: The synchronous machine instance or None if such is not found.
        :rtype: IscSynMachine
        """
        pass

    @overload
    def GetGridInfeed(self, nUID: int):
        """
        Returns an IscGridInfeed instance for the grid infeed identified by the UID.

        :param nUID: The selected grid infeed UID.
        :type nUID: int
        :return: The grid infeed instance or None if such is not found.
        :rtype: IscGridInfeed
        """
        pass

    @overload
    def GetGridInfeed(self, strPythonName: str):
        """
        Returns an IscGridInfeed instance for the grid infeed identified by the Python name.

        :param strPythonName: The selected grid infeed name.
        :type strPythonName: str
        :return: The grid infeed instance or None if such is not found.
        :rtype: IscGridInfeed
        """
        pass

    def GetGridInfeed(self, strPythonName: str):
        """
        Returns an IscGridInfeed instance for the grid infeed identified by the UID or the Python name.

        You can use either nUID specifying the grid infeed UID, or strPythonName specifying its name.

        :param nUID: The selected grid infeed UID.
        :type nUID: int
        :param strPythonName: The selected grid infeed name.
        :type strPythonName: str
        :return: The grid infeed instance or None if such is not found.
        :rtype: IscGridInfeed
        """
        pass

    @overload
    def GetIndMachine(self, nUID: int):
        """
        Returns an IscIndMachine instance for the induction motor identified by the UID.

        :param nUID: The selected induction motor UID.
        :type nUID: int
        :return: The induction motor instance or None if such is not found.
        :rtype: IscIndMachine
        """
        pass

    @overload
    def GetIndMachine(self, strPythonName: str):
        """
        Returns an IscIndMachine instance for the induction motor identified by the Python name.

        :param strPythonName: The selected induction motor name.
        :type strPythonName: str
        :return: The induction motor instance or None if such is not found.
        :rtype: IscIndMachine
        """
        pass

    def GetIndMachine(self, strPythonName: str):
        """
        Returns an IscIndMachine instance for the induction motor identified by the UID or the Python name.

        You can use either nUID specifying the induction motor UID, or strPythonName specifying its name.

        :param nUID: The selected induction motor UID.
        :type nUID: int
        :param strPythonName: The selected induction motor name.
        :type strPythonName: str
        :return: The induction motor instance or None if such is not found.
        :rtype: IscIndMachine
        """
        pass

    @overload
    def GetFilter(self, nUID: int):
        """
        Returns an IscFilter instance for the harmonic filter identified by the UID.

        :param nUID: The selected harmonic filter UID.
        :type nUID: int
        :return: The harmonic filter instance or None if such is not found.
        :rtype: IscFilter
        """
        pass

    @overload
    def GetFilter(self, strPythonName: str):
        """
        Returns an IscFilter instance for the harmonic filter identified by the Python name.

        :param strPythonName: The selected harmonic filter name.
        :type strPythonName: str
        :return: The harmonic filter instance or None if such is not found.
        :rtype: IscFilter
        """
        pass

    def GetFilter(self, strPythonName: str):
        """
        Returns an IscFilter instance for the harmonic filter identified by the UID or the Python name.

        You can use either nUID specifying the harmonic filter UID, or strPythonName specifying its name.

        :param nUID: The selected harmonic filter UID.
        :type nUID: int
        :param strPythonName: The selected harmonic filter name.
        :type strPythonName: str
        :return: The harmonic filter instance or None if such is not found.
        :rtype: IscFilter
        """
        pass

    @overload
    def GetMechSwCapacitor(self, nUID: int):
        """
        Returns an IscMechSwCapacitor instance for the mechanically switched capacitor identified by the UID.

        :param nUID: The selected mechanically switched capacitor UID.
        :type nUID: int
        :return: The mechanically switched capacitor instance or None if such is not found.
        :rtype: IscMechSwCapacitor
        """
        pass

    @overload
    def GetMechSwCapacitor(self, strPythonName: str):
        """
        Returns an IscMechSwCapacitor instance for the mechanically switched capacitor identified by the Python name.

        :param strPythonName: The selected mechanically switched capacitor name.
        :type strPythonName: str
        :return: The mechanically switched capacitor instance or None if such is not found.
        :rtype: IscMechSwCapacitor
        """
        pass

    def GetMechSwCapacitor(self, strPythonName: str):
        """
        Returns an IscMechSwCapacitor instance for the mechanically switched capacitor identified by
        the UID or the Python name.

        You can use either nUID specifying the mechanically switched capacitor UID,
        or strPythonName specifying its name.

        :param nUID: The selected mechanically switched capacitor UID.
        :type nUID: int
        :param strPythonName: The selected mechanically switched capacitor name.
        :type strPythonName: str
        :return: The mechanically switched capacitor instance or None if such is not found.
        :rtype: IscMechSwCapacitor
        """
        pass

    @overload
    def GetStaticVC(self, nUID: int):
        """
        Returns an IscStaticVC instance for the static VAR compensator identified by the UID.

        :param nUID: The selected static VAR compensator UID.
        :type nUID: int
        :return: The static VAR compensator instance or None if such is not found.
        :rtype: IscStaticVC
        """
        pass

    @overload
    def GetStaticVC(self, strPythonName: str):
        """
        Returns an IscStaticVC instance for the static VAR compensator identified by the Python name.

        :param strPythonName: The selected static VAR compensator name.
        :type strPythonName: str
        :return: The static VAR compensator instance or None if such is not found.
        :rtype: IscStaticVC
        """
        pass

    def GetStaticVC(self, strPythonName: str):
        """
        Returns an IscStaticVC instance for the static VAR compensator identified by the UID or the Python name.

        You can use either nUID specifying the static VAR compensator UID, or strPythonName specifying its name.

        :param nUID: The selected static VAR compensator UID.
        :type nUID: int
        :param strPythonName: The selected static VAR compensator name.
        :type strPythonName: str
        :return: The static VAR compensator instance or None if such is not found.
        :rtype: IscStaticVC
        """
        pass

    @overload
    def GetUMachine(self, nUID: int):
        """
        Returns an IscUMachine instance for the universal machine identified by the UID.

        :param nUID: The selected universal machine UID.
        :type nUID: int
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    @overload
    def GetUMachine(self, strPythonName: str):
        """
        Returns an IscUMachine instance for the universal machine identified by the Python name.

        :param strPythonName: The selected universal machine name.
        :type strPythonName: str
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    def GetUMachine(self, strPythonName: str):
        """
        Returns an IscUMachine instance for the universal machine identified by the UID or the Python name.

        You can use either nUID specifying the universal machine UID, or strPythonName specifying its name.

        :param nUID: The selected universal machine UID.
        :type nUID: int
        :param strPythonName: The selected universal machine name.
        :type strPythonName: str
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    @overload
    def GetHarmonic(self, nUID: int):
        """
        Returns an IscHarmonic instance for the harmonic source identified by the UID.

        :param nUID: The selected harmonic source UID.
        :type nUID: int
        :return: The harmonic source instance or None if such is not found.
        :rtype: IscHarmonic
        """
        pass

    @overload
    def GetHarmonic(self, strPythonName: str):
        """
        Returns an IscHarmonic instance for the harmonic source identified by the Python name.

        :param strPythonName: The selected harmonic source name.
        :type strPythonName: str
        :return: The harmonic source instance or None if such is not found.
        :rtype: IscHarmonic
        """
        pass

    def GetHarmonic(self, strPythonName: str):
        """
        Returns an IscHarmonic instance for the harmonic source identified by the UID or the Python name.

        You can use either nUID specifying the harmonic source UID, or strPythonName specifying its name.

        :param nUID: The selected harmonic source UID.
        :type nUID: int
        :param strPythonName: The selected harmonic source name.
        :type strPythonName: str
        :return: The harmonic source instance or None if such is not found.
        :rtype: IscHarmonic
        """
        pass

    @overload
    def GetCircuitBreaker(self, nUID: int):
        """
        Returns an IscCircuitBreaker instance for the circuit breaker identified by the Python name.

        :param nUID: The selected circuit breaker UID.
        :type nUID: int
        :return: The circuit breaker instance or None if such is not found.
        :rtype: IscCircuitBreaker
        """
        pass

    @overload
    def GetCircuitBreaker(self, strPythonName: str):
        """
        Returns an IscCircuitBreaker instance for the circuit breaker identified by the Python name.

        :param strPythonName: The selected circuit breaker name.
        :type strPythonName: str
        :return: The circuit breaker instance or None if such is not found.
        :rtype: IscCircuitBreaker
        """
        pass

    def GetCircuitBreaker(self, strPythonName: str):
        """
        Returns an IscCircuitBreaker instance for the circuit breaker identified by the UID or the Python name.

        You can use either nUID specifying the circuit breaker UID, or strPythonName specifying its name.

        :param nUID: The selected circuit breaker UID.
        :type nUID: int
        :param strPythonName: The selected circuit breaker name.
        :type strPythonName: str
        :return: The circuit breaker instance or None if such is not found.
        :rtype: IscCircuitBreaker
        """
        pass

    @overload
    def GetBattery(self, nUID: int):
        """
        Returns an IscBattery instance for the DC battery identified by the UID.

        :param nUID: The selected DC battery UID.
        :type nUID: int
        :return: The DC battery instance or None if such is not found.
        :rtype: IscBattery
        """
        pass

    @overload
    def GetBattery(self, strPythonName: str):
        """
        Returns an IscBattery instance for the DC battery identified by the Python name.

        :param strPythonName: The selected DC battery name.
        :type strPythonName: str
        :return: The DC battery instance or None if such is not found.
        :rtype: IscBattery
        """
        pass

    def GetBattery(self, strPythonName: str):
        """
        Returns an IscBattery instance for the DC battery identified by the UID or the Python name.

        You can use either nUID specifying the DC battery UID, or strPythonName specifying its name.

        :param nUID: The selected DC battery UID.
        :type nUID: int
        :param strPythonName: The selected DC battery name.
        :type strPythonName: str
        :return: The DC battery instance or None if such is not found.
        :rtype: IscBattery
        """
        pass

    @overload
    def GetDCMachine(self, nUID: int):
        """
        Returns an IscDCMachine instance for the DC machine identified by the UID.

        :param nUID: The selected DC machine UID.
        :type nUID: int
        :return: The DC machine instance or None if such is not found.
        :rtype: IscDCMachine
        """
        pass

    @overload
    def GetDCMachine(self, strPythonName: str):
        """
        Returns an IscDCMachine instance for the DC machine identified by the Python name.

        :param strPythonName: The selected DC machine name.
        :type strPythonName: str
        :return: The DC machine instance or None if such is not found.
        :rtype: IscDCMachine
        """
        pass

    def GetDCMachine(self, strPythonName: str):
        """
        Returns an IscDCMachine instance for the DC machine identified by the UID or the Python name.

        You can use either nUID specifying the DC machine UID, or strPythonName specifying its name.

        :param nUID: The selected DC machine UID.
        :type nUID: int
        :param strPythonName: The selected DC machine name.
        :type strPythonName: str
        :return: The DC machine instance or None if such is not found.
        :rtype: IscDCMachine
        """
        pass

    @overload
    def GetConverter(self, nUID: int):
        """
        Returns an IscConverter instance for the AC/DC convertor identified by the UID.

        :param nUID: The selected AC/DC convertor UID.
        :type nUID: int
        :return: The AC/DC convertor instance or None if such is not found.
        :rtype: IscConverter
        """
        pass

    @overload
    def GetConverter(self, strPythonName: str):
        """
        Returns an IscConverter instance for the AC/DC convertor identified by the Python name.

        :param strPythonName: The selected AC/DC convertor name.
        :type strPythonName: str
        :return: The AC/DC convertor instance or None if such is not found.
        :rtype: IscConverter
        """
        pass

    def GetConverter(self, strPythonName: str):
        """
        Returns an IscConverter instance for the AC/DC convertor identified by the UID or the Python name.

        You can use either nUID specifying the AC/DC convertor UID, or strPythonName specifying its name.

        :param nUID: The selected AC/DC convertor UID.
        :type nUID: int
        :param strPythonName: The selected AC/DC convertor name.
        :type strPythonName: str
        :return: The AC/DC convertor instance or None if such is not found.
        :rtype: IscConverter
        """
        pass

    @overload
    def GetChopper(self, nUID: int):
        """
        Returns an IscChopper instance for the AC/DC convertor identified by the UID.

        :param nUID: The selected AC/DC convertor UID.
        :type nUID: int
        :return: The AC/DC chopper instance or None if such is not found.
        :rtype: IscChopper
        """
        pass

    @overload
    def GetChopper(self, strPythonName: str):
        """
        Returns an IscChopper instance for the AC/DC convertor identified by the Python name.

        :param strPythonName: The selected AC/DC convertor name.
        :type strPythonName: str
        :return: The AC/DC chopper instance or None if such is not found.
        :rtype: IscChopper
        """
        pass

    def GetChopper(self, strPythonName: str):
        """
        Returns an IscChopper instance for the AC/DC convertor identified by the UID or the Python name.

        You can use either nUID specifying the AC/DC convertor UID, or strPythonName specifying its name.

        :param nUID: The selected AC/DC convertor UID.
        :type nUID: int
        :param strPythonName: The selected AC/DC convertor name.
        :type strPythonName: str
        :return: The AC/DC chopper instance or None if such is not found.
        :rtype: IscChopper
        """
        pass

    @overload
    def GetMGSet(self, nUID: int):
        """
        Returns an IscMGSet instance for the motor generator set identified by the UID.

        :param nUID: The selected motor generator set UID.
        :type nUID: int
        :return: The motor generator set instance or None if such is not found.
        :rtype: IscMGSet
        """
        pass

    @overload
    def GetMGSet(self, strPythonName: str):
        """
        Returns an IscMGSet instance for the motor generator set identified by the Python name.

        :param strPythonName: The selected motor generator set name.
        :type strPythonName: str
        :return: The motor generator set instance or None if such is not found.
        :rtype: IscMGSet
        """
        pass

    def GetMGSet(self, strPythonName: str):
        """
        Returns an IscMGSet instance for the motor generator set identified by the UID or the Python name.

        You can use either nUID specifying the motor generator set UID, or strPythonName specifying its name.

        :param nUID: The selected motor generator set UID.
        :type nUID: int
        :param strPythonName: The selected motor generator set name.
        :type strPythonName: str
        :return: The motor generator set instance or None if such is not found.
        :rtype: IscMGSet
        """
        pass

    @overload
    def GetVoltageRegulator(self, nUID: int):
        """
        Returns an IscVoltageRegulator instance for the voltage regulator identified by the UID.

        :param nUID: The selected voltage regulator UID.
        :type nUID: int
        :return: The voltage regulator instance or None if such is not found.
        :rtype: IscVoltageRegulator
        """
        pass

    @overload
    def GetVoltageRegulator(self, strPythonName: str):
        """
        Returns an IscVoltageRegulator instance for the voltage regulator identified by the Python name.

        :param strPythonName: The selected voltage regulator name.
        :type strPythonName: str
        :return: The voltage regulator instance or None if such is not found.
        :rtype: IscVoltageRegulator
        """
        pass

    def GetVoltageRegulator(self, strPythonName: str):
        """
        Returns an IscVoltageRegulator instance for the voltage regulator identified by the UID or the Python name.

        You can use either nUID specifying the voltage regulator UID, or strPythonName specifying its name.

        :param nUID: The selected voltage regulator UID.
        :type nUID: int
        :param strPythonName: The selected voltage regulator name.
        :type strPythonName: str
        :return: The voltage regulator instance or None if such is not found.
        :rtype: IscVoltageRegulator
        """
        pass

    @overload
    def GetProtectionDevice(self, nUID: int):
        """
        Returns an IscProtectionDevice instance for the protection device identified by the UID.

        :param nUID: The selected protection device  UID.
        :type nUID: int
        :return: The protection device instance or None if such is not found.
        :rtype: IscProtectionDevice
        """
        pass

    @overload
    def GetProtectionDevice(self, strPythonName: str):
        """
        Returns an IscProtectionDevice instance for the protection device identified by the Python name.

        :param strPythonName: The selected protection device name.
        :type strPythonName: str
        :return: The protection device instance or None if such is not found.
        :rtype: IscProtectionDevice
        """
        pass

    def GetProtectionDevice(self, strPythonName: str):
        """
        Returns an IscProtectionDevice instance for the protection device identified by the UID or the Python name.

        You can use either nUID specifying the protection device UID, or strPythonName specifying its name.

        :param nUID: The selected protection device  UID.
        :type nUID: int
        :param strPythonName: The selected protection device name.
        :type strPythonName: str
        :return: The protection device instance or None if such is not found.
        :rtype: IscProtectionDevice
        """
        pass

    @overload
    def GetAnnotation(self, nUID: int):
        """
        Returns an IscAnnotation instance for the diagram annotation identified by the UID.

        :param nUID: The selected diagram annotation UID.
        :type nUID: int
        :return: The diagram annotation instance or None if such is not found.
        :rtype: IscAnnotation
        """
        pass

    @overload
    def GetAnnotation(self, strPythonName: str):
        """
        Returns an IscAnnotation instance for the diagram annotation identified by the Python name.

        :param strPythonName: The selected diagram annotation name.
        :type strPythonName: str
        :return: The diagram annotation instance or None if such is not found.
        :rtype: IscAnnotation
        """
        pass

    def GetAnnotation(self, strPythonName: str):
        """
        Returns an IscAnnotation instance for the diagram annotation identified by the UID or the Python name.

        You can use either nUID specifying the diagram annotation UID, or strPythonName specifying its name.

        :param nUID: The selected diagram annotation UID.
        :type nUID: int
        :param strPythonName: The selected diagram annotation name.
        :type strPythonName: str
        :return: The diagram annotation instance or None if such is not found.
        :rtype: IscAnnotation
        """
        pass

    @overload
    def GetGroup(self, nUID: int):
        """
        Returns an IscGroup instance for the group identified by the UID.

        :param nUID: The selected group UID.
        :type nUID: int
        :return: The group instance or None if such is not found.
        :rtype: IscGroup
        """
        pass

    @overload
    def GetGroup(self, strPythonName: str):
        """
        Returns an IscGroup instance for the group identified by the Python name.

        :param strPythonName: The selected group name.
        :type strPythonName: str
        :return: The group instance or None if such is not found.
        :rtype: IscGroup
        """
        pass

    def GetGroup(self, strPythonName: str):
        """
        Returns an IscGroup instance for the group identified by the UID or the Python name.

        You can use either nUID specifying the group UID, or strPythonName specifying its name.

        :param nUID: The selected group UID.
        :type nUID: int
        :param strPythonName: The selected group name.
        :type strPythonName: str
        :return: The group instance or None if such is not found.
        :rtype: IscGroup
        """
        pass

    @overload
    def GetIntertrip(self, nUID: int):
        """
        Returns an IscIntertrip instance for the intertrip identified by the UID.

        :param nUID: The selected intertrip UID.
        :type nUID: int
        :return: The intertrip instance or None if such is not found.
        :rtype: IscIntertrip
        """
        pass

    @overload
    def GetIntertrip(self, strPythonName: str):
        """
        Returns an IscIntertrip instance for the intertrip identified by the Python name.

        :param strPythonName: The selected intertrip name.
        :type strPythonName: str
        :return: The intertrip instance or None if such is not found.
        :rtype: IscIntertrip
        """
        pass

    def GetIntertrip(self, strPythonName: str):
        """
        Returns an IscIntertrip instance for the intertrip identified by the UID or the Python name.

        You can use either nUID specifying the intertrip UID, or strPythonName specifying its name.

        :param nUID: The selected intertrip UID.
        :type nUID: int
        :param strPythonName: The selected intertrip name.
        :type strPythonName: str
        :return: The intertrip instance or None if such is not found.
        :rtype: IscIntertrip
        """
        pass

    def GetIntertripFromBreaker(self, nBreakerUID: int) -> int:
        """"
        Returns the UID of the intertrip the breaker identified by nBreakerUID belongs to.
        Returns 0 if no intertrip is found.

        :param nBreakerUID: The breaker UID.
        :type nBreakerUID: int
        :return: The UID of the intertrip associated with the breaker or 0 if none is found.
        :rtype: int
        """
        pass

    @overload
    def GetPlugin(self, nUID: int):
        """
        Returns an IscPlugin instance for the plugin identified by the UID.

        :param nUID: The selected plugin UID.
        :type nUID: int
        :return: The plugin instance or None if such is not found.
        :rtype: IscPlugin
        """
        pass

    @overload
    def GetPlugin(self, strPythonName: str):
        """
        Returns an IscPlugin instance for the plugin identified by the Python name.
        :param strPythonName: The selected plugin name.
        :type strPythonName: str
        :return: The plugin instance or None if such is not found.
        :rtype: IscPlugin
        """
        pass

    def GetPlugin(self, strPythonName: str):
        """
        Returns an IscPlugin instance for the plugin identified by the UID or the Python name.

        You can use either nUID specifying the plugin UID, or strPythonName specifying its name.

        :param nUID: The selected plugin UID.
        :type nUID: int
        :param strPythonName: The selected plugin name.
        :type strPythonName: str
        :return: The plugin instance or None if such is not found.
        :rtype: IscPlugin
        """
        pass

    @overload
    def GetUnbalancedLoad(self, nUID: int):
        """
        Returns an IscUnbalancedLoad instance for the unbalanced load identified by the UID.

        :param nUID: The selected unbalanced load UID.
        :type nUID: int
        :return: The unbalanced load instance or None if such is not found.
        :rtype: IscUnbalancedLoad
        """
        pass

    @overload
    def GetUnbalancedLoad(self, strPythonName: str):
        """
        Returns an IscUnbalancedLoad instance for the unbalanced load identified by the Python name.

        :param strPythonName: The selected unbalanced load name.
        :type strPythonName: str
        :return: The unbalanced load instance or None if such is not found.
        :rtype: IscUnbalancedLoad
        """
        pass

    def GetUnbalancedLoad(self, strPythonName: str):
        """
        Returns an IscUnbalancedLoad instance for the unbalanced load identified by the UID or the Python name.

        :param nUID: The selected unbalanced load UID.
        :type nUID: int
        :param strPythonName: The selected unbalanced load name.
        :type strPythonName: str
        :return: The unbalanced load instance or None if such is not found.
        :rtype: IscUnbalancedLoad
        """
        pass

    @overload
    def GetUnbalancedLine(self, nUID: int):
        """
        Returns an IscUnbalancedLine instance for the unbalanced line identified by the UID.

        :param nUID: The selected unbalanced line UID.
        :type nUID: int
        :return: The unbalanced line instance or None if such is not found.
        :rtype: IscUnbalancedLine
        """
        pass

    @overload
    def GetUnbalancedLine(self, strPythonName: str):
        """
        Returns an IscUnbalancedLine instance for the unbalanced line identified by the Python name.

        :param strPythonName: The selected unbalanced line name.
        :type strPythonName: str
        :return: The unbalanced line instance or None if such is not found.
        :rtype: IscUnbalancedLine
        """
        pass

    def GetUnbalancedLine(self, strPythonName: str):
        """
        Returns an IscUnbalancedLine instance for the unbalanced line identified by the UID or the Python name.

        :param nUID: The selected unbalanced line UID.
        :type nUID: int
        :param strPythonName: The selected unbalanced line name.
        :type strPythonName: str
        :return: The unbalanced line instance or None if such is not found.
        :rtype: IscUnbalancedLine
        """
        pass

    @overload
    def GetUnbalancedTransformer(self, nUID: int):
        """
        Returns an IscUnbalancedTransformer instance for the unbalanced transformer identified by
        the UID.

        :param nUID: The selected unbalanced transformer UID.
        :type nUID: int
        :return: The unbalanced transformer instance or None if such is not found.
        :rtype: IscUnbalancedTransformer
        """
        pass

    @overload
    def GetUnbalancedTransformer(self, strPythonName: str):
        """
        Returns an IscUnbalancedTransformer instance for the unbalanced transformer identified by
        the Python name.

        :param strPythonName: The selected unbalanced transformer name.
        :type strPythonName: str
        :return: The unbalanced transformer instance or None if such is not found.
        :rtype: IscUnbalancedTransformer
        """
        pass

    def GetUnbalancedTransformer(self, nUID: int):
        """
        Returns an IscUnbalancedTransformer instance for the unbalanced transformer identified by
        the UID or the Python name.

        :param nUID: The selected unbalanced transformer UID.
        :type nUID: int
        :param strPythonName: The selected unbalanced transformer name.
        :type strPythonName: str
        :return: The unbalanced transformer instance or None if such is not found.
        :rtype: IscUnbalancedTransformer
        """
        pass

    def GetNetworkData(self):
        """
        Returns an IscNetworkData instance of the network.
        The IscNetworkData object provides access to network wide properties such as the base MVA.

        :return: A network data instance of the network.
        :rtype: IscNetworkData
        """
        pass

    def GetBusbarUID(self, strName: str) -> int:
        """
        Returns the UID of a busbar with the given name.

        :param strName: The selected busbar name.
        :type strName: str
        :return: The busbar UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetBusbarUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscBusbar]:
        """
        Returns a dictionary of all busbar UIDs in the network.
        The keys are the integer UIDs and the values are the IscBusbar instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all busbar UIDs.
        :rtype: dict(int,IscBusbar)
        """
        pass

    def GetBranchUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a branch with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected branch name.
        :type strName: str
        :return: The branch UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetBranchUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscBranch]:
        """
        Returns a dictionary of all branch UIDs in the network.
        The keys are the integer UIDs and the values are the IscBranch instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all branches.
        :rtype: dict(int,IscBranch)
        """
        pass

    @overload
    def GetBranchUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all branches connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of branch UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetBranchUIDs(self, nFirstBusID: int, nSecondBusID: int) -> List[int]:
        """
        Returns all branches connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :return: List of branch UIDs.
        :rtype: list(int)
        """
        pass

    def GetBranchUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscBranch]:
        """
        Returns either a dictionary of all branch UIDs in the network or a list of branches connected to the busbars
        specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscBranch instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of branch UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all branches.
        :rtype: dict(int,IscBranch)
        """
        pass

    def GetTransformerUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a transformer with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected transformer name.
        :type strName: str
        :return: The transformer UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetTransformerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscTransformer]:
        """
        Returns a dictionary of all transformer UIDs in the network.
        The keys are the integer UIDs and the values are the IscTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all transformer UIDs.
        :rtype: dict(int,IscTransformer)
        """
        pass

    @overload
    def GetTransformerUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all transformers connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of transformer UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetTransformerUIDs(self, nFirstBusID: int, nSecondBusID: int) -> List[int]:
        """
        Returns all transformers connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :return: List of transformer UIDs.
        :rtype: list(int)
        """
        pass

    def GetTransformerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscTransformer]:
        """
        Returns either a dictionary of all transformer UIDs in the network or a list of transformers connected to the
        busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscTransformer instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of transformer UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all transformers.
        :rtype: dict(int,IscTransformer)
        """
        pass

    def Get3WTransformerUID(self, nFromID: int, nToID: int, nTeritaryID: int, strName: str) -> int:
        """
        Returns the UID of a 3 winding transformer with the given name between three busbars that are specified
        by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param nTeritaryID: The UID of the Teritary busbar.
        :type nTeritaryID: int
        :param strName: The selected 3 winding transformer name.
        :type strName: str
        :return: The 3 winding transformer UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def Get3WTransformerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, Isc3WTransformer]:
        """
        Returns a dictionary of all 3W transformer UIDs in the network.
        The keys are the integer UIDs and the values are the Isc3WTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all 3W Transformers.
        :rtype: dict(int,Isc3WTransformer)
        """
        pass

    @overload
    def Get3WTransformerUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all 3W transformers connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of 3W transformer UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def Get3WTransformerUIDs(self, nFirstBusID: int, nSecondBusID: int, nThirdBusID: int) -> List[int]:
        """
        Returns all 3W transformers connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param nThirdBusID: The UID of the third busbar.
        :type nThirdBusID: int
        :return: List of 3W transformer UIDs.
        :rtype: list(int)
        """
        pass

    def Get3WTransformerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, Isc3WTransformer]:
        """
        Returns either a dictionary of all 3W transformer UIDs in the network or a list of 3W transformers connected to
        the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscTransformer instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param nThirdBusID: The UID of the third busbar.
        :type nThirdBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of 3W transformer UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all 3W transformers.
        :rtype: dict(int,Isc3WTransformer)
        """
        pass

    def GetLoadUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a load with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected load name.
        :type strName: str
        :return: The load UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetLoadUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all loads connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of load UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetLoadUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscLoad]:
        """
        Returns a dictionary of all load UIDs in the network.
        The keys are the integer UIDs and the values are the IscLoad instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all loads.
        :rtype: dict(int,IscLoad)
        """
        pass

    def GetLoadUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscLoad]:
        """
        Returns either a dictionary of all load UIDs in the network or a list of loads connected to
        the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscLoad instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of load UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all loads.
        :rtype: dict(int,IscLoad)
        """
        pass

    def GetSynMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a synchronous machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected synchronous machine name.
        :type strName: str
        :return: The synchronous machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetSynMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all synchronous machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of synchronous machine UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetSynMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscSynMachine]:
        """
        Returns a dictionary of all synchronous machine UIDs in the network.
        The keys are the integer UIDs and the values are the IscSynMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all synchronous machines.
        :rtype: dict(int,IscSynMachine)
        """
        pass

    def GetSynMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscSynMachine]:
        """
        Returns either a dictionary of all synchronous machine UIDs in the network or a list of synchronous machines
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscSynMachine instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of synchronous machine UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all synchronous machines.
        :rtype: dict(int,IscSynMachine)
        """
        pass

    def GetGridInfeedUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a grid infeed with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected grid infeed name.
        :type strName: str
        :return: The grid infeed UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetGridInfeedUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all grid infeeds connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of grid infeed UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetGridInfeedUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscGridInfeed]:
        """
        Returns a dictionary of all grid infeed UIDs in the network.
        The keys are the integer UIDs and the values are the IscGridInfeed instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all grid infeeds.
        :rtype: dict(int,IscGridInfeed)
        """
        pass

    def GetGridInfeedUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscGridInfeed]:
        """
        Returns either a dictionary of all grid infeed UIDs in the network or a list of grid infeeds
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscGridInfeed instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of grid infeed UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all grid infeeds.
        :rtype: dict(int,IscGridInfeed)
        """
        pass

    def GetIndMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of an induction machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected induction machine name.
        :type strName: str
        :return: The induction machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetIndMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all induction machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of induction machine UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetIndMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscIndMachine]:
        """
        Returns a dictionary of all induction machine UIDs in the network.
        The keys are the integer UIDs and the values are the IscIndMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all induction machines.
        :rtype: dict(int,IscIndMachine)
        """
        pass

    def GetIndMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscIndMachine]:
        """
        Returns either a dictionary of all induction machine UIDs in the network or a list of induction machines
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscIndMachine instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of induction machine UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all induction machines.
        :rtype: dict(int,IscIndMachine)
        """
        pass

    def GetFilterUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a filter with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected filter name.
        :type strName: str
        :return: The filter UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetFilterUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all filters connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of filter UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetFilterUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscFilter]:
        """
        Returns a dictionary of all filter UIDs in the network.
        The keys are the integer UIDs and the values are the IscFilter instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all filters.
        :rtype: dict(int,IscFilter)
        """
        pass

    def GetFilterUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscFilter]:
        """
        Returns either a dictionary of all filter UIDs in the network or a list of filters
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscFilter instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of filter UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all filters.
        :rtype: dict(int,IscFilter)
        """
        pass

    def GetMechSwCapacitorUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a mechanically switched capacitor with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected mechanically switched capacitor name.
        :type strName: str
        :return: The mechanically switched capacitor UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetMechSwCapacitorUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all mechanically switched capacitors connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of mechanically switched capacitor UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetMechSwCapacitorUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscMechSwCapacitor]:
        """
        Returns a dictionary of all mechanically switched capacitor UIDs in the network.
        The keys are the integer UIDs and the values are the IscMechSwCapacitor instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all mechanically switched capacitors.
        :rtype: dict(int,IscMechSwCapacitor)
        """
        pass

    def GetMechSwCapacitorUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscMechSwCapacitor]:
        """
        Returns either a dictionary of all mechanically switched capacitor UIDs in the network or a list of
        mechanically switched capacitors
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscMechSwCapacitor instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of mechanically switched capacitor UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all mechanically switched capacitors.
        :rtype: dict(int,IscMechSwCapacitor)
        """
        pass

    def GetStaticVCUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a static VAr compensator with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected static VAr compensator name.
        :type strName: str
        :return: The static VAr compensator UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetStaticVCUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all static VAr compensators connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of static VAr compensator UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetStaticVCUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscStaticVC]:
        """
        Returns a dictionary of all static VAr compensator UIDs in the network.
        The keys are the integer UIDs and the values are the IscStaticVC instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all static VAr compensators.
        :rtype: dict(int,IscStaticVC)
        """
        pass

    def GetStaticVCUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscStaticVC]:
        """
        Returns either a dictionary of all static VAr compensator UIDs in the network or a list of
        static VAr compensators
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscStaticVC instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of static VAr compensator UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all static VAr compensators.
        :rtype: dict(int,IscStaticVC)
        """
        pass

    def GetUMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a universal machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected universal machine name.
        :type strName: str
        :return: The universal machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetUMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all universal machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of universal machine UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetUMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUMachine]:
        """
        Returns a dictionary of all universal machine UIDs in the network.
        The keys are the integer UIDs and the values are the IscUMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all universal machines.
        :rtype: dict(int,IscUMachine)
        """
        pass

    def GetUMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUMachine]:
        """
        Returns either a dictionary of all universal machine UIDs in the network or a list of universal machines
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscUMachine instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of universal machine UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all universal machines.
        :rtype: dict(int,IscUMachine)
        """
        pass

    def GetHarmonicUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a harmonic source with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected harmonic source name.
        :type strName: str
        :return: The harmonic source UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetHarmonicUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all harmonic sources connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of harmonic source UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetHarmonicUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscHarmonic]:
        """
        Returns a dictionary of all harmonic source UIDs in the network.
        The keys are the integer UIDs and the values are the IscHarmonic instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all harmonic sources.
        :rtype: dict(int,IscHarmonic)
        """
        pass

    def GetHarmonicUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscHarmonic]:
        """
        Returns either a dictionary of all harmonic source UIDs in the network or a list of harmonic sources
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscHarmonic instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of harmonic source UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all harmonic sources.
        :rtype: dict(int,IscHarmonic)
        """
        pass

    def GetCircuitBreakerUID(self, nBranchOrTxID: int, nClosestBusbarUID: int) -> int:
        """
        Returns the UID of a circuit breaker located on the branch or transformer specified by its UID.
        The From or To end of the branch is specified by the nClosestBusbarUID parameter.

        :param nBranchOrTxID: The UID of the branch or the transformer.
        :type nBranchOrTxID: int
        :param nClosestBusbarUID: Identifies the busbar at either the From or To end.
        :type nClosestBusbarUID: int
        :return: The circuit breaker UID, 0 if no matches.
        :rtype: int
        """
        pass

    @overload
    def GetCircuitBreakerUIDs(self, nBranchID: int) -> List[int]:
        """
        Returns all circuit breakers connected to the component specified by the given UID.

        :param nBranchID: The UID of the component.
        :type nBranchID: int
        :return: List of circuit breaker UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetCircuitBreakerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscCircuitBreaker]:
        """
        Returns a dictionary of all circuit breaker UIDs in the network.
        The keys are the integer UIDs and the values are the IscCircuitBreaker instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all circuit breakers.
        :rtype: dict(int,IscCircuitBreaker)
        """
        pass

    def GetCircuitBreakerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscCircuitBreaker]:
        """
        Returns either a dictionary of all circuit breaker UIDs in the network or a list of circuit breakers
        connected to the component specified by the given UID.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscCircuitBreaker instances.

        :param nBranchID: The UID of the component.
        :type nBranchID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of circuit breaker UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all circuit breakers.
        :rtype: dict(int,IscCircuitBreaker)
        """
        pass

    def GetFromCircuitBreakerUID(self, nBranchOrTxID: int) -> int:
        """
        Returns the UID of a circuit breaker located on the "From" end of the branch or transformer
        specified by its UID.

        :param nBranchOrTxID: The UID of the branch or the transformer.
        :type nBranchOrTxID: int
        :return: The circuit breaker UID, 0 if no matches.
        :rtype: int
        """
        pass

    def GetToCircuitBreakerUID(self, nBranchOrTxID: int) -> int:
        """
        Returns the UID of a circuit breaker located on the "To" end of the branch or transformer
        specified by its UID.

        :param nBranchOrTxID: The UID of the branch or the transformer.
        :type nBranchOrTxID: int
        :return: The circuit breaker UID, 0 if no matches.
        :rtype: int
        """
        pass

    def GetBatteryUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a battery with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected battery name.
        :type strName: str
        :return: The battery UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetBatteryUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all batteries connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of battery UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetBatteryUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscBattery]:
        """
        Returns a dictionary of all battery UIDs in the network.
        The keys are the integer UIDs and the values are the IscBattery instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all batteries.
        :rtype: dict(int,IscBattery)
        """
        pass

    def GetBatteryUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscBattery]:
        """
        Returns either a dictionary of all battery UIDs in the network or a list of batteries
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscBattery instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of battery UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all batteries.
        :rtype: dict(int,IscBattery)
        """
        pass

    def GetDCMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a DC Machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected DC Machine name.
        :type strName: str
        :return: The DC Machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetDCMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all DC Machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of DC Machine UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetDCMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscDCMachine]:
        """
        Returns a dictionary of all DC Machine UIDs in the network.
        The keys are the integer UIDs and the values are the IscDCMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all DC Machines.
        :rtype: dict(int,IscDCMachine)
        """
        pass

    def GetDCMachineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscDCMachine]:
        """
        Returns either a dictionary of all DC Machine UIDs in the network or a list of DC Machines
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscDCMachine instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of DC Machine UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all DC Machines.
        :rtype: dict(int,IscDCMachine)
        """
        pass

    def GetConverterUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a converter with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected converter name.
        :type strName: str
        :return: The converter UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetConverterUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all converters connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of converter UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetConverterUIDs(self, nFirstBusID: int, nSecondBusID: int) -> List[int]:
        """
        Returns all converters connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :return: List of converter UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetConverterUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscConverter]:
        """
        Returns a dictionary of all converter UIDs in the network.
        The keys are the integer UIDs and the values are the IscConverter instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all converters.
        :rtype: dict(int,IscConverter)
        """
        pass

    def GetConverterUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscConverter]:
        """
        Returns either a dictionary of all converter UIDs in the network or a list of converters connected to the
        busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscConverter instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of converter UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all converters.
        :rtype: dict(int,IscConverter)
        """
        pass

    def GetChopperUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a chopper with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected chopper name.
        :type strName: str
        :return: The chopper UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetChopperUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all choppers connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of chopper UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetChopperUIDs(self, nFirstBusID: int, nSecondBusID: int) -> List[int]:
        """
        Returns all choppers connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :return: List of chopper UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetChopperUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscChopper]:
        """
        Returns a dictionary of all chopper UIDs in the network.
        The keys are the integer UIDs and the values are the IscChopper instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all choppers.
        :rtype: dict(int,IscChopper)
        """
        pass

    def GetChopperUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscChopper]:
        """
        Returns either a dictionary of all chopper UIDs in the network or a list of choppers connected to the
        busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscChopper instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of chopper UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all choppers.
        :rtype: dict(int,IscChopper)
        """
        pass

    def GetMGSetUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a motor/generator with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected motor/generator name.
        :type strName: str
        :return: The motor/generator UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetMGSetUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all motors/generator sets connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of motors/generator set UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetMGSetUIDs(self, nFirstBusID: int, nSecondBusID: int) -> List[int]:
        """
        Returns all motors/generator sets connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :return: List of motors/generator set UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetMGSetUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscMGSet]:
        """
        Returns a dictionary of all motors/generator set UIDs in the network.
        The keys are the integer UIDs and the values are the IscMGSet instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all motors/generator sets.
        :rtype: dict(int,IscMGSet)
        """
        pass

    def GetMGSetUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscMGSet]:
        """
        Returns either a dictionary of all motors/generator set UIDs in the network or a list of motors/generator sets
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscMGSet instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of motors/generator set UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all motors/generator sets.
        :rtype: dict(int,IscMGSet)
        """
        pass

    def GetUnbalancedLoadUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of an unbalanced load with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected unbalanced load name.
        :type strName: str
        :return: The unbalanced load UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetUnbalancedLoadUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all unbalanced loads connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of unbalanced load UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetUnbalancedLoadUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUnbalancedLoad]:
        """
        Returns a dictionary of all unbalanced load UIDs in the network.
        The keys are the integer UIDs and the values are the IscUnbalancedLoad instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all unbalanced loads.
        :rtype: dict(int,IscUnbalancedLoad)
        """
        pass

    def GetUnbalancedLoadUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUnbalancedLoad]:
        """
        Returns either a dictionary of all unbalanced load UIDs in the network or a list of unbalanced loads
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscUnbalancedLoad instances.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of unbalanced load UIDs connected to the items specified by the given UID.
        :rtype: list(int)
        :return: Dictionary of all unbalanced loads.
        :rtype: dict(int,IscUnbalancedLoad)
        """
        pass

    def GetUnbalancedLineUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of an unbalanced line with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected unbalanced line name.
        :type strName: str
        :return: The unbalanced line UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetUnbalancedLineUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all unbalanced lines connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of unbalanced line UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetUnbalancedLineUIDs(self, nFirstBusID: int, nSecondBusID: int) -> List[int]:
        """
        Returns all unbalanced lines connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :return: List of unbalanced line UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetUnbalancedLineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUnbalancedLine]:
        """
        Returns a dictionary of all unbalanced line UIDs in the network.
        The keys are the integer UIDs and the values are the IscUnbalancedLine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all unbalanced lines.
        :rtype: dict(int,IscUnbalancedLine)
        """
        pass

    def GetUnbalancedLineUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUnbalancedLine]:
        """
        Returns either a dictionary of all unbalanced line UIDs in the network or a list of unbalanced lines
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscUnbalancedLine instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of unbalanced line UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all unbalanced lines.
        :rtype: dict(int,IscUnbalancedLine)
        """
        pass

    def GetUnbalancedTransformerUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of an unbalanced transformer with the given name between two busbars that are specified
        by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected unbalanced transformer name.
        :type strName: str
        :return: The unbalanced transformer UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetUnbalancedTransformerUIDs(self, nFirstBusID: int) -> List[int]:
        """
        Returns all unbalanced transformers connected to the busbar specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of unbalanced transformer UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetUnbalancedTransformerUIDs(self, nFirstBusID: int, nSecondBusID: int) -> List[int]:
        """
        Returns all unbalanced transformers connected to both busbars specified by the given UIDs.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :return: List of unbalanced transformer UIDs.
        :rtype: list(int)
        """
        pass

    @overload
    def GetUnbalancedTransformerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUnbalancedTransformer]:
        """
        Returns a dictionary of all unbalanced transformer UIDs in the network.
        The keys are the integer UIDs and the values are the IscUnbalancedTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all unbalanced transformers.
        :rtype: dict(int,IscUnbalancedTransformer)
        """
        pass

    def GetUnbalancedTransformerUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUnbalancedTransformer]:
        """
        Returns either a dictionary of all unbalanced transformer UIDs in the network or a list of
        unbalanced transformers
        connected to the busbars specified by the given UIDs.

        If a dictionary is returned, the keys are the integer UIDs and the values are the IscUnbalancedTransformer
        instances.

        :param nFirstBusID: The UID of the first busbar.
        :type nFirstBusID: int
        :param nSecondBusID: The UID of the second busbar.
        :type nSecondBusID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: List of unbalanced transformer UIDs connected to the items specified by the given UIDs.
        :rtype: list(int)
        :return: Dictionary of all unbalanced transformers.
        :rtype: dict(int,IscUnbalancedTransformer)
        """
        pass

    def GetVoltageRegulatorUID(self, nBranchID: int) -> int:
        """
        Returns the UID of a voltage regulator at branch specified by its UID.

        :param nBranchID: The UID of the branch.
        :type nBranchID: int
        :return: The voltage regulator UID.
        :rtype: int
        """
        pass

    def GetVoltageRegulatorUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscVoltageRegulator]:
        """
        Returns a dictionary of all voltage regulator UIDs in the network.
        The keys are the integer UIDs and the values are the IscVoltageRegulator instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all voltage regulators.
        :rtype: dict(int,IscVoltageRegulator)
        """
        pass

    def GetProtectionDeviceUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscProtectionDevice]:
        """
        Returns a dictionary of all protection device UIDs in the network.
        The keys are the integer UIDs and the values are the IscProtectionDevice instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all protection devices UIDs.
        :rtype: dict(int,IscProtectionDevice)
        """
        pass

    def GetAnnotationUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscAnnotation]:
        """
        Returns a dictionary of all annotation UIDs in the network.
        The keys are the integer UIDs and the values are the IscAnnotation instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all annotation UIDs.
        :rtype: dict(int,IscAnnotation)
        """
        pass

    def GetGroupUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscGroup]:
        """
        Returns a dictionary of all group UIDs in the network.
        The keys are the integer UIDs and the values are the IscGroup instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all group UIDs.
        :rtype: dict(int,IscGroup)
        """
        pass

    def GetIntertripUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscIntertrip]:
        """
        Returns a dictionary of all intertrip UIDs in the network.
        The keys are the integer UIDs and the values are the IscIntertrip instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all intertrip UIDs.
        :rtype: dict(int,IscIntertrip)
        """
        pass

    def GetPluginUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscPlugin]:
        """
        Returns a dictionary of all Plugin UIDs in the network.
        The keys are the integer UIDs and the values are the IscIntertrip instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all Plugin UIDs.
        :rtype: dict(int,IscIntertrip)
        """
        pass

    def GetProfileUID(self, nUID: int) -> int:
        """
        Returns the integer UID of the profile for the component UID.

        :param nUID: The UID of component. nUID may be the UID of a load, generator, grid infeed or Universal Machine.
        :type nUID: int
        :return: The profile for the component UID, 0 if the component nUID does not have a profile assigned to it,
            or if nUID is not a load, generator, grid infeed or universal machine.
        :rtype: int
        """
        pass

    def GetLoadProfilePQActualUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscLoadProfilePQActual]:
        """
        Returns a dictionary of all PQ Actual Load profile UIDs in the network.
        The keys are the integer UIDs and the values are the IscLoadProfilePQActual instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all PQ Actual Load profile UIDs.
        :rtype: dict(int,IscLoadProfilePQActual)
        """
        pass

    def GetLoadProfilePQScaleUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscLoadProfilePQScale]:
        """
        Returns a dictionary of all PQ Scale Load profile UIDs in the network.
        The keys are the integer UIDs and the values are the IscLoadProfilePQScale instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all PQ Actual Load profile UIDs.
        :rtype: dict(int,IscLoadProfilePQScale)
        """
        pass

    def GetGeneratorProfilePQActualUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscGeneratorProfilePQActual]:
        """
        Returns a dictionary of all PQ Actual Generator profile UIDs in the network.
        The keys are the integer UIDs and the values are the IscGeneratorProfilePQActual instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all PQ Actual Generator profile UIDs.
        :rtype: dict(int,IscGeneratorProfilePQActual)
        """
        pass

    def GetGeneratorProfilePQScaleUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscGeneratorProfilePQScale]:
        """
        Returns a dictionary of all PQ Scale Generator profile UIDs in the network.
        The keys are the integer UIDs and the values are the IscGeneratorProfilePQScale instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all PQ Scale Generator profile UIDs.
        :rtype: dict(int,IscGeneratorProfilePQScale)
        """
        pass

    def GetUMachineProfilePQActualUIDs(self, bFetchFromSystem: bool = True) -> Dict[int, IscUMachineProfilePQActual]:
        """
        Returns a dictionary of all PQ Actual UMachine profile UIDs in the network.
        The keys are the integer UIDs and the values are the IscUMachineProfilePQActual instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps.
            If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all PQ Actual UMachine profile UIDs.
        :rtype: dict(int,IscUMachineProfilePQActual)
        """
        pass

    def CreateBusbar(self, strName: str) -> int:
        """
        Returns the UID for the newly created busbar.

        **Warning: It is up to the script to ensure that the busbar name is unique.**


        :param strName: The branch name string if required.
        :type strName: str
        :return: The UID for the newly created busbar, 0 on failure.
        :rtype: int
        """
        pass

    def CreateBusbarNoGraphics(self, strName: str):
        """
        Returns an IscBusbar object for the newly created busbar.

        **Warning: It is up to the script to ensure that the busbar name is unique.**


        :param strName: The busbar name string if required.
        :type strName: str
        :return: The IscBusbar object for the newly created busbar.
        :rtype: IscBusbar
        """
        pass

    @overload
    def CreateBranch(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created branch.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The branch name string if required.
        :type strName: str
        :return: The UID for the newly created branch, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateBranch(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscBranch object for the newly created branch.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The branch name string if required.
        :type strName: str
        :return: The IscBranch object for the newly created branch.
        :rtype: IscBranch
        """
        pass

    def CreateBranch(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscBranch object for the newly created branch.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The branch name string if required.
        :type strName: str
        :return: The UID for the newly created branch, 0 on failure.
        :rtype: int
        :return: The IscBranch object for the newly created branch.
        :rtype: IscBranch
        """
        pass

    @overload
    def CreateTransformer(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The transformer name string if required.
        :type strName: str
        :return: The UID for the newly created transformer, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscTransformer object for the newly created transformer.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The transformer name string if required.
        :type strName: str
        :return: The IscTransformer object for the newly created transformer.
        :rtype: IscTransformer
        """
        pass

    def CreateTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscTransformer object for the newly created transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The transformer name string if required.
        :type strName: str
        :return: The UID for the newly created transformer, 0 on failure.
        :rtype: int
        :return: The IscTransformer object for the newly created transformer.
        :rtype: IscTransformer
        """
        pass

    @overload
    def Create3WTransformer(self, nFromBusbarUID: int, nToBusbarUID: int, nTeritaryBusUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created 3-winding transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param nTeritaryBusUID: The "Teritary" busbar UID.
        :type nTeritaryBusUID: int
        :param strName: The 3-winding transformer name string if required.
        :type strName: str
        :return: The UID for the newly created 3-winding transformer, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def Create3WTransformer(self, pFromBusbar, pToBusbar, pTeritaryBus, strName: str):
        """
        Returns an Isc3WTransformer object for the newly created 3-winding transformer.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param pTeritaryBus: The "Teritary" busbar.
        :type pTeritaryBus: IscBusbar
        :param strName: The 3-winding transformer name string if required.
        :type strName: str
        :return: The Isc3WTransformer object for the newly created 3-winding transformer.
        :rtype: Isc3WTransformer
        """
        pass

    def Create3WTransformer(self, pFromBusbar, pToBusbar, pTeritaryBus, strName: str):
        """
        Returns the UID or an Isc3WTransformer object for the newly created 3-winding transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param nTeritaryBusUID: The "Teritary" busbar UID.
        :type nTeritaryBusUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param pTeritaryBus: The "Teritary" busbar.
        :type pTeritaryBus: IscBusbar
        :param strName: The 3-winding transformer name string if required.
        :type strName: str
        :return: The UID for the newly created 3-winding transformer, 0 on failure.
        :rtype: int
        :return: The Isc3WTransformer object for the newly created 3-winding transformer.
        :rtype: Isc3WTransformer
        """
        pass

    @overload
    def CreateLoad(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The load name string if required.
        :type strName: str
        :return: The UID for the newly created load, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateLoad(self, pAtBusbar, strName: str):
        """
        Returns an IscLoad object for the newly created load.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The load name string if required.
        :type strName: str
        :return: The IscLoad object for the newly created load.
        :rtype: IscLoad
        """
        pass

    def CreateLoad(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscLoad object for the newly created load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The load name string if required.
        :type strName: str
        :return: The UID for the newly created load, 0 on failure.
        :rtype: int
        :return: The IscLoad object for the newly created load.
        :rtype: IscLoad
        """
        pass

    @overload
    def CreateIndMachine(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created induction machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The induction machine name string if required.
        :type strName: str
        :return: The UID for the newly created induction machine, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateIndMachine(self, pAtBusbar, strName: str):
        """
        Returns an IscIndMachine object for the newly created induction machine.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The induction machine name string if required.
        :type strName: str
        :return: The IscIndMachine object for the newly created induction machine.
        :rtype: IscIndMachine
        """
        pass

    def CreateIndMachine(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscIndMachine object for the newly created induction machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The induction machine name string if required.
        :type strName: str
        :return: The UID for the newly created induction machine, 0 on failure.
        :rtype: int
        :return: The IscIndMachine object for the newly created induction machine.
        :rtype: IscIndMachine
        """
        pass

    @overload
    def CreateSynMachine(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created synchronous machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The synchronous machine name string if required.
        :type strName: str
        :return: The UID for the newly created synchronous machine, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateSynMachine(self, pAtBusbar, strName: str):
        """
        Returns an IscSynMachine object for the newly created synchronous machine.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The synchronous machine name string if required.
        :type strName: str
        :return: The IscSynMachine object for the newly created synchronous machine.
        :rtype: IscSynMachine
        """
        pass

    def CreateSynMachine(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscSynMachine object for the newly created synchronous machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The synchronous machine name string if required.
        :type strName: str
        :return: The UID for the newly created synchronous machine, 0 on failure.
        :rtype: int
        :return: The IscSynMachine object for the newly created synchronous machine.
        :rtype: IscSynMachine
        """
        pass

    @overload
    def CreateGridInfeed(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created grid infeed.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The grid infeed name string if required.
        :type strName: str
        :return: The UID for the newly created grid infeed, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateGridInfeed(self, pAtBusbar, strName: str):
        """
        Returns an IscGridInfeed object for the newly created grid infeed.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The grid infeed name string if required.
        :type strName: str
        :return: The IscGridInfeed object for the newly created grid infeed.
        :rtype: IscGridInfeed
        """
        pass

    def CreateGridInfeed(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscGridInfeed object for the newly created grid infeed.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The grid infeed name string if required.
        :type strName: str
        :return: The UID for the newly created grid infeed, 0 on failure.
        :rtype: int
        :return: The IscGridInfeed object for the newly created grid infeed.
        :rtype: IscGridInfeed
        """
        pass

    @overload
    def CreateFilter(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created filter.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The filter name string if required.
        :type strName: str
        :return: The UID for the newly created filter, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateFilter(self, pAtBusbar, strName: str):
        """
        Returns an IscFilter object for the newly created filter.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The filter name string if required.
        :type strName: str
        :return: The IscFilter object for the newly created filter.
        :rtype: IscFilter
        """
        pass

    def CreateFilter(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscFilter object for the newly created filter.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The filter name string if required.
        :type strName: str
        :return: The UID for the newly created filter, 0 on failure.
        :rtype: int
        :return: The IscFilter object for the newly created filter.
        :rtype: IscFilter
        """
        pass

    @overload
    def CreateHarmonic(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created harmonic source.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The harmonic source name string if required.
        :type strName: str
        :return: The UID for the newly created harmonic source, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateHarmonic(self, pAtBusbar, strName: str):
        """
        Returns an IscHarmonic object for the newly created harmonic source.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The harmonic source name string if required.
        :type strName: str
        :return: The IscHarmonic object for the newly created harmonic source.
        :rtype: IscHarmonic
        """
        pass

    def CreateHarmonic(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscHarmonic object for the newly created harmonic source.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The harmonic source name string if required.
        :type strName: str
        :return: The UID for the newly created harmonic source, 0 on failure.
        :rtype: int
        :return: The IscHarmonic object for the newly created harmonic source.
        :rtype: IscHarmonic
        """
        pass

    @overload
    def CreateMechSwCapacitor(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created mechanically switched capacitor.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The capacitor name string if required.
        :type strName: str
        :return: The UID for the newly created mechanically switched capacitor, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateMechSwCapacitor(self, pAtBusbar, strName: str):
        """
        Returns an IscMechSwCapacitor object for the newly created mechanically switched capacitor.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The capacitor name string if required.
        :type strName: str
        :return: The IscMechSwCapacitor object for the newly created mechanically switched capacitor.
        :rtype: IscMechSwCapacitor
        """
        pass

    def CreateMechSwCapacitor(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscMechSwCapacitor object for the newly created mechanically switched capacitor.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The capacitor name string if required.
        :type strName: str
        :return: The UID for the newly created mechanically switched capacitor, 0 on failure.
        :rtype: int
        :return: The IscMechSwCapacitor object for the newly created mechanically switched capacitor.
        :rtype: IscMechSwCapacitor
        """
        pass

    @overload
    def CreateCircuitBreaker(self, nBranchOrTxUID: int, bAtFromEnd: bool, strName: str) -> int:
        """
        Returns the UID for the newly created circuit breaker. In order to draw this component, the function
        :meth:`IscDiagram.DrawUndrawnItemsAttachedToBusbar` needs to be called before :meth:`IscDiagram.DrawLine`.

        :param nBranchOrTxUID: The UID of the branch or the transformer where the circuit breaker is located.
        :type nBranchOrTxUID: int
        :param bAtFromEnd: Adds the circuit breaker to the “From” end of the component, if True.
        :type bAtFromEnd: bool
        :param strName: The circuit breaker name string if required.
        :type strName: str
        :return: The UID for the newly created circuit breaker, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateCircuitBreaker(self, pBranchOrTx, bAtFromEnd: bool, strName: str):
        """
        Returns an IscCircuitBreaker object for the newly created circuit breaker. In order to draw this component, the
        function :meth:`IscDiagram.DrawUndrawnItemsAttachedToBusbar` needs to be called before :meth:`IscDiagram.DrawLine`.

        :param pBranchOrTx: The IscBranch or IscTransformer object of the branch or transformer where the circuit breaker is located.
        :type pBranchOrTx: IscBranch or IscTransformer
        :param bAtFromEnd: Adds the circuit breaker to the “From” end of the component, if True.
        :type bAtFromEnd: bool
        :param strName: The circuit breaker name string if required.
        :type strName: str
        :return: The IscCircuitBreaker object for the newly created circuit breaker.
        :rtype: IscCircuitBreaker
        """
        pass

    def CreateCircuitBreaker(self, pBranchOrTx, bAtFromEnd: bool, strName: str):
        """
        Returns the UID or an IscCircuitBreaker object for the newly created circuit breaker. In order to draw this
        component, the function :meth:`IscDiagram.DrawUndrawnItemsAttachedToBusbar` needs to be called before
        :meth:`IscDiagram.DrawLine`.

        :param nBranchOrTxUID: The UID of the branch or the transformer where the circuit breaker is located.
        :type nBranchOrTxUID: int
        :param pBranchOrTx: The IscBranch or IscTransformer object of the branch or transformer where the circuit breaker is located.
        :type pBranchOrTx: IscBranch or IscTransformer
        :param bAtFromEnd: Adds the circuit breaker to the “From” end of the component, if True.
        :type bAtFromEnd: bool
        :param strName: The circuit breaker name string if required.
        :type strName: str
        :return: The UID for the newly created circuit breaker, 0 on failure.
        :rtype: int
        :return: The IscCircuitBreaker object for the newly created circuit breaker.
        :rtype: IscCircuitBreaker
        """
        pass

    @overload
    def CreateStaticVC(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created static VAr compensator.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The static VAr compensator name string if required.
        :type strName: str
        :return: The UID for the newly created static VAr compensator, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateStaticVC(self, pAtBusbar, strName: str):
        """
        Returns an IscStaticVC object for the newly created static VAr compensator.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The static VAr compensator name string if required.
        :type strName: str
        :return: The IscStaticVC object for the newly created static VAr compensator.
        :rtype: IscStaticVC
        """
        pass

    def CreateStaticVC(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscStaticVC object for the newly created static VAr compensator.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The static VAr compensator name string if required.
        :type strName: str
        :return: The UID for the newly created static VAr compensator, 0 on failure.
        :rtype: int
        :return: The IscStaticVC object for the newly created static VAr compensator.
        :rtype: IscStaticVC
        """
        pass

    @overload
    def CreateUMachine(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created universal machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The universal machine name string if required.
        :type strName: str
        :return: The UID for the newly created universal machine, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateUMachine(self, pAtBusbar, strName: str):
        """
        Returns an IscUMachine object for the newly created universal machine.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The universal machine name string if required.
        :type strName: str
        :return: The IscUMachine object for the newly created universal machine.
        :rtype: IscUMachine
        """
        pass

    def CreateUMachine(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscUMachine object for the newly created universal machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The universal machine name string if required.
        :type strName: str
        :return: The UID for the newly created universal machine, 0 on failure.
        :rtype: int
        :return: The IscUMachine object for the newly created universal machine.
        :rtype: IscUMachine
        """
        pass

    @overload
    def CreateBattery(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created battery.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The battery name string if required.
        :type strName: str
        :return: The UID for the newly created battery, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateBattery(self, pAtBusbar, strName: str):
        """
        Returns an IscBattery object for the newly created battery.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The battery name string if required.
        :type strName: str
        :return: The IscBattery object for the newly created battery.
        :rtype: IscBattery
        """
        pass

    def CreateBattery(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscBattery object for the newly created battery.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The battery name string if required.
        :type strName: str
        :return: The UID for the newly created battery, 0 on failure.
        :rtype: int
        :return: The IscBattery object for the newly created battery.
        :rtype: IscBattery
        """
        pass

    @overload
    def CreateDCMachine(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created DC machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The DC machine name string if required.
        :type strName: str
        :return: The UID for the newly created DC machine, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateDCMachine(self, pAtBusbar, strName: str):
        """
        Returns an IscDCMachine object for the newly created DC machine.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The DC machine name string if required.
        :type strName: str
        :return: The IscDCMachine object for the newly created DC machine.
        :rtype: IscDCMachine
        """
        pass

    def CreateDCMachine(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscDCMachine object for the newly created DC machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The DC machine name string if required.
        :type strName: str
        :return: The UID for the newly created DC machine, 0 on failure.
        :rtype: int
        :return: The IscDCMachine object for the newly created DC machine.
        :rtype: IscDCMachine
        """
        pass

    @overload
    def CreateConverter(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created AC/DC converter.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The AC/DC converter name string if required.
        :type strName: str
        :return: The UID for the newly created AC/DC converter, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateConverter(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscConverter object for the newly created AC/DC converter.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The AC/DC converter name string if required.
        :type strName: str
        :return: The IscConverter object for the newly created AC/DC converter.
        :rtype: IscConverter
        """
        pass

    def CreateConverter(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscConverter object for the newly created AC/DC converter.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The AC/DC converter name string if required.
        :type strName: str
        :return: The UID for the newly created AC/DC converter, 0 on failure.
        :rtype: int
        :return: The IscConverter object for the newly created AC/DC converter.
        :rtype: IscConverter
        """
        pass

    @overload
    def CreateChopper(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created chopper.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The DC/DC converter name string if required.
        :type strName: str
        :return: The UID for the newly created chopper, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateChopper(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscChopper object for the newly created chopper.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The DC/DC converter name string if required.
        :type strName: str
        :return: The IscChopper object for the newly created chopper.
        :rtype: IscChopper
        """
        pass

    def CreateChopper(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscChopper object for the newly created chopper.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The DC/DC converter name string if required.
        :type strName: str
        :return: The UID for the newly created chopper, 0 on failure.
        :rtype: int
        :return: The IscChopper object for the newly created chopper.
        :rtype: IscChopper
        """
        pass

    @overload
    def CreateMGSet(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created motor/generator set.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The motor/generator set name string if required.
        :type strName: str
        :return: The UID for the newly created motor/generator set, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateMGSet(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscMGSet object for the newly created motor/generator set.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The motor/generator set name string if required.
        :type strName: str
        :return: The IscMGSet object for the newly created motor/generator set.
        :rtype: IscMGSet
        """
        pass

    def CreateMGSet(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscMGSet object for the newly created motor/generator set.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The motor/generator set name string if required.
        :type strName: str
        :return: The UID for the newly created motor/generator set, 0 on failure.
        :rtype: int
        :return: The IscMGSet object for the newly created motor/generator set.
        :rtype: IscMGSet
        """
        pass

    @overload
    def CreateVoltageRegulator(self, nBranchUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created voltage regulator.

        :param nBranchUID: The branch the voltage regulator is upon
        :type nBranchUID: int
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The UID for the newly created voltage regulator, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateVoltageRegulator(self, pBranch, strName: str):
        """
        Returns an IscVoltageRegulator object for the newly created voltage regulator.

        :param pBranch: The branch the voltage regulator is upon
        :type pBranch: IscBranch
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The IscVoltageRegulator object for the newly created voltage regulator.
        :rtype: IscVoltageRegulator
        """
        pass

    def CreateVoltageRegulator(self, pBranch, strName: str):
        """
        Returns the UID or an IscVoltageRegulator object for the newly created voltage regulator.

        :param nBranchUID: The branch the voltage regulator is upon
        :type nBranchUID: int
        :param pBranch: The branch the voltage regulator is upon
        :type pBranch: IscBranch
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The UID for the newly created voltage regulator, 0 on failure.
        :rtype: int
        :return: The IscVoltageRegulator object for the newly created voltage regulator.
        :rtype: IscVoltageRegulator
        """
        pass

    @overload
    def CreateUnbalancedLoad(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created unbalanced load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The unbalanced load name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced load, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateUnbalancedLoad(self, pAtBusbar, strName: str):
        """
        Returns an IscUnbalancedLoad object for the newly created unbalanced load.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The unbalanced load name string if required.
        :type strName: str
        :return: The IscUnbalancedLoad object for the newly created unbalanced load.
        :rtype: IscUnbalancedLoad
        """
        pass

    def CreateUnbalancedLoad(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscUnbalancedLoad object for the newly created unbalanced load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The unbalanced load name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced load, 0 on failure.
        :rtype: int
        :return: The IscUnbalancedLoad object for the newly created unbalanced load.
        :rtype: IscUnbalancedLoad
        """
        pass

    @overload
    def CreateUnbalancedLine(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created unbalanced line.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The unbalanced line name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced line, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateUnbalancedLine(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscUnbalancedLine object for the newly created unbalanced line.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced line name string if required.
        :type strName: str
        :return: The IscUnbalancedLine object for the newly created unbalanced line.
        :rtype: IscUnbalancedLine
        """
        pass

    def CreateUnbalancedLine(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscUnbalancedLine object for the newly created unbalanced line.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced line name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced line, 0 on failure.
        :rtype: int
        :return: The IscUnbalancedLine object for the newly created unbalanced line.
        :rtype: IscUnbalancedLine
        """
        pass

    @overload
    def CreateUnbalancedTransformer(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created unbalanced transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The unbalanced transformer name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced transformer, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateUnbalancedTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscUnbalancedTransformer object for the newly created unbalanced transformer.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced transformer name string if required.
        :type strName: str
        :return: The IscUnbalancedTransformer object for the newly created unbalanced transformer.
        :rtype: IscUnbalancedTransformer
        """
        pass

    def CreateUnbalancedTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscUnbalancedTransformer object for the newly created unbalanced transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced transformer name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced transformer, 0 on failure.
        :rtype: int
        :return: The IscUnbalancedTransformer object for the newly created unbalanced transformer.
        :rtype: IscUnbalancedTransformer
        """
        pass

    def CreateGroup(self, strName: str, nGroupType: int) -> int:
        """
        Create a new empty group of components and returns the group UID.
        Group types:

            - 0 = No group type
            - 1 = Area type group (contains all busbars in an area)
            - 2 = Mixed item group
            - 3 = Load scaling group
            - 4 = Load transfer group
            - 5 = Protection device group

        :param strName: The group name.
        :type strName: str
        :param nGroupType: The group type.
        :type nGroupType: int
        :return: The group UID, 0 on failure.
        :rtype: int
        """
        pass

    def CreateGroupNoGraphics(self, strName: str, nGroupType: int):
        """
        Create a new empty group of components and returns the group object.
        Group types:

            - 0 = No group type
            - 1 = Area type group (contains all busbars in an area)
            - 2 = Mixed item group
            - 3 = Load scaling group
            - 4 = Load transfer group
            - 5 = Protection device group

        :param strName: The group name.
        :type strName: str
        :param nGroupType: The group type.
        :type nGroupType: int
        :return: The IscGroup object.
        :rtype: IscGroup
        """
        pass

    def CreateIntertrip(self, strName: str) -> int:
        """
        Create a new empty intertrip and returns the intertrip UID.
        Note the new intertrip name must be **unique** or no new intertrip will be created.

        :param strName: The intertrip name.
        :type strName: str
        :return: The intertrip UID, 0 on failure.
        :rtype: int
        """
        pass

    def CreateIntertripNoGraphics(self, strName: str):
        """
        Create a new empty intertrip and returns the IscIntertrip object.
        Note the new intertrip name must be **unique** or no new intertrip will be created.

        :param strName: The intertrip name.
        :type strName: str
        :return: The IscIntertrip object or None on failure.
        :rtype: IscIntertrip
        """
        pass

    @overload
    def CreatePlugin(self, nCompUID: int, sPluginName: str, sName: str) -> int:
        """
        Returns the UID for the newly created plugin.
        A different plugin UID is required for each component with a plugin,
        therefore this function should be used every time a plugin is assigned to a component,
        even if the same type of plugin is being assigned.

        :param nCompUID: The UID of the component to which the plugin is to be assigned.
        :type nCompUID: int
        :param sPluginName: The name of the plugin itself, for example ‘Constant Current Load’.
        :type sPluginName: str
        :param sName: The user defined plugin name or empty string.
        :type sName: str
        :return: The plugin UID, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreatePlugin(self, pComponent, sPluginName: str, sName: str) -> int:
        """
        Returns the IscPlugin object for the newly created plugin.
        A different plugin UID is required for each component with a plugin,
        therefore this function should be used every time a plugin is assigned to a component,
        even if the same type of plugin is being assigned.

        :param pComponent: The component object (i.e., IscBranch, IscUMachine) to which the plugin is to be assigned.
        :type pComponent: IscNetComponent
        :param sPluginName: The name of the plugin itself, for example ‘Constant Current Load’.
        :type sPluginName: str
        :param sName: The user defined plugin name or empty string.
        :type sName: str
        :return: The IscPlugin object for the newly created plugin or None on failure.
        :rtype: IscPlugin
        """
        pass

    def CreatePlugin(self, pComponent, sPluginName: str, sName: str) -> int:
        """
        Returns the UID or the IscPlugin object for the newly created plugin.
        A different plugin UID is required for each component with a plugin,
        therefore this function should be used every time a plugin is assigned to a component,
        even if the same type of plugin is being assigned.

        :param nCompUID: The UID of the component to which the plugin is to be assigned.
        :type nCompUID: int
        :param pComponent: The component object (i.e., IscBranch, IscUMachine) to which the plugin is to be assigned.
        :type pComponent: IscNetComponent
        :param sPluginName: The name of the plugin itself, for example ‘Constant Current Load’.
        :type sPluginName: str
        :param sName: The user defined plugin name or empty string.
        :type sName: str
        :return: The IscPlugin object for the newly created plugin or None on failure.
        :rtype: IscPlugin
        :return: The plugin UID, 0 on failure.
        :rtype: int
        """
        pass

    def ReverseBranch(self, nBranchUID: int) -> bool:
        """
        Reverses the connection of branch or transformer supplied.

        :param nBranchUID: the branch or transformer UID.
        :type nBranchUID: int
        :return: denotes if the branch has been successfully reversed.
        :rtype: bool
        """
        pass

    def SplitBranch(self, nBranchUID: int, nSection: int, dDistanceRatio: float, strNewBusName: str) -> int:
        """
        Splits a branch or transformer into two sections connected by a new busbar.

        :param nBranchUID: The branch UID.
        :type nBranchUID: int
        :param nSection: Specifies which section of a multi-section branch is split.
            For branches with only one section then nSection should be set to 0.
        :type nSection: int
        :param dDistanceRatio: Specifies how the branch impedances are divided between the new branches.
            A value of 0.0 sets the split position to be at the “From” end whilst a value of 1.0 specifies the “To” end.
            Values between 0.0 and 1.0 split the branch in proportion.
            For multi-section branches dRatio splits the section identified by nSection.
        :type dDistanceRatio: float
        :param strName: The name of the new busbar.
        :type strName: str
        :return: The UID of the new branch. If it is not greater than 0, the branch has not been split.
            This is because there is a protection device or controller on the branch or the branch is connected to an
            embedded diagram.
        :rtype: int
        """
        pass

    def ChangeConnection(self, nUID: int, nOldBusUID: int, nNewBusUID: int) -> bool:
        """
        Changes the connection busbar for the component specified by nUID. nOldBusUID must identify a busbar currently
        connected to the component, and nNewBusUID but identify an existing busbar which is not already connected to
        the component.

        :param nUID: The UID of the component with the connection to be changed.
        :type nUID: int
        :param nOldBusUID: The UID of the connection busbar to be disconnected.
        :type nOldBusUID: int
        :param nNewBusUID: The UID of the new connection busbar to be connected.
        :type nNewBusUID: int
        :return: denotes if the connection change has been successful.
        :rtype: bool
        """
        pass

    def DeleteBusbar(self, pBusbar) -> bool:
        """
        Deletes a busbar by passing the IscBusbar object for deletion.

        :param pBusbar: The IscBusbar object for deletion.
        :type pBusbar: IscBusbar
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteBranch(self, pBranch) -> bool:
        """
        Deletes a branch by passing the IscBranch object for deletion and all the circuit breakers attached to it.

        :param pBranch: The IscBranch object for deletion.
        :type pBranch: IscBranch
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteTransformer(self, pTransformer) -> bool:
        """
        Deletes a transformer by passing the IscTransformer object for deletion.

        :param pTransformer: The IscTransformer object for deletion.
        :type pTransformer: IscTransformer
        :return: True if successful.
        :rtype: bool
        """
        pass

    def Delete3WTransformer(self, p3WTransformer) -> bool:
        """
        Deletes a 3-winding transformer by passing the Isc3WTransformer object for deletion.

        :param p3WTransformer: The Isc3WTransformer object for deletion.
        :type p3WTransformer: Isc3WTransformer
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteLoad(self, pLoad) -> bool:
        """
        Deletes a load by passing the IscLoad object for deletion.

        :param pLoad: The IscLoad object for deletion.
        :type pLoad: IscLoad
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteSynMachine(self, pSynMachine) -> bool:
        """
        Deletes a synchronous machine by passing the IscSynMachine object for deletion.

        :param pSynMachine: The IscSynMachine object for deletion.
        :type pSynMachine: IscSynMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteIndMachine(self, pIndMachine) -> bool:
        """
        Deletes an induction machine by passing the IscIndMachine object for deletion.

        :param pIndMachine: The IscIndMachine object for deletion.
        :type pIndMachine: IscIndMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGridInfeed(self, pGridInfeed) -> bool:
        """
        Deletes a grid infeed by passing the IscSynMachine object for deletion.

        :param pGridInfeed: The IscSynMachine object for deletion.
        :type pGridInfeed: IscSynMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteFilter(self, pFilter) -> bool:
        """
        Deletes a filter by passing the IscFilter object for deletion.

        :param pFilter: The IscFilter object for deletion.
        :type pFilter: IscFilter
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteMechSwCapacitor(self, pMechSwCapacitor) -> bool:
        """
        Deletes a mechanical switched capacitor by passing the IscMechSwCapacitor object for deletion.

        :param pMechSwCapacitor: The IscMechSwCapacitor object for deletion.
        :type pMechSwCapacitor: IscMechSwCapacitor
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteStaticVC(self, pStaticVC) -> bool:
        """
        Deletes a synchronous machine by passing the IscStaticVC object for deletion.

        :param pStaticVC: The IscStaticVC object for deletion.
        :type pStaticVC: IscStaticVC
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUMachine(self, pUMachine) -> bool:
        """
        Deletes an universal machine by passing the IscUMachine object for deletion.

        :param pUMachine: The IscUMachine object for deletion.
        :type pUMachine: IscUMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteHarmonic(self, pHarmonic) -> bool:
        """
        Deletes a harmonic source by passing the IscHarmonic object for deletion.

        :param pHarmonic: The IscHarmonic object for deletion.
        :type pHarmonic: IscHarmonic
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteCircuitBreaker(self, pCircuitBreaker) -> bool:
        """
        Deletes a circuit breaker by passing the IscCircuitBreaker object for deletion.

        :param pCircuitBreaker: The IscCircuitBreaker object for deletion.
        :type pCircuitBreaker: IscCircuitBreaker
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteBattery(self, pBattery) -> bool:
        """
        Deletes a battery by passing the IscBattery object for deletion.

        :param pBattery: The IscBattery object for deletion.
        :type pBattery: IscBattery
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteDCMachine(self, pDCMachine) -> bool:
        """
        Deletes a DC machine by passing the IscDCMachine object for deletion.

        :param pDCMachine: The IscDCMachine object for deletion.
        :type pDCMachine: IscDCMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteConverter(self, pConverter) -> bool:
        """
        Deletes a converter by passing the IscConverter object for deletion.

        :param pConverter: The IscConverter object for deletion.
        :type pConverter: IscConverter
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteChopper(self, pChopper) -> bool:
        """
        Deletes a chopper by passing the IscChopper object for deletion.

        :param pChopper: The IscChopper object for deletion.
        :type pChopper: IscChopper
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteMGSet(self, pMGSet) -> bool:
        """
        Deletes a motor/generator set by passing the IscMGSet object for deletion.

        :param pMGSet: The IscMGSet object for deletion.
        :type pMGSet: IscMGSet
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteVoltageRegulator(self, pVoltageRegulator) -> bool:
        """
        Deletes a voltage regulator by passing the IscVoltageRegulator object for deletion.

        :param pVoltageRegulator: The IscVoltageRegulator object for deletion.
        :type pVoltageRegulator: IscVoltageRegulator
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteAnnotation(self, pAnnotation) -> bool:
        """
        Deletes an annotation by passing the IscAnnotation object for deletion.

        :param pAnnotation: The IscAnnotation object for deletion.
        :type pAnnotation: IscAnnotation
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUnbalancedLoad(self, pUnbalancedLoad) -> bool:
        """
        Deletes an unbalanced load by passing the IscUnbalancedLoad object for deletion.

        :param pUnbalancedLoad: The IscUnbalancedLoad object for deletion.
        :type pUnbalancedLoad: IscUnbalancedLoad
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUnbalancedLine(self, pUnbalancedLine) -> bool:
        """
        Deletes an unbalanced line by passing the IscUnbalancedLine object for deletion.

        :param pUnbalancedLine: The IscUnbalancedLine object for deletion.
        :type pUnbalancedLine: IscUnbalancedLine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUnbalancedTransformer(self, pUnbalancedTransformer) -> bool:
        """
        Deletes an unbalanced transformer by passing the IscUnbalancedTransformer object for deletion.

        :param pUnbalancedTransformer: The IscUnbalancedTransformer object for deletion.
        :type pUnbalancedTransformer: IscUnbalancedTransformer
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGroup(self, pGroup) -> bool:
        """
        Deletes a group by passing the IscGroup object for deletion.

        :param pGroup: The IscGroup object for deletion.
        :type pGroup: IscGroup
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteIntertrip(self, pIntertrip) -> bool:
        """
        Deletes a group by passing the IscIntertrip object for deletion.

        :param pIntertrip: The IscIntertrip object for deletion.
        :type pIntertrip: IscIntertrip
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeletePlugin(self, pPlugin) -> bool:
        """
        Deletes a plugin by passing the IscPlugin object for deletion.

        :param pPlugin: The IscPlugin object for deletion.
        :type pPlugin: IscPlugin
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteAllItems(self):
        """
        Delete all items in the network. This will delete all the components, groups, automations, contingencies and
        intertrips.

        It will delete all versions and the entire undo history.

        Analysis settings, network settings and diagrams will be unchanged.
        """
        pass

    def DeleteBusBarSlack(self, strBusbar: str) -> bool:
        """
        Deletes a slack busbar from the network busbar slack list.
        **It does not delete the busbar in the same way as DeleteBusbar(pBusbar)**,
        instead it uses the busbar name for deletion.

        :param strBusbar: The slack busbar name.
        :type strBusbar: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetRatingIndex(self, strName: str) -> int:
        """
        Returns an integer representing the rating set for a specified name.

        :param strName: The specified name.
        :type strName: str
        :return: The rating set index, or -1 if no rating set with that name exists in the network.
        :rtype: int
        """
        pass

    def GetBranchRatingName(self, nIndex: int) -> str:
        """
        Returns the name representing the rating set identified by an index.

        :param nIndex: The specified index.
        :type nIndex: int
        :return: The rating set name, or empty set if no rating set with that index exists in the network.
        :rtype: str
        """
        pass

    def SetRatingName(self, nIndex: int, strName: str) -> None:
        """
        Sets the name of the rating set identified by an index to specified name.
        If the rating set name does not exist it will be created by the function.

        :param nIndex: The specified index.
        :type nIndex: int
        :param strName: The specified name.
        :type strName: str
        """
        pass

    def SetLimitsForOverloadChecks(self, dMaxVoltsPU: float, dMinVoltsPU: float, nRatingIndex: int, strDiagram: str)\
            -> None:
        """
        Sets the limits for overload checking on diagrams.

        :param dMaxVoltsPU: The maximum voltage in per unit.
        :type dMaxVoltsPU: float
        :param dMinVoltsPU: The minimum voltage in per unit.
        :type dMinVoltsPU: float
        :param nRatingIndex: The index of the rating set to be used for the thermal overload checks.
        :type nRatingIndex: int
        :param strDiagram: The name of the diagram that these limits will be applied to.
        :type strDiagram: str
        """
        pass

    def CreateLoadProfilePQActual(self, strName: str) -> int:
        """
        Returns the load profile UID representing a load profile which uses actual MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The load profile UID, 0 if a load profile cannot be created.
        :rtype: int
        """
        pass

    def CreateLoadProfilePQActualNoGraphics(self, strName: str):
        """
        Returns an IscLoadProfilePQActual object representing a load profile
        which uses actual MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQActual object.
        :rtype: IscLoadProfilePQActual
        """
        pass

    def CreateGeneratorProfilePQActual(self, strName: str) -> int:
        """
        Returns the generator profile UID representing a generator profile which uses actual MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The generator profile UID, 0 if a generator profile cannot be created.
        :rtype: int
        """
        pass

    def CreateGeneratorProfilePQActualNoGraphics(self, strName: str):
        """
        Returns an IscGeneratorProfilePQActual object representing a generator profile
        which uses actual MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQActual object.
        :rtype: IscGeneratorProfilePQActual
        """
        pass

    def CreateUMachineProfilePQActual(self, strName: str) -> int:
        """
        Returns the universal machine profile UID representing a universal machine profile which uses actual
        MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The universal machine profile UID, 0 if a universal machine profile cannot be created.
        :rtype: int
        """
        pass

    def CreateUMachineProfilePQActualNoGraphics(self, strName: str):
        """
        Returns an IscUMachineProfilePQActual object representing a universal machine profile
        which uses actual MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscUMachineProfilePQActual object.
        :rtype: IscUMachineProfilePQActual
        """
        pass

    def CreateLoadProfilePQScale(self, strName: str) -> int:
        """
        Returns the load profile UID representing a load which scales the existing MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The load profile UID, 0 if a generator profile cannot be created.
        :rtype: int
        """
        pass

    def CreateLoadProfilePQScaleNoGraphics(self, strName: str):
        """
        Returns an IscLoadProfilePQScale object representing a load profile
        which scales the existing MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQScale object.
        :rtype: IscLoadProfilePQScale
        """
        pass

    def CreateGeneratorProfilePQScale(self, strName: str) -> int:
        """
        Returns the generator profile UID representing a generator which scales the existing MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The generator profile UID, 0 if a generator profile cannot be created.
        :rtype: int
        """
        pass

    def CreateGeneratorProfilePQScaleNoGraphics(self, strName: str):
        """
        Returns an IscGeneratorProfilePQScale object representing a generator profile
        which scales the existing MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQScale object.
        :rtype: IscGeneratorProfilePQScale
        """
        pass

    def GetLoadProfilePQActuals(self):
        """
        Returns a dictionary of all IscLoadProfilePQActual objects in the network for actual load profiles.
        The keys are the profile UIDs and the values are the IscLoadProfilePQActual objects.

        :return: A dictionary of all IscLoadProfilePQActual objects in the network for actual load profiles.
        :rtype: dict(int,IscIscLoadProfilePQActual)
        """
        pass

    def GetGeneratorProfilePQActuals(self):
        """
        Returns a dictionary of all IscGeneratorProfilePQActual objects in the network for actual generator profiles.
        The keys are the profile UIDs and the values are the IscGeneratorProfilePQActual objects.

        :return: A dictionary of all IscGeneratorProfilePQActual objects in the network for actual generator profiles.
        :rtype: dict(int,IscGeneratorProfilePQActual)
        """
        pass

    def GetUMachineProfilePQActuals(self):
        """
        Returns a dictionary of all IscUMachineProfilePQActual objects in the network for actual universal machine
        profiles.
        The keys are the profile UIDs and the values are the IscUMachineProfilePQActual objects.

        :return: A dictionary of all IscUMachineProfilePQActual objects in the network for actual universal machine profiles.
        :rtype: dict(int,IscUMachineProfilePQActual)
        """
        pass

    def GetLoadProfilePQScales(self):
        """
        Returns a dictionary of all IscLoadProfilePQScale objects in the network for scaled load profiles.
        The keys are the profile UIDs and the values are the IscLoadProfilePQScale objects.

        :return: A dictionary of all IscLoadProfilePQScale objects in the network for scaled load profiles.
        :rtype: dict(int,IscLoadProfilePQScale)
        """
        pass

    def GetGeneratorProfilePQScales(self):
        """
        Returns a dictionary of all IscGeneratorProfilePQScale objects in the network for scaled generator profiles.
        The keys are the profile UIDs and the values are the IscGeneratorProfilePQScale objects.

        :return: A dictionary of all IscGeneratorProfilePQScale objects in the network for scaled generator profiles.
        :rtype: dict(int,IscGeneratorProfilePQScale)
        """
        pass

    @overload
    def GetLoadProfilePQActual(self, nUID: int):
        """
        Returns an IscLoadProfilePQActual object for the actual MW/MVAr load profile with a specified UID.

        :param nUID: The profile UID.
        :type nUID: int
        :return: IscLoadProfilePQActual object for the actual MW/MVAr load profile.
            Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQActual
        """
        pass

    @overload
    def GetLoadProfilePQActual(self, strPythonName: str):
        """
        Returns an IscLoadProfilePQActual object for the actual MW/MVAr load profile with a specified python name.

        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscLoadProfilePQActual object for the actual MW/MVAr load profile.
            Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQActual
        """
        pass

    def GetLoadProfilePQActual(self, strPythonName: str):
        """
        Returns an IscLoadProfilePQActual object for the actual MW/MVAr load profile with a specified UID or python name.

        :param nUID: The profile UID.
        :type nUID: int
        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscLoadProfilePQActual object for the actual MW/MVAr load profile.
            Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQActual
        """
        pass

    @overload
    def GetGeneratorProfilePQActual(self, nUID: int):
        """
        Returns an IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile with a specified UID.

        :param nUID: The profile UID.
        :type nUID: int
        :return: IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile.
            Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQActual
        """
        pass

    @overload
    def GetGeneratorProfilePQActual(self, strPythonName: str):
        """
        Returns an IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile with a specified python name.

        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile.
            Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQActual
        """
        pass

    def GetGeneratorProfilePQActual(self, strPythonName: str):
        """
        Returns an IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile with a specified UID
        or python name.

        :param nUID: The profile UID.
        :type nUID: int
        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile.
            Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQActual
        """
        pass

    @overload
    def GetUMachineProfilePQActual(self, nUID: int):
        """
        Returns an IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile with
        a specified UID.

        :param nUID: The profile UID.
        :type nUID: int
        :return: IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile.
            Returns None if a profile cannot be found.
        :rtype: IscUMachineProfilePQActual
        """
        pass

    @overload
    def GetUMachineProfilePQActual(self, strPythonName: str):
        """
        Returns an IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile with
        a specified python name.

        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile.
            Returns None if a profile cannot be found.
        :rtype: IscUMachineProfilePQActual
        """
        pass

    def GetUMachineProfilePQActual(self, strPythonName: str):
        """
        Returns an IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile with
        a specified UID or python name.

        :param nUID: The profile UID.
        :type nUID: int
        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile.
            Returns None if a profile cannot be found.
        :rtype: IscUMachineProfilePQActual
        """
        pass

    @overload
    def GetLoadProfilePQScale(self, nUID: int):
        """
        Returns an IscLoadProfilePQScale object for the scaled MW/MVAr load profile with a specified UID.

        :param nUID: The profile UID.
        :type nUID: int
        :return: IscLoadProfilePQScale object for the scaled MW/MVAr load profile.
            Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQScale
        """
        pass

    @overload
    def GetLoadProfilePQScale(self, strPythonName: str):
        """
        Returns an IscLoadProfilePQScale object for the scaled MW/MVAr load profile with a specified python name.

        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscLoadProfilePQScale object for the scaled MW/MVAr load profile.
            Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQScale
        """
        pass

    def GetLoadProfilePQScale(self, strPythonName: str):
        """
        Returns an IscLoadProfilePQScale object for the scaled MW/MVAr load profile with a specified UID or python name.

        :param nUID: The profile UID.
        :type nUID: int
        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscLoadProfilePQScale object for the scaled MW/MVAr load profile.
            Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQScale
        """
        pass

    @overload
    def GetGeneratorProfilePQScale(self, nUID: int):
        """
        Returns an IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile with a specified UID.

        :param nUID: The profile UID.
        :type nUID: int
        :return: IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile.
            Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQScale
        """
        pass

    @overload
    def GetGeneratorProfilePQScale(self, strPythonName: str):
        """
        Returns an IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile with a specified
        python name.

        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile.
            Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQScale
        """
        pass

    def GetGeneratorProfilePQScale(self, strPythonName: str):
        """
        Returns an IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile with a specified UID or
        python name.

        :param strPythonName: The profile name.
        :type strPythonName: str
        :return: IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile.
            Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQScale
        """
        pass

    def DeleteLoadProfilePQActual(self, pProfile) -> bool:
        """
        Deletes the actual load profile from the network by passing an IscLoadProfilePQActual object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscLoadProfilePQActual
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteLoadProfilePQScale(self, pProfile) -> bool:
        """
        Deletes the scaled load profile from the network by passing an IscLoadProfilePQScale object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscLoadProfilePQScale
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGeneratorProfilePQActual(self, pProfile) -> bool:
        """
        Deletes the actual generator profile from the network by passing an IscGeneratorProfilePQActual object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscGeneratorProfilePQActual
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGeneratorProfilePQScale(self, pProfile) -> bool:
        """
        Deletes the scaled generator profile from the network by passing an IscGeneratorProfilePQScale object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscGeneratorProfilePQScale
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUMachineProfilePQActual(self, pProfile) -> bool:
        """
        Deletes the actual universal machine profile from the network by passing an IscUMachineProfilePQActual object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscUMachineProfilePQActual
        :return: True if successful.
        :rtype: bool
        """
        pass

    def RunProfile(self) -> int:
        """
        Runs the profile study. Returns the calculation UID of the study which has just been run.

        :return: The calculation UID of the study which has been run.
        :rtype: int
        """
        pass

    @overload
    def GetDiagram(self, strName: str):
        """
        Returns an IscDiagram instance for the diagram with given name contained in the network.

        :param strName: The name of the diagram.
        :type strName: str
        :return: The diagram of the IPSA network.
        :rtype: IscDiagram
        """
        pass

    @overload
    def GetDiagram(self, nUID: int):
        """
        Returns an IscDiagram instance for the diagram with ID nUID contained in the network.

        :param nUID: The diagram ID.
        :type nUID: int
        :return: The diagram of the Ipsa network.
        :rtype: IscDiagram
        """
        pass

    def GetDiagram(self, strName: str):
        """
        Returns an IscDiagram instance for the diagram with name strName or ID nUID contained in the network.

        :param strName: The name of the diagram.
        :type strName: str
        :param nUID: The diagram ID.
        :type nUID: int
        :return: The diagram of the Ipsa network.
        :rtype: IscDiagram
        """
        pass

    def GetAllDiagrams(self):
        """
        Returns a list of IscDiagram objects for the network.

        :return: List of IscDiagram objects for the network.
        :rtype: list(IscDiagram)
        """
        pass

    def GetAllDiagramsNames(self) -> List[str]:
        """
        Returns a list of the names of the diagrams for the network.

        :return: The names of the diagrams for the network.
        :rtype: list(str)
        """
        pass

    def GetAllDiagramsUIDs(self, bFetchFromSystem: bool = True):
        """
        Returns a dictionary of diagrams for the network. The keys are the Diagram IDs.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the IscDiagram data maps.
            If set to False, it only rebuilds if IscDiagrams have been added/deleted since the last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of diagrams for the network.
        :rtype: dict(int, IscDiagram)
        """
        pass

    @overload
    def AddDiagram(self,
            strSceneTitle: str,
            bIsDiagramSingleLine: bool,
            dGeoSceneScale: float,
            nSceneMeasurementUnit: int):
        """
        Creates a new diagram for the network based on the supplied parameters.
        Returns an IscDiagram object corresponding to the new diagram.
        Note that this function causes IPSA to rebuild the IscDiagram data maps.

        :param strSceneTitle: The name of the new diagram.
        :type strSceneTitle: str
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :return: The IscDiagram object for the newly created diagram.
        :rtype: IscDiagram
        """
        pass

    @overload
    def AddDiagram(self,
            strSceneTitle: str,
            bIsDiagramSingleLine: bool,
            dGeoSceneScale: float,
            nSceneMeasurementUnit: int,
            nCopyWhat: int,
            pDiagramToCopy: IscDiagram):
        """
        Creates a new diagram for the network based on the supplied parameters.
        Returns an IscDiagram object corresponding to the new diagram.
        Note that this function causes IPSA to rebuild the IscDiagram data maps.
        pDiagramToCopy provides a reference diagram, which this new diagram is based upon.

        :param strSceneTitle: The name of the new diagram.
        :type strSceneTitle: str
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :param nCopyWhat: Determines what is copied from the provided diagram pDiagramToCopy

            * 0 if copy nothing
            * 1 if copy the busbars as they are
            * 2 if copy the busbars as junctions
            * 3 if copy everything
        :type nCopyWhat: int
        :param pDiagramToCopy: The IscDiagram object that any components may be copied from.
        :type pDiagramToCopy: IscDiagram
        :return: The IscDiagram object for the newly created diagram.
        :rtype: IscDiagram
        """
        pass

    def AddDiagram(self,
            strSceneTitle: str,
            bIsDiagramSingleLine: bool,
            dGeoSceneScale: float,
            nSceneMeasurementUnit: int,
            nCopyWhat: int,
            pDiagramToCopy: IscDiagram):
        """
        Creates a new diagram for the network based on the supplied parameters.
        Returns an IscDiagram object corresponding to the new diagram.
        Note that this function causes IPSA to rebuild the IscDiagram data maps.

        If nCopy what and pDiagramToCopy are provided, they provide a reference diagram and determine what is copied
        from that diagram into the new diagram.

        :param strSceneTitle: The name of the new diagram.
        :type strSceneTitle: str
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :param nCopyWhat: Determines what is copied from the provided diagram pDiagramToCopy

            * 0 if copy nothing
            * 1 if copy the busbars as they are
            * 2 if copy the busbars as junctions
            * 3 if copy everything
        :type nCopyWhat: int
        :param pDiagramToCopy: The IscDiagram object that any components may be copied from.
        :type pDiagramToCopy: IscDiagram
        :return: The IscDiagram object for the newly created diagram.
        :rtype: IscDiagram
        """
        pass

    @overload
    def DeleteDiagram(self, pDiagram: IscDiagram)-> None:
        """
        Deletes the diagram associated with the IscDiagram object.

        :param pDiagram: The diagram to be deleted.
        :type pDiagram: IscDiagram
        """
        pass

    @overload
    def DeleteDiagram(self, nUID: int) -> None:
        """
        Deletes the diagram identified by ID nUID.

        :param nUID: The diagram ID to be deleted.
        :type nUID: int
        """
        pass

    @overload
    def DeleteDiagram(self, strName: str) -> None:
        """
        Deletes the diagram identified by name strName.

        :param strName: The name of the diagram to be deleted.
        :type strName: str
        """
        pass

    def DeleteDiagram(self, strName: str) -> None:
        """
        Deletes the diagram identified by name strName, ID nUID or IscDiagram pDiagram.

        :param strName: The name of the diagram to be deleted.
        :type strName: str
        :param nUID: The diagram ID to be deleted.
        :type nUID: int
        :param pDiagram: The diagram to be deleted.
        :type pDiagram: IscDiagram
        """
        pass

    def GetAnalysisLF(self):
        """
        Returns an IscAnalysisLF object which can be used to get and set the load flow analysis parameters.

        :return: IscAnalysisLF object.
        :rtype: IscAnalysisLF
        """
        pass

    def SetResultsForTheseUIDs(self, nUIDs: int) -> None:
        """
        This function restricts the number of results that are returned from the load flow calculation engine to Python
        in order to reduce the execution time.
        Call this function before DoLoadFlow() or DoSimpleLoadFlow().

        :param nUIDs: The component UIDs.
        :type nUIDs: int
        """
        pass

    def DoLoadFlow(self, bNoEngineLoad: bool, bDontUpdateData: bool, bUseDC: bool = False) -> bool:
        """
        Performs a load flow calculation.

        :param bNoEngineLoad: If False (default), loads the engine from the Ipsa model before doing a load flow calculation.
            If True, skips the load from the Ipsa model and uses whatever network is currently loaded in the engine.
        :type bNoEngineLoad: bool
        :param bDontUpdateData: If False (default), allows the load flow results being written back to the network model
            data (e.g. Busbar voltages and angles). If True, skips this stage, so the network model remains the same as
            it was loaded. **Note that calling the function with no arguments is allowed and works as if it has been
            called with bNoEngineLoad and bDontUpdateData set to False.**
        :type bDontUpdateData: bool
        :param bUseDC: Tells the user that they can run a DC load flow instead of a normal load flow.
            If True, the program will run a DC load flow instead of an AC load flow. Default value of bUseDC is False.
        :type bUseDC: bool
        :return: True if the load flow converges, False on a non-convergence.
        :rtype: bool
        """
        pass

    def DoSimpleLoadFlow(self):
        """
        Performs a load flow calculation without prompting the user to confirm analysis options.
        Identical to the DoLoadFlow(False, False) call with no user interaction.

        :return: True if the load flow converges, False on a non-convergence.
        :rtype: bool
        """
        pass

    def GetAnalysisDCLF (self):
        """
        Returns an IscAnalysisDCLF object which can be used to get and set the DC load flow analysis parameters.

        :return: IscAnalysisDCLF object.
        :rtype: IscAnalysisDCLF
        """
        pass


    def DoDCLoadFlow(self):
        """
        Performs a DC load flow calculation while assuming you do not want to update the engines or results.

        :return: True if the load flow converges, False on a non-convergence.
        :rtype: bool
        """
        pass

    def SetBranchStatus(self, nUID: int, nStatus: int) -> None:
        """
        Changes the status of the branch or transformer UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the branch status
        does not need to be stored with the network.
        **Note: If the nUID is not a branch or transformer UID, it does nothing!**

        :param nUID: The branch or transformer UID.
        :type nUID: int
        :param nStatus: The status.
        :type nStatus: int
        """
        pass

    def SetLoadStatus(self, nUID: int, nStatus: int) -> None:
        """
        Changes the status of the load UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the load status
        does not need to be stored with the network.

        :param nUID: The load UID.
        :type nUID: int
        :param nStatus: The status.
        :type nStatus: int
        """
        pass

    def SetLoadPower(self, nUID: int, dMW: float, dMVAr: float) -> None:
        """
        Changes the power of the load UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the load power
        does not need to be stored with the network.

        :param nUID: The load UID.
        :type nUID: int
        :param dMW: The MW power.
        :type dMW: float
        :param dMVAr: The MVAr power.
        :type dMVAr: float
        """
        pass

    def SetGeneratorStatus(self, nUID: int, nStatus: int) -> None:
        """
        Changes the status of the generator UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the generator status
        does not need to be stored with the network.

        :param nUID: The generator UID.
        :type nUID: int
        :param nStatus: The status.
        :type nStatus: int
        """
        pass

    def SetGeneratorPower(self, nUID: int, dMW: float, dMVAr: float) -> None:
        """
        Changes the power of the generator UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the generator power
        does not need to be stored with the network.

        :param nUID: The generator UID.
        :type nUID: int
        :param dMW: The MW power.
        :type dMW: float
        :param dMVAr: The MVAr power.
        :type dMVAr: float
        """
        pass

    def GetLoadFlowMessage(self) -> str:
        """
        Returns the last load flow engine message.

        :return: The last load flow engine message.
        :rtype: str
        """
        pass

    def SetEngineMessageSuppression(self, nLevel: int) -> None:
        """
        Sets the verbosity of the load flow messages that are generated in the IPSA progress window.
        This can provide a speed improvement for complex scripts

            - 0 = Displays all messages
            - 1 = Shows only error messages
            - 2 = Shows no engine error messages

        :param nLevel: The verbosity of the load flow messages.
        :type nLevel: int
        """
        pass

    def GetLFSummaryResults(self) -> None:
        """
        Call this function to obtain the load flow summary results.
        """
        pass

    def GetHighestBusbarVoltagePU(self) -> float:
        """
        Returns the highest busbar voltage in per unit.

        :return: The highest busbar voltage in per unit.
        :rtype: float
        """
        pass

    def GetLowestBusbarVoltagePU(self) -> float:
        """
        Returns the lowest busbar voltage in per unit. GetLFSummaryResults()must be called first.

        :return: The lowest busbar voltage in per unit.
        :rtype: float
        """
        pass

    def GetTotalGenerationOutputMW(self) -> float:
        """
        Returns the total network generation real power, excluding slack generators, in MW.
        GetLFSummaryResults() must be called first.

        :return: The total network generation real power, excluding slack generators, in MW.
        :rtype: float
        """
        pass

    def GetTotalGenerationOutputMVAr(self) -> float:
        """
        Returns the total network generation reactive power, excluding slack generators, in MVAr.
        GetLFSummaryResults() must be called first.

        :return: The total network generation reactive power, excluding slack generators, in MVAr.
        :rtype: float
        """
        pass

    def GetTotalLoadInputMW(self) -> float:
        """
        Returns the total network load real power in MW. GetLFSummaryResults() must be called first.

        :return: The total network load real power in MW.
        :rtype: float
        """
        pass

    def GetTotalLoadInputMVAr(self) -> float:
        """
        Returns the total network load reactive power in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network load reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetTotalInductionInputMW(self) -> float:
        """
        Returns the total network induction motor real power in MW. GetLFSummaryResults() must be called first.

        :return: The total network induction motor real power in MW.
        :rtype: float
        """
        pass

    def GetTotalInductionInputMVAr(self) -> float:
        """
        Returns the total network induction motor load in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network induction motor load in MVAr.
        :rtype: float
        """
        pass

    def GetTotalUniMachineOutputMW(self) -> float:
        """
        Returns the total network universal machine generation real power in MW. GetLFSummaryResults() must be called first.

        :return: The total network universal machine generation real power in MW.
        :rtype: float
        """
        pass

    def GetTotalUniMachineOutputMVAr (self) -> float:
        """
        Returns the total network universal machine generation reactive power in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network universal machine generation reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetSlackOutputMW(self) -> float:
        """
        Returns the total network slack generation real power in MW. GetLFSummaryResults() must be called first.

        :return: The total network slack generation real power in MW.
        :rtype: float
        """
        pass

    def GetSlackOutputMVAr(self) -> float:
        """
        Returns the total network slack generation reactive power in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network slack generation reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetNumberOutsideLimits(self) -> int:
        """
        Returns the number of busbars outside voltage limits plus the number of overloaded branches and transformers.

        :return: The number of busbars outside voltage limits plus the number of overloaded branches and transformers.
        :rtype: int
        """
        pass

    def GetOutsideLimitText(self) -> str:
        """
        Returns a string detailing the busbar, branch or transformer with the most excessive overload/overvoltage
        in percentage terms. GetNumberOutsideLimits() must be called first.
        The name returned is the Python name of the component, e.g. Busbar1.Busbar2.Transformer

        :return: A string detailing the busbar, branch or transformer with the most excessive overload/overvoltage in
            percentage terms.
        :rtype: str
        """
        pass

    def AreLFLimitsIdentical(self) -> bool:
        """
        Returns True if the LF limits are identical.

        :return: True if the LF limits are identical.
        :rtype: bool
        """
        pass

    def SaveLFState(self) -> int:
        """
        Saves the current LF state and returns a state handle to restore it with.

        :return: State handle to restore the current LF state.
        :rtype: int
        """
        pass

    def RestoreLFState(self, nStateIndex: int) -> bool:
        """
        Restore the LF state. This function can fail if the number of items in a network is different from
        when the state was saved, which can happen in a subtle way if zero impedance branches are switched in or out.

        :param nStateIndex: The state index.
        :type nStateIndex: int
        :return: True if the restore operation succeeded.
        :rtype: bool
        """
        pass

    def DeleteAllLFStates(self) -> None:
        """
        Delete all LF saved states.
        """
        pass

    def IsComponentOutsideLimits(self, pComponent) -> int:
        """
        Checks whether a given component has values within limits after a load flow has been run.
        The function returns 0 if the values are within limits, 1 if they are over limits and if they are under.

        :param pComponent: The component object to be checked.
        :type pComponent: IscNetComponent
        :return: 0 if it's in limits, 1 if it is over limits and 2 if it is under limits.
        :rtype: int
        """
        pass

    def GetBusbarsOutsideLimits(self) -> Dict[int, bool]:
        """
        Returns a dictionary of busbar UIDs that are outside voltage limits for the previous load flow study.

        :return: A dictionary of busbar UIDs that are outside voltage limits for the previous load flow study.
        :rtype: dict(int,bool)
        """
        pass

    def GetBranchesOutsideLimits(self) -> Dict[int, bool]:
        """
        Returns a dictionary of branch UIDs that are above their ratings for the previous load flow study.

        :return: A dictionary of branch UIDs that are above their ratings for the previous load flow study.
        :rtype: dict(int,bool)
        """
        pass

    def GetTransformersOutsideLimits(self) -> Dict[int, bool]:
        """
        Returns a dictionary of transformer UIDs that are above their ratings for the previous load flow study.

        :return: A dictionary of transformer UIDs that are above their ratings for the previous load flow study.
        :rtype: dict(int,bool)
        """
        pass

    def RunArcFlashForBusbar(self, nBusbarUID: int, dBusFaultCurrentkA: float, dOperatingTimeSec: float) -> bool:
        """
        Performs an ArcFlash calculation for a single busbar using the fault current in kA and the operating time.
        The default reduction for comparison is 15% less for the current and 2.5x the arc duration given.

        :param nBusbarUID: The UID of the selected busbar.
        :type nBusbarUID: int
        :param dBusFaultCurrentkA: The fault current in kA.
        :type dBusFaultCurrentkA: float
        :param dOperatingTimeSec: The operating time in seconds.
        :type dOperatingTimeSec: float
        :return: Returns True if it is successful.
        :rtype: bool
        """
        pass

    def RunTotalArcFlash(self, bRunIPSAFaultLevel: bool, dOperatingTimeSec: float, dReducedOperatingTimeSec: float) -> List[Dict[int,bool]]:
        """
        Runs a thorough arc flash calculation for the whole network.
        **Note that here either the analysis class default for the fault current calculation is used or IPSA can run a
        fault level to calculate the fault current at each busbar.**
        Returns a list of pairs that map the UID to a boolean of whether the code ran correctly or not.

        :param bRunIPSAFaultLevel: Variable denoting whether it runs the IPSA fault lever before the arc flash.
        :type bRunIPSAFaultLevel: bool
        :param dOperatingTimeSec: The operating time in seconds.
        :type dOperatingTimeSec: float
        :param dReducedOperatingTimeSec: The reduced operating time in seconds.
        :type dReducedOperatingTimeSec: float
        :return: A a list of pairs that map the UID to a boolean of whether the code ran correctly or not.
        :rtype: list(dict(int,bool))
        """
        pass

    def DoFlatStart(self, bSetBuses: bool, bSetTransformerTaps: bool, bSetIMSlips: bool) -> None:
        """
        Runs a flatstart preparation for load flow depending on whether the user wants to flat start the busbar voltages,
        transformer tap positions, induction machine rotor slips or a combination of all 3.

        :param bSetBuses: Enabling flat start for the busbar voltages.
        :type bSetBuses: bool
        :param bSetTransformerTaps: Enabling flat start for the transformer tap positions.
        :type bSetTransformerTaps: bool
        :param bSetIMSlips: Enabling flat start for the induction machine rotor slips.
        :type bSetIMSlips: bool
        """
        pass

    def GetAnalysisFL(self):
        """
        Returns an IscAnlaysisFL object which can be used to get and set the fault level analysis parameters.

        :return: IscAnlaysisFL object.
        :rtype: IscAnlaysisFL
        """
        pass

    def DoFaultLevel(self) -> bool:
        """
        Performs a fault level calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def DoIECFaultLevel(self) -> bool:
        """
        Performs an IEC 60909 fault calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetAnalysisHM(self):
        """
        Returns an IscAnlaysisHM object which can be used to get and set the load flow analysis parameters.

        :return: IscAnlaysisHM object.
        :rtype: IscAnlaysisHM
        """
        pass

    def DoHarmPenetration(self) -> bool:
        """
        Performs a harmonic penetration calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def DoHarmSensitivity(self) -> bool:
        """
        Performs a harmonic voltage sensitivity calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def DoStorageFlip(self, lGeneratorsUID: List[int]) -> None:
        """
        Flips the storage of all defined Energy Storage units in the given list of UIDs.

        :param lGeneratorsUID: The given list of generators UIDs.
        :type lGeneratorsUID: list(int)
        """
        pass

    def DoSingleStorageFlip(self, nGeneratorUID: int) -> None:
        """
        Flips the storage of the Energy Storage unit defined by its UID.

        :param nGeneratorUID: The generator UID.
        :type nGeneratorUID: int
        """
        pass

    def DoGlobalStorageFlip(self, bFlipsImports: bool, bFlipExports: bool) -> None:
        """
        Flips all the storage units defined in the network depending on whether you want to flip imports to exports or
        vice versa.

        :param bFlipsImports: Variable denoting whether you want to flip imports to exports.
        :type bFlipsImports: bool
        :param bFlipExports: Variable denoting whether you want to flip exports to imports.
        :type bFlipExports: bool
        """
        pass

    def GetLastSuccessfulAutomationUID(self) -> int:
        """
        Returns the integer UID of the last successful automation.
        Note these are the UIDs of the automation not the study IDs.

        :return: The last successful automation UID.
        :rtype: int
        """
        pass

    def GetLastSuccessfulContingencyUID(self) -> int:
        """
        Returns the integer UID of the last successful contingency.
        Note these are the UIDs of the contingency not the study IDs.

        :return: The last successful contingency UID.
        :rtype: int
        """
        pass

    def RunContingency(self, nUID: int, bUseProfiles: bool) -> None:
        """
        Performs the contingency study identified by the integer UID.

        :param nUID: The contingency study UID.
        :type nUID: int
        :param bUseProfiles: If False then the contingency study is performed using the standard load and generator data.
            If True then the contingency study is performed using load and generator profiles assigned in the network.
            In this instance the switching operation is performed first followed by a load flow calculation for all of
            the profile categories.
        :type bUseProfiles: bool
        """
        pass

    def CreateContingency(self, nDepth: int, bExtendToBreakers: bool) -> int:
        """
        Creates a new contingency study and returns the UID of the study created.
        The depth of the study is configured as follows:

            - 1 = N - 1
            - 2 = N - 2
            - 3 = N - 3
            - 4 = N - 1 - 1

        :param nDepth: The depth of the study.
        :type nDepth: int
        :param bExtendToBreakers: If False then individual branches and transfers are switched out during the study.
            If True then the nearest circuit breakers are switched out allowing multiple components to be switched for
            each study.
        :type bExtendToBreakers: bool
        :return: The UID of the contingency created.
        :rtype: int
        """
        pass

    def CreateSpecificContingency(self, nDepth: int, bExtendToBreakers: bool, lBusbarsRequired) -> int:
        """
        Will design and create a specific contingency of given depth with only the busbars defined by the given list.

        :param nDepth: The depth of the study.
        :type nDepth: int
        :param bExtendToBreakers: If False then individual branches and transfers are switched out during the study.
            If True then the nearest circuit breakers are switched out allowing multiple components to be switched for
            each study.
        :type bExtendToBreakers: bool
        :param lBusbarsRequired: The specified list of busbars.
        :type lBusbarsRequired: list(IscBusbar)
        :return: The UID of the contingency created.
        :rtype: int
        """
        pass

    def GetStudies(self, nReportType: int) -> List[str]:
        """
        Returns a list of strings containing the individual automation or contingency study titles.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :return: The individual automation or contingency study titles.
        :rtype: list(str)
        """
        pass

    def GetStudyRowTitles(self, nReportType: int) -> str:
        """
        Returns a string in html format for the table header row associated with the automation or contingency results.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :return: String in html format.
        :rtype: str
        """
        pass

    def GetStudyRowOutput(self, nReportType: int, strStudyTitle: str) -> str:
        """
        Returns a string in html format for the table rows associated with the specified automation or contingency
        study.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :param strStudyTitle: The specified automation or contingency study.
        :type strStudyTitle: str
        :return: String in html format.
        :rtype: str
        """
        pass

    def GetStudyIDs(self, nReportType: int) -> List[int]:
        """
        Returns a list containing the individual automation or contingency study IDs.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :return: The individual automation or contingency study IDs.
        :rtype: list(int)
        """
        pass

    def GetContingencyStudyItemResults(self, nStudyID: int) -> Dict[int, int]:
        """
        Returns a dict of the component UIDs to the result ID for each component for the study with the given ID.
        The result IDs can be understood as followed:

            - 1 = Busbar over voltage (balanced or unbalanced)
            - 2 = Busbar under voltage (balanced or unbalanced)
            - 3 = Branch over rating (balanced or unbalanced)
            - 4 = Transformer over rating (2- or 3- winding, or unbalanced)
            - 0 = Otherwise

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The map of the component UIDs to the result IDs for the contingency study ID.
        :rtype: dict[int, int]
        """
        pass

    def GetAutomationStudyItemResults(self, nStudyID: int) -> Dict[int, int]:
        """
        Returns a dict of the component UIDs to the result ID for each component for the study with the given ID.
        The result IDs can be understood as followed:

            - 1 = Busbar over voltage (balanced or unbalanced)
            - 2 = Busbar under voltage (balanced or unbalanced)
            - 3 = Branch over rating (balanced or unbalanced)
            - 4 = Transformer over rating (2- or 3- winding, or unbalanced)
            - 0 = Otherwise

        :param nStudyID: The automation study ID.
        :type nStudyID: int
        :return: The map of the component UIDs to the result IDs for the automation study ID.
        :rtype: dict[int, int]
        """
        pass

    def GetStudyProfileIndex(self, nStudyID: int) -> int:
        """
        Returns the profile category index associated with the contingency or automation study.
        This is used to identify which profile category is associated with the study ID.

        :param nStudyID: The study ID.
        :type nStudyID: int
        :return: The profile category index associated with the contingency or automation study.
        :rtype: int
        """
        pass

    def GetStudyItemsSwitchedOutUIDs(self, nStudyID: int) -> List[int]:
        """
        Returns a list of integers containing the component UIDs for switched out components in contingency study ID.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The component UIDs for switched out components in contingency study ID.
        :rtype: list(int)
        """
        pass

    def GetContingencyStudyResultMagnitude(self, nStudyID: int, nResultID: int) -> float:
        """
        Returns the result magnitude for the result ID in contingency study ID.
        The nResultID is obtained from the GetContingencyStudyItemResults function.
        For busbars the return value is the per unit busbar voltage.
        For branches and transformers the return value is the largest power flow in MVA.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :param nResultID: The result ID.
        :type nResultID: int
        :return: The result magnitude for the result ID in contingency study ID.
        :rtype: float
        """
        pass

    def GetContingencyStudyDynamicallyOverloadedUIDs(self, nStudyID: int) -> List[int]:
        """
        Returns a list of integers which represent lines which are overloaded due to the action
        of a dynamic rating plugin.
        Dynamic rating plugins can be used to model the thermal response of OHLs,
        transformers and cables and provide ratings which are based on these models.
        The normal IPSA rating of a component is overridden if it has a dynamic rating plugin applied.
        In this case this function returns the UIDs of all such overloaded components in contingency study ID.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The lines which are overloaded due to the action of a dynamic rating plugin.
        :rtype: list(int)
        """
        pass

    def GetContingencyBranchRatingIndex(self) -> int:
        """
        Returns the IPSA rating index of the rating set used during the contingency study.

        :return: The IPSA rating index.
        :rtype: int
        """
        pass

    def GetProtectionDeviceSettings(self, nProtectionDeviceUID: int) -> List[str]:
        """
        Generates the protection devices details for the protection device indicated by the UID.
        The data is formatted as a list containing the html table filled with the settings, as presented in the
        protection settings report.
        *Note this formatting may be updated in the future.*

        :param nProtectionDeviceUID: The UID of the protection device of interest.
        :type nProtectionDeviceUID: int
        :returns: The protection device settings in an html table.
        :rtype: list(str)
        """
        pass

    def GetAllProtectionDeviceSettings (self) -> List[str]:
        """
        Generates the protection devices details for all the protection devices.
        The data is formatted as a list containing the html tables filled with the settings, as presented in the
        protection settings report.
        *Note this formatting may be updated in the future.*

        :returns: All the protection device settings as a list of html tables.
        :rtype: list(str)
        """
        pass

    def RunReliability(self) -> bool:
        """
        Performs the reliability study on the current network.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetReliabilityCI(self) -> float:
        """
        Returns the customer interruptions (CI) for the full network.

        :return: The customer interruptions (CI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityCML(self) -> float:
        """
        Returns the customer minutes lost (CMLs) for the full network.

        :return: The customer minutes lost (CMLs) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilitySAIFI(self) -> float:
        """
        Returns the system average interruption frequency index (SAIFI) for the full network.

        :return: The system average interruption frequency index (SAIFI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASIFI(self) -> float:
        """
        Returns the average service interruption frequency index (ASIFI) for the full network.

        :return: The average service interruption frequency index (ASIFI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilitySAIDI(self) -> float:
        """
        Returns the system average interruption duration index (SAIDI) for the full network.

        :return: The system average interruption duration index (SAIDI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityCAIDI(self) -> float:
        """
        Returns the customer average interruption duration index (CAIDI) for the full network.

        :return: The customer average interruption duration index (CAIDI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASIDI(self) -> float:
        """
        Returns the average system interruption duration index (ASIDI) for the full network.

        :return: The average system interruption duration index (ASIDI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASAI(self) -> float:
        """
        Returns the average service availability index (ASAI) for the full network.

        :return: The average service availability index (ASAI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASUI(self) -> float:
        """
        Returns the average service unavailability index (ASUI) for the full network.

        :return: The average service unavailability index (ASUI) for the full network.
        :rtype: float
        """
        pass

    def GetBusbarsWithArcFlashResults(self) -> List[int]:
        """
        Returns a list of busbar UIDs which have arc flash results.
        This is then used to get arc flash results for individual busbars.

        :return: Busbar UIDs which have arc flash results.
        :rtype: list(int)
        """
        pass

    def GetArcFlashCSV(self, nBusbarUID: int, bUseLegacyStandard: bool) -> str:
        """
        Creates a CSV result for a given busbar arcflash calculation and uses the 2018 standard if bUseLegacyStandard
        is set to False.

        :param nBusbarUID: The busbar UID.
        :type nBusbarUID: int
        :param bUseLegacyStandard: Variable denoting whether the legacy standard used.
        :type bUseLegacyStandard: bool
        :return: The CSV result for a given busbar arcflash calculation.
        :rtype: str
        """
        pass

    def GetTotalArcFlashCSV(self) -> str:
        """
        Returns total CSV formatted function for ArcFlash results from all busbars.

        :return: The total CSV formatted function for ArcFlash results from all busbars.
        :rtype: str
        """
        pass

    def GetArcFlashReportText(self, nUID: int) -> str:
        """
        Returns a string containing the arc flash result for the busbar identified by the UID.

        :param nUID: The busbar ID.
        :type nUID: int
        :return: The average service unavailability index (ASUI) for the full network.
        :rtype: str
        """
        pass

    def GetAnalysisAF(self):
        """
        Returns an IscAnalysisAF object which can be used to get and set the ArcFlash analysis parameters.

        :return: IscAnlaysisAF object.
        :rtype: IscAnlaysisAF
        """
        pass

    def SetBusbarOverloadLimits(self, dBusVoltHighPU: float, dBusVoltlowPU: float) -> None:
        """
        Sets the network global high and low limits for busbar overloads.

        :param dBusVoltHighPU: The high limit for busbar overloads in per unit.
        :type dBusVoltHighPU: float
        :param dBusVoltlowPU: The low limit for busbar overloads in per unit.
        :type dBusVoltlowPU: float
        """
        pass

    def SetBranchOverloadLimits(self, dBranchRatingHighPC: float, dBranchRatingLowPC: float, nRatingIndex: int) -> None:
        """
        Sets the network global percentage ratings for branches with a given rating index that is lifted from IscBranch
        (i.e., Standard, Summer, Winter, Short).

        :param dBranchRatingHighPC: The high network global percentage rating limit.
        :type dBranchRatingHighPC: float
        :param dBranchRatingLowPC: The low network global percentage rating limit.
        :type dBranchRatingLowPC: float
        :param nRatingIndex: The given rating index.
        :type nRatingIndex: int
        """
        pass

class IscNetworkData:
    """
    Provides access to the IPSA network data.
    """
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

    def GetBranchRatingName(self, nIndex: int) -> str:
        """
        Returns the name representing the rating set identified by an index.

        :param nIndex: The specified index.
        :type nIndex: int
        :return: The rating set name, or empty set if no rating set with that index exists in the network.
        :rtype: str
        """
        pass

class Isc__ProfilePQ__:
    """
    Provides access to the actual given profile class.
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

    def SetCategoryNames(self, dictCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary would add 3 categories to the profile with the strings as the
        categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dictCategories: The profile categories for the profile instance.
        :type dictCategories: dict(int,str)
        """
        pass

    def GetCategoryNames(self) -> Dict[int, str]:
        """
        Returns the profile categories for the profile instance.
        The string values are used as the individual category labels whilst the integer keys are only used internally.

        :return: The profile categories for the profile instance.
        :rtype: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For scaling profiles the values are the per unit scaling values.
        For example, passing the following dictionary would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW or pu values to the profile categories.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def GetPMW(self) -> Dict[int, float]:
        """
        Returns the MW values assigned to the profile categories.
        The float values are the MW data values whilst the integer keys should be identical to those used defining the
        categories.
        For scaling profiles the values are the per unit scaling values.

        :return: MW or pu values to the profile categories.
        :rtype: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For scaling profiles the values are the per unit scaling values.
        For example, passing the following dictionary would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr or pu values to the profile categories.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def GetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Returns the MVAr values assigned to the profile categories.
        The float values are the MVAr data values whilst the integer keys should be identical to those used defining the
        categories.
        For scaling profiles the values are the per unit scaling values.

        :return: MVAr or pu values to the profile categories.
        :rtype: dict(int,float)
        """
        pass
class IscLoadProfilePQActual:
    """
    Provides access to the actual load profile class.
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

    def SetCategoryNames(self, dictCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the actual load profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary would add 3 categories to the profile with the strings as the
        categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dictCategories: The profile categories for the actual load profile instance.
        :type dictCategories: dict(int,str)
        """
        pass

    def GetCategoryNames(self) -> Dict[int, str]:
        """
        Returns the profile categories for the actual load profile instance.
        The string values are used as the individual category labels whilst the integer keys are only used internally.

        :return: The profile categories for the actual load profile instance.
        :rtype: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the actual load profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW values to the actual load profile categories.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def GetPMW(self) -> Dict[int, float]:
        """
        Returns the MW values assigned to the actual load profile categories.
        The float values are the MW data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MW values to the actual load profile categories.
        :rtype: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the actual load profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr values to the actual load profile categories.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def GetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Returns the MVAr values assigned to the actual load profile categories.
        The float values are the MVAr data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MVAr values to the actual load profile categories.
        :rtype: dict(int,float)
        """
        pass

class IscLoadProfilePQScale:
    """
    Provides access to the scaled load profile class.
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

    def SetCategoryNames(self, dictCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the scaled load profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary would add 3 categories to the profile with the strings as the
        categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dictCategories: The profile categories for the scaled load profile instance.
        :type dictCategories: dict(int,str)
        """
        pass

    def GetCategoryNames(self) -> Dict[int, str]:
        """
        Returns the profile categories for the scaled load profile instance.
        The string values are used as the individual category labels whilst the integer keys are only used internally.

        :return: The profile categories for the scaled load profile instance.
        :rtype: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the scaled load profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW values to the scaled load profile categories as per unit scaling values.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def GetPMW(self) -> Dict[int, float]:
        """
        Returns the MW values assigned to the scaled load profile categories.
        The float values are the MW data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MW values to the scaled load profile categories as per unit scaling values.
        :rtype: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the scaled load profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr values to the scaled load profile categories as per unit scaling values.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def GetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Returns the MVAr values assigned to the scaled load profile categories.
        The float values are the MVAr data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MVAr values to the scaled load profile categories as per unit scaling values.
        :rtype: dict(int,float)
        """
        pass
class IscGeneratorProfilePQActual:
    """
    Provides access to the actual generator profile class.
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

    def SetCategoryNames(self, dictCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the actual generator profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary would add 3 categories to the profile with the strings as the
        categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dictCategories: The profile categories for the actual generator profile instance.
        :type dictCategories: dict(int,str)
        """
        pass

    def GetCategoryNames(self) -> Dict[int, str]:
        """
        Returns the profile categories for the actual generator profile instance.
        The string values are used as the individual category labels whilst the integer keys are only used internally.

        :return: The profile categories for the actual generator profile instance.
        :rtype: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the actual generator profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW values to the actual generator profile categories.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def GetPMW(self) -> Dict[int, float]:
        """
        Returns the MW values assigned to the actual generator profile categories.
        The float values are the MW data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MW values to the actual generator profile categories.
        :rtype: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the actual generator profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr values to the actual generator profile categories.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def GetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Returns the MVAr values assigned to the actual generator profile categories.
        The float values are the MVAr data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MVAr values to the actual generator profile categories.
        :rtype: dict(int,float)
        """
        pass

class IscGeneratorProfilePQScale:
    """
    Provides access to the scaled generator profile class.
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

    def SetCategoryNames(self, dictCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the scaled generator profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary would add 3 categories to the profile with the strings as the
        categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dictCategories: The profile categories for the scaled generator profile instance.
        :type dictCategories: dict(int,str)
        """
        pass

    def GetCategoryNames(self) -> Dict[int, str]:
        """
        Returns the profile categories for the scaled generator profile instance.
        The string values are used as the individual category labels whilst the integer keys are only used internally.

        :return: The profile categories for the scaled generator profile instance.
        :rtype: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the scaled generator profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW values to the scaled generator profile categories as per unit scaling values.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def GetPMW(self) -> Dict[int, float]:
        """
        Returns the MW values assigned to the scaled generator profile categories.
        The float values are the MW data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MW values to the scaled generator profile categories as per unit scaling values.
        :rtype: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the scaled generator profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr values to the scaled generator profile categories as per unit scaling values.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def GetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Returns the MVAr values assigned to the scaled generator profile categories.
        The float values are the MVAr data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MVAr values to the scaled generator profile categories as per unit scaling values.
        :rtype: dict(int,float)
        """
        pass
class IscUMachineProfilePQActual:
    """
    Provides access to the actual universal machine profile class.
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

    def SetCategoryNames(self, dictCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the actual universal machine profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary would add 3 categories to the profile with the strings as the
        categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dictCategories: The profile categories for the actual universal machine profile instance.
        :type dictCategories: dict(int,str)
        """
        pass

    def GetCategoryNames(self) -> Dict[int, str]:
        """
        Returns the profile categories for the actual universal machine profile instance.
        The string values are used as the individual category labels whilst the integer keys are only used internally.

        :return: The profile categories for the actual universal machine profile instance.
        :rtype: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the actual universal machine profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW values to the actual universal machine profile categories.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def GetPMW(self) -> Dict[int, float]:
        """
        Returns the MW values assigned to the actual universal machine profile categories.
        The float values are the MW data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MW values to the actual universal machine profile categories.
        :rtype: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the actual universal machine profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For example, passing the following dictionary would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr values to the actual universal machine profile categories.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def GetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Returns the MVAr values assigned to the actual universal machine profile categories.
        The float values are the MVAr data values whilst the integer keys should be identical to those used defining the
        categories.

        :return: MVAr values to the actual universal machine profile categories.
        :rtype: dict(int,float)
        """
        pass

class IscPlugin:
    """
    Provides access to an IPSA plugin.
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

    def SetIntParameter(self, nPluginIndex: int, nValue: int) -> bool:
        """
        Sets the index of the specific plugin parameter for the field from an integer value. The parameters are specific for the plugin object.

        :param nPluginIndex: The index to the specific plugin parameter.
        :type nPluginIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetDoubleParameter(self, nPluginIndex: int, dValue: float) -> bool:
        """
        Sets the index of the specific plugin parameter for the field from a double value. The parameters are specific for the plugin object.

        :param nPluginIndex: The index to the specific plugin parameter.
        :type nPluginIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetBoolParameter(self, nPluginIndex: int, strValue: int) -> bool:
        """
        Sets the index of the specific plugin parameter for the field from a boolean value. The parameters are specific for the plugin object.

        :param nPluginIndex: The index to the specific plugin parameter.
        :type nPluginIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetIntParameter(self, nPluginIndex: int) -> int:
        """
        Returns an integer parameter for the enumerated field defined by the specific plugin parameter.
        The parameters are specific for the plugin object.

        :param nPluginIndex: The index to the specific plugin parameter.
        :type nPluginIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDoubleParameter(self, nPluginIndex: int) -> float:
        """
        Returns a double parameter for the enumerated field defined by the specific plugin parameter.
        The parameters are specific for the plugin object.

        :param nPluginIndex: The index to the specific plugin parameter.
        :type nPluginIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetBoolParameter(self, nPluginIndex: int) -> bool:
        """
        Returns a boolean parameter for the enumerated field defined by the specific plugin parameter. The parameters are specific for the plugin object.

        :param nPluginIndex: The index to the specific plugin parameter.
        :type nPluginIndex: int
        :return: The string value.
        :rtype: bool
        """
        pass

    def GetIntOutput(self, nFieldIndex: int) -> int:
        """
        Returns the integer output of the plugin itself for the field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDoubleOutput(self, nFieldIndex: int) -> float:
        """
        Returns the double output of the plugin itself for the field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetBoolOutput(self, nFieldIndex: int) -> bool:
        """
        Returns the boolean output of the plugin itself for the field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: bool
        """
        pass

class IscProtectionDevice:
    """
    Provides access to a single protection device, such as a relay.
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

class IscStaticVC:
    """
    Provides access to an IPSA Static VAR Compensator (SVC).
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

    def GetReactivePowerMVAr(self) -> float:
        """
        Returns the SVC produced power in MVAr.

        :return: The SVC produced power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerkVAr(self) -> float:
        """
        Returns the SVC produced power in kVAr.

        :return: The SVC produced power in kVAr.
        :rtype: float
        """
        pass

    def GetTotalPowerMVA(self) -> float:
        """
        Returns the SVC produced total power in MVA.

        :return: The SVC produced total power in MVA.
        :rtype: float
        """
        pass

    def GetTotalPowerkVA(self) -> float:
        """
        Returns the SVC produced total power in kVA.

        :return: The SVC produced total power in kVA.
        :rtype: float
        """
        pass

    def GetCurrentkA(self) -> float:
        """
        Returns the SVC injected current in kA.

        :return: The SVC injected current in kA.
        :rtype: float
        """
        pass

class IscSynMachine:
    """
    Provides access to an IPSA generator (or more specifically, a synchronous machine).
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

    def PopulateByDBEntry(self, strGeneratorDataName: str, nParallel: int) -> bool:
        """
        Populates the object data with database information from the first database that was loaded.

        :param strGeneratorDataName: The name of the generator.
        :type strGeneratorDataName: str
        :param nParallel: The number of parallel components.
        :type nParallel: int
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

    def GetDCLFRealPowerMW(self) -> float:
        """
        Returns the generator output in MW.

        :return: The generator output in MW.
        :rtype: float
        """
        pass

    def GetDCLFRealPowerkW(self) -> float:
        """
        Returns the generator output in kW.

        :return: The generator output in kW.
        :rtype: float
        """
        pass

class IscTransformer:
    """
    Provides access to an IPSA transformer.
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

    def GetListDValue(self, nFieldIndex: int) -> list[float]:
        """
        Returns a list of double values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[float]
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

    def SetListDValue(self, nFieldIndex: int, lDValue: list[float]) -> bool:
        """
        Sets the value for the enumerated field from a list of doubles.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lDValue: The given list of double values.
        :type lDValue: list[float]
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetLineIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the field index for the line associated with this transformer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value for the field index for the line associated with this transformer.
        :rtype: int
        """
        pass

    def GetLineDValue(self, nFieldIndex: int) -> float:
        """
        Returns a double value for the field index for the line associated with this transformer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value for the field index for the line associated with this transformer.
        :rtype: float
        """
        pass

    def GetLineSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the field index for the line associated with this transformer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value for the field index for the line associated with this transformer.
        :rtype: str
        """
        pass

    def SetLineIValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the value for the field index from an integer for the line associated with this transformer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetLineDValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the value for the field index from a double for the line associated with this transformer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetLineSValue(self, nFieldIndex: int, strValue: int) -> bool:
        """
        Sets the value for the field index from a string for the line associated with this transformer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetRatingskA(self, nRatingIndex: int, dSendRatingkA: float, dRecieveRatingkA: float) -> None:
        """
        Sets the sending and receiving end current ratings in kA for the transformer.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :param dSendRatingkA: The sending end current rating in kA for the transformer.
        :type dSendRatingkA: float
        :param dRecieveRatingkA: The receiving end current rating in kA for the transformer.
        :type dRecieveRatingkA: float
        """
        pass

    def SetRatingMVA(self, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating for the transformer.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :param dRatingMVA: The MVA rating for the transformer.
        :type dRatingMVA: float
        """
        pass

    def GetRatingSendkA(self, nRatingIndex: int) -> float:
        """
        Returns the sending end current ratings in kA for the transformer.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The sending end current ratings in kA for the transformer.
        :rtype: float
        """
        pass

    def GetRatingReceivekA(self, nRatingIndex: int) -> float:
        """
        Returns the receiving end current ratings in kA for the transformer.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The receiving end current ratings in kA for the transformer.
        :rtype: float
        """
        pass

    def GetRatingMVA(self, nRatingIndex: int) -> float:
        """
        Returns the MVA rating for the transformer.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The MVA rating for the transformer.
        :rtype: float
        """
        pass

    def GetControlledBusbarName(self) -> str:
        """
        Returns the name of the busbar whose voltage is controlled by the transformer.

        :return: The name of the busbar whose voltage is controlled by the transformer.
        :rtype: str
        """
        pass

    def PopulateByDBEntry(self, strTransformerDataName: str, strLine1DataName: str, strLine2DataName: str,
                          nParallel: int, nParallelFrom: int, nParallelTo: int, dlengthFrom: float, dLengthTo: float) -> bool:
        """
        Populates the object data with database information from the first database that was loaded.

        :param strTransformerDataName: The name of the transformer.
        :type strTransformerDataName: str
        :param strLine1DataName: The name of the From branch.
        :type strLine1DataName: str
        :param strLine2DataName: The name of the To branch.
        :type strLine2DataName: str
        :param nParallel: The number of parallel components.
        :type nParallel: int
        :param nParallelFrom: The number of parallel components for the From branch.
        :type nParallelFrom: int
        :param nParallelTo: The number of parallel components for the To branch.
        :type nParallelTo: int
        :param dlengthFrom: The length of the From branch.
        :type dlengthFrom: float
        :param dLengthTo: The length of the To branch.
        :type dLengthTo: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetSendPowerMagnitudeMVA(self) -> float:
        """
        Returns the transformer sending end power in MVA.

        :return: The transformer sending end power in MVA.
        :rtype: float
        """
        pass

    def GetSendPowerMagnitudekVA(self) -> float:
        """
        Returns the transformer sending end power in kVA.

        :return: The transformer sending end power in kVA.
        :rtype: float
        """
        pass

    def GetSendRealPowerMW(self) -> float:
        """
        Returns the transformer sending end power in MW.

        :return: The transformer sending end power in MW.
        :rtype: float
        """
        pass

    def GetSendReactivePowerMVAr(self) -> float:
        """
        Returns the transformer sending end power in MVAr.

        :return: The transformer sending end power in MVAr.
        :rtype: float
        """
        pass

    def GetSendRealPowerkW(self) -> float:
        """
        Returns the transformer sending end power in kW.

        :return: The transformer sending end power in kW.
        :rtype: float
        """
        pass

    def GetSendReactivePowerkVAr(self) -> float:
        """
        Returns the transformer sending end power in kVAr.

        :return: The transformer sending end power in kVAr.
        :rtype: float
        """
        pass

    def GetReceivePowerMagnitudeMVA(self) -> float:
        """
        Returns the transformer receiving end power in MVA.

        :return: The transformer receiving end power in MVA.
        :rtype: float
        """
        pass

    def GetReceivePowerMagnitudekVA(self) -> float:
        """
        Returns the transformer receiving end power in kVA.

        :return: The transformer receiving end power in kVA.
        :rtype: float
        """
        pass

    def GetReceiveRealPowerMW(self) -> float:
        """
        Returns the transformer receiving end power in MW.

        :return: The transformer receiving end power in MW.
        :rtype: float
        """
        pass

    def GetReceiveReactivePowerMVAr(self) -> float:
        """
        Returns the transformer receiving end power in MVAr.

        :return: The transformer receiving end power in MVAr.
        :rtype: float
        """
        pass

    def GetReceiveRealPowerkW(self) -> float:
        """
        Returns the transformer receiving end power in kW.

        :return: The transformer receiving end power in kW.
        :rtype: float
        """
        pass

    def GetReceiveReactivePowerkVAr(self) -> float:
        """
        Returns the transformer receiving end power in kVAr.

        :return: The transformer receiving end power in kVAr.
        :rtype: float
        """
        pass

    @overload
    def GetLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest transformer power in MVA.

        :return: The highest transformer power in MVA.
        :rtype: float
        """
        pass

    @overload
    def GetLargestPowerMagnitudeMVA(self, nStudyUID: int) -> float:
        """
        Returns the highest transformer power in MVA.

        :param nStudyUID: The automation or contingency study UID which the results belong to.
        :type nStudyUID: int
        :return: The highest transformer power in MVA.
        :rtype: float
        """
        pass

    def GetLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest transformer power in MVA.

        :param nStudyUID: If supplied, the automation or contingency study UID which the results belong to.
        :type nStudyUID: int
        :return: The highest transformer power in MVA.
        :rtype: float
        """
        pass

    def GetLargestPowerMagnitudekVA(self) -> float:
        """
        Returns the highest transformer power in kVA.

        :return: The highest transformer power in kVA.
        :rtype: float
        """
        pass

    def GetLargestRealPowerMW(self) -> float:
        """
        Returns the highest transformer power in MW.

        :return: The highest transformer power in MW.
        :rtype: float
        """
        pass

    def GetLargestReactivePowerMVAr(self) -> float:
        """
        Returns the highest transformer power in MVAr.

        :return: The highest transformer power in MVAr.
        :rtype: float
        """
        pass

    def GetLargestRealPowerkW(self) -> float:
        """
        Returns the highest transformer power in kW.

        :return: The highest transformer power in kW.
        :rtype: float
        """
        pass

    def GetLargestReactivePowerkVAr(self) -> float:
        """
        Returns the highest transformer power in kVAr.

        :return: The highest transformer power in kVAr.
        :rtype: float
        """
        pass

    def GetLossesMW(self) -> float:
        """
        Returns the transformer losses in MW.

        :return: The transformer losses in MW.
        :rtype: float
        """
        pass

    def GetLossesMVAr(self) -> float:
        """
        Returns the transformer losses in MVAr.

        :return: The transformer losses in MVAr.
        :rtype: float
        """
        pass

    def GetLosseskW(self) -> float:
        """
        Returns the transformer losses in kW.

        :return: The transformer losses in kW.
        :rtype: float
        """
        pass

    def GetLosseskVAr(self) -> float:
        """
        Returns the transformer losses in kVAr.

        :return: The transformer losses in kVAr.
        :rtype: float
        """
        pass

    def GetCapacityHeadroomPC(self) -> float:
        """
        Returns the transformer capacity headroom as a percentage.

        :return: The transformer capacity headroom as a percentage.
        :rtype: float
        """
        pass

    def GetSpecVoltagePU(self) -> float:
        """
        Returns the target busbar voltage in per unit.

        :return: The target busbar voltage in per unit.
        :rtype: float
        """
        pass

    def GetActualVoltagePU(self) -> float:
        """
        Returns the actual busbar voltage in per unit.

        :return: The actual busbar voltage in per unit.
        :rtype: float
        """
        pass

    def GetTapPC(self) -> float:
        """
        Returns the current tap position in percentage.

        :return: The current tap position in percentage.
        :rtype: float
        """
        pass

    def GetMinTapPC(self) -> float:
        """
        Returns the minimum tap position in percentage.

        :return: The minimum tap position in percentage.
        :rtype: float
        """
        pass

    def GetMaxTapPC(self) -> float:
        """
        Returns the maximum tap position in percentage.

        :return: The maximum tap position in percentage.
        :rtype: float
        """
        pass

    def GetPhShiftDeg(self) -> float:
        """
        Returns the current phase shift in degrees.

        :return: The current phase shift in degrees.
        :rtype: float
        """
        pass

    def GetPhShiftRad(self) -> float:
        """
        Returns the current phase shift in radians.

        :return: The current phase shift in radians.
        :rtype: float
        """
        pass

    def GetHasCompounding(self) -> bool:
        """
        Returns True if the transformer has compounding, False otherwise.

        :return: True if the transformer has compounding, False otherwise.
        :rtype: bool
        """
        pass

    def GetFaultRedComponentFromMVA(self) -> float:
        """
        Returns the red phase fault level component in MVA at the “From” end of the transformer.

        :return: The red phase fault level component in MVA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultRedComponentToMVA(self) -> float:
        """
        Returns the red phase fault level component in MVA at the “To” end of the transformer.

        :return: The red phase fault level component in MVA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentFromMVA(self) -> float:
        """
        Returns the yellow phase fault level component in MVA at the “From” end of the transformer.

        :return: The yellow phase fault level component in MVA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentToMVA(self) -> float:
        """
        Returns the yellow phase fault level component in MVA at the “To” end of the transformer.

        :return: The yellow phase fault level component in MVA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentFromMVA(self) -> float:
        """
        Returns the blue phase fault level component in MVA at the “From” end of the transformer.

        :return: The blue phase fault level component in MVA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentToMVA(self) -> float:
        """
        Returns the blue phase fault level component in MVA at the “To” end of the transformer.

        :return: The blue phase fault level component in MVA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultRedComponentFromkA(self) -> float:
        """
        Returns the red phase fault level component in kA at the “From” end of the transformer.

        :return: The red phase fault level component in kA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultRedComponentTokA(self) -> float:
        """
        Returns the red phase fault level component in kA at the “To” end of the transformer.

        :return: The red phase fault level component in kA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentFromkA(self) -> float:
        """
        Returns the yellow phase fault level component in kA at the “From” end of the transformer.

        :return: The yellow phase fault level component in kA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentTokA(self) -> float:
        """
        Returns the yellow phase fault level component in kA at the “To” end of the transformer.

        :return: The yellow phase fault level component in kA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentFromkA(self) -> float:
        """
        Returns the blue phase fault level component in kA at the “From” end of the transformer.

        :return: The blue phase fault level component in kA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentTokA(self) -> float:
        """
        Returns the blue phase fault level component in kA at the “To” end of the transformer.

        :return: The blue phase fault level component in kA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentFromMVA(self) -> float:
        """
        Returns the positive sequence fault level component in MVA at the “From” end of the transformer.

        :return: The positive sequence fault level component in MVA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentToMVA(self) -> float:
        """
        Returns the positive sequence fault level component in MVA at the “To” end of the transformer.

        :return: The positive sequence fault level component in MVA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentFromMVA(self) -> float:
        """
        Returns the negative sequence fault level component in MVA at the “From” end of the transformer.

        :return: The negative sequence fault level component in MVA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentToMVA(self) -> float:
        """
        Returns the negative sequence fault level component in MVA at the “To” end of the transformer.

        :return: The negative sequence fault level component in MVA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentFromMVA(self) -> float:
        """
        Returns the zero sequence fault level component in MVA at the “From” end of the transformer.

        :return: The zero sequence fault level component in MVA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentToMVA(self) -> float:
        """
        Returns the zero sequence fault level component in MVA at the “To” end of the transformer.

        :return: The zero sequence fault level component in MVA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentFromkA(self) -> float:
        """
        Returns the positive sequence fault level component in kA at the “From” end of the transformer.

        :return: The positive sequence fault level component in kA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentTokA(self) -> float:
        """
        Returns the positive sequence fault level component in kA at the “To” end of the transformer.

        :return: The positive sequence fault level component in kA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentFromkA(self) -> float:
        """
        Returns the negative sequence fault level component in kA at the “From” end of the transformer.

        :return: The negative sequence fault level component in kA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentTokA(self) -> float:
        """
        Returns the negative sequence fault level component in kA at the “To” end of the transformer.

        :return: The negative sequence fault level component in kA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentFromkA(self) -> float:
        """
        Returns the zero sequence fault level component in kA at the “From” end of the transformer.

        :return: The zero sequence fault level component in kA at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentTokA(self) -> float:
        """
        Returns the zero sequence fault level component in kA at the “To” end of the transformer.

        :return: The zero sequence fault level component in kA at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultRedComponentFromAngleDeg(self) -> float:
        """
        Returns the red phase component of fault angle in degrees at the “From” end of the transformer.

        :return: The red phase component of fault angle in degrees at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultRedComponentToAngleDeg(self) -> float:
        """
        Returns the red phase component of fault angle in degrees at the “To” end of the transformer.

        :return: The red phase component of fault angle in degrees at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentFromAngleDeg(self) -> float:
        """
        Returns the yellow phase component of fault angle in degrees at the “From” end of the transformer.

        :return: The yellow phase component of fault angle in degrees at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultYellowComponentToAngleDeg(self) -> float:
        """
        Returns the yellow phase component of fault angle in degrees at the “To” end of the transformer.

        :return: The yellow phase component of fault angle in degrees at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentFromAngleDeg(self) -> float:
        """
        Returns the blue phase component of fault angle in degrees at the “From” end of the transformer.

        :return: The blue phase component of fault angle in degrees at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultBlueComponentToAngleDeg(self) -> float:
        """
        Returns the blue phase component of fault angle in degrees at the “To” end of the transformer.

        :return: The blue phase component of fault angle in degrees at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentFromAngleDeg(self) -> float:
        """
        Returns the positive sequence component of fault angle in degrees at the “From” end of the transformer.

        :return: The positive sequence component of fault angle in degrees at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultPositiveComponentToAngleDeg(self) -> float:
        """
        Returns the positive sequence component of fault angle in degrees at the “To” end of the transformer.

        :return: The positive sequence component of fault angle in degrees at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentFromAngleDeg(self) -> float:
        """
        Returns the negative sequence component of fault angle in degrees at the “From” end of the transformer.

        :return: The negative sequence component of fault angle in degrees at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultNegativeComponentToAngleDeg(self) -> float:
        """
        Returns the negative sequence component of fault angle in degrees at the “To” end of the transformer.

        :return: The negative sequence component of fault angle in degrees at the “To” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentFromAngleDeg(self) -> float:
        """
        Returns the zero sequence component of fault angle in degrees at the “From” end of the transformer.

        :return: The zero sequence component of fault angle in degrees at the “From” end of the transformer.
        :rtype: float
        """
        pass

    def GetFaultZeroComponentToAngleDeg(self) -> float:
        """
        Returns the zero sequence component of fault angle in degrees at the “To” end of the transformer.

        :return: The zero sequence component of fault angle in degrees at the “To” end of the transformer.
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

    def GetResistance(self, dOrder: float) -> float:
        """
        Returns the transformer harmonic resistance in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The transformer harmonic resistance in per unit.
        :rtype: float
        """
        pass

    def GetReactance(self, dOrder: float) -> float:
        """
        Returns the transformer harmonic reactance in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The transformer harmonic reactance in per unit.
        :rtype: float
        """
        pass
        
    def GetShuntResistance(self, dOrder: float) -> float:
        """
        Returns the transformer harmonic shunt resistance in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The transformer shunt resistance in per unit.
        :rtype: float

        """
        pass

    def GetShuntReactance(self, dOrder: float) -> float:
        """
        Returns the transformer harmonic shunt reactance in per unit on the network base for the harmonic order.

        :param dOrder: The harmonic order.
        :type dOrder: float
        :return: The transformer shunt reactance in per unit.
        :rtype: float

        """
        pass

    def GetProfileMinimumFlowMVA(self) -> float:
        """
        Returns the minimum branch flow in MVA from the profile study results.

        :return: The minimum branch flow in MVA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMinimumFlowkA(self) -> float:
        """
        Returns the minimum branch flow in kA from the profile study results.

        :return: The minimum branch flow in kA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMaximumFlowMVA(self) -> float:
        """
        Returns the maximum branch flow in MVA from the profile study results.

        :return: The maximum branch flow in MVA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMaximumFlowkA(self) -> float:
        """
        Returns the maximum branch flow in kA from the profile study results.

        :return: The maximum branch flow in kA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMedianFlowMVA(self) -> float:
        """
        Returns the median of the branch flow in MVA from the profile study results.

        :return: The median of the branch flow in MVA from the profile study results.
        :rtype: float
        """
        pass

    def GetProfileMedianFlowkA(self) -> float:
        """
        Returns the median of the branch flow in kA from the profile study results.

        :return: The median of the branch flow in kA from the profile study results.
        :rtype: float
        """
        pass

    def GetMinimumProfileIndex(self) -> int:
        """
        Returns the category index which identifies the minimum branch flow from the profile study results.

        :return: The minimum category index.
        :rtype: int
        """
        pass

    def GetMaximumProfileIndex(self) -> int:
        """
        Returns the category index which identifies the maximum branch flow from the profile study results.

        :return: The maximum category index.
        :rtype: int
        """

    def GetDCLFSendPowerMagnitudeMVA(self) -> float:
        """
        Returns the transformer sending end power in MVA.

        :return: The transformer sending end power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFSendPowerMagnitudekVA(self) -> float:
        """
        Returns the transformer sending end power in kVA.

        :return: The transformer sending end power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFSendRealPowerMW(self) -> float:
        """
        Returns the transformer sending end power in MW.

        :return: The transformer sending end power in MW.
        :rtype: float
        """
        pass

    def GetDCLFSendRealPowerkW(self) -> float:
        """
        Returns the transformer sending end power in kW.

        :return: The transformer sending end power in kW.
        :rtype: float
        """
        pass

    def GetDCLFReceivePowerMagnitudeMVA(self) -> float:
        """
        Returns the transformer receiving end power in MVA.

        :return: The transformer receiving end power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFReceivePowerMagnitudekVA(self) -> float:
        """
        Returns the transformer receiving end power in kVA.

        :return: The transformer receiving end power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFReceiveRealPowerMW(self) -> float:
        """
        Returns the transformer receiving end power in MW.

        :return: The transformer receiving end power in MW.
        :rtype: float
        """
        pass

    def GetDCLFReceiveRealPowerkW(self) -> float:
        """
        Returns the transformer receiving end power in kW.

        :return: The transformer receiving end power in kW.
        :rtype: float
        """
        pass

    def GetDCLFReceiveReactivePowerkVAr(self) -> float:
        """
        Returns the transformer receiving end power in kVAr.

        :return: The transformer receiving end power in kVAr.
        :rtype: float
        """
        pass

    def GetDCLFLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest transformer end power in MVA.

        :return: The highest transformer end power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFLargestPowerMagnitudekVA(self) -> float:
        """
        Returns the highest transformer end power in kVA.

        :return: The highest transformer end power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFLargestRealPowerMW(self) -> float:
        """
        Returns the highest transformer end power in MW.

        :return: The highest transformer end power in MW.
        :rtype: float
        """
        pass

    def GetDCLFLargestRealPowerkW(self) -> float:
        """
        Returns the highest transformer end power in kW.

        :return: The highest transformer end power in kW.
        :rtype: float
        """
        pass

    def GetDCLFLossesMW(self) -> float:
        """
        Returns the transformer losses in MW.

        :return: The transformer losses in MW.
        :rtype: float
        """
        pass

    def GetDCLFLosseskW(self) -> float:
        """
        Returns the transformer losses in kW.

        :return: The transformer losses in kW.
        :rtype: float
        """
        pass

    def GetDCLFPhShiftDeg(self) -> float:
        """
        Returns the transformer phase shift in degrees.

        :return: The transformer phase shift in degrees.
        :rtype: float
        """
        pass

    def GetDCLFPhShiftRad(self) -> float:
        """
        Returns the transformer phase shift in radians.

        :return: The transformer phase shift in radians.
        :rtype: float
        """
        pass

class IscUMachine:
    """
    Provides access to an IPSA universal machine.
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

    def GetListDValue(self, nFieldIndex: int) -> list[float]:
        """
        Returns a list of double values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[float]
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

    def SetListDValue(self, nFieldIndex: int, lDValue: list[float]) -> bool:
        """
        Sets the value for the enumerated field from a list of doubles.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lDValue: The given list of double values.
        :type lDValue: list[float]
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetRealPowerMW(self) -> float:
        """
        Returns the universal machine output in MW.

        :return: The universal machine output in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerMVAr(self) -> float:
        """
        Returns the universal machine output in MVAr.

        :return: The universal machine output in MVAr.
        :rtype: float
        """
        pass

    def GetRealPowerkW(self) -> float:
        """
        Returns the universal machine output in kW.

        :return: The universal machine output in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerkVAr(self) -> float:
        """
        Returns the universal machine output in kVAr.

        :return: The universal machine output in kVAr.
        :rtype: float
        """
        pass

    def GetTotalPowerMVA(self) -> float:
        """
        Returns the universal machine produced total power in MVA.

        :return: The universal machine produced total power in MVA.
        :rtype: float
        """
        pass

    def GetTotalPowerkVA(self) -> float:
        """
        Returns the universal machine produced total power in kVA.

        :return: The universal machine produced total power in kVA.
        :rtype: float
        """
        pass

    def GetPowerFactor(self) -> float:
        """
        Returns the universal machine power factor.

        :return: The universal machine power factor.
        :rtype: float
        """
        pass

    def GetCurrentkA(self) -> float:
        """
        Returns the universal machine injected current in kA.

        :return: The universal machine injected current in kA.
        :rtype: float
        """
        pass

    def GetDCLFRealPowerMW(self) -> float:
        """
        Returns the universal machine output in MW.

        :return: The universal machine output in MW.
        :rtype: float
        """
        pass

    def GetDCLFRealPowerkW(self) -> float:
        """
        Returns the universal machine output in kW.

        :return: The universal machine output in kW.
        :rtype: float
        """
        pass

    def GetDCLFTotalPowerMVA(self) -> float:
        """
        Returns the universal machine produced total power in MVA.

        :return: The universal machine produced total power in MVA.
        :rtype: float
        """
        pass

    def GetDCLFTotalPowerkVA(self) -> float:
        """
        Returns the universal machine produced total power in kVA.

        :return: The universal machine produced total power in kVA.
        :rtype: float
        """
        pass

    def GetDCLFCurrentkA(self) -> float:
        """
        Returns the universal machine injected current in kA.

        :return: The universal machine injected current in kA.
        :rtype: float
        """
        pass

    def TransformCDPParameters(self, dMachineMVA: float) -> bool:
        """
        Transforms the given CDP parametrisation based on the ratio
        between the machine and system base. Note this function should only be used if
        the user has the CDP parameters in machine base.

        :param dMachineMVA: Machine base in MVA
        :type dMachineMVA: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def ActivateCDP(self) -> bool:
        """
        Switches the CDP functionality for the given Universal Machine on

        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeactivateCDP(self) -> bool:
        """
        Switches the CDP functionality for the given Universal Machine off

        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetCDPVoltagePU(self) -> List[float]:
        """
        Returns the synchronous region voltages for the CDP advanced mode

        :return: List of voltage entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPVoltageTransientPU(self) -> List[float]:
        """
        Returns the transient region voltages for the CDP advanced mode

        :return: List of voltage entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPVoltageSubTransientPU(self) -> List[float]:
        """
        Returns the subtransient region voltages for the CDP advanced mode

        :return: List of voltage entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPRealCurrentPU(self) -> List[float]:
        """
        Returns the synchronous real current values for the CDP advanced mode

        :return: List of real current entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPRealCurrentTransientPU(self) -> List[float]:
        """
        Returns the transient real current values for the CDP advanced mode

        :return: List of real current entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPRealCurrentSubTransientPU(self) -> List[float]:
        """
        Returns the subtransient real current values for the CDP advanced mode

        :return: List of real current entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPReactiveCurrentPU(self) -> List[float]:
        """
        Returns the synchronous reactive current values for the CDP advanced mode

        :return: List of reactive current entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPReactiveCurrentTransientPU(self) -> List[float]:
        """
        Returns the transient reactive current values for the CDP advanced mode

        :return: List of reactive current entries (PU)
        :rtype: list(float)
        """
        pass

    def GetCDPReactiveCurrentSubTransientPU(self) -> List[float]:
        """
        Returns the subtransient reactive current values for the CDP advanced mode

        :return: List of reactive current entries (PU)
        :rtype: list(float)
        """
        pass

    def SetCDPVoltagePU(self, lVoltage: List[float]) -> bool:
        """
        Sets the synchronous region voltages for the CDP advanced mode

        :param: List of voltage entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPVoltageTransientPU(self, lVoltage: List[float]) -> bool:
        """
        Sets the transient region voltages for the CDP advanced mode

        :param: List of voltage entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPVoltageSubTransientPU(self, lVoltage: List[float]) -> bool:
        """
        Sets the subtransient region voltages for the CDP advanced mode

        :param: List of voltage entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPRealCurrentPU(self, lRealCurrent: List[float]) -> bool:
        """
        Sets the synchronous real current values for the CDP advanced mode

        :param: List of real current entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPRealCurrentTransientPU(self, lRealCurrent: List[float]) -> bool:
        """
        Sets the transient real current values for the CDP advanced mode

        :param: List of real current entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPRealCurrentSubTransientPU(self, lRealCurrent: List[float]) -> bool:
        """
        Sets the subtransient real current values for the CDP advanced mode

        :param: List of real current entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPReactiveCurrentPU(self, lReactiveCurrent: List[float]) -> bool:
        """
        Sets the synchronous reactive current values for the CDP advanced mode

        :param: List of reactive current entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPReactiveCurrentTransientPU(self, lReactiveCurrent: List[float]) -> bool:
        """
        Sets the transient reactive current values for the CDP advanced mode

        :param: List of reactive current entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass

    def SetCDPReactiveCurrentSubTransientPU(self, lReactiveCurrent: List[float]) -> bool:
        """
        Sets the subtransient reactive current values for the CDP advanced mode

        :param: List of reactive current entries (PU)
        :type: list(float)
        :return: True is successful
        :rtype: bool
        """
        pass


class IscUnbalancedLine:
    """
    Provides access to the three-phase unbalanced lines.
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

    def GetListDValue(self, nFieldIndex: int) -> list[float]:
        """
        Returns a list of double values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[float]
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

    def SetListDValue(self, nFieldIndex: int, lDValue: list[float]) -> bool:
        """
        Sets the value for the enumerated field from a list of doubles.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lDValue: The given list of double values.
        :type lDValue: list[float]
        :return: True if successful.
        :rtype: bool
        """
        pass

    def AddSections(self, nSections: int) -> None:
        """
        Add sections to the unbalanced line. All unbalanced lines start with one section.

        :param nSections: The number of sections.
        :type nSections: int
        """
        pass

    def GetSections(self) -> int:
        """
        Returns the number of sections in the unbalanced line. All unbalanced lines have at least one section.

        :return: The number of sections in the unbalanced line.
        :rtype: int
        """
        pass

    def GetRatingMVA(self, nRatingIndex: int) -> float:
        """
        Returns the MVA rating associated with the rating set.
        The same rating is used for all phases.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The MVA rating for the transformer.
        :rtype: float
        """
        pass

    def SetRatingkA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the kA rating to given value for the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The kA rating value.
        :type dRatingkA: float
        """
        pass

    def SetRatingMVA(self, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating to given value for the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingMVA: The MVA rating value.
        :type dRatingMVA: float
        """
        pass

    def GetRatingSendkA(self, nRatingIndex: int) -> float:
        """
        Returns the sending end kA rating associated with the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The sending end kA rating.
        :rtype: float
        """
        pass

    def GetRatingReceivekA(self, nRatingIndex: int) -> float:
        """
        Returns the receiving end kA rating associated with the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The receiving end kA rating.
        :rtype: float
        """
        pass

    def GetRealPowerSendAMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the A phase.

        :return: The branch sending end real power in MW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendBMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the B phase.

        :return: The branch sending end real power in MW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendCMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the C phase.

        :return: The branch sending end real power in MW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendNMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the N phase.

        :return: The branch sending end real power in MW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendAMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the A phase.

        :return: The branch sending end reactive power in MVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendBMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the B phase.

        :return: The branch sending end reactive power in MVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendCMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the C phase.

        :return: The branch sending end reactive power in MVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the N phase.

        :return: The branch sending end reactive power in MVAr in the N phase.
        :rtype: float
        """
        pass

    def GetSendPowerAMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the A phase.

        :return: The branch sending end power in MVA in the A phase.
        :rtype: float
        """
        pass

    def GetSendPowerBMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the B phase.

        :return: The branch sending end power in MVA in the B phase.
        :rtype: float
        """
        pass

    def GetSendPowerCMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the C phase.

        :return: The branch sending end power in MVA in the C phase.
        :rtype: float
        """
        pass

    def GetSendPowerNMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the N phase.

        :return: The branch sending end power in MVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendAkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the A phase.

        :return: The branch sending end real power in kW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendBkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the B phase.

        :return: The branch sending end real power in kW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendCkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the C phase.

        :return: The branch sending end real power in kW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendNkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the N phase.

        :return: The branch sending end real power in kW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendAkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the A phase.

        :return: The branch sending end reactive power in kVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendBkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the B phase.

        :return: The branch sending end reactive power in kVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendCkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the C phase.

        :return: The branch sending end reactive power in kVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the N phase.

        :return: The branch sending end reactive power in kVAr in the N phase.
        :rtype: float
        """
        pass

    def GetSendPowerAkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the A phase.

        :return: The branch sending end power in kVA in the A phase.
        :rtype: float
        """
        pass

    def GetSendPowerBkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the B phase.

        :return: The branch sending end power in kVA in the B phase.
        :rtype: float
        """
        pass

    def GetSendPowerCkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the C phase.

        :return: The branch sending end power in kVA in the C phase.
        :rtype: float
        """
        pass

    def GetSendPowerNkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the N phase.

        :return: The branch sending end power in kVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvAMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the A phase.

        :return: The branch receive end real power in MW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvBMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the B phase.

        :return: The branch receive end real power in MW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvCMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the C phase.

        :return: The branch receive end real power in MW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the N phase.

        :return: The branch receive end real power in MW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvAMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the A phase.

        :return: The branch receive end reactive power in MVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvBMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the B phase.

        :return: The branch receive end reactive power in MVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvCMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the C phase.

        :return: The branch receive end reactive power in MVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the N phase.

        :return: The branch receive end reactive power in MVAr in the N phase.
        :rtype: float
        """
        pass

    def GetRecvPowerAMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the A phase.

        :return: The branch receive end power in MVA in the A phase.
        :rtype: float
        """
        pass

    def GetRecvPowerBMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the B phase.

        :return: The branch receive end power in MVA in the B phase.
        :rtype: float
        """
        pass

    def GetRecvPowerCMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the C phase.

        :return: The branch receive end power in MVA in the C phase.
        :rtype: float
        """
        pass

    def GetRecvPowerNMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the N phase.

        :return: The branch receive end power in MVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvAkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the A phase.

        :return: The branch receive end real power in kW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvBkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the B phase.

        :return: The branch receive end real power in kW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvCkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the C phase.

        :return: The branch receive end real power in kW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the N phase.

        :return: The branch receive end real power in kW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvAkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the A phase.

        :return: The branch receive end reactive power in kVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvBkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the B phase.

        :return: The branch receive end reactive power in kVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvCkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the C phase.

        :return: The branch receive end reactive power in kVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the N phase.

        :return: The branch receive end reactive power in kVAr in the N phase.
        :rtype: float
        """
        pass

    def GetRecvPowerAkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the A phase.

        :return: The branch receive end power in kVA in the A phase.
        :rtype: float
        """
        pass

    def GetRecvPowerBkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the B phase.

        :return: The branch receive end power in kVA in the B phase.
        :rtype: float
        """
        pass

    def GetRecvPowerCkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the C phase.

        :return: The branch receive end power in kVA in the C phase.
        :rtype: float
        """
        pass

    def GetRecvPowerNkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the N phase.

        :return: The branch receive end power in kVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendMeanMW(self) -> float:
        """
        Returns the real power mean in MW of the three branch phase send end powers.

        :return: The real power mean in MW of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMeanMVAr(self) -> float:
        """
        Returns the reactive power mean in MVAr of the three branch phase send end powers.

        :return: The real power mean in MVAr of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetSendPowerMeanMVA(self) -> float:
        """
        Returns the power mean in MVA of the three branch phase send end powers.

        :return: The power mean in MVA of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetRealPowerSendMeankW(self) -> float:
        """
        Returns the real power mean in kW of the three branch phase send end powers.

        :return: The real power mean in kW of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMeankVAr(self) -> float:
        """
        Returns the reactive power mean in kVAr of the three branch phase send end powers.

        :return: The reactive power mean in kVAr of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetSendPowerMeankVA(self) -> float:
        """
        Returns the power mean in kVA of the three branch phase send end powers.

        :return: The power mean in kVA of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetRealPowerSendMaxMW(self) -> float:
        """
        Returns the highest real power of the three branch phase send end powers in MW.

        :return: The highest real power of the three branch phase send end powers in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMaxMVAr(self) -> float:
        """
        Returns the highest reactive power of the three branch phase send end powers in MVAr.

        :return: The highest reactive power of the three branch phase send end powers in MVAr.
        :rtype: float
        """
        pass

    def GetSendPowerMaxMVA(self) -> float:
        """
        Returns the highest power of the three branch phase send end powers in MVA.

        :return: The highest power of the three branch phase send end powers in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerSendMaxkW(self) -> float:
        """
        Returns the highest real power of the three branch phase send end powers in kW.

        :return: The highest real power of the three branch phase send end powers in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMaxkVAr(self) -> float:
        """
        Returns the highest reactive power of the three branch phase send end powers in kVAr.

        :return: The highest reactive power of the three branch phase send end powers in kVAr.
        :rtype: float
        """
        pass

    def GetSendPowerMaxkVA(self) -> float:
        """
        Returns the highest power of the three branch phase send end powers in kVA.

        :return: The highest power of the three branch phase send end powers in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMeanMW(self) -> float:
        """
        Returns the mean of the three branch phase receive end real powers in MW.

        :return: The mean of the three branch phase receive end real powers in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMeanMVAr(self) -> float:
        """
        Returns the mean of the three branch phase receive end reactive powers in MVAr.

        :return: The mean of the three branch phase receive end reactive powers in MVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMeanMVA(self) -> float:
        """
        Returns the mean of the three branch phase receive end powers in MVA.

        :return: The mean of the three branch phase receive end powers in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMeankW(self) -> float:
        """
        Returns the mean of the three branch phase receive end real powers in kW.

        :return: The mean of the three branch phase receive end real powers in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMeankVAr(self) -> float:
        """
        Returns the mean of the three branch phase receive end reactive powers in kVAr.

        :return: The mean of the three branch phase receive end reactive powers in kVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMeankVA(self) -> float:
        """
        Returns the mean of the three branch phase receive end powers in kVA.

        :return: The mean of the three branch phase receive end powers in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMaxMW(self) -> float:
        """
        Returns the highest of the three branch phase receive end real powers in MW.

        :return: The highest of the three branch phase receive end real powers in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMaxMVAr(self) -> float:
        """
        Returns the highest of the three branch phase receive end reactive powers in MVAr.

        :return: The highest of the three branch phase receive end reactive powers in MVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMaxMVA(self) -> float:
        """
        Returns the highest of the three branch phase receive end powers in MVA.

        :return: The highest of the three branch phase receive end powers in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMaxkW(self) -> float:
        """
        Returns the highest of the three branch phase receive end real powers in kW.

        :return: The highest of the three branch phase receive end real powers in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMaxkVAr(self) -> float:
        """
        Returns the highest of the three branch phase receive end reactive powers in kVAr.

        :return: The highest of the three branch phase receive end reactive powers in kVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMaxkVA(self) -> float:
        """
        Returns the highest of the three branch phase receive end powers in kVA.

        :return: The highest of the three branch phase receive end powers in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerSendPosMW(self) -> float:
        """
        Returns the positive branch phase sequence send end real power in MW.

        :return: The positive branch phase sequence send end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerSendNegMW(self) -> float:
        """
        Returns the negative branch phase sequence send end real power in MW.

        :return: The negative branch phase sequence send end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerSendZeroMW(self) -> float:
        """
        Returns the zero branch phase sequence send end real power in MW.

        :return: The zero branch phase sequence send end real power in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendPosMVAr(self) -> float:
        """
        Returns the positive branch phase sequence send end reactive power in MVAr.

        :return: The positive branch phase sequence send end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNegMVAr(self) -> float:
        """
        Returns the negative branch phase sequence send end reactive power in MVAr.

        :return: The negative branch phase sequence send end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendZeroMVAr(self) -> float:
        """
        Returns the zero branch phase sequence send end reactive power in MVAr.

        :return: The zero branch phase sequence send end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetSendPowerPosMVA(self) -> float:
        """
        Returns the positive branch phase sequence send end power in MVA.

        :return: The positive branch phase sequence send end power in MVA.
        :rtype: float
        """
        pass

    def GetSendPowerNegMVA(self) -> float:
        """
        Returns the negative branch phase sequence send end power in MVA.

        :return: The negative branch phase sequence send end power in MVA.
        :rtype: float
        """
        pass

    def GetSendPowerZeroMVA(self) -> float:
        """
        Returns the zero branch phase sequence send end power in MVA.

        :return: The zero branch phase sequence send end power in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerSendPoskW(self) -> float:
        """
        Returns the positive branch phase sequence send end real power in kW.

        :return: The positive branch phase sequence send end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerSendNegkW(self) -> float:
        """
        Returns the negative branch phase sequence send end real power in kW.

        :return: The negative branch phase sequence send end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerSendZerokW(self) -> float:
        """
        Returns the zero branch phase sequence send end real power in kW.

        :return: The zero branch phase sequence send end real power in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendPoskVAr(self) -> float:
        """
        Returns the positive branch phase sequence send end reactive power in kVAr.

        :return: The positive branch phase sequence send end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNegkVAr(self) -> float:
        """
        Returns the negative branch phase sequence send end reactive power in kVAr.

        :return: The negative branch phase sequence send end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendZerokVAr(self) -> float:
        """
        Returns the zero branch phase sequence send end reactive power in kVAr.

        :return: The zero branch phase sequence send end reactive power in kVAr.
        :rtype: float
        """
        pass
        pass

    def GetSendPowerPoskVA(self) -> float:
        """
        Returns the positive branch phase sequence send end power in kVA.

        :return: The positive branch phase sequence send end power in kVA.
        :rtype: float
        """
        pass

    def GetSendPowerNegkVA(self) -> float:
        """
        Returns the negative branch phase sequence send end power in kVA.

        :return: The negative branch phase sequence send end power in kVA.
        :rtype: float
        """
        pass

    def GetSendPowerZerokVA(self) -> float:
        """
        Returns the zero branch phase sequence send end power in kVA.

        :return: The zero branch phase sequence send end power in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvPosMW(self) -> float:
        """
        Returns the positive branch phase sequence receive end real power in MW.

        :return: The positive branch phase sequence receive end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNegMW(self) -> float:
        """
        Returns the negative branch phase sequence receive end real power in MW.

        :return: The negative branch phase sequence receive end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvZeroMW(self) -> float:
        """
        Returns the zero branch phase sequence receive end real power in MW.

        :return: The zero branch phase sequence receive end real power in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvPosMVAr(self) -> float:
        """
        Returns the positive branch phase sequence receive end reactive power in MVAr.

        :return: The positive branch phase sequence receive end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNegMVAr(self) -> float:
        """
        Returns the negative branch phase sequence receive end reactive power in MVAr.

        :return: The negative branch phase sequence receive end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvZeroMVAr(self) -> float:
        """
        Returns the zero branch phase sequence receive end reactive power in MVAr.

        :return: The zero branch phase sequence receive end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerPosMVA(self) -> float:
        """
        Returns the positive branch phase sequence receive end power in MVA.

        :return: The positive branch phase sequence receive end power in MVA.
        :rtype: float
        """
        pass

    def GetRecvPowerNegMVA(self) -> float:
        """
        Returns the negative branch phase sequence receive end power in MVA.

        :return: The negative branch phase sequence receive end power in MVA.
        :rtype: float
        """
        pass

    def GetRecvPowerZeroMVA(self) -> float:
        """
        Returns the zero branch phase sequence receive end power in MVA.

        :return: The zero branch phase sequence receive end power in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvPoskW(self) -> float:
        """
        Returns the positive branch phase sequence receive end real power in kW.

        :return: The positive branch phase sequence receive end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNegkW(self) -> float:
        """
        Returns the negative branch phase sequence receive end real power in kW.

        :return: The negative branch phase sequence receive end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvZerokW(self) -> float:
        """
        Returns the zero branch phase sequence receive end real power in kW.

        :return: The zero branch phase sequence receive end real power in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvPoskVAr(self) -> float:
        """
        Returns the positive branch phase sequence receive end reactive power in kVAr.

        :return: The positive branch phase sequence receive end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNegkVAr(self) -> float:
        """
        Returns the negative branch phase sequence receive end reactive power in kVAr.

        :return: The negative branch phase sequence receive end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvZerokVAr(self) -> float:
        """
        Returns the zero branch phase sequence receive end reactive power in kVAr.

        :return: The zero branch phase sequence receive end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerPoskVA(self) -> float:
        """
        Returns the positive branch phase sequence receive end power in kVA.

        :return: The positive branch phase sequence receive end power in kVA.
        :rtype: float
        """
        pass

    def GetRecvPowerNegkVA(self) -> float:
        """
        Returns the negative branch phase sequence receive end power in kVA.

        :return: The negative branch phase sequence receive end power in kVA.
        :rtype: float
        """
        pass

    def GetRecvPowerZerokVA(self) -> float:
        """
        Returns the zero branch phase sequence receive end power in kVA.

        :return: The zero branch phase sequence receive end power in kVA.
        :rtype: float
        """
        pass

class IscUnbalancedLoad:
    """
    Provides access to the three phase unbalanced load components.
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

    def GetReactivePowerAMVAr(self) -> float:
        """
        Returns the A phase power for the load in MVAr.

        :return: The A phase power for the load in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerBMVAr(self) -> float:
        """
        Returns the B phase power for the load in MVAr.

        :return: The B phase power for the load in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerCMVAr(self) -> float:
        """
        Returns the C phase power for the load in MVAr.

        :return: The C phase power for the load in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerAkVAr(self) -> float:
        """
        Returns the A phase power for the load in kVAr.

        :return: The A phase power for the load in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerBkVAr(self) -> float:
        """
        Returns the B phase power for the load in kVAr.

        :return: The B phase power for the load in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerCkVAr(self) -> float:
        """
        Returns the C phase power for the load in kVAr.

        :return: The C phase power for the load in kVAr.
        :rtype: float
        """
        pass

class IscUnbalancedTransformer:
    """
    Provides access to the three phase unbalanced transformer.
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

    def GetListDValue(self, nFieldIndex: int) -> list[float]:
        """
        Returns a list of double values for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The list of values.
        :rtype: list[float]
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

    def SetListDValue(self, nFieldIndex: int, lDValue: list[float]) -> bool:
        """
        Sets the value for the enumerated field from a list of doubles.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param lDValue: The given list of double values.
        :type lDValue: list[float]
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetRatingMVA(self, nRatingIndex: int) -> float:
        """
        Returns the MVA rating associated with the rating set.
        The same rating is used for all phases.

        :param nRatingIndex: Specifies which rating set the data is applied to.
        :type nRatingIndex: int
        :return: The MVA rating for the transformer.
        :rtype: float
        """
        pass

    def SetRatingkA(self, nRatingIndex: int, dRatingkA: float) -> None:
        """
        Sets the kA rating to given value for the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The kA rating value.
        :type dRatingkA: float
        """
        pass

    def SetRatingMVA(self, nRatingIndex: int, dRatingMVA: float) -> None:
        """
        Sets the MVA rating to given value for the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingMVA: The MVA rating value.
        :type dRatingMVA: float
        """
        pass

    def GetRatingSendkA(self, nRatingIndex: int) -> float:
        """
        Returns the sending end kA rating associated with the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The sending end kA rating.
        :rtype: float
        """
        pass

    def GetRatingReceivekA(self, nRatingIndex: int) -> float:
        """
        Returns the receiving end kA rating associated with the rating set given by the rating index.
        The same rating is used for all phases.

        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :return: The receiving end kA rating.
        :rtype: float
        """
        pass

    def GetRealPowerSendAMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the A phase.

        :return: The branch sending end real power in MW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendBMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the B phase.

        :return: The branch sending end real power in MW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendCMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the C phase.

        :return: The branch sending end real power in MW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendNMW(self) -> float:
        """
        Returns the branch sending end real power in MW in the N phase.

        :return: The branch sending end real power in MW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendAMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the A phase.

        :return: The branch sending end reactive power in MVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendBMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the B phase.

        :return: The branch sending end reactive power in MVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendCMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the C phase.

        :return: The branch sending end reactive power in MVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNMVAr(self) -> float:
        """
        Returns the branch sending end reactive power in MVAr in the N phase.

        :return: The branch sending end reactive power in MVAr in the N phase.
        :rtype: float
        """
        pass

    def GetSendPowerAMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the A phase.

        :return: The branch sending end power in MVA in the A phase.
        :rtype: float
        """
        pass

    def GetSendPowerBMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the B phase.

        :return: The branch sending end power in MVA in the B phase.
        :rtype: float
        """
        pass

    def GetSendPowerCMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the C phase.

        :return: The branch sending end power in MVA in the C phase.
        :rtype: float
        """
        pass

    def GetSendPowerNMVA(self) -> float:
        """
        Returns the branch sending end power in MVA in the N phase.

        :return: The branch sending end power in MVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendAkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the A phase.

        :return: The branch sending end real power in kW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendBkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the B phase.

        :return: The branch sending end real power in kW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendCkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the C phase.

        :return: The branch sending end real power in kW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendNkW(self) -> float:
        """
        Returns the branch sending end real power in kW in the N phase.

        :return: The branch sending end real power in kW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendAkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the A phase.

        :return: The branch sending end reactive power in kVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendBkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the B phase.

        :return: The branch sending end reactive power in kVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendCkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the C phase.

        :return: The branch sending end reactive power in kVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNkVAr(self) -> float:
        """
        Returns the branch sending end reactive power in kVAr in the N phase.

        :return: The branch sending end reactive power in kVAr in the N phase.
        :rtype: float
        """
        pass

    def GetSendPowerAkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the A phase.

        :return: The branch sending end power in kVA in the A phase.
        :rtype: float
        """
        pass

    def GetSendPowerBkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the B phase.

        :return: The branch sending end power in kVA in the B phase.
        :rtype: float
        """
        pass

    def GetSendPowerCkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the C phase.

        :return: The branch sending end power in kVA in the C phase.
        :rtype: float
        """
        pass

    def GetSendPowerNkVA(self) -> float:
        """
        Returns the branch sending end power in kVA in the N phase.

        :return: The branch sending end power in kVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvAMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the A phase.

        :return: The branch receive end real power in MW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvBMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the B phase.

        :return: The branch receive end real power in MW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvCMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the C phase.

        :return: The branch receive end real power in MW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNMW(self) -> float:
        """
        Returns the branch receive end real power in MW in the N phase.

        :return: The branch receive end real power in MW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvAMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the A phase.

        :return: The branch receive end reactive power in MVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvBMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the B phase.

        :return: The branch receive end reactive power in MVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvCMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the C phase.

        :return: The branch receive end reactive power in MVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNMVAr(self) -> float:
        """
        Returns the branch receive end reactive power in MVAr in the N phase.

        :return: The branch receive end reactive power in MVAr in the N phase.
        :rtype: float
        """
        pass

    def GetRecvPowerAMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the A phase.

        :return: The branch receive end power in MVA in the A phase.
        :rtype: float
        """
        pass

    def GetRecvPowerBMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the B phase.

        :return: The branch receive end power in MVA in the B phase.
        :rtype: float
        """
        pass

    def GetRecvPowerCMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the C phase.

        :return: The branch receive end power in MVA in the C phase.
        :rtype: float
        """
        pass

    def GetRecvPowerNMVA(self) -> float:
        """
        Returns the branch receive end power in MVA in the N phase.

        :return: The branch receive end power in MVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvAkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the A phase.

        :return: The branch receive end real power in kW in the A phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvBkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the B phase.

        :return: The branch receive end real power in kW in the B phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvCkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the C phase.

        :return: The branch receive end real power in kW in the C phase.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNkW(self) -> float:
        """
        Returns the branch receive end real power in kW in the N phase.

        :return: The branch receive end real power in kW in the N phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvAkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the A phase.

        :return: The branch receive end reactive power in kVAr in the A phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvBkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the B phase.

        :return: The branch receive end reactive power in kVAr in the B phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvCkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the C phase.

        :return: The branch receive end reactive power in kVAr in the C phase.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNkVAr(self) -> float:
        """
        Returns the branch receive end reactive power in kVAr in the N phase.

        :return: The branch receive end reactive power in kVAr in the N phase.
        :rtype: float
        """
        pass

    def GetRecvPowerAkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the A phase.

        :return: The branch receive end power in kVA in the A phase.
        :rtype: float
        """
        pass

    def GetRecvPowerBkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the B phase.

        :return: The branch receive end power in kVA in the B phase.
        :rtype: float
        """
        pass

    def GetRecvPowerCkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the C phase.

        :return: The branch receive end power in kVA in the C phase.
        :rtype: float
        """
        pass

    def GetRecvPowerNkVA(self) -> float:
        """
        Returns the branch receive end power in kVA in the N phase.

        :return: The branch receive end power in kVA in the N phase.
        :rtype: float
        """
        pass

    def GetRealPowerSendMeanMW(self) -> float:
        """
        Returns the real power mean in MW of the three branch phase send end powers.

        :return: The real power mean in MW of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMeanMVAr(self) -> float:
        """
        Returns the reactive power mean in MVAr of the three branch phase send end powers.

        :return: The real power mean in MVAr of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetSendPowerMeanMVA(self) -> float:
        """
        Returns the power mean in MVA of the three branch phase send end powers.

        :return: The power mean in MVA of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetRealPowerSendMeankW(self) -> float:
        """
        Returns the real power mean in kW of the three branch phase send end powers.

        :return: The real power mean in kW of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMeankVAr(self) -> float:
        """
        Returns the reactive power mean in kVAr of the three branch phase send end powers.

        :return: The reactive power mean in kVAr of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetSendPowerMeankVA(self) -> float:
        """
        Returns the power mean in kVA of the three branch phase send end powers.

        :return: The power mean in kVA of the three branch phase send end powers.
        :rtype: float
        """
        pass

    def GetRealPowerSendMaxMW(self) -> float:
        """
        Returns the highest real power of the three branch phase send end powers in MW.

        :return: The highest real power of the three branch phase send end powers in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMaxMVAr(self) -> float:
        """
        Returns the highest reactive power of the three branch phase send end powers in MVAr.

        :return: The highest reactive power of the three branch phase send end powers in MVAr.
        :rtype: float
        """
        pass

    def GetSendPowerMaxMVA(self) -> float:
        """
        Returns the highest power of the three branch phase send end powers in MVA.

        :return: The highest power of the three branch phase send end powers in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerSendMaxkW(self) -> float:
        """
        Returns the highest real power of the three branch phase send end powers in kW.

        :return: The highest real power of the three branch phase send end powers in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendMaxkVAr(self) -> float:
        """
        Returns the highest reactive power of the three branch phase send end powers in kVAr.

        :return: The highest reactive power of the three branch phase send end powers in kVAr.
        :rtype: float
        """
        pass

    def GetSendPowerMaxkVA(self) -> float:
        """
        Returns the highest power of the three branch phase send end powers in kVA.

        :return: The highest power of the three branch phase send end powers in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMeanMW(self) -> float:
        """
        Returns the mean of the three branch phase receive end real powers in MW.

        :return: The mean of the three branch phase receive end real powers in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMeanMVAr(self) -> float:
        """
        Returns the mean of the three branch phase receive end reactive powers in MVAr.

        :return: The mean of the three branch phase receive end reactive powers in MVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMeanMVA(self) -> float:
        """
        Returns the mean of the three branch phase receive end powers in MVA.

        :return: The mean of the three branch phase receive end powers in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMeankW(self) -> float:
        """
        Returns the mean of the three branch phase receive end real powers in kW.

        :return: The mean of the three branch phase receive end real powers in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMeankVAr(self) -> float:
        """
        Returns the mean of the three branch phase receive end reactive powers in kVAr.

        :return: The mean of the three branch phase receive end reactive powers in kVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMeankVA(self) -> float:
        """
        Returns the mean of the three branch phase receive end powers in kVA.

        :return: The mean of the three branch phase receive end powers in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMaxMW(self) -> float:
        """
        Returns the highest of the three branch phase receive end real powers in MW.

        :return: The highest of the three branch phase receive end real powers in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMaxMVAr(self) -> float:
        """
        Returns the highest of the three branch phase receive end reactive powers in MVAr.

        :return: The highest of the three branch phase receive end reactive powers in MVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMaxMVA(self) -> float:
        """
        Returns the highest of the three branch phase receive end powers in MVA.

        :return: The highest of the three branch phase receive end powers in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvMaxkW(self) -> float:
        """
        Returns the highest of the three branch phase receive end real powers in kW.

        :return: The highest of the three branch phase receive end real powers in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvMaxkVAr(self) -> float:
        """
        Returns the highest of the three branch phase receive end reactive powers in kVAr.

        :return: The highest of the three branch phase receive end reactive powers in kVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerMaxkVA(self) -> float:
        """
        Returns the highest of the three branch phase receive end powers in kVA.

        :return: The highest of the three branch phase receive end powers in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerSendPosMW(self) -> float:
        """
        Returns the positive branch phase sequence send end real power in MW.

        :return: The positive branch phase sequence send end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerSendNegMW(self) -> float:
        """
        Returns the negative branch phase sequence send end real power in MW.

        :return: The negative branch phase sequence send end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerSendZeroMW(self) -> float:
        """
        Returns the zero branch phase sequence send end real power in MW.

        :return: The zero branch phase sequence send end real power in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendPosMVAr(self) -> float:
        """
        Returns the positive branch phase sequence send end reactive power in MVAr.

        :return: The positive branch phase sequence send end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNegMVAr(self) -> float:
        """
        Returns the negative branch phase sequence send end reactive power in MVAr.

        :return: The negative branch phase sequence send end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendZeroMVAr(self) -> float:
        """
        Returns the zero branch phase sequence send end reactive power in MVAr.

        :return: The zero branch phase sequence send end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetSendPowerPosMVA(self) -> float:
        """
        Returns the positive branch phase sequence send end power in MVA.

        :return: The positive branch phase sequence send end power in MVA.
        :rtype: float
        """
        pass

    def GetSendPowerNegMVA(self) -> float:
        """
        Returns the negative branch phase sequence send end power in MVA.

        :return: The negative branch phase sequence send end power in MVA.
        :rtype: float
        """
        pass

    def GetSendPowerZeroMVA(self) -> float:
        """
        Returns the zero branch phase sequence send end power in MVA.

        :return: The zero branch phase sequence send end power in MVA.
        :rtype: float
        """
        pass

    def GetSendPowerPoskVA(self) -> float:
        """
        Returns the positive branch phase sequence send end power in kVA.

        :return: The positive branch phase sequence send end power in kVA.
        :rtype: float
        """
        pass

    def GetSendPowerNegkVA(self) -> float:
        """
        Returns the negative branch phase sequence send end power in kVA.

        :return: The negative branch phase sequence send end power in kVA.
        :rtype: float
        """
        pass

    def GetSendPowerZerokVA(self) -> float:
        """
        Returns the zero branch phase sequence send end power in kVA.

        :return: The zero branch phase sequence send end power in kVA.
        :rtype: float
        """
        pass

    def GetRealPowerSendPoskW(self) -> float:
        """
        Returns the positive branch phase sequence send end real power in kW.

        :return: The positive branch phase sequence send end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerSendNegkW(self) -> float:
        """
        Returns the negative branch phase sequence send end real power in kW.

        :return: The negative branch phase sequence send end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerSendZerokW(self) -> float:
        """
        Returns the zero branch phase sequence send end real power in kW.

        :return: The zero branch phase sequence send end real power in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerSendPoskVAr(self) -> float:
        """
        Returns the positive branch phase sequence send end reactive power in kVAr.

        :return: The positive branch phase sequence send end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendNegkVAr(self) -> float:
        """
        Returns the negative branch phase sequence send end reactive power in kVAr.

        :return: The negative branch phase sequence send end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerSendZerokVAr(self) -> float:
        """
        Returns the zero branch phase sequence send end reactive power in kVAr.

        :return: The zero branch phase sequence send end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetRealPowerRecvPosMW(self) -> float:
        """
        Returns the positive branch phase sequence receive end real power in MW.

        :return: The positive branch phase sequence receive end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNegMW(self) -> float:
        """
        Returns the negative branch phase sequence receive end real power in MW.

        :return: The negative branch phase sequence receive end real power in MW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvZeroMW(self) -> float:
        """
        Returns the zero branch phase sequence receive end real power in MW.

        :return: The zero branch phase sequence receive end real power in MW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvPosMVAr(self) -> float:
        """
        Returns the positive branch phase sequence receive end reactive power in MVAr.

        :return: The positive branch phase sequence receive end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNegMVAr(self) -> float:
        """
        Returns the negative branch phase sequence receive end reactive power in MVAr.

        :return: The negative branch phase sequence receive end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvZeroMVAr(self) -> float:
        """
        Returns the zero branch phase sequence receive end reactive power in MVAr.

        :return: The zero branch phase sequence receive end reactive power in MVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerPosMVA(self) -> float:
        """
        Returns the positive branch phase sequence receive end power in MVA.

        :return: The positive branch phase sequence receive end power in MVA.
        :rtype: float
        """
        pass

    def GetRecvPowerNegMVA(self) -> float:
        """
        Returns the negative branch phase sequence receive end power in MVA.

        :return: The negative branch phase sequence receive end power in MVA.
        :rtype: float
        """
        pass

    def GetRecvPowerZeroMVA(self) -> float:
        """
        Returns the zero branch phase sequence receive end power in MVA.

        :return: The zero branch phase sequence receive end power in MVA.
        :rtype: float
        """
        pass

    def GetRealPowerRecvPoskW(self) -> float:
        """
        Returns the positive branch phase sequence receive end real power in kW.

        :return: The positive branch phase sequence receive end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvNegkW(self) -> float:
        """
        Returns the negative branch phase sequence receive end real power in kW.

        :return: The negative branch phase sequence receive end real power in kW.
        :rtype: float
        """
        pass

    def GetRealPowerRecvZerokW(self) -> float:
        """
        Returns the zero branch phase sequence receive end real power in kW.

        :return: The zero branch phase sequence receive end real power in kW.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvPoskVAr(self) -> float:
        """
        Returns the positive branch phase sequence receive end reactive power in kVAr.

        :return: The positive branch phase sequence receive end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvNegkVAr(self) -> float:
        """
        Returns the negative branch phase sequence receive end reactive power in kVAr.

        :return: The negative branch phase sequence receive end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetReactivePowerRecvZerokVAr(self) -> float:
        """
        Returns the zero branch phase sequence receive end reactive power in kVAr.

        :return: The zero branch phase sequence receive end reactive power in kVAr.
        :rtype: float
        """
        pass

    def GetRecvPowerPoskVA(self) -> float:
        """
        Returns the positive branch phase sequence receive end power in kVA.

        :return: The positive branch phase sequence receive end power in kVA.
        :rtype: float
        """
        pass

    def GetRecvPowerNegkVA(self) -> float:
        """
        Returns the negative branch phase sequence receive end power in kVA.

        :return: The negative branch phase sequence receive end power in kVA.
        :rtype: float
        """
        pass

    def GetRecvPowerZerokVA(self) -> float:
        """
        Returns the zero branch phase sequence receive end power in kVA.

        :return: The zero branch phase sequence receive end power in kVA.
        :rtype: float
        """
        pass

class IscVoltageRegulator:
    """
    Provides access to a series voltage regulator.
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

    def GetBranchUID(self) -> int:
        """
        Returns the UID of the branch that the voltage regulator is located on.

        :return: The branch UID.
        :rtype: int
        """
        pass
