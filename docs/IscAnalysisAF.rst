IscAnalysisAF
==============

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscAnalysisAF Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - IEEEStandard
     - Standard according to IEEE-1584 for the arc flash calculation used:

        - 0 = 2002 standard
        - 1 = 2018 standard
   * - Float
     - BoundaryEnergyJcm2
     - Boundary energy defined at the standard level for a 2nd degree burn (defaults to 5 J/cm2).
   * - Float
     - ReducedFaultCurrentPC
     - Reduction of fault current for more conservative arc flash calculation (default to 15%).
   * - Integer
     - ProtPlotFault
     - Whether it should plot at fault location or by current:

        - 1 = plot overcurrent at busbar
        - 2 = plot overcurrent for given current
   * - Integer
     - ProtFaultBusbar
     - The busbar to fault.
   * - Float
     - ProtFaultCurrentA
     - Fault current in Amps.
   * - Float
     - FaultTime
     - Fault time in seconds.
   * - Float
     - FaultResistance
     - Fault resistance in per unit.
   * - Float
     - FaultReactance
     - Fault reactance in per unit.
   * - Boolean
     - FaultFlatStart
     - If True, apply flat start voltages before calculating fault.
   * - Integer
     - UseSaturatedImpedances
     - SM saturation representation:

        - 0 = None
        - 1 = G74
        - 2 = Always
   * - Integer
     - AssumeAVRAction
     - Assume generator impedances decay to transient rather than steady state values:

        - 0 = None
        - 1 = Decay to Xd
   * - Integer
     - SMSaliency
     - SM saliency representation:

        - 0 = As given
        - 1 = Xq = Xd
   * - Integer
     - XRCalcMethod
     - X/R ratio is calculation method:

        - 0 = DC decay (single exponential)
        - 1 = Driving point impedance
   * - Integer
     - XRSMEnhanced
     - Enhanced modelling of synchronous machine DC decay:

        - 0 = Not in use
        - 1 = In use
   * - Boolean
     - FaultUse2ndHarmonic
     - If True, use 2nd Harmonic in Peak Results.
   * - Integer
     - NFPAStandard
     - NFPA Standard:

        - 0 = 2000
        - 1 = 2004
        - 2 = 2009
        - 3 = 2012
        - 4 = User-Defined
   * - List[Float]
     - NFPAUserDefined
     - List of user-defined PPE incident energy levels in (cal/cm^2).
   * - Integer
     - ProtCalculateOpTime
     - How the analysis obtains the clearing time:

        - 0 = Calculate the clearing time (requires protection devices)
        - 1 = Specify the clearing time (requires a time)
   * - Float
     - ProtSetOpTimeS
     - Fault clearing time in seconds.
   * - Float
     - ProtSetReducedOpTimeS
     - Fault clearing time for reduced arc flash current in seconds.
   * - Boolean
     - LimitMaximumOpTime
     - If True, limit the maximum fault clearing time, to that set.
   * - Float
     - MaximumOpTimeS
     - Maximum fault clearing time in seconds.
   * - List[Integer]
     - ProtPlotOCDevices
     - Overcurrent devices to plot.

IscAnalysisAF Class
--------------------

.. autoclass:: ipsa.IscAnalysisAF
   :members:
