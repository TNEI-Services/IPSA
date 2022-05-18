**************
IscNetworkData
**************

The ``IscNetworkData`` class provides access to the IPSA network data such as the system base MVA, to set and get data values.

Field Values
============

.. list-table:: **IscNetworkData Field Values**
   :widths: 2 5 15
   :class: tight-table
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
   * - Float
     - Frequency
     - Gets or sets the system base frequency in hertz for the network.

IscAnalysisHM Class
====================

.. autoclass:: ipsa.IscNetworkData
   :members:
