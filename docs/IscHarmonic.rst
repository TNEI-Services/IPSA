IscHarmonic
============

The ``IscHarmonic`` class provides access to an IPSA harmonic source. Individual harmonic orders are indexed using an integer number. This corresponds to a specific harmonic order which is a float, meaning that harmonic orders may be any value as shown below:

.. list-table::
   :widths: 5 7
   :class: tight-table
   :header-rows: 1

   * - Order Index
     - Harmonic Order
   * - 1
     - 2
   * - 2
     - 2.5
   * - 3
     - 3.75
   * - 4
     - 15

Field Values
-------------

.. list-table:: **IscHarmonic Field Values**
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
     - Gets the harmonic source name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Integer
     - InjectionType
     - Sets and gets the harmonic injection type which is defined as follows:

        - 0 = Current injection
        - 1 = Voltage injection
   * - Integer
     - ImpedanceType
     - Sets and gets the harmonic impedance type which is defined as follows:

        - 0 = Not specified
        - 1 = Ideal impedance
        - 2 = Single R and X value for all harmonic orders
        - 3 = User defined R and X values for each harmonic order
   * - String
     - VoltageImpedanceR
     - Sets and gets the resistance for the harmonic impedance if ``ImpedanceType`` is 2.
   * - String
     - VoltageImpedanceX
     - Sets and gets the reactance for the harmonic impedance if ``ImpedanceType`` is 2.

IscHarmonic Class
------------------

.. autoclass:: ipsa.IscHarmonic
   :members:
