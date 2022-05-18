IscStaticVC
============

The ``IscStaticVC`` class provides access to an IPSA Static VAR Compensator (SVC), to set and get data values and to retrieve load flow results.


Field Values
-------------

.. list-table:: **IscStaticVC Field Values**
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
     - Gets the Compensator name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Float
     - QMinMVAr
     - Gets and sets the minimum reactive SVC output in MVAr. This corresponds to the maximum voltage setting.
   * - Float
     - QMaxMVAr
     - Gets and sets the maximum reactive SVC output in MVAr. This corresponds to the minimum voltage setting.
   * - Float
     - VminPU
     - Gets and sets the minimum voltage setting in per unit. This corresponds to the maximum reactive SVC output.
   * - Float
     - VmaxPU
     - Gets and sets the maximum voltage setting in per unit. This corresponds to the minimum reactive SVC output.

IscStaticVC Class
------------------

.. autoclass:: ipsa.IscStaticVC
   :members:
