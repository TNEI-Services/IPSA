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
    Provides access to an Ipsa battery.
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
        :rtype: bool
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The boolean value.
        :rtype: bool
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
        :type nSection: int
        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param bValue: The given boolean value.
        :type bValue: bool
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
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

        :param nSection: The number of sections.
        :type nSection: int
        :param nRatingIndex: The rating index.
        :type nRatingIndex: int
        :param dRatingkA: The rating kA.
        :type dRatingkA: float
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

    def GetLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest branch power in MVA.

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

    def GetFaultDValue(self, nCircuitBreakerFieldIndex: int) -> float:
        """
        Returns a float value for the circuit breaker field.
        **Note that nCircuitBreakerFieldIndex should be one of MakePeakkA, BreakRMSkA, BreakDCPC, BreakTimemS or
        NomCurrentkA – it is an IscCircuitBreaker field index.**
        This function is used to get fault (breaker) ratings for a busbar.

        :param nCircuitBreakerFieldIndex: MakePeakkA, BreakRMSkA, BreakDCPC, BreakTimemS or NomCurrentkA – it is an IscCircuitBreaker field index.
        :type nCircuitBreakerFieldIndex: int
        :return: The float value for the selected field.
        :rtype: float
        """
        pass

    def SetFaultDValue(self, nCircuitBreakerFieldIndex: int) -> bool:
        """
        Sets the value for the circuit breaker field.
        **Note that nCircuitBreakerFieldIndex should be one of MakePeakkA, BreakRMSkA, BreakDCPC, BreakTimemS or
        NomCurrentkA – it is an IscCircuitBreaker field index.**
        This function is used to set fault (breaker) ratings for a busbar.

        :param nCircuitBreakerFieldIndex: MakePeakkA, BreakRMSkA, BreakDCPC, BreakTimemS or NomCurrentkA – it is an IscCircuitBreaker field index.
        :type nCircuitBreakerFieldIndex: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetVoltageMagnitudekV(self) -> float:
        """
        Returns the voltage magnitude in kV.

        :return: The voltage magnitude.
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

    def GetVoltageMagnitudePU(self, dOrder: float) -> float:
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
        A hexagonal busbar symbol is a circle.

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

    def CreateTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
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

    def CreateUnbalancedTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
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

    def AddPointToLine(self, nLineUID: int, dX: float, dY: float, bFromEnd: bool) -> bool:
        """
        Adds a knee point to the line identified by the unique ID.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param dX: The knee point x coordinate.
        :type dX: float
        :param dY: The knee point y coordinate.
        :type dY: float
        :param bFromEnd: If True then the knee point is added to the last segment, i.e. furthest from the From end.
            If False then the knee point is added to the first segment.
        :type bFromEnd: float
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
        Splits a branch into two sections connected by a new busbar.

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
        Deletes the graphic item identified by the ID. This may be a line, radial component or busbar.

        :param nUID: The graphical item UID.
        :type nUID: int
        :return: Denoting whether the item was deleted.
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

        :param nUID: The diagraqm object UID.
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

        :param nUID: The diagraqm object UID.
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

    def GetItemX(self, nUID: int) -> float:
        """
        Returns the screen X coordinate of the busbar.
        The screen co-ordinates are relative to the nominal centre point of the screen.

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

    def PrintPDF(self, strFileName: str) -> None:
        """
        Print the diagram to a PDF file.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen Y coordinate.
        :rtype: float
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

        :param dictHarmonicData: Dictionary in the following format: **{double dHarmonicOrder:double dHarmonicImpedance, …}** where dHarmonicImpedance is a value specifying the harmonic resistance at the frequency given by the harmonic order dHarmonicOrder. Up to 120 different orders may be specified in each grid infeed.
        :type dictHarmonicData: dict(float,float)
        """
        pass

    def SetHarmonicX(self, dictHarmonicData: Dict[float, float]) -> None:
        """
        Sets the values for the harmonic reactance of the grid infeed.

        :param dictHarmonicData: Dictionary in the following format: **{double dHarmonicOrder:double dHarmonicImpedance, …}** where dHarmonicImpedance is a value specifying the harmonic resistance at the frequency given by the harmonic order dHarmonicOrder. Up to 120 different orders may be specified in each grid infeed.
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

from typing import List


class IscGroup:
    """
    The IscGroup class provides access to an IPSA group to set and get group members.
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
        Sets the group members to the list of component integers.
        This replaces any existing members with the supplied list of UIDs.

        :param nUIDs: List of component integers.
        :type nUIDs: list(int)
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

class IscInterface:
    """
    The main interface class used to access all other IPSA objects and functions.
    """
    def ReadFile(self, strName: str):
        """
        Opens an Ipsa i2f file strName and returns an IscNetwork instance for that file.

        :param strName: The Ipsa i2f file that is going to be opened.
        :type strName: str
        :return: The IscNetwork instance for the strName file
        :rtype: IscNetwork
        """
        pass

    def ReadIpsa1File(self, strName: str):
        """
        Imports an Ipsa 1 (\*.iif) file strName and returns an IscNetwork instance for that file.

        :param strName: The Ipsa i2f file that is going to be imported.
        :type strName: str
        :return: The IscNetwork instance for the strName file
        :rtype: IscNetwork
        """
        pass

    def GetNetwork(self):
        """
        Returns an IscNetwork instance for the current Ipsa network.

        :return: The IscNetwork instance of the Ipsa network.
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

    def GetDiagram(self, network, strName: str):
        """
        Returns an IscDiagram instance for the diagram with name strName contained in the network
        referred to by iscNetwork.

        :param network: The IscNetwork instance of the Ipsa network.
        :type network: IscNetwork
        :param strName: The name of the diagram.
        :type strName: str
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
        Creates a new Ipsa network based on the supplied parameters. Returns False if the network can’t be created.

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
        Merges the Ipsa I2F file sMergeName into the current network.

        :param sMergeName: The name of the file being merged.
        :type sMergeName: str
        :return: Returns True if successful, False on merge failure.
        :rtype: bool
        """
        pass

    def ValidatedMergeFile(self, sMergeName: str) -> bool:
        """
        Performs a consistency check to determine if the Ipsa I2F file sMergeName can be merged into
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

    def WriteArea(self, nAreaUID: int, strName: str) -> bool:
        """
        Saves the area group nAreaUID as a new Ipsa i2f network file with the file name strName.
        The integer nAreaUID can be obtained using the IscGroup functions.
        The file is saved in the current working directory. The file name should include the .i2f extension

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
        Returns a tuple of IscDiagram instances for the network referred to by IscNetwork.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :return: The network diagram.
        :rtype: tuple(IscDiagram)
        """
        pass

    def GetAllDiagramsNames(self, network) -> List[str]:
        """
        Returns a list of all the diagram names for the network referred to by IscNetwork.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :return: List of diagram names.
        :rtype: list(str)
        """
        pass

    def PrintPDF(self, diagram, strFileName) -> None:
        """
        Print the IscDiagram instance to a PDF format file with name strFileName.

        :param diagram: The diagram of the Ipsa network.
        :type diagram: IscDiagram
        :param strFileName: The name of the pdf file.
        :type strFileName: str
        """
        pass

    @overload
    def GetLineLength(self, diagram, pComponent) -> float:
        """
        Returns the component length as drawn on the diagram.
        When used on geographic diagrams this function returns the physical as drawn line length.

        :param diagram: IscDiagram instance obtained from the GetDiagram function.
        :type diagram: IscDiagram
        :param pComponent: IscBranch instance returned by a GetBranch function.
        :type pComponent: IscBranch
        :return: The component length.
        :rtype: float
        """
        pass

    @overload
    def GetLineLength(self, diagram, nLineUID: int) -> float:
        """
        Returns the component length as drawn on the diagram.
        When used on geographic diagrams this function returns the physical as drawn line length.

        :param diagram: IscDiagram instance obtained from the GetDiagram function.
        :type diagram: IscDiagram
        :param nLineUID: The unique integer for the line.
        :type nLineUID: int
        :return: The component length.
        :rtype: float
        """
        pass

    def GetLineLength(self, diagram, nLineUID: int) -> float:
        """
        Returns the component length as drawn on the diagram.
        When used on geographic diagrams this function returns the physical as drawn line length.

        :param diagram: IscDiagram instance obtained from the GetDiagram function.
        :type diagram: IscDiagram
        :param pComponent: IscBranch instance returned by a GetBranch function.
        :type pComponent: IscBranch
        :param nLineUID: The unique integer for the line.
        :type nLineUID: int
        :return: The component length.
        :rtype: float
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
        Setting bAllow to True prevents the Ipsa stack bar from updating during script execution.
        This can provide speed improvements since redrawing the stack bar is prevented.

        :param bAllow: Deciding whether the Ipsa stack bar can be updated during script execution.
        :type bAllow: bool
        """
        pass

    def GetDate(self) -> str:
        """
        Returns the date and time that Ipsa was launched, e.g. 06 Nov 2012 22:53:17.

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
        Displays the Ipsa results table which will contain the results of the last analysis.

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
            - ipsa.IscInterface.MGSetLF = motor- generator set load flow results
            - ipsa.IscInterface.BusbarFL = busbar fault level results
            - ipsa.IscInterface.GeneratorFL = generator fault level results
            - ipsa.IscInterface.GridInfeedFL = grid infeed fault level results
            - ipsa.IscInterface.LoadFL = load object fault level results
            - ipsa.IscInterface.IMachineFL = motor fault level results
            - ipsa.IscInterface.LineFL = branch fault level results
            - ipsa.IscInterface.TransformerFL = transformer fault level results
            - ipsa.IscInterface.ThreeWindingTransformerFL = 3 winding transformer fault level results
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
        If no file path is specified then the file is created in the Ipsa bin directory.

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
        (only identical to the Ipsa name for busbars).

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

    def GetFromBusbarUID(self, nBranchUID: int) -> int:
        """
        Returns the FROM busbar UID of the given branch.

        :param nBranchUID: The branch UID.
        :type nBranchUID: int
        :return: The FROM busbar UID.
        :rtype: int
        """
        pass

    def GetToBusbarUID(self, nBranchUID: int) -> int:
        """
        Returns the TO busbar UID of the given branch.

        :param nBranchUID: The branch UID.
        :type nBranchUID: int
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

    def AddDataExtension(self, strName: str, default: Union[int,float,str]) -> int:
        """
        Adds an integer data field and returns the new field index. Sets the default value.

        **Note: The variable of the function is not called default.**

        You can use either nDefault, dDefault, or strDefault specifying the default value.

        :param strName: The name of the field.
        :type strName: str
        :param nDefault: The integer default value.
        :type nDefault: int
        :param dDefault: The float default value.
        :type dDefault: float
        :param strDefault: The string default value.
        :type strDefault: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListIntDataExtension(self, strName: str) -> int:
        """
        Adds a list of integers data field and returns the new field index.
        Sets the default value to an empty list.

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

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
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
        Forces Ipsa to rebuild its internal component data maps.
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
        Saves the area group UID as a new Ipsa i2f network file.
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
        Performs a consistency check to determine if the Ipsa I2F file can be merged into the current network.
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
        Creates an Ipsa merge file based on the network differences between the given version and the current version.

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

    def GetLastSuccessfulAutomationUID(self) -> int:
        """
        Returns the integer UID of the last successful automation study.

        :return: The last successful automation study UID.
        :rtype: int
        """
        pass

    def GetLastSuccessfulContingencyUID(self) -> int:
        """
        Returns the integer UID of the last successful contingency study.

        :return: The last successful contingency study UID.
        :rtype: int
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

    def GetBusbars(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of busbars. The keys are the busbar names.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of busbars.
        :rtype: dict(str,IscBusbar)
        """
        pass

    def GetBusbarsOrderedByVoltage(self, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of busbar UIDs, sorted in ascending order of voltage and then by busbar name.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of busbars UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedBranches(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of branch UIDs attached to the busbar specified by busbar UID.
        Only branches are returned, not transformers.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of busbars UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedTransformers(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of transformer UIDs attached to the busbar specified by busbar UID.
        Only transformers are returned, not branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttached3WTransformers(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of 3-winding transformer UIDs attached to the busbar specified by busbar UID.
        Only 3-winding transformers are returned, not 2-winding transformers or branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of 3-winding transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedUnbalancedBranches(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of unbalanced branch UIDs attached to the busbar specified by busbar UID.
        Only unbalanced branches are returned, not unbalanced transformers.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of unbalanced branch UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBranches(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscBranch instances.
        Key values (sPyName) are the Python names and the associated values are IscBranch instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of branches.
        :rtype: dict(str,IscBranch)
        """
        pass

    def GetBusbarAttachedUnbalancedTransformers(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of unbalanced transformer UIDs attached to the busbar specified by busbar UID.
        Only unbalanced transformers are returned, not unbalanced branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Tuple of unbalanced transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetTransformers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscTransformer instances.
        Keys (sPyName) are the Python names and the associated values are IscTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of transformers.
        :rtype: dict(str,IscTransformer)
        """
        pass

    def Get3WTransformers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of Isc3WTransformer instances.
        Keys (sPyName) are the Python names and the associated values are Isc3WTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of 3WTransformers.
        :rtype: dict(str,Isc3WTransformer)
        """
        pass

    def GetLoads(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscLoad instances.
        Keys (sPyName) are the Python names and the associated values are IscLoad instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of loads.
        :rtype: dict(str,IscLoad)
        """
        pass

    def GetSynMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscSynMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscSynMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of synchronous machines.
        :rtype: dict(str,IscSynMachine)
        """
        pass

    def GetGridInfeeds(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscGridInfeed instances.
        Keys (sPyName) are the Python names and the associated values are IscGridInfeed instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of grid infeeds.
        :rtype: dict(str,IscGridInfeed)
        """
        pass

    def GetFilters(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscFilter instances.
        Keys (sPyName) are the Python names and the associated values are IscFilter instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of filters.
        :rtype: dict(str,IscFilter)
        """
        pass

    def GetIndMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscIndMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscIndMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of induction machines.
        :rtype: dict(str,IscIndMachine)
        """
        pass

    def GetMechSwCapacitors(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscMechSwCapacitor instances.
        Keys (sPyName) are the Python names and the associated values are IscMechSwCapacitor instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of mechanical switch capacitors.
        :rtype: dict(str,IscMechSwCapacitor)
        """
        pass

    def GetStaticVCs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscStaticVC instances.
        Keys (sPyName) are the Python names and the associated values are IscStaticVC instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of static var compensators.
        :rtype: dict(str,IscStaticVC)
        """
        pass

    def GetUMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscUMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of universal machines.
        :rtype: dict(str,IscUMachine)
        """
        pass

    def GetHarmonics(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscHarmonic instances.
        Keys (sPyName) are the Python names and the associated values are IscHarmonic instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of harmonics.
        :rtype: dict(str,IscHarmonic)
        """
        pass

    def GetCircuitBreakers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscCircuitBreaker instances.
        Keys (sPyName) are the Python names and the associated values are IscCircuitBreaker instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of circuit breakers.
        :rtype: dict(str,IscCircuitBreaker)
        """
        pass

    def GetBatteries(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscBattery instances.
        Keys (sPyName) are the Python names and the associated values are IscBattery instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of batteries.
        :rtype: dict(str,IscBattery)
        """
        pass

    def GetDCMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscDCMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscDCMachine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of DC machines.
        :rtype: dict(str,IscDCMachine)
        """
        pass

    def GetConverters(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscConverter instances.
        Keys (sPyName) are the Python names and the associated values are IscConverter instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of converters.
        :rtype: dict(str,IscConverter)
        """
        pass

    def GetMGSets(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscMGSet instances.
        Keys (sPyName) are the Python names and the associated values are IscMGSet instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of MG sets.
        :rtype: dict(str,IscMGSet)
        """
        pass

    def GetProtectionDevices(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscProtectionDevice instances.
        Keys (sPyName) are the Python names and the associated values are IscProtectionDevice instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of protection devices.
        :rtype: dict(str,IscProtectionDevice)
        """
        pass

    def GetUnbalancedLoads(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUnbalancedLoad instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedLoad instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced loads.
        :rtype: dict(str,IscUnbalancedLoad)
        """
        pass

    def GetUnbalancedLines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUnbalancedLine instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedLine instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced lines.
        :rtype: dict(str,IscUnbalancedLine)
        """
        pass

    def GetUnbalancedTransformers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUnbalancedTransformer instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced transformers.
        :rtype: dict(str,IscUnbalancedTransformer)
        """
        pass

    def GetVoltageRegulators(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscVoltageRegulator instances.
        Keys (sPyName) are the Python names and the associated values are IscVoltageRegulator instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of voltage regulators.
        :rtype: dict(str,IscVoltageRegulator)
        """
        pass

    def GetAnnotations(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscAnnotation instances.
        Keys (sPyName) are the Python names and the associated values are IscAnnotation instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of annotations.
        :rtype: dict(str,IscAnnotation)
        """
        pass

    def GetGroups(self):
        """
        Returns a dictionary of IscGroup instances.
        Keys (sPyName) are the Python names and the associated values are IscGroup instances.

        :return: Dictionary of groups.
        :rtype: dict(str,IscGroup)
        """
        pass

    def GetGroupsForItem(self, nUID: int) -> Tuple[int]:
        """
        Returns a tuple containing the group UIDs for each group that the component UID is a member of.

        :param nUID: Component UID.
        :type nUID: int
        :return: Tuple of group UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetPlugins(self):
        """
        Returns a dictionary of IscPlugin instances.
        Keys (sPyName) are the Python names and the associated values are IscPlugin instances.

        :return: Dictionary of plugins.
        :rtype: dict(str,IscPlugin)
        """
        pass

    def GetBusbarUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all busbar UIDs in the network.
        The keys are the integer UIDs and the values are the IscBusbar instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all busbar UIDs.
        :rtype: dict(int,IscBusbar)
        """
        pass

    def GetProtectionDeviceUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all protection device UIDs in the network.
        The keys are the integer UIDs and the values are the IscProtectionDevice instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all protection devices UIDs.
        :rtype: dict(int,IscProtectionDevice)
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
    def GetBranchGetUMachine(self, nUID: int):
        """
        Returns an IscUMachine instance for the universal machine identified by the UID.

        :param nUID: The selected universal machine UID.
        :type nUID: int
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    @overload
    def GetBranchGetUMachine(self, strPythonName: str):
        """
        Returns an IscUMachine instance for the universal machine identified by the Python name.

        :param strPythonName: The selected universal machine name.
        :type strPythonName: str
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    def GetBranchGetUMachine(self, strPythonName: str):
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

    def GetUnbalancedLoad(self, nUID: int):
        """
        Returns an IscUnbalancedLoad instance for the unbalanced load identified by the UID or the Python name.

        :param nUID: The selected unbalanced load UID.
        :type nUID: int
        :return: The unbalanced load instance or None if such is not found.
        :rtype: IscUnbalancedLoad
        """
        pass

    def GetUnbalancedLine(self, nUID: int):
        """
        Returns an IscUnbalancedLine instance for the unbalanced line identified by the UID or the Python name.

        :param nUID: The selected unbalanced line UID.
        :type nUID: int
        :return: The unbalanced line instance or None if such is not found.
        :rtype: IscUnbalancedLine
        """
        pass

    def GetUnbalancedTransformer(self, nUID: int):
        """
        Returns an IscUnbalancedTransformer instance for the unbalanced transformer identified by
        the UID or the Python name.

        :param nUID: The selected unbalanced transformer UID.
        :type nUID: int
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

    def GetBranchUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all branch UIDs in the network.
        The keys are the integer UIDs and the values are the IscBranch instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
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

    def GetTransformerUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all transformer UIDs in the network.
        The keys are the integer UIDs and the values are the IscTransformer instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all transformer UIDs.
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

    def Get3WTransformerUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all busbar UIDs in the network.
        The keys are the integer UIDs and the values are the IscBusbar instances.

        :param bFetchFromSystem: If set to True, IPSA rebuilds the data maps. If set to False, it only rebuilds if a new component has been built since last Get() function.
        :type bFetchFromSystem: bool
        :return: Dictionary of all 3WTransformers.
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

    def GetLoadUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all loads connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of load UIDs.
        :rtype: list(int)
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

    def GetSynMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all synchronous machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of synchronous machine UIDs.
        :rtype: list(int)
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

    def GetGridInfeedUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all grid infeeds connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of grid infeed UIDs.
        :rtype: list(int)
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

    def GetIndMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all induction machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of induction machine UIDs.
        :rtype: list(int)
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

    def GetFilterUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all filters connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of filter UIDs.
        :rtype: list(int)
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

    def GetMechSwCapacitorUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all mechanically switched capacitors connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of mechanically switched capacitor UIDs.
        :rtype: list(int)
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

    def GetStaticVCUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all static VAr compensators connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of static VAr compensator UIDs.
        :rtype: list(int)
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

    def GetUMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all universal machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of universal machine UIDs.
        :rtype: list(int)
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

    def GetHarmonicUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all harmonic sources connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of harmonic source UIDs.
        :rtype: list(int)
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

    def GetBatteryUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all batteries connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of battery UIDs.
        :rtype: list(int)
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

    def GetDCMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all DC Machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of DC Machine UIDs.
        :rtype: list(int)
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

    def GetConverterUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns all converters connected between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: List of converter UIDs.
        :rtype: list(int)
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

    def GetMGSetUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns all motors/generators connected between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: List of motor/generator UIDs.
        :rtype: list(int)
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

    def GetVoltageRegulatorUID(self, nBranchID: int) -> int:
        """
        Returns the UID of a voltage regulator at branch specified by its UID.

        :param nBranchID: The UID of the branch.
        :type nBranchID: int
        :return: The voltage regulator UID.
        :rtype: int
        """
        pass

    def GetProfileUID(self, nUID: int) -> int:
        """
        Returns the integer UID of the profile for the component UID.

        :param nUID: The UID of component. nUID may be the UID of a load, generator, grid infeed or Universal Machine.
        :type nUID: int
        :return: The profile for the component UID, 0 if the component nUID does not have a profile assigned to it, or if nUID is not a load, generator, grid infeed or universal machine.
        :rtype: int
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
    def CreateVoltageRegulator(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created voltage regulator.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The UID for the newly created voltage regulator, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateVoltageRegulator(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscVoltageRegulator object for the newly created voltage regulator.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The IscVoltageRegulator object for the newly created voltage regulator.
        :rtype: IscVoltageRegulator
        """
        pass

    def CreateVoltageRegulator(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscVoltageRegulator object for the newly created voltage regulator.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
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

    def CreatePlugin(self, nCompUID: int, sPluginName: str, sName: str) -> int:
        """
        Returns the UID for the newly created plugin.
        A different plugin UID is required for each component with a plugin,
        therefore this function should be used every time a plugin is assigned to a component,
        even if the same type of plugin is being assigned.

        :param nCompUID: The UID of the component to which the plugin is to be assigned to.
        :type nCompUID: int
        :param sPluginName: The name of the plugin itself, for example ‘Constant Current Load’.
        :type sPluginName: str
        :param sName: The user defined plugin name or empty string.
        :type sName: str
        :return: The plugin UID, 0 on failure.
        :rtype: int
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

    def DeletePlugin(self, pPlugin) -> bool:
        """
        Deletes a plugin by passing the IscPlugin object for deletion.

        :param pPlugin: The IscPlugin object for deletion.
        :type pPlugin: IscPlugin
        :return: True if successful.
        :rtype: bool
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
        Returns a dictionary of all IscGeneratorProfilePQActual objects in the network for actual generator profiles. The keys are the profile UIDs and the values are the IscGeneratorProfilePQActual objects.

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
        Returns a dictionary of all IscLoadProfilePQScale objects in the network for scaled load profiles. The keys are the profile UIDs and the values are the IscLoadProfilePQScale objects.

        :return: A dictionary of all IscLoadProfilePQScale objects in the network for scaled load profiles.
        :rtype: dict(int,IscLoadProfilePQScale)
        """
        pass

    def GetGeneratorProfilePQScales(self):
        """
        Returns a dictionary of all IscGeneratorProfilePQScale objects in the network for scaled generator profiles. The keys are the profile UIDs and the values are the IscGeneratorProfilePQScale objects.

        :return: A dictionary of all IscGeneratorProfilePQScale objects in the network for scaled generator profiles.
        :rtype: dict(int,IscGeneratorProfilePQScale)
        """
        pass

    def GetLoadProfilePQActual(self, strName: str):
        """
        Returns an IscLoadProfilePQActual object for the actual MW/MVAr load profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQActual object for the actual MW/MVAr load profile. Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQActual
        """
        pass

    def GetGeneratorProfilePQActual(self, strName: str):
        """
        Returns an IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile. Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQActual
        """
        pass

    def GetUMachineProfilePQActual(self, strName: str):
        """
        Returns an IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile with
        a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile. Returns None if a profile cannot be found.
        :rtype: IscUMachineProfilePQActual
        """
        pass

    def GetLoadProfilePQScale(self, strName: str):
        """
        Returns an IscLoadProfilePQScale object for the scaled MW/MVAr load profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQScale object for the scaled MW/MVAr load profile. Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQScale
        """
        pass

    def GetGeneratorProfilePQScale(self, strName: str):
        """
        Returns an IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile. Returns None if a profile cannot be found.
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

    def SetCategoryNames(self, dicCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary to an IscLoadProfilePQActual instance would add 3 categories to
        the profile with the strings as the categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dicCategories: The profile categories for the profile instance.
        :type dicCategories: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For scaling profiles the values are the per unit scaling values.
        For example, passing the following dictionary to an IscLoadProfilePQActual instance would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW values to the profile categories.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For scaling profiles the values are the per unit scaling values.
        For example, passing the following dictionary to an IscLoadProfilePQActual instance would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr values to the profile categories.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def RunProfile(self) -> int:
        """
        Runs the profile study. Returns the number of profile categories which have been run.

        :return: The number of profile categories which have been run.
        :rtype: int
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

    def GetAnalysisLF(self):
        """
        Returns an IscAnlaysisLF object which can be used to get and set the load flow analysis parameters.

        :return: IscAnlaysisLF object.
        :rtype: IscAnlaysisLF
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

        :param bNoEngineLoad: If False (default), loads the engine from the Ipsa model before doing a load flow calculation. If True, skips the load from the Ipsa model and uses whatever network is currently loaded in the engine.
        :type bNoEngineLoad: bool
        :param bDontUpdateData: If False (default), allows the load flow results being written back to the network model data (e.g. Busbar voltages and angles). If True, skips this stage, so the network model remains the same as it was loaded. **Note that calling the function with no arguments is allowed and works as if it has been called with bNoEngineLoad and bDontUpdateData set to False.**
        :type bDontUpdateData: bool
        :param bUseDC: Tells the user that they can run a DC load flow instead of a normal load flow. If True, the program will run a DC load flow instead of an AC load flow. Default value of bUseDC is False.
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

    def SetBranchStatus(self, nUID: int, nStatus: int) -> None:
        """
        Changes the status of the branch or transformer UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the branch status
        does not need to be stored with the network. **Note: If the nUID is not a branch or transformer UID, it does nothing!**

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
        Sets the verbosity of the load flow messages that are generated in the Ipsa progress window.
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
        Returns the total network generation, excluding slack generators, in MW.
        GetLFSummaryResults() must be called first.

        :return: The total network generation, excluding slack generators, in MW.
        :rtype: float
        """
        pass

    def GetTotalGenerationOutputMVAr(self) -> float:
        """
        Returns the total network generation, excluding slack generators, in MVAr.
        GetLFSummaryResults() must be called first.

        :return: The total network generation, excluding slack generators, in MVAr.
        :rtype: float
        """
        pass

    def GetTotalLoadInputMW(self) -> float:
        """
        Returns the total network load in MW. GetLFSummaryResults() must be called first.

        :return: The total network load in MW.
        :rtype: float
        """
        pass

    def GetTotalLoadInputMVAr(self) -> float:
        """
        Returns the total network load in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network load in MVAr.
        :rtype: float
        """
        pass

    def GetTotalInductionInputMW(self) -> float:
        """
        Returns the total network induction motor load in MW. GetLFSummaryResults() must be called first.

        :return: The total network induction motor load in MW.
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

    def GetSlackOutputMW(self) -> float:
        """
        Returns the total network slack generation in MW. GetLFSummaryResults() must be called first.

        :return: The total network slack generation in MW.
        :rtype: float
        """
        pass

    def GetSlackOutputMVAr(self) -> float:
        """
        Returns the total network slack generation in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network slack generation in MVAr.
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

        :return: A string detailing the busbar, branch or transformer with the most excessive overload/overvoltage in percentage terms.
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
        **Note that here either the analysis class default for the fault current calculation is used or IPSA can run a fault level to calculate the fault current at each busbar.**
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

    def DoStorageFlip(self, lGeneratorsUID: List[int]) -> bool:
        """
        Flips the storage of all defined Energy Storage units in the given list of UIDs.

        :param lGeneratorsUID: The given list of generators UIDs.
        :type lGeneratorsUID: list(int)
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DoGlobalStorageFlip(self, bFlipsImports: bool, bFlipExports: bool) -> bool:
        """
        Flips all the storage units defined in the network depending on whether you want to flip imports to exports or vice versa.

        :param bFlipsImports: Variable denoting whether you want to flip imports to exports.
        :type bFlipsImports: bool
        :param bFlipExports: Variable denoting whether you want to flip exports to imports.
        :type bFlipExports: bool
        :return: True if successful.
        :rtype: bool
        """
        pass

    def RunContingency(self, nUID: int, bUseProfiles: bool) -> None:
        """
        Performs the contingency study identified by the integer UID.

        :param nUID: The contingency study UID.
        :type nUID: int
        :param bUseProfiles: If False then the contingency study is performed using the standard load and generator data. If True then the contingency study is performed using load and generator profiles assigned in the network. In this instance the switching operation is performed first followed by a load flow calculation for all of the profile categories.
        :type bUseProfiles: bool
        """
        pass

    def CreateContingency(self, nDepth: int, bExtendToBreakers: bool) -> None:
        """
        Creates a new contingency study and returns the UID of the study created.
        The depth of the study is configured as follows:

            - 1 = N - 1
            - 2 = N - 2
            - 3 = N - 3
            - 4 = N - 1 - 1

        :param nDepth: The depth of the study.
        :type nDepth: int
        :param bExtendToBreakers: If False then individual branches and transfers are switched out during the study. If True then the nearest circuit breakers are switched out allowing multiple components to be switched for each study.
        :type bExtendToBreakers: bool
        """
        pass

    def CreateSpecificContingency(self, nDepth: int, bExtendToBreakers: bool, lBusbarsRequired) -> int:
        """
        Will design and create a specific contingency of given depth with only the busbars defined by the given list.

        :param nDepth: The depth of the study.
        :type nDepth: int
        :param bExtendToBreakers: If False then individual branches and transfers are switched out during the study. If True then the nearest circuit breakers are switched out allowing multiple components to be switched for each study.
        :type bExtendToBreakers: bool
        :param lBusbarsRequired: The specified list of busbars.
        :type lBusbarsRequired: list(IscBusbar)
        :return: The UID of the contingency.
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

    def GetContingencyStudyItemResults(self, nStudyID: int) -> List[int]:
        """
        Returns a list of integers containing the study result IDs for the contingency study ID.
        Each switching operation in a contingency study may produce a number of constraints.
        Each constraint can be examined using the result IDs returned by this function.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The study result IDs for the contingency study ID.
        :rtype: list(int)
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
        The normal Ipsa rating of a component is overridden if it has a dynamic rating plugin applied.
        In this case this function returns the UIDs of all such overloaded components in contingency study ID.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The lines which are overloaded due to the action of a dynamic rating plugin.
        :rtype: list(int)
        """
        pass

    def GetContingencyBranchRatingIndex(self) -> int:
        """
        Returns the Ipsa rating index of the rating set used during the contingency study.

        :return: The Ipsa rating index.
        :rtype: int
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
        Creates a CSV result for a given busbar arcflash calculation and uses the 2018 standard if bUseLegacyStandard is set to False.

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

    def SetBusbarOverloadLimits(self, dBusVoltHighPU: float, dBusVoltlowPU: float) -> None:
        """
        Sets the network global high and low limits for busbar overloads.

        :param dBusVoltHighPU: The high limit for busbar overloads per unit.
        :type dBusVoltHighPU: float
        :param dBusVoltlowPU: The low limit for busbar overloads per unit.
        :type dBusVoltlowPU: float
        """
        pass

    def SetBranchOverloadLimits(self, dBranchRatingHighPC: float, dBranchRatingLowPC: float, nRatingIndex: int) -> None:
        """
        Sets the network global percentage ratings for branches with a given rating index that is lifted from IscBranch (i.e., Standard, Summer, Winter, Short).

        :param dBranchRatingHighPC: The high network global percentage rating limit.
        :type dBranchRatingHighPC: float
        :param dBranchRatingLowPC: The low network global percentage rating limit.
        :type dBranchRatingLowPC: float
        :param nRatingIndex: The given rating index.
        :type nRatingIndex: int
        """
        pass

    def GetAnalysisAF(self):
        """
        Returns an IscAnalysisAF object which can be used to get and set the AirFlash analysis parameters.

        :return: IscAnlaysisAF object.
        :rtype: IscAnlaysisAF
        """
        pass

    def DoFlatStart(self, bSetBuses: bool, bSetTransformerTaps: bool, bSetIMSlips: bool) -> None:
        """
        Runs a flatstart preparation for load flow depending on whether the user wants to flat start the busbar voltages, transformer tap positions, induction machine rotor slips or a combination of all 3.

        :param bSetBuses: Enabling flat start for the busbar voltages.
        :type bSetBuses: bool
        :param bSetTransformerTaps: Enabling flat start for the transformer tap positions.
        :type bSetTransformerTaps: bool
        :param bSetIMSlips: Enabling flat start for the induction machine rotor slips.
        :type bSetIMSlips: bool
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
        Returns an integer parameter for the enumerated field defined by the specific plugin parameter. The parameters are specific for the plugin object.

        :param nPluginIndex: The index to the specific plugin parameter.
        :type nPluginIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDoubleParameter(self, nPluginIndex: int) -> float:
        """
        Returns a double parameter for the enumerated field defined by the specific plugin parameter. The parameters are specific for the plugin object.

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

    def GetLargestPowerMagnitudeMVA(self) -> float:
        """
        Returns the highest transformer power in MVA.

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

class IscUnbalancedLine:
    """
    Provides access to the three phase unbalanced lines.
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
