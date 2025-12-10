IscLoad
=========

The ``IscLoad`` class provides access to an IPSA load, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscLoad Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
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
     - Gets the load name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - 1 = Switched out
   * - Float
     - RealMW
     - Gets and sets the real power output in MW.
   * - Float
     - ReactiveMVAr
     - Gets and sets the reactive power output in MVAr.
   * - Integer
     - ProfileUID
     - Sets and gets the load profile UID for the load.
   * - Integer
     - Customers
     - Sets and gets the number of customers that this load represents. Used for reliability analysis.
   * - Integer
     - CustomerType
     - Sets and gets the customer type that this load represents.
   * - Boolean
     - IsEquivalent
     - If ``True`` then the load is an equivalent load.
   * - Integer
     - LoadPlanningStage
     - The stage the load is currently at:

        - 0 = Proposed
        - 1 = Accepted
        - 2 = Completed
        - 3 = Energised (default, in service)
   * - Float
     - RatedPowerMW
     - Gets and sets the real power rating value for the load in MW.
   * - Float
     - RatedPowerMVA
     - Gets and sets the apparent power rating value for the load in MVA.
   * - Boolean
     - EquivalentMotorFault
     - Gets and sets boolean on whether this load has a motor fault contribution.
   * - Integer
     - FaultPowerMode
     - Gets and sets whether the power used is:

        - 0 = Rated Power (MVA)
        - 1 = Actual Power (MVA)
   * - Float
     - FaultScaling
     - Gets and sets the scale factor for rescaling the chosen power to divide through the equivalent impedance parameters.
   * - Integer
     - EquivalentMotorModel
     - Gets and sets the motor model:

        - 0 = Inner/Outer
        - 1 = Running/Standstill
   * - Float
     - EquivalentStatorRPU
     - Gets and sets the motor equivalent stator resistance in PU.
   * - Float
     - EquivalentStatorXPU
     - Gets and sets the motor equivalent stator reactance in PU.
   * - Float
     - EquivalentMagXPU
     - Gets and sets the motor equivalent magnetising reactance in PU.
   * - Float
     - EquivInnerRPU
     - Gets and sets the motor equivalent inner resistance in PU.
   * - Float
     - EquivInnerXPU
     - Gets and sets the motor equivalent inner reactance in PU.
   * - Float
     - EquivOuterRPU
     - Gets and sets the motor equivalent outer resistance in PU.
   * - Float
     - EquivOuterXPU
     - Gets and sets the motor equivalent outer reactance in PU.
   * - Boolean
     - EquivUseManual
     - Gets and sets  whether to give the equivalent parameters with a manual override.
   * - Float
     - ActualPowerMVA
     - Gets the load flow result power that arises from the load flow and scaling and profile selection.
   * - String
     - Comment
     - Gets and sets the comments.
   * - Boolean
     - Aggregate
     - An equivalent for a collection of the same object.


IscLoad Class
--------------

.. autoclass:: ipsa.IscLoad
   :members:
