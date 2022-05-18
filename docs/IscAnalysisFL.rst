IscAnalysisFL
==============

Field Values
-------------

.. list-table:: **IscAnalysisFL Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FaultEngine
     - Sets the fault level engine to either the standard Ipsa method or the IEC60909 method. Should be one of:

        - 0 = Standard Ipsa method
        - 1 = IEC60909 method
   * - Integer
     - FaultStudyType
     - Specifies the type of fault study. Should be one of:

        - ``FaultAllBusbars``
        - ``FaultSelectedBusbars``
        - ``FaultSingleBusbar``
        - ``FaultLine``
        - ``FaultTransformer``
        - ``FaultWaveformBus``
        - ``FaultWaveformBranch``
        - ``FaultBreakerDuty``
        - ``FaultMotorStart``
   * - Float
     - FaultTime
     - Time of fault in seconds.
   * - Float
     - FaultResistance
     - Fault resistance in per unit on the system base.
   * - Float
     - FaultReactance
     - Fault reactance in per unit on the system base.
   * - Integer
     - FaultEngineType
     - Type of fault to be applied. Should be one of:

        - LineGround
        - LineLine
        - LineLineGround
        - LineLineLine
   * - Integer
     - FaultEngineResultType
     - Type of fault result obtained. Should be one of:

        - SymRMS
        - AsymPeak
        - AsymRMS
        - BusWave
        - BranchWave
   * - Integer
     - MaxFaultIterations
     - Maximum number of iterations to run the fault level.
   * - Boolean
     - FaultFlatStart
     - Sets voltages at 1 p.u. before calculating fault levels, returns ``True`` if successful.
   * - Integer
     - UseSaturatedImpedances
     - Uses generator saturated impedances in fault calculation.
   * - Integer
     - AssumeAVRAction
     - Assumes generator impedances decay to transient rather than steady state values.
   * - Integer
     - SMSaliency
     - Sets the synchronous machine salience to either the given value or (Xq = Xd). Should be one of:

        - 0 = As given: The direct axis and quadrature axis parameters entered for each generator will be used in the fault calculations.
        - 1 = (Xq = Xd): Steady-state quadrature axis parameters are assumed to be the same as direct axis parameters for all generators.
   * - Integer
     - XRCalcMethod
     - Sets the X/R calculation method to either DC decay or Driving Point. Should be one of:

        - 0 = DC decay: The DC component decays with time, following a single exponential curve, and the X/R ratio will change. **(Note: Under this option the calculation takes the DC component at the time of fault, and the DC component at the specified time after the fault, and then fits a single exponential to these values.)**
        - 1 = Driving point: The X/R ratio is calculated at the time the fault occurs and does not change.
   * - Integer
     - XRSMEnhanced
     - Set to 0 to use the Ipsa 2.3.2 method of calculating the DC decay. Set to 1 to use the Ipsa 2.4.2 enhanced method of calculating the DC decay.
   * - Boolean
     - FaultUse2ndHarmonic
     - If selected then second harmonic fault level will be included in any peak fault calculation for line-to-line faults.
   * - Integer
     - SingleBusToFault
     - Busbar UID to apply fault on.
   * - Integer
     - BranchToFault
     - Branch UID to apply fault on.
   * - Float
     - DistanceAlongBranch
     - Distance along branch to apply fault on. This is a per unit value with zero representing the “From” end of the branch and 1.0 representing the “To” end of the branch.
   * - Float
     - IEC909DefaultPhaseAngle
     - Specifies the default synchronous machine power factor. ``IEC909UseDefaultPF`` should be set to ``True`` to use this value.
   * - Integer
     - IEC909Method
     - Sets the method used to determine the X/R ratio as defined by:

        - 1 = IEC 60909 Method A
        - 2 = IEC 60909 Method B
        - 3 = IEC 60909 Method C
   * - Boolean
     - IEC909IgnoreImpedanceCorrection
     - If set to ``True`` then IEC60909 impedance correction factors will not be applied to generators and power station transformers.
   * - Integer
     - IEC909VoltageCorrectionFactor
     - One of the following IEC60909 voltage level based correction factors to be applied to the pre-fault voltage at the faulted busbar:

        - 1 = Ignore
        - 2 = Cmax (LV + 6%)
        - 3 = Cmax (LV + 10%)
        - 4 = Cmin
   * - Boolean
     - IEC909UseDefaultPF
     - Set to ``True`` to use the synchronous machine default power factor.
   * - Boolean
     - IEC909NearTo
     - Setting to ``True`` causes all faults as assumed to be "Near-To". If it is not selected then the analysis will neglect any decay effects.
   * - Integer
     - IEC909TFRatingIndex
     - Identifies which rating set to use for transformers.
   * - Integer
     - FaultPlotSteps
     - Fault plot steps per iteration for waveform plots.
   * - Float
     - FaultPlotMaxTime
     - Fault plot max time in seconds for waveform plots.
   * - Boolean
     - FaultPlotinCycles
     - Fault plot time in cycles for waveform plots, returns ``True`` if successful.
   * - Boolean
     - FaultPlotinkA
     - Fault plot current in kA for waveform plots, returns ``True`` if successful.

        - 1 = not selected
        - 2 = selected
   * - Boolean
     - FaultPlotRed
     - Fault plot red phase for waveform plots, returns ``True`` if successful.
   * - Boolean
     - FaultPlotYellow
     - Fault plot yellow phase for waveform plots, returns ``True`` if successful.
   * - Boolean
     - FaultPlotBlue
     - Fault plot blue phase for waveform plots, returns ``True`` if successful.
   * - Boolean
     - FaultPlotDC
     - Fault plot DC component for waveform plots, returns ``True`` if successful.
   * - Boolean
     - FaultPlotRMS
     - Fault plot RMS component for waveform plots, returns ``True`` if successful.
   * - Boolean
     - FaultPlot2Harm
     - Fault plot 2nd harmonic component for waveform plots, returns ``True`` if successful.
   * - Boolean
     - FaultPlotMaxAsymmRed
     - Fault plot maximum asymmetry in red phase for waveform plots, returns ``True`` if successful.
   * - Integer
     - MotorToStart
     - The motor calculation is started for the motor UID.

IscAnalysisFL Class
--------------------

.. autoclass:: ipsa.IscAnalysisFL
   :members:
