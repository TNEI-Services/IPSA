Isc3WTransformer
=================

The ``Isc3WTransformer`` class provides access to an IPSA 3-winding transformer, to set and get data values and to retrieve load flow and fault level results. In the following functions and field values the following conventions are used;

    - Primary winding = winding 1. Winding number ``nWinding = 1``
    - Secondary winding = winding 2. Winding number ``nWinding = 2``
    - Tertiary winding = winding 3. Winding number ``nWinding = 3``

Field Values
-------------

.. list-table:: **Isc3WTransformer Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique ID of the primary winding busbar.
   * - Integer
     - ToUID
     - Gets the unique ID of the secondary winding busbar.
   * - Integer
     - ThreeUID
     - Gets the unique ID of the tertiary winding busbar.
   * - String
     - FromBusName
     - Gets the primary winding busbar name.
   * - String
     - ToBusName
     - Gets the secondary winding busbar name.
   * - String
     - ToBusName
     - Gets the tertiary winding busbar name.
   * - String
     - Name
     - Gets the 3-winding transformer name.
   * - Integer
     - Status
     - Status:

        - 0 = All windings switched in
        - -1 = All windings switched out
   * - Integer
     - Winding
     - Transformer winding type connection as follows:

        - 1 = none
        - 2 = xd1d1
        - 3 = xd1d11
        - 4 = xd11d1
        - 5 = xd11d11
        - 6 = xxd1
        - 7 = xxd11
        - 8 = xd1x
        - 9 = xd11x
        - 10 = xyd1
        - 11 = xyd11
        - 12 = xd1y
        - 13 = xd11y
        - 14 = ddx1
        - 15 = ddx11
        - 16 = dx1d
        - 17 = dx11d
        - 18 = ddy1
        - 19 = ddy11
        - 20 = dy1d
        - 21 = dy11d
        - 22 = dx1x1
        - 23 = dx11x11
        - 24 = dy1y1
        - 25 = dy11y11
        - 26 = dx1y1
        - 27 = dx11y11
        - 28 = dy1x1
        - 29 = dy11x11
        - 30 = yd1d1
        - 31 = yd1d11
        - 32 = yd11d1
        - 33 = yd11d11
        - 34 = yyd1
        - 35 = yyd11
        - 36 = yd1y
        - 37 = yd11y
        - 38 = yxd1
        - 39 = yxd11
        - 40 = yd1x
        - 41 = yd11x
        - 42 = xxy
        - 43 = xyx
        - 44 = yxx
        - 45 = yyx
        - 46 = yxy
        - 47 = xyy
        - 48 = xxx
        - 49 = yyy
        - 50 = ddd


        where:

        - X = Earthed star
        - Y = Unearthed star
        - D = Delta
        - Z = Zig-zag
   * - Float
     - W1W2ResistancePU
     - Gets and sets the winding 1 to winding 2 resistance in per unit.
   * - Float
     - W1W2ReactancePU
     - Gets and sets the winding 1 to winding 2 reactance in per unit.
   * - Float
     - W1W3ResistancePU
     - Gets and sets the winding 1 to winding 3 resistance in per unit.
   * - Float
     - W1W3ReactancePU
     - Gets and sets the winding 1 to winding 3 reactance in per unit.
   * - Float
     - W2W3ResistancePU
     - Gets and sets the winding 2 to winding 3 reactance in per unit.
   * - Float
     - W2W3ReactancePU
     - Gets and sets the winding 2 to winding 3 reactance in per unit.
   * - Float
     - W1W2ZSResistancePU
     - Gets and sets the winding 1 to winding 2 zero sequence resistance in per unit.
   * - Float
     - W1W2ZSReactancePU
     - Gets and sets the winding 1 to winding 2 zero sequence reactance in per unit.
   * - Float
     - W1W3ZSResistancePU
     - Gets and sets the winding 1 to winding 3 zero sequence resistance in per unit.
   * - Float
     - W1W3ZSReactancePU
     - Gets and sets the winding 1 to winding 3 zero sequence reactance in per unit.
   * - Float
     - W2W3ZSResistancePU
     - Gets and sets the winding 2 to winding 3 zero sequence resistance in per unit.
   * - Float
     - W2W3ZSReactancePU
     - Gets and sets the winding 2 to winding 3 zero sequence reactance in per unit.
   * - Float
     - W1NEResistancePU
     - Gets and sets the winding 1 neutral earth resistance in per unit.
   * - Float
     - W1NEReactancePU
     - Gets and sets the winding 1 neutral earth reactance in per unit.
   * - Float
     - W2NEResistancePU
     - Gets and sets the winding 2 neutral earth resistance in per unit.
   * - Float
     - W2NEReactancePU
     - Gets and sets the winding 2 neutral earth reactance in per unit.
   * - Float
     - W3NEResistancePU
     - Gets and sets the winding 3 neutral earth resistance in per unit.
   * - Float
     - W3NEReactancePU
     - Gets and sets the winding 3 neutral earth reactance in per unit.
   * - Boolean
     - LockTap
     - Gets and sets the flag to lock the tap changer on the primary winding.
   * - Float
     - W1TapNominalPC
     - Gets and sets the winding 1 nominal tap position in percent, optionally used in a flat start.
   * - Float
     - W2TapNominalPC
     - Gets and sets the winding 2 nominal tap position in percent, optionally used in a flat start.
   * - Float
     - W3TapNominalPC
     - Gets and sets the winding 3 nominal tap position in percent, optionally used in a flat start.
   * - Float
     - W1TapStartPC
     - Gets and sets the winding 1 tap position in percent, used as a starting point for the next load flow.
   * - Float
     - W2TapStartPC
     - Gets and sets the winding 2 tap position in percent, used as a starting point for the next load flow.
   * - Float
     - W3TapStartPC
     - Gets and sets the winding 3 tap position in percent, used as a starting point for the next load flow.
   * - Float
     - W1MinTapPC
     - Gets and sets the winding 1 minimum tap position in percent, normally negative or zero.
   * - Float
     - W2MinTapPC
     - Gets and sets the winding 2 minimum tap position in percent, normally negative or zero.
   * - Float
     - W3MinTapPC
     - Gets and sets the winding 3 minimum tap position in percent, normally negative or zero.
   * - Float
     - W1TapStepPC
     - Gets and sets the winding 1 tap increment in percent. This defaults to 0.01 if left blank.
   * - Float
     - W2TapStepPC
     - Gets and sets the winding 2 tap increment in percent. This defaults to 0.01 if left blank.
   * - Float
     - W3TapStepPC
     - Gets and sets the winding 3 tap increment in percent. This defaults to 0.01 if left blank.
   * - Float
     - W1MaxTapPC
     - Gets and sets the winding 1 maximum tap position in percent, normally positive or zero.
   * - Float
     - W2MaxTapPC
     - Gets and sets the winding 2 maximum tap position in percent, normally positive or zero.
   * - Float
     - W3MaxTapPC
     - Gets and sets the winding 3 maximum tap position in percent, normally positive or zero.
   * - Float
     - W1SpecVPU
     - Gets and sets the winding 1 target voltage in per unit. Positive values only. Magnitudes of less than 0.5 pu mean fixed tap operation.
   * - Integer
     - W1SpecVWinding
     - Specifies the busbar whose voltage is controlled by the tap changer on winding 1.
   * - Float
     - W1RBWidthPC
     - Full bandwidth of the winding 1 voltage sensing relay. This should be larger than tap step size.
   * - Float
     - W1CompRPC
     - Winding 1 line drop compensation resistance in percentage on the compensation rating base.
   * - Float
     - W1CompXPC
     - Winding 1 line drop compensation reactance in percentage on the compensation rating base.
   * - Float
     - W1CompRatingMVA
     - Winding 1 line drop compensation rating in MVA used to provide load compensation.
   * - Float
     - VoltFactorPt
     - Sets the voltage factor for use in IEC60909 fault calculations.
   * - Integer
     - HarmonicModel
     - Transformer harmonic model. One of the following:

        - 0 = Polynomial resistance mode
        - 1 = Resistance square root model
        - 2 = Constant X/R model
   * - Float
     -
        HarmRC0
        HarmRC12
        HarmRC1
        HarmRC2
        HarmRC3
     - Harmonic polynomial constants RC0, RC12, RC1, RC2 and RC3 in:

       :math:`R_{h} = R[RC0 + RC12.h^{0.5} 0 + RC1.h + RC2.h^2 + RC3.h^3]`

Isc3WTransformer Class
-----------------------

.. autoclass:: ipsa.Isc3WTransformer
   :members:
