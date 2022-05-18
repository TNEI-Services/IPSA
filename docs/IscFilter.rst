IscFilter
============

The ``IscFilter`` class provides access to an IPSA harmonic filter, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. list-table:: **IscFilter Field Values**
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
     - Data1
     - Get or set the resistance R1 in per unit on the system MVA.
   * - Float
     - Data2
     - Get or set the reactance XL1 in per unit on the system MVA.
   * - Float
     - Data3
     - Get or set the capacitance XC1 in per unit on the system MVA.
   * - Float
     - Data4
     - Get or set the capacitance XC2 in per unit on the system MVA - double tuned and C type only.
   * - Float
     - Data5
     - Get or set the reactance XL2 in per unit on the system MVA - double tuned only.

IscFilter Class
----------------

.. autoclass:: ipsa.IscFilter
   :members:
