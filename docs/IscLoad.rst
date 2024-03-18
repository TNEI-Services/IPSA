IscLoad
=========

The ``IscLoad`` class provides access to an IPSA load, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscLoad Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
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
     - Gets the load name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - 1 = Switched out
   * - Float
     - RealMW
     - Gets and sets the real power output in MW.
   * - Float
     - ReactiveMVAr
     - Gets and sets the reactive power output in MVAr.
   * - Integer
     - ProfileUID
     - Sets and gets the load profile UID for the load.
   * - Integer
     - Customers
     - Sets and gets the number of customers that this load represents. Used for reliability analysis.
   * - Integer
     - CustomerType
     - Sets and gets the customer type that this load represents.
   * - Boolean
     - IsEquivalent
     - If ``True`` then the load is an equivalent load.
   * - Integer
     - LoadPlanningStage
     - The stage the load is currently at:

        - 0 = Proposed
        - 1 = Accepted
        - 2 = Completed
        - 3 = Energised (default, in service)

IscLoad Class
--------------

.. autoclass:: ipsa.IscLoad
   :members:
