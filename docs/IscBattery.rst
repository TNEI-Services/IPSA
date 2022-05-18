IscBattery
============

The IscBattery class provides access to an IPSA battery, to set and get data values and to retrieve load flow results.

Field Values
-------------

.. list-table:: **IscBattery Field Values**
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
     - Model
     - Sets and gets the model type for the battery:

        - 0 = Voltage type
        - 1 = Current type
   * - Float
     - VoltPU
     - Sets and gets the battery terminal voltage in per unit.
   * - Float
     - EmfPU
     - Sets and gets the battery internal EMF in per unit.
   * - Float
     - ResistancePU
     - Sets and gets the internal battery resistance in per unit.
   * - Float
     - CurrentPU
     - Sets and gets the battery current in per unit.
   * - Float
     - InductancePU
     - Sets and gets the internal battery inductance in per unit.

IscBattery Class
-----------------

.. autoclass:: ipsa.IscBattery
   :members:
