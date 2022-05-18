IscUnbalancedTransformer
=========================

The ``IscUnbalancedTransformer`` class provides access to the three phase unbalanced transformer to get and set data values.

Field Values
-------------

.. list-table:: **IscUnbalancedTransformer Field Values**
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
     - Gets the transformer name.
   * - Integer
     - Type
     - Specifies the transformer type:

        - 1 = Not set
        - 2 = Ground Mounted
        - 3 = Pole Mounted
        - 7 = Secondary Distribution
   * - Integer
     - Winding
     - Transformer winding type connection as follows:

        - 1 = XX
        - 2 = YY
        - 3 = DD
        - 4 = XD
        - 5 = YD

        where:

        - X = Earthed star
        - Y = Unearthed star
        - D = Delta
   * - Integer
     - Status
     - Line status:

        - 0 = Switched in.
        - -1 = Sending/From end switched out
        - -2 = Receiving/To end switched out
        - -3 = Both ends switched out
   * - Float
     - ResistancePhasePU
     - Gets or sets the positive sequence resistance in all phases.
   * - Float
     - ReactancePhasePU
     - Gets or sets the positive sequence reactance in all phases.
   * - Float
     - EarthPrimaryResistancePU
     - Gets or sets the primary winding earth resistance in all phases.
   * - Float
     - EarthPrimaryReactancePU
     - Gets or sets the primary winding earth reactance in all phases.
   * - Float
     - EarthSecondaryResistancePU
     - Gets or sets the secondary winding earth resistance in all phases.
   * - Float
     - EarthSecondaryReactancePU
     - Gets or sets the secondary winding earth reactance in all phases.
   * - Float
     - TapPrimaryNominalPC
     - Nominal tap position on the primary winding, optionally used in a flat start.
   * - Float
     - TapPrimaryPositionPC
     - Present tap position on the primary winding, used as a starting point for the next load flow.
   * - Float
     - MinTapPrimaryPC
     - Minimum tap position on the primary winding, normally negative or zero.
   * - Float
     - TapPrimaryStepPC
     - Tap step or increment on the primary winding. This defaults to 0.01 if left blank.
   * - Float
     - MaxTapPrimaryPC
     - Maximum tap position on the primary winding, normally positive or zero.
   * - Float
     - TapSecondaryNominalPC
     - Nominal tap position on the secondary winding, optionally used in a flat start.
   * - Float
     - TapSecondaryPositionPC
     - Present tap position on the secondary winding, used as a starting point for the next load flow.
   * - Float
     - MinTapSecondaryPC
     - Minimum tap position on the secondary winding, normally negative or zero.
   * - Float
     - TapSecondaryStepPC
     - Tap step or increment on the secondary winding. This defaults to 0.01 if left blank.
   * - Float
     - MaxTapSecondaryPC
     - Maximum tap position on the secondary winding, normally positive or zero.
   * - String
     - DbType
     - Gets the branch database type.
   * - Integer
     - DbPar
     - Gets the branch database number in parallel.


IscUnbalancedTransformer Class
-------------------------------

.. autoclass:: ipsa.IscUnbalancedTransformer
   :members:
