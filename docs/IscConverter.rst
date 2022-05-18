IscConverter
============

The ``IscConverter`` class provides access to an AC/DC Converter, to set and get data values and to retrieve load flow results.

Field Values
-------------

.. list-table:: **IscConverter Field Values**
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
     - Gets the converter name.
   * - Integer
     - Status
     - Status of converter:

        - 0 = Converter is switched in.
        - 1 = Converter is connected but only used for harmonic analysis.
        - -1 = Converter is switched out.
   * - Integer
     - Type
     - The type of converter:

        - 0 = Thyristor or line commuted converter
        - 51 = PWM or voltage source converter
   * - Float
     - DCPowerMW
     - Gets and sets the DC power in MW.
   * - Float
     - DCVoltagePU
     - Gets and sets the DC terminal voltage in per unit.
   * - Float
     - ACReactivePowerMVAr
     - Gets and sets the AC reactive power in MVAr.
   * - Float
     - PowerFactor
     - Returns the operating power factor.
   * - Float
     - TransEqReactancePU
     - Gets and sets the internal transformer reactance in per unit.
   * - Float
     - TransOperateTapPC
     - Gets and sets the operating tap position of the internal transformer in percent.
   * - Float
     - MinTapPC
     - Gets and sets the minimum tap position of the internal transformer in percent.
   * - Float
     - TapStepPC
     - Gets and sets the tap step of the internal transformer in percent.
   * - Float
     - MaxTapPC
     - Gets and sets the maximum tap position of the internal transformer in percent.
   * - Integer
     - PulseNumber
     - Gets and sets the pulse number of the converter, should be either 6, 12, 24 or 48.
   * - Integer
     - NumParaBridges
     - Gets and sets the number of parallel bridges.
   * - Float
     - CommutateReactPU
     - Gets and sets the commutation reactance in per unit.
   * - Float
     - MaxACCurrentPU
     - Gets and sets the maximum AC current trip limit in per unit.
   * - Float
     - VoltRatio
     - Gets and sets the voltage ratio of the internal converter transformer.
   * - Float
     - FilterResisPU
     - Gets and sets the filter resistance in per unit.
   * - Float
     - FilterInductPU
     - Gets and sets the filter inductance in per unit.
   * - Float
     - DCEquivCapPU
     - Gets and sets the DC side capacitance in per unit.
   * - Float
     - MinFireAngleDeg
     - Gets and sets the minimum firing angle in degrees.
   * - Float
     - MaxDCCurrentPU
     - Gets and sets the maximum DC current limit in per unit.

IscConverter Class
-------------------

.. autoclass:: ipsa.IscConverter
   :members:
