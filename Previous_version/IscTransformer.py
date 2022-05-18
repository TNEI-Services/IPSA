class IscTransformer:
    """
    The IscTransformer class provides access to an Ipsa transformer, to set and get data values and
    to retrieve load flow and fault level results.

    **Note that in Ipsa a transformer is modelled as a combination of a branch and a tap changer.**
    Therefore, the transformer impedance data is stored in a branch instance and functions such as GetLineDValue()
    are used to access branch type data.
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
