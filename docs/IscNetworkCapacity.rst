IscNetworkCapacity
===================

The ``IscNetworkCapacity`` class provides access to the IPSA Network Capacity settings, to set and get data values and to 
retrieve the Network Capacity results

Field Values
---------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscNetworkCapacity Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Float
     - DemandPowerFactor
     - The power factor used for the step of apparent power used in the network capacity.
   * - Float
     - MaximumCapacityMVA
     - The maximum apparent power value in MVA that the network capacity tool will iterate from.
   * - Float
     - MinimumCapStepMVA
     - The minimum step size in MVA that the network capacity tool will iterate until (incrementally stops when it hits this value).
   * - Integer
     - RealStudyType
     - Choice of demand, generation or both for real power (which will create a copy of each for each busbar).

         - 0 = Export
         - 1 = Import
         - 2 = Both
   * - Integer
     - ReactiveStudyType
     - Choice of demand or generation for reactive power.

         - 0 = Export
         - 1 = Import
   * - Float
     - LowCapacityLimitPC
     - Percentage marker that indicates poor capacity retained.
   * - Float
     - HighCapacityLimitPC
     - Percentage marker that indicates good capacity retained.
   * - List[Integer]
     - SelectBusbarUIDs
     - List of busbar UIDs that are selected for the network capacity. If empty all will be selected.
   * - Boolean
     - DisplayCapacityPointInfo
     - Boolean of whether to display the basic info for each capacity point to the user.
   * - Boolean
     - DisplayBusbarTestInfo
     - Boolean of whether to display the basic info for each iteration busbar test to the user.
   * - Boolean
     - DisplayLineTestInfo
     - Boolean of whether to display the basic info for each iteration branch test to the user.


IscNetworkCapacity Class
--------------------------------

.. autoclass:: ipsa.IscNetworkCapacity
   :members:
