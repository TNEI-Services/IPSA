IscGridInfeed
==============

The ``IscGridInfeed`` class provides access to an IPSA grid infeed, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. list-table:: **IscGridInfeed Field Values**
   :widths: 2 5 15
   :class: tight-table
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
     - Gets the grid infeed name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Float
     - VoltPU
     - Per unit voltage target.
   * - Float
     - GenMW
     - Generated real power.
   * - Float
     - GenMVAr
     - Generated reactive power.
   * - Integer
     - ProfileUID
     - Gets or sets the profile, ``ProfileUID``, to be applied to the universal machine.
   * - Float
     - PeakLLL
     - Peak asymmetric three phase fault contribution in MVA.
   * - Float
     - RMSLLL
     - RMS three phase fault contribution in MVA at the break time specified by ``Tbreak``.
   * - Float
     - X2RLLL
     - Three phase X / R ratio determining the DC decay. A single exponential decay is modelled.
   * - Float
     - PeakLG
     - Peak asymmetric single phase to ground fault contribution in MVA.
   * - Float
     - RMSLG
     - RMS single phase to ground contribution in MVA at the break time specified by ``Tbreak``.
   * - Float
     - Tac
     - AC decay time constant for three phase faults, in seconds.
   * - Float
     - Tbreak
     - RMS fault time in seconds.

IscGridInfeed Class
--------------------

.. autoclass:: ipsa.IscGridInfeed
   :members:
