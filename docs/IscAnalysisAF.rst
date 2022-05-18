IscAnalysisAF
==============

Field Values
-------------

.. list-table:: **IscAnalysisAF Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - IEEEStandard
     - Standard according to IEEE-1584  for the arc flash calculation used:

        - 0 = 2002 standard
        - 1 = 2018 standard
   * - Float
     - BoundaryEnergyJcm2
     - Boundary energy defined at the standard level for a 2nd degree burn (defaults to 5 J/cm2).
   * - Float
     - ReducedFaultCurrentPC
     - Reduction of fault current for more conservative arc flash calculation (default to 15%).

IscAnalysisAF Class
--------------------

.. autoclass:: ipsa.IscAnalysisAF
   :members:
