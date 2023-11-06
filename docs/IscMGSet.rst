IscMGSet
============

The ``IscMGSet`` class provides access to an IPSA motor-generator set, to set and get data values and to retrieve load flow results.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscMGSet Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - String
     - FromBusName
     - Gets the sending busbar name.
   * - String
     - ToBusName
     - Gets the receiving busbar name.
   * - String
     - Name
     - Gets the MG set name.
   * - Integer
     - Status
     - Status of MG set:

        - 0 = Switched in
        - -1 = Switched out

IscMGSet Class
---------------

.. autoclass:: ipsa.IscMGSet
   :members:
