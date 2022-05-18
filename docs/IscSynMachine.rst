IscSynMachine
==============

The ``IscSynMachine`` class provides access to an IPSA generator (or more specifically, a synchronous machine), to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. list-table:: **IscSynMachine Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique ID for busbar.
   * - String
     - BusName
     - Gets the busbar name.
   * - String
     - Name
     - Gets the synchronous machine name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Float
     - VoltPU
     - Per unit voltage target.
   * - Float
     - VoltBandwidthPC
     - Bandwidth of acceptable busbar voltage.
   * - Integer
     - CtlBusbar
     - UID of controlled busbar.
   * - Float
     - GenMW
     - Generated real power.
   * - Float
     - GenMVAr
     - Generated reactive power.
   * - Float
     - GenMVArMax
     - Maximum reactive power limit for PV control.
   * - Float
     - GenMVArMin
     - Minimum reactive power limit for PV control.
   * - Float
     - GenRatedMW
     - Generator rated MW.
   * - Float
     - GenRatedMVA
     - Generator rated MVA.
   * - Integer
     - ProfileUID
     - Gets and sets the UID identifying the profile to be applied to the synchronous machine.
   * - Float
     - SynResistancePU
     - Positive sequence or armature resistance.
   * - Float
     - SynReactancePU
     - Positive sequence or d-axis synchronous reactance.
   * - Float
     - ZSResistancePU
     - Zero sequence resistance.
   * - Float
     - ZSReactancePU
     - Zero sequence reactance.
   * - Float
     - NEResistancePU
     - Neutral earthing resistance.
   * - Float
     - NEReactancePU
     - Neutral earthing reactance.
   * - Integer
     - WindingEarthing
     - Neutral earthing connection type:

        - 0 = Star wound, unearthed
        - 1 = Star wound, neutral earthed
   * - Float
     - DAxisTrXPU
     - D-axis transient reactance.
   * - Float
     - DAxisTrTCSec
     - D-axis transient open-circuit time constant.
   * - Float
     - DAxisStrXPU
     - D-axis sub transient reactance.
   * - Float
     - DAxisStrTCSec
     - D-axis sub transient open-circuit time constant.
   * - Float
     - QAxisXPU
     - Q-axis synchronous reactance.
   * - Float
     - QAxisTrXPU
     - Q-axis transient reactance.
   * - Float
     - QAxisTrTCSec
     - Q-axis transient open-circuit time constant.
   * - Float
     - QAxisStrXPU
     - Q-axis sub transient reactance.
   * - Float
     - QAxisStrTCSec
     - Q-axis sub transient open-circuit time constant.
   * - Float
     - InertiaSec
     - Inertia constant.
   * - Float
     - DampFactor
     - Damping factor.
   * - Float
     - PotierXPU
     - Potier reactance (required only if a saturation factor is entered).
   * - Float
     - SaturationFact
     - Per unit field current required to generate 1.2 per unit voltage in open circuit.
   * - Integer
     - TID
     - Gets the ID for two generators to share the same prime mover.
   * - Float
     - PMaxMW
     - Maximum machine real power.
   * - Float
     - SMaxMVA
     - Maximum machine apparent power.
   * - Float
     - SatDAxisXPU
     - Saturated d-axis synchronous reactance.
   * - Float
     - SatDAxisTrXPU
     - Saturated d-axis transient reactance.
   * - Float
     - SatDAxisTrTCSec
     - Saturated d-axis transient open-circuit time constant.
   * - Float
     - SatDAxisStTrXPU
     - Saturated d-axis sub transient reactance.
   * - Float
     - SatDAxisStrTCSec
     - Saturated d-axis sub transient open-circuit time constant.
   * - Float
     - SatQAxisStrXPU
     - Saturated q-axis sub transient reactance.
   * - String
     - DbGenType
     - Gets the database type.
   * - Integer
     - DbGenPar
     - Gets the number of database generators in parallel.
   * - Boolean
     - EnhancedModelling
     - ``True`` to indicate if rotor field current, calculated from the leakage reactance is modelled in transient stability. ``False`` if the leakage reactance is not used.
   * - Float
     - LeakageReactance
     - The leakage reactance in per unit, required for extended field modelling.
   * - Float
     - VoltageFactorPg
     - The voltage factor (P_g) of the machine, only for use in IEC60909 fault calculations.
   * - Integer
     - GenTechnology
     - The specific type of generator that can be categorized:

        - 0 = Synchronous machine (default)
        - 1 = Energy storage
        - 2 = Solar
        - 3 = Wind
        - 4 = Hydroelectric
        - 5 = Nuclear
        - 6 = Gas
        - 7 = Coal
        - 8 = Diesel
        - 9 = Geothermal
        - 10 = Tidal
        - 11 = Future generation (TBC)
   * - Integer
     - GenStage
     - The stage at which the generation production/planning is situated:

        - 0 = Proposed
        - 1 = Accepted
        - 2 = Completed
        - 3 = Energized (default, in service)
   * - Float
     - StorageIERatio
     - For energy storage components, this is the ratio between where a storage unit behaves as an import or an export. If the storage is flipped from export to import, the real power is multiplied by this ratio. Default is 1.

IscSynMachine Class
--------------------

.. autoclass:: ipsa.IscSynMachine
   :members:
