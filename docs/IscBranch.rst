IscBranch
============

The ``IscBranch`` class provides access to an IPSA branch, to set and get data values and to retrieve analysis results.

**Note that the branch rating sets are defined in the** ``IscNetwork`` **class.**

Field Values
-------------

.. list-table:: **IscBranch Field Values**
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
   * - Boolean
     - HideLabel
     - ``True`` if the branch label (usually the name and any results) should be hidden on the diagram.
   * - Integer
     - Type
     - Gets the branch/line type as defined below.

        - 0 = Unset
        - 1 = Overhead lines
        - 2 = Cable
        - 3 = Ducted
        - 4 = Mixed
   * - Integer
     - Status
     - Line status as defined below:

        - 0 = Switched in.
        - 1 = Switched in, sending end will be opened in transient stability.
        - 2 = Switched in, receiving end will be opened in transient stability.
        - 3 = Switched in, both ends will be opened in transient stability.
        - -1 = Switched out, sending end will be closed in transient stability.
        - -2 = Switched out, receiving end will be closed in transient stability.
        - -3 = Switched out, both ends will be closed in transient stability.
   * - Float
     - ResistancePU
     - Positive sequence resistance.
   * - Float
     - MinResistancePU
     - Positive sequence minimum resistance.
   * - Float
     - ReactancePU
     - Positive sequence reactance.
   * - Float
     - SusceptancePU
     - Positive sequence susceptance.
   * - Float
     - ZSResistancePU
     - Zero sequence resistance.
   * - Float
     - ZSReactancePU
     - Zero sequence reactance.
   * - Boolean
     - ZeroImpedance
     - ``True`` if treated as a zero impedance line.
   * - Boolean
     - ZeroSequence
     - ``True`` if treated as a zero sequence only line.
   * - Float
     - SwitchTime1Sec
     - Line switching time 1.
   * - Float
     - SwitchTime2Sec
     - Line switching time 2.
   * - Float
     -
        HarmRC0
        HarmRC12
        HarmRC1
        HarmRC2
        HarmRC3
     - Harmonic polynomial constants RC0, RC12, RC1, RC2 and RC3 in:

       :math:`R_{h} = R[RC0 + RC12.h^{0.5} 0 + RC1.h + RC2.h^2 + RC3.h^3]`
   * - Float
     -
        HarmXC0
        HarmXC1
        HarmXC2
        HarmXC3
        HarmXCEX
        HarmXEX
     - Harmonic polynomial constants XC0, XC1, XC2, XC3, XCEX and XEX in:

       :math:`X{h} = X[XC0 + XC1.h + XC2.h^2 + XC3.h^3] + XCEX.X.h^{XEX}`
   * - Float
     - FailureRateYr
     - Branch failure rate per annum.
   * - Float
     - RepairTimeHr
     - Branch repair time in hours.
   * - String
     - DbType1
     - Branch database type. For representing the cable at the From end of the transformer.
   * - String
     - DbType2
     - Second cable database type representing the cable at the To end of the transformer.
   * - Float
     - DbLength1
     - First cable database length.
   * - Float
     - DbLength2
     - Second cable database length (for transformers only).
   * - Integer
     - DbPar1
     - Gets the number of lines of database type 1 in parallel.
   * - Integer
     - DbPar2
     - Gets the number of lines of database type 2 in parallel.
   * - String
     - DbTranType
     - Gets the transformer database type (only for transformers).
   * - Integer
     - DbTranPar
     - Gets the number of transformers in parallel (database only and only for transformers).
   * - String
     - UdmID
     - Gets the UDM ID.
   * - Integer
     - UdmDevEnd
     - Gets the device end.
   * - Integer
     - UdmCtrlType
     - Gets the UDM type.
   * - Integer
     - UdmCtrlUID
     - Gets the UDM control ID.
   * - String
     - PluginID
     - Plugin Name, empty string means no plugin is assigned.

IscBranch Class
----------------

.. autoclass:: ipsa.IscBranch
   :members:
