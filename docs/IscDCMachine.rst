IscDCMachine
============

The ``IscDCMachine`` class provides access to an IPSA DC machine, to set and get data values and to retrieve load flow results.

Field Values
-------------

.. list-table:: **IscDCMachine Field Values**
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
     - Gets the DC machine name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Float
     - BusVoltagePU
     - Sets and gets the busbar voltage in per unit.
   * - Float
     - MechPowerMW
     - Sets and gets the mechanical output power in MW.
   * - Float
     - Efficiency
     - Sets and gets the machine efficiency in percent.
   * - Float
     - Speed
     - Sets and gets the machine speed in per unit.
   * - Float
     - ArmResistPU
     - Sets and gets the armature resistance in per unit.
   * - Float
     - ShuntResisPU
     - Sets and gets the shunt resistance in per unit.
   * - Float
     - ControlResisPU
     - Sets and gets the control field resistance in per unit.
   * - Float
     - ShuntTRatio
     - Sets and gets the shunt field turns ratio.
   * - Float
     - SeriesTRatio
     - Sets and gets the series field turns ratio.
   * - Float
     - Compounding
     - Sets and gets the flag to indicate if the machine has a compound winding.
   * - Float
     - SatFac75
     - Sets and gets the saturation factor for the MMF at 75% of flux.
   * - Float
     - SatFac120
     - Sets and gets the saturation factor for the MMF at 120% of flux.
   * - Float
     - ArmSelfIndPU
     - Sets and gets the armature field self-inductance in per unit.
   * - Float
     - SeriesSelfIndPU
     - Sets and gets the series field self-inductance in per unit.
   * - Float
     - ShuntSelfIndPU
     - Sets and gets the shunt field self-inductance in per unit.
   * - Float
     - CtrlSelfIndPU
     - Sets and gets the control field self-inductance in per unit.
   * - Float
     - LeakageIndPU
     - Sets and gets the shunt field leakage inductance in per unit.
   * - Float
     - MechLossConst
     - Sets and gets the mechanical loss coefficient.
   * - Float
     - InertiaSec
     - Sets and gets the machine inertia.
   * - Float
     - TSlipB
     - Sets and gets the load torque slip coefficient B.
   * - Float
     - TSlipC
     - Sets and gets the load torque slip coefficient C.

IscDCMachine Class
--------------------

.. autoclass:: ipsa.IscDCMachine
   :members:
