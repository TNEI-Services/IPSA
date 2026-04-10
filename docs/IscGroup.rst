IscGroup
============

The ``IscGroup`` class provides access to all IPSA group types to get and set the group members and to modify group specific information.


Field Values
--------------
Get and Set functions through field index are only exposed for demand groups and fault level groups. 
The exposed field values are specific to the group type, so it is advised to always check group type before using the Get and Set functions 
to ensure the desired behaviour occurs.


.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscGroup Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Float
     - FirmCapacityNonSeasonalMVA
     - Demand group property: The firm capacity non-seasonal apparent power in MVA.
   * - Float
     - FirmCapacitySummerMVA
     - Demand group property: The firm capacity summer apparent power in MVA.
   * - Float
     - FirmCapacityWinterMVA
     - Demand group property: The firm capacity winter apparent power in MVA.
   * - Float
     - MaxLoadingNonSeasonalMVA
     - Demand group property: The maximum non-coincidental load non-seasonal apparent power in MVA.
   * - Float
     - MaxLoadingSummerMVA
     - Demand group property: The maximum non-coincidental load summer apparent power in MVA.
   * - Float
     - MaxLoadingWinterMVA
     - Demand group property: The maximum non-coincidental load winter apparent power in MVA.
   * - Float
     - MaxLoadingNonSeasonalPowerFactor
     - Demand group property: The maximum non-coincidental load non-seasonal power factor.
   * - Float
     - MaxLoadingSummerPowerFactor
     - Demand group property: The maximum non-coincidental load summer power factor.
   * - Float
     - MaxLoadingWinterPowerFactor
     - Demand group property: The maximum non-coincidental load winter power factor.
   * - String
     - FirmCapacityDescription
     - Demand group property: The firm capacity description.
   * - String
     - MaxLoadingDescription
     - Demand group property: The maximum non-coincidental load description.
 
 
   * - Integer
     - FaultKind
     - Fault level group property: Describes whether the fault level results are from a three-phase or single-phase fault.

        - 0 = Three-phase fault
        - 1 = Single-phase fault
   * - Float
     - DCComponentkA
     - Fault level group property: The decaying (aperiodic) component of short-circuit current in kA. It is a mean value between the top and the bottom envelope of a 
       short-circuit current decaying from an initial value to zero.
   * - Float
     - InitSymmPowerMVA
     - Fault level group property: The initial symmetrical short-circuit power in MVA. It is a fictitious value determined as a product of the initial symmetrical 
       short-circuit current, the nominal system voltage, and the factor square root of 3.
   * - Float
     - InitSymmCurrentkA
     - Fault level group property: The initial symmetrical short-circuit current in kA. It is a root mean square (RMS) value of the alternate current (AC) symmetrical component 
       of a prospective (available) short-circuit current, applicable at the instant of short circuit if the impedance remains at zero-time value. 
   * - Float
     - SymmBreakCurrentkA
     - Fault level group property: The symmetrical short-circuit breaking current in kA. It is an RMS value of an integral cycle of the symmetrical AC component of the 
       prospective short-circuit current at the instant of contact separation of the first pole to open of a switching device.
   * - Float
     - SymmBreakAngleDeg
     - Fault level group property: The symmetrical short-circuit breaking current angle in dgrees. It is the angle of an RMS value of an integral cycle of the symmetrical 
       AC component of the prospective short-circuit current at the instant of contact separation of the first pole to open of a switching device.
   * - Float
     - PeakCurrentkA
     - Fault level group property: The peak short-circuit current in kA. It is the maximum possible instantaneous value of prospective (available) short-circuit current.
   * - Float
     - MaxSteadyCurrentkA
     - Fault level group property: The maximum steady state short-circuit current in kA.
   * - Float
     - MinSteadyCurrentkA
     - Fault level group property: The minimum steady state short-circuit current in kA.
   * - Float
     - SteadyCurrentkA
     - Fault level group property: The steady state short-circuit current in kA. It is an RMS value of the short-circuit current which remains after the decay of the 
       transient phenomena.
   * - Float
     - PosSeqResistanceOhm
     - Fault level group property: The resistance in Ohms of the positive-sequence system as viewed from the short-circuit location.
   * - Float
     - PosSeqReactanceOhm
     - Fault level group property: The reactance in Ohms of the positive-sequence system as viewed from the short-circuit location.
   * - Float
     - ZeroSeqResistanceOhm
     - Fault level group property: The resistance in Ohms of the zero-sequence system as viewed from the short-circuit location.
   * - Float
     - ZeroSeqReactanceOhm
     - Fault level group property: The reactance in Ohms of the zero-sequence system as viewed from the short-circuit location.
   * - String
     - FaultLevelDescription
     - Fault level group property: A description of the fault level analysis that produces the fault level results.
   
  

IscGroup Class
-----------------

.. autoclass:: ipsa.IscGroup
   :members:
