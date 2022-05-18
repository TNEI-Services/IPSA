IscUnbalancedLine
==================

The ``IscUnbalancedLine`` class provides access to the three phase unbalanced lines to get and set data values.

Field Values
-------------

.. list-table:: **IscUnbalancedLine Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique component ID for the “From” busbar.
   * - Integer
     - ToUID
     - Gets the unique component ID for the “To” busbar.
   * - String
     - FromBusName
     - Gets the sending busbar name.
   * - String
     - ToBusName
     - Gets the receiving busbar name.
   * - String
     - Name
     - Gets the branch name.
   * - Integer
     - Type
     - Gets the branch/line type:

        - 0 = Unset
        - 1 = Overhead lines
        - 2 = Cable
        - 3 = Ducted
        - 4 = Mixed
   * - Integer
     - Status
     - Line status:

        - 0 = Switched in.
        - -1 = Sending/From end switched out
        - -2 = Receiving/To end switched out
        - -3 = Both ends switched out
   * - Boolean
     - HasPhaseA
     - Gets or sets if the line has the A phase connected. Set to ``True`` to enable the A phase.
   * - Boolean
     - HasPhaseB
     - Gets or sets if the line has the B phase connected. Set to ``True`` to enable the B phase.
   * - Boolean
     - HasPhaseC
     - Gets or sets if the line has the C phase connected. Set to ``True`` to enable the C phase.
   * - Boolean
     - HasNeutral
     - Gets or sets if the line has the neutral conductor connected. Set to ``True`` to enable the neutral conductor.
   * - Float
     - ResistancePhasePU
     - Gets or sets the positive sequence resistance in all phases.
   * - Float
     - ReactancePhasePU
     - Gets or sets the positive sequence reactance in all phases.
   * - Float
     - SusceptancePhasePU
     - Gets or sets the positive sequence susceptance in all phases.
   * - Float
     - ResistanceNeutralPU
     - Gets or sets the neutral conductor resistance in all phases.
   * - Float
     - ReactanceNeutralPU
     - Gets or sets the neutral conductor reactance in all phases.
   * - Float
     - SusceptanceNeutralPU
     - Gets or sets the neutral conductor susceptance in all phases.
   * - String
     - DbType
     - Gets the branch database type.
   * - Float
     - DbLength
     - Gets the branch database length.
   * - Integer
     - DbPar
     - Gets the branch database number in parallel.

IscUnbalancedLine Class
------------------------

.. autoclass:: ipsa.IscUnbalancedLine
   :members:
