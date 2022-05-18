from typing import overload


class IscBranch:
    """
    The IscBranch class provides access to an Ipsa branch, to set and get data values and to retrieve analysis results.
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
