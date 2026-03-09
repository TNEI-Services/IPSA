**************
IscNetworkData
**************

The ``IscNetworkData`` class provides access to the IPSA network data such as the system base MVA, to set and get data values.

Field Values
============

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscNetworkData Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - String
     - Title
     - Gets or sets the network title.
   * - String
     - Author
     - Gets or sets the network author.
   * - String
     - CreationTime
     - Gets the date and time when the network was first created.
   * - String
     - Comment
     - Gets the comment entered for the network data.
   * - Float
     - Base
     - Gets or sets the system base MVA for the network.
   * - Boolean
     - BaseinKVA
     - ``True`` if the Base is in KVA otherwise the base is in MVA.
   * - Float
     - Frequency
     - Gets or sets the system base frequency in hertz for the network.
   * - Boolean
     - SetNewAggregatesTrue
     - Gets or sets the default aggregate value for new components.
   * - Boolean
     - DoGroupsTriggerIntertrips
     - Gets or sets whether switching groups should trigger intertrips.
   * - Boolean
     - ScenariosIgnoreStudyChanges
     - Gets or sets whether scenarios/undo should ignore changes caused by analysis results.
   * - Boolean
     - ScenariosUseSameView
     - Gets or sets whether the same diagram views should be used in all scenarios/undo.
   * - Boolean
     - ScenariosUseSameAnalysisData
     - Gets or sets whether the same analysis data values (e.g., the IscAnalysis class values) should be used in all scenarios/undo.
   * - Boolean
     - ScenariosUseSameDiagramData
     - Gets or sets whether the same diagram properties should be used in all scenarios/undo.
   * - Boolean
     - ScenariosUseSameDisplayStyles
     - Gets or sets whether the same data and results display styles should be used in all scenarios/undo.


IscNetworkData Class
====================

.. autoclass:: ipsa.IscNetworkData
   :members:
