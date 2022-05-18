IscMechSwCapacitor
==================

The ``IscMechSwCapacitor`` class provides access to an IPSA mechanical switched capacitor, to set and get data values and to retrieve load flow results.


Field Values
-------------

.. list-table:: **IscMechSwCapacitor Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique ID of the sending busbar.
   * - String
     - BusName
     - Gets the busbar name.
   * - String
     - Name
     - Gets the mechanical switched capacitor name.
   * - Integer
     - Status
     - Status of mechanical switched capacitor:

        - 0 = Switched in
        - -1 = Switched out
   * - Integer
     - ControlMode
     - Sets or returns the control mode of the mechanical switched capacitor:

        - 0 = Local voltage control
        - 1 = Remote busbar voltage control
        - 2 = Reactive power flow control at receive end of branch
        - 3 = Reactive power control at send end of branch
   * - Integer
     - ControlSteps
     - Sets or returns the control mode of the mechanical switched capacitor:

        - 0 = Switch based on discrete steps
        - 1 = Continuous control based on min and max limits (see ``MinContinuousMVAr`` and ``MaxContinuousMVAr``)
   * - Integer
     - CapSteps
     - Sets or returns the number of capacitor steps.
   * - Integer
     - IndSteps
     - Sets or returns the number of inductor steps.
   * - Float
     - CapStepSizeMVAr
     - Sets or returns the capacitor step size in MVAr.
   * - Float
     - IndStepSizeMVAr
     - Sets or returns the inductor step size in MVAr.
   * - Float
     - TargetVoltagePU
     - Sets or returns the target voltage in per unit.
   * - Float
     - BandwidthPC
     - Sets or returns the bandwidth of acceptable voltage in percentage.
   * - Integer
     - InitPosition
     - Sets or returns the initial position of the mechanical switched capacitor. Positive values represent capacitor steps and negative values are inductive steps.
   * - Float
     - MaxContinuousMVAr
     - Sets or returns the maximum MVAr output of the MSC when in continuous control mode.
   * - Float
     - MinContinuousMVAr
     - Sets or returns the minimum MVAr output of the MSC when in continuous control mode.
   * - Float
     - ContinuousOutputMVAr
     - Sets or returns the operating output of the MSC when in continuous control mode.
   * - Integer
     - ControlActive
     - Sets or returns the voltage or power factor control status of the MSC:

        - 0 = Voltage or power factor control off
        - 1 = Voltage or power factor control is active
   * - Integer
     - ControlledUID
     - Sets or returns the busbar UID for the remote busbar whose voltage is being controlled.
   * - Integer
     - SendEnd
     - Sets or returns the branch end that is controlled when in power factor control mode:

        - 0 = Control power factor at receiving end
        - 1 = Control power factor at send end

IscMechSwCapacitor Class
-------------------------

.. autoclass:: ipsa.IscMechSwCapacitor
   :members:
