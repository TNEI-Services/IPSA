IscCircuitBreaker
==================

The ``IscCircuitBreaker`` class provides access to an IPSA circuit breaker, to set and get data values. There are no analysis results associated with circuit breakers in this version.

Field Values
-------------

.. list-table:: **IscCircuitBreaker Field Values**
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
     - Gets the busbar name nearest to the circuit breaker.
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
   * - String
     - DbType
     - Gets the database type.

IscCircuitBreaker Class
------------------------

.. autoclass:: ipsa.IscCircuitBreaker
   :members:
