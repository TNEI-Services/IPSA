class IscUnbalancedLine:
    """
    The IscUnbalancedLine class provides access to the three phase unbalanced lines to get and set data values.
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
