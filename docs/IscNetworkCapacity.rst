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
     - PowerFactor
     - The power factor of capacity type for busbar.
   * - Float
     - MaximumCapacityMVA
     - The maximum capacity value in MVA that will be used in the analysis.
   * - Float
     - MinimumCapStepMVA
     - The minimum step size before a given busbar iteration terminates.
   * - Integer
     - RealStudyType
     - The type of analysis done for active power:

         - 0 = Export
         - 1 = Import
         - 2 = Both
   * - Integer
     - ReactiveStudyType
     - The type of analysis done for reactive power:

         - 0 = Export
         - 1 = Import
   * - Float
     - LowCapacityLimitPC
     - User definition of the lower capacity divider as a percentage.
   * - Float
     - HighCapacityLimitPC
     - User definition of the higher capacity divider as a percentage.
   * - List[Integer]
     - SelectBusbarUIDs
     - List of busbar UIDs that are selected for the network capacity. If empty all will be selected.
   * - Boolean
     - DisplayCapacityPointInfo
     - Boolean option to show the capacity point information through the simulation.
   * - Boolean
     - DisplayBusbarTestInfo
     - Boolean option to show the information for each busbar capacity limit test through the simulation.
   * - Boolean
     - DisplayLineTestInfo
     - Boolean option to show the information for each branch capacity limit test through the simulation.
   * - Boolean
     - UsePercentiles
     - Boolean option on whether to use and render the percentiles.
   * - Boolean
     - FlatStartIncremental
     - Boolean option on whether to run a flat start before every incremental load flow (per busbar and per load value tested in the tool).


IscNetworkCapacity Class
--------------------------

.. autoclass:: ipsa.IscNetworkCapacity
   :members:
