IscTransformer
===============

The ``IscTransformer`` class provides access to an IPSA transformer, to set and get data values and to retrieve load flow and fault level results. **Note that in IPSA a transformer is modelled as a combination of a branch and a tap changer. Therefore the transformer impedance data is stored in a branch instance and functions such as** ``GetLineDValue()`` **are used to access branch type data.**

Field Values
-------------

.. list-table:: **IscTransformer Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique ID of the sending busbar.
   * - Integer
     - ToUID
     - Gets the unique ID of the receiving busbar.
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
     - Specifies the transformer type as follows:

        - 0 = Unknown
        - 1 = Ground Mounted
        - 2 = Pole Mounted
        - 3 = Bulk Supply
        - 4 = Grid Supply
        - 5 = Super Grid
        - 6 = Primary Distribution
        - 7 = Secondary Distribution
   * - Integer
     - Winding
     - Transformer winding type connection as follows:

        - 1 = none
        - 2 = Xx0
        - 3 = Yy0
        - 4 = Dd0
        - 5 = Xy0
        - 6 = Yx0
        - 7 = Dx11
        - 8 = Dy11
        - 9 = Xd11
        - 10 = Yd11
        - 11 = Dx1
        - 12 = Dy1
        - 13 = Xd1
        - 14 = Yd1
        - 15 = Xy0, zero sequence current passing
        - 16 = Yx0, zero sequence current passing
        - 17 = Dz0
        - 18 = Zd0

        where:

        - X = Earthed star
        - Y = Unearthed star
        - D = Delta
        - Z = Zig-zag
   * - Float
     - NEResistanceW1PU
     - Winding 1 neutral earth resistance in per unit.
   * - Float
     - NEReactanceW1PU
     - Winding 1 neutral earth reactance in per unit.
   * - Float
     - NEResistanceW2PU
     - Winding 2 neutral earth resistance in per unit.
   * - Float
     - NEReactanceW2PU
     - Winding 2 neutral earth reactance in per unit.
   * - Float
     - TapNominalPC
     - Nominal tap position, optionally used in a flat start.
   * - Float
     - TapStartPC
     - Present tap position, used as a starting point for the next load flow.
   * - Float
     - MinTapPC
     - Minimum tap position, normally negative or zero.
   * - Float
     - TapStepPC
     - Tap increment. This defaults to 0.01 if left blank.
   * - Float
     - MaxTapPC
     - Maximum tap position, normally positive or zero.
   * - Float
     - DxDTap
     - Changes in reactance with tap change. This value is used in compounding only.
   * - Boolean
     - LockTap
     - Sets the flag to lock the transformer tap changer. Use ``True`` to lock, ``False`` to unlock.
   * - Float
     - SpecVPU
     - Target voltage in per unit. Positive means control 'to' busbar, negative means control 'from' busbar. Magnitudes of less than 0.5 pu mean fixed tap operation.
   * - Float
     - RBWidthPC
     - Full bandwidth of the voltage sensing relay. This should be larger than tap step size.
   * - Float
     - CompRPC
     - Line drop compensation resistance in percentage on the compensation rating base.
   * - Float
     - CompXPC
     - Line drop compensation reactance in percentage on the compensation rating base.
   * - Float
     - RatingMVA
     - Rating used for line drop compensation impedances. This can be a different value from the branch rating used for overloads.
   * - Float
     - PhShiftDeg
     - Phase shift angle. A positive value makes the receiving end voltage lead the sending end voltage.
   * - Float
     - SpecPowerMW
     - Quad Booster target power in MW - can be specified as zero.
   * - Boolean
     - SpecPowerAtSend
     - Control the power at the “from” side of the transformer.
   * - Float
     - MinPhShiftDeg
     - Min phase shift angle - both angle limits are required for Power control.
   * - Float
     - MaxPhShiftDeg
     - Max phase shift angle - both angle limits are required for Power control.
   * - Float
     - PhShiftStepDeg
     - Phase shift step - default value is 0.01 degrees.
   * - String
     - DbType
     - Gets the transformer database type including both tap and impedance information.
   * - Integer
     - DbParallel
     - Gets the number of transformers in parallel. This is only used for database transformers.
   * - String
     - PluginID
     - Gets and sets the plugin name associated with this transformer.
   * - Float
     - VoltFactorPt
     - Sets the voltage factor for use in IEC60909 fault calculations.
   * - Integer
     - RemoteCtlBusbarUID
     - Specifies the UID of the remote busbar which is used as the basis for the transformer voltage control.

IscTransformer Class
---------------------

.. autoclass:: ipsa.IscTransformer
   :members:
