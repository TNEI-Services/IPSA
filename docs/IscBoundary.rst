IscBoundary
===================

The ``IscBoundary`` class provides access to the IPSA Boundary class, to set and get data values which 
are important for interfacing with Network Reduction.

Field Values
---------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscBoundary Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - String
     - Name
     - The name of the boundary.
   * - String
     - Description
     - The description of the boundary.
   * - Boolean
     - UseBoundaryConfigMode
     - True if using directions method, False if using reduced area method. 
   * - List[int]
     - BoundaryBusbarUIDs
     - The list of boundary busbars.
   * - List[int]
     - BoundaryBranchUIDs
     - The list of branches that are connected from the boundary busbars.
   * - List[int]
     - ReducedBusbarUIDs
     - The list of reduced (that is equivalenced) busbars.
   * - Boolean
     - ShowBoundaryBranchMessages
     - If True, the boundary branch messages will be shown.
   * - Boolean
     - ShowBoundaryBusMessages
     - If True, the boundary bus messages will be shown.


IscBoundary Class
--------------------------

.. autoclass:: ipsa.IscBoundary
   :members:
