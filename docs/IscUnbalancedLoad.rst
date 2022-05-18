IscUnbalancedLoad
==================

The ``IscUnbalancedLoad`` class provides access to the three phase unbalanced load components to get and set data values.

Field Values
-------------

.. list-table:: **IscUnbalancedLoad Field Values**
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
     - Gets the branch name.
   * - Integer
     - Status
     - Line status:

        - 0 = Switched in
        - -1 = Switched out
   * - Boolean
     - HasPhaseA
     - Gets or sets if the line has the A phase connected. Set to ``True`` to enable the A phase.
   * - Boolean
     - HasPhaseB
     - Gets or sets if the line has the B phase connected. Set to ``True`` to enable the B phase.
   * - Boolean
     - HasPhaseC
     - Gets or sets if the line has the C phase connected. Set to ``True`` to enable the C phase.
   * - Float
     - RealPhaseAMW
     - Gets or sets the A phase power in MW.
   * - Float
     - ReactivePhaseAMVAr
     - Gets or sets the A phase power in MVAr.
   * - Float
     - RealPhaseBMW
     - Gets or sets the B phase power in MW.
   * - Float
     - ReactivePhaseBMVAr
     - Gets or sets the B phase power in MVAr.
   * - Float
     - RealPhaseCMW
     - Gets or sets the C phase power in MW.
   * - Float
     - ReactivePhaseCMVAr
     - Gets or sets the C phase power in MVAr.
   * - Integer
     - ProfilePhaseAUID
     - Gets or sets the load profile UID applied to the A phase of this load.
   * - Float
     - ProfilePhaseBUID
     - Gets or sets the load profile UID applied to the B phase of this load.
   * - Integer
     - ProfilePhaseCUID
     - Gets or sets the load profile UID applied to the C phase of this load.

IscUnbalancedLoad Class
------------------------

.. autoclass:: ipsa.IscUnbalancedLoad
   :members:
