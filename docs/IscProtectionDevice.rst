IscProtectionDevice
====================

The ``IscProtectionDevice`` class provides access to a single protection device, such as a relay, allowing data to be set and cleared.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscProtectionDevice Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique ID of the nearest busbar to the protection device.
   * - String
     - BusName
     - Gets of the nearest busbar to the protection device.
   * - String
     - Name
     - Gets and sets the name of the protection device.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - String
     - DeviceManufacturer
     - Gets the name of the manufacturer for the relay assigned to the protection device.
   * - String
     - DeviceFamily
     - Gets the name of the relay family for the relay assigned to the protection device.
   * - String
     - DeviceDBName
     - Gets the data base name of the relay assigned to the protection device.
   * - String
     - DeviceVersion
     - Gets the version text of the relay assigned to the protection device.
   * - String
     - DeviceComments
     - Gets the comments for the relay assigned to the protection device.
   * - Float
     - OCNominalCurrentA
     - Gets the UID nominal operating current of the relay in Amps.

IscProtectionDevice Class
--------------------------

.. autoclass:: ipsa.IscProtectionDevice
   :members:
