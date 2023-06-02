IscChopper
============

The ``IscChopper`` class provides access to a DC/DC Converter, to set and get data values and to retrieve load flow results.

Field Values
-------------

.. list-table:: **IscChopper Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique ID of the sending busbar.
   * - Integer
     - ToUID
     - Gets the unique ID of the receiving busbar.
   * - String
     - FromBusName
     - Gets the sending busbar name.
   * - String
     - ToBusName
     - Gets the receiving busbar name.
   * - String
     - Name
     - Gets the chopper name.
   * - Integer
     - ChopperModel
     - The chopper gain calculation model:

        - 0 = Voltage gain amplification parameter.
        - 1 = Duty cycle parametrisation (buck-boost).
   * - String
     - DispChopperModel
     - Gets the name of the chopper calculation model.
   * - Float
     - VoltGainRatio
     - Gets and sets the voltage gain ratio for the ratio model.
   * - Float
     - VoltGainDutyCycle
     - Gets and sets the duty cycle value for the duty model.
   * - Float
     - ConductancePU
     - Gets and sets the per unit parallel conductive losses for the capacitor component of the chopper.
   * - Float
     - ConverterEfficiencyPC
     - Gets and sets the efficiency of the chopper in percent.

IscChopper Class
-------------------

.. autoclass:: ipsa.IscChopper
   :members:
