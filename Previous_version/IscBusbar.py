from typing import List


class IscBusbar:
    """
    The IscBusbar class provides access to an Ipsa busbar,
    to set and get data values and to retrieve load flow and fault level results.
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
