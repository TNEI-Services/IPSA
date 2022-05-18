IscIndMachine
==============

The ``IscIndMachine`` class provides access to an IPSA induction machine, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. list-table:: **IscIndMachine Field Values**
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
     - Gets the induction machine name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - 1 = Switched in, but can be switched out during transient studies
        - -1 = Switched out, but can be switched in during transient studies
   * - Float
     - MechPowerMW
     - Mechanical power output of motor. Use negative values for induction generators.
   * - Float
     - SlipPC
     - Slip in %.
   * - Float
     - MagnetXPU
     - Magnetising reactance.
   * - Float
     - StatorRPU
     - Stator resistance.
   * - Float
     - StatorXPU
     - Stator reactance.
   * - Integer
     - Model
     - The motor model used:

        - 0 = Running - standstill
        - 1 = Inner - outer
        - 2 = Not used
        - 3 = Not used
        - 4 = Running - standstill DFIG with slip control
        - 5 = Inner - outer DFIG with slip control
        - 6 = Running - standstill DFIG with slip and power factor control
        - 7 = Inner - outer DFIG with slip and power factor control
   * - Float
     - RotorRPU
     - Inner cage or running rotor resistance.
   * - Float
     - RotorXPU
     - Inner cage or running rotor reactance.
   * - Float
     - StandRPU
     - Outer cage or standstill rotor resistance.
   * - Float
     - StartXPU
     - Outer cage or standstill rotor reactance.
   * - Float
     - TSlipB
     - Load torque-speed coefficient B.
   * - Float
     - TSlipC
     - Load torque-speed squared coefficient C.
   * - Float
     - InertiaSec
     - Inertia constant in kWs / kVA.
   * - Float
     - DropoffVPU
     - If the voltage falls below this value disconnection will begin.
   * - Float
     - DropPickUpDelaySec
     - The time taken to disconnect the machine.
   * - Float
     - LockTimeSec
     - If a machine is disconnected for this length of time it will not be reconnected.
   * - Float
     - UnderspeedPU
     - Under speed setting in per unit.
   * - Float
     - OverspeedPU
     - Overspeed setting in per unit.
   * - Float
     - PickUpTimeSec
     - The time taken to reconnect the machine.
   * - Float
     - PickUpVoltagePU
     - If the voltage in per unit rises above this value reconnection will begin.
   * - Float
     - SwitchOut1Sec
     - Time for the first switch-out operation. If the machine is already switched out, leave this entry blank.
   * - Float
     - SwitchIn1Sec
     - Time for first switch-in.
   * - Float
     - SwitchOut2Sec
     - Time for second switch-out.
   * - Float
     - SwitchIn2Sec
     - Time for second switch-in.
   * - Integer
     - MaxSwitchOp
     - Maximum number of automatic switching operations before the machine is locked out.
   * - Integer
     - DFFeedBusbar
     - Feed busbar UID for doubly-fed model.
   * - Float
     - DFPowerFactor
     - Power factor for doubly-fed model.
   * - Boolean
     - DFExportQ
     - If ``True`` then reactive power is exported by the machine, else it is imported.
   * - Integer
     - DFRotorReferenceFrame
     - Rotor reference frame, either:

        - 0 = Direct-Quadrature aligned to stator voltage
        - 1 = Real-Imaginary aligned to stator voltage
   * - Integer
     - DFFaultSwitchMode
     - How the DFIG behaves when a fault is detected:

        - 0 = Turn off rotor, stator and turbine.
        - 1 = Turn off rotor, switch permanently to induction generator mode.
        - 2 = Turn off rotor, switch to induction generator mode, reset on time.
        - 3 = Turn off rotor, switch to induction generator mode, reset on current.
   * - Float
     - DFFaultRotorCurrentLimit
     - When DFIG rotor current exceeds this value the DFIG alters its behaviour as determined by the fault switch mode.
   * - Float
     - DFFaultCrowbarLimit
     - The effect of this parameter is determined by the fault switch mode. See the online help manual for details.
   * - Float
     - DFFaultCrowbarResPU
     - Crowbar fault resistance (per unit on system base and rotor voltage base).
   * - String
     - DbType
     - Gets the database type.
   * - Integer
     - DbPar
     - Gets the number of motors in parallel.
   * - Integer
     - ControlModelType
     - Gets the Dynamic Model type.

        - 0 = Built in
        - 1 = Plugin
        - 2 = UDM
   * - Float
     - RatedMW
     - The rated MW power of the machine. Only used in IEC60909 fault analysis.
   * - Float
     - RatedMVA
     - The rated MVA power of the machine. Only used in IEC60909 fault analysis.
   * - Integer
     - PolePairs
     - The number of pole pairs of the machine. Only used in IEC60909 fault analysis.
   * - String
     - ControlPluginID
     - Gets the control plugin ID.

IscIndMachine Class
--------------------

.. autoclass:: ipsa.IscIndMachine
   :members:
