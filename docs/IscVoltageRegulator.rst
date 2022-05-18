IscVoltageRegulator
====================

The ``IscVoltageRegulator`` class provides access to a series voltage regulator to get and set data values.

Field Values
-------------

.. list-table:: **IscVoltageRegulator Field Values**
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
     - FromBusName
     - Returns the busbar name at the From end of the branch the regulator is located on.
   * - String
     - ToBusName
     - Returns the busbar name at the To end of the branch the regulator is located on.
   * - String
     - Name
     - Name of the voltage regulator.
   * - Integer
     - Status
     - Status of voltage regulator:

        - 0 = Switched in
        - -1 = Switched out
   * - Float
     - ResistancePU
     - Gets or sets the resistance of the voltage regulator in per unit.
   * - Float
     - ReactancePU
     - Gets or sets the reactance of the voltage regulator in per unit.
   * - Float
     - TapStart
     - Present tap position, used as a starting point for the next load flow.
   * - Float
     - MinTap
     - Minimum tap position, normally negative or zero.
   * - Float
     - TapStep
     - Tap increment. This defaults to 0.01 if left blank.
   * - Float
     - MaxTap
     - Maximum tap position, normally positive or zero.
   * - Integer
     - ControlsUID
     - Returns the UID of the branch that the voltage regulator is located on.
   * - Integer
     - ControlMode
     - Gets or sets the control mode of the voltage regulator as defined by:

        - 0 = Manual tap control
        - 1 = Forward locked mode
        - 2 = Reverse locked mode
        - 3 = Neutral reverse mode
        - 4 = Cogeneration mode
        - 5 = Normal bi-directional mode
        - 6 = Reactive bi-directional mode
   * - Float
     - VoltageSetpointForward
     - Gets or sets the target voltage in per unit when operating in the forward direction.
   * - Float
     - CompensatingRForward
     - Gets or sets the compensating resistance in per unit when operating in the forward direction.
   * - Float
     - CompensatingXForward
     - Gets or sets the compensating reactance in per unit when operating in the forward direction.
   * - Float
     - VoltageSetpointBackward
     - Gets or sets the target voltage in per unit when operating in the reverse direction.
   * - Float
     - CompensatingRBackward
     - Gets or sets the compensating resistance in per unit when operating in the reverse direction.
   * - Float
     - CompensatingXBackward
     - Gets or sets the compensating reactance in per unit when operating in the reverse direction.

IscVoltageRegulator Class
--------------------------

.. autoclass:: ipsa.IscVoltageRegulator
   :members:
