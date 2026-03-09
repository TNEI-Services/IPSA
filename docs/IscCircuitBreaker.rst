IscCircuitBreaker
==================

The ``IscCircuitBreaker`` class provides access to an IPSA circuit breaker, to set and get data values. There are no analysis results associated with circuit breakers in this version.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscCircuitBreaker Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - String
     - BusName *or* NearBusName
     - Gets the busbar name nearest to the circuit breaker.
   * - String
     - FarBusName
     - For a circuit breaker on a branch, gets the busbar name at the other end of the branch to the circuit breaker.
   * - String
     - BranchName
     - Gets the branch name the circuit breaker is located on.
   * - String
     - Name
     - Gets the circuit breaker name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Boolean
     - NOP
     - If ``True`` then the circuit breaker is normally open.
   * - Float
     - MakePeakkA
     - Sets and gets the peak rating in kA.
   * - Float
     - BreakRMSkA
     - Sets and gets the symmetrical break rating in kA.
   * - Float
     - BreakDCPC
     - Sets and gets the rated percentage DC component of the device.
   * - Float
     - BreakTimemS
     - Sets and gets the time for the break rating in milliseconds.
   * - Float
     - MakePeakSinglekA
     - Sets and gets the make peak rated current for single phase in kA.
   * - Float
     - BreakRMSSinglekA
     - Sets and gets the break RMS rated current for single phase in kA.
   * - Float
     - BreakDCSinglePC
     - Sets and gets the break DC rated percentage for single phase.
   * - Float
     - BreakTimeSinglemS
     - Sets and gets the break rated current time for single phase in milliseconds.
   * - Float
     - WithstandRMSkA
     - Sets and gets the withstand RMS rated current as part of STWC in kA.
   * - Float
     - WithstandRMSSinglekA
     - Sets and gets the withstand RMS single phase rated current as part of STWC in kA.
   * - Float
     - WithstandBreakTimeMs
     - Sets and gets the time for withstand RMS rated current as part of STWC in milliseconds.
   * - Float
     - WithstandBreakTimeSingleMs
     - Sets and gets the time for withstand RMS rated current (single phase) in milliseconds.
   * - Integer
     - BreakerType
     - Sets and gets the circuit breaker type:

        - 0 = Circuit breaker
        - 1 = Isolator
        - 2 = Disconnector
        - 3 = Recloser (reliability)
        - 4 = Remote control switch (reliability)
        - 5 = Fuse (reliability)
   * - Float
     - SwitchTimeHr
     - Sets and gets the switch time in hours, used for reliability analysis.
   * - Float
     - NomCurrentkA
     - Sets and gets the nominal current rating in kA
   * - Boolean
     - FeederCB
     - True if this breaker is a feeder breaker
   * - String
     - DbType
     - Gets the database type.
   * - Boolean
     - Aggregate
     - An equivalent for a collection of the same object.

IscCircuitBreaker Class
------------------------

.. autoclass:: ipsa.IscCircuitBreaker
   :members:
