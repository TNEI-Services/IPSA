IscUMachine
============

The ``IscUMachine`` class provides access to an IPSA universal machine, to set and get data values and to retrieve load flow results.

Field Values
-------------

.. list-table:: **IscUMachine Field Values**
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
     - Gets the universal machine name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Float
     - RealMW
     - Gets and sets the real power output in MW.
   * - Float
     - ReactiveMVAr
     - Gets and sets the reactive power output in MVAr.
   * - Integer
     - ProfileUID
     - Gets and sets the UID of the profile applied to the universal machine. Set to 0 to not use any profiles.
   * - Integer
     - PluginID
     - Gets and sets the ID of the plugin applied to the universal machine. Set to 0 to not use any profiles.

IscUMachine Class
------------------

.. autoclass:: ipsa.IscUMachine
   :members:
