IscIntertrip
==================

The ``IscIntertrip`` class provides access to an IPSA Intertrip group, to get and set member breakers and values that govern its behaviour.


Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscIntertrip Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - String
     - Name
     - The intertrip name.
   * - Integer
     - TypeMaster
     - The master control type:

        - 0 = master breakers can have different switch states
        - 1 = master breakers must all have the same switch state
   * - Integer
     - TypeSlave
     - The slave control type:

        - 0 = slave breakers will change state whenever a master breaker changes
        - 1 = slave breakers will take the opposite state to the changed master breaker
        - 2 = slave breakers will take the same state as the changed master breaker
        - 3 = slave breakers will all switch in if any master breaker is switched out
   * - List[Integer]
     - Masters
     - The UIDs of the master breakers in the intertrip.
   * - List[Integer]
     - Slaves
     - The UIDs of the slave breakers in the intertrip.
   * - Float
     - SignalTimeS
     - The time for the operation signal from master to slaves in seconds.

IscIntertrip Class
-------------------------

.. autoclass:: ipsa.IscIntertrip
   :members:
