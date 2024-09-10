IscFilter
============

The ``IscFilter`` class provides access to an IPSA harmonic filter, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscFilter Field Values**
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
     - Gets the harmonic filter name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Integer
     - FilterType
     - Filter Type:

        - 1 = Single tuned
        - 2 = Single tuned high pass
        - 3 = Double tuned
        - 4 = C Type
   * - Boolean
     - Ground
     - Get or set the grounded status of the filter. ``True`` if grounded , ``False`` if isolated.
   * - Float
     - R1 *or* Data1
     - Get or set the resistance R1 in per unit on the system MVA.
   * - Float
     - XL1 *or* Data2
     - Get or set the reactance XL1 in per unit on the system MVA.
   * - Float
     - XC1 *or* Data3
     - Get or set the capacitance XC1 in per unit on the system MVA.
   * - Float
     - XC2 *or* Data4
     - Get or set the capacitance XC2 in per unit on the system MVA - double tuned and C type only.
   * - Float
     - XL2 *or* Data5
     - Get or set the reactance XL2 in per unit on the system MVA - double tuned only.
   * - Float
     - TuningHarmonic
     - Get the harmonic the filter is tuned to to remove from the network - single tuned and single tuned high pass only.
   * - Float
     - QualityFactor
     - Get the measure of the damping achieved at the tuning harmonic frequency - single tuned and single tuned high pass only.
   * - Float
     - SizeMVAr
     - Get the size of the filter in MVAr associated with the tuning harmonic and quality factor - single tuned and single tuned high pass only.

IscFilter Class
----------------

.. autoclass:: ipsa.IscFilter
   :members:
