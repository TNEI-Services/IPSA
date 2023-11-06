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
   * - Float
     - Frequency
     - Gets or sets the system base frequency in hertz for the network.

IscNetworkData Class
====================

.. autoclass:: ipsa.IscNetworkData
   :members:
