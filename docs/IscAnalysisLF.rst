IscAnalysisLF
==============

Field Values
-------------

.. list-table:: **IscAnalysisLF Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Float
     - Convergence
     - Accuracy for load flow solution.
   * - Integer
     - MaxIterations
     - Maximum number of iterations to run the load flow.
   * - Float
     - UndervoltagePU
     - Lower voltage limit for busbars (reporting only).
   * - Float
     - OvervoltagePU
     - Upper voltage limit for busbars (reporting only).
   * - Integer
     - LockTaps
     - Lock all transformer taps based on the following settings:

        - 0 = Do not lock taps
        - 1 = Lock taps during outage analysis only
        - 2 = Lock taps
   * - Boolean
     - NoPhaseShift
     - Do not apply phase shifts to load flow.

        - False = Use phase shifting in load flow
        - True = No phase shifting
   * - Integer
     - TapOscIterStart
     - Starts counting the iteration number of transformer tap oscillations.
   * - Integer
     - TapOscSuccessive
     - Number of successive iterations of tap oscillation.
   * - Integer
     - TapOscLimit
     - Tap oscillation limit after which transformer taps are locked.
   * - Integer
     - TapOscIterEnd
     - Stops counting the iteration number of transformer tap oscillations.
   * - Integer
     - FillkARatings
     - Automatically complete kA rating fields for lines.
   * - Boolean
     - UseLoadScaling
     - Enable scaling of loads in the LF calculation.
   * - Float
     - RealLoadScale
     - Per unit factor used to scale all real loads (default = 1.0).
   * - Float
     - ReactiveLoadScale
     - Per unit factor used to scale all reactive loads (default = 1.0).
   * - Boolean
     - CheckProtection
     - Set ``True`` to check protection devices after load flow.
   * - Boolean
     - UseLegacyPhiftCheck
     - Enables or disables the legacy load flow engine code.
   * - Boolean
     - DisplayOptionDialog
     - Setting this field to ``True`` causes the load flow options dialog to be displayed whenever a load flow is required.
   * - Float
     - FeederSlackVoltagePU
     - Sets the busbar voltage for the slack busbar when performing a feeder load flow.
   * - Integer
     - FeederSetTarget
     - Set to 1 to specify a target power when performing a feeder load flow.
   * - Boolean
     - SingleTapMovement
     - Setting this item to ``True`` forces all tap changes to be moved a maximum of one step in each load flow iteration.
   * - Boolean
     - SlowTapMovement
     - Setting this item to ``True`` forces all tap changes to be adjusted every fourth load flow iteration instead of every iteration.
   * - Integer
     - WhichImpedance
     - The default setting is 0 which will use the normal resistance value for branches when performing calculations. Set this value to 1 to use the minimum resistance value for branches when performing calculations.
   * - Integer
     - IslandMethod
     - The default setting is 0 where any island with a slack will have load flow results, assuming the network converges. Setting this value to 1 means any island with a slack busbar must also have a voltage-controlling generator on that busbar in order to have load flow results (again assuming that the network converges).
   * - Boolean
     - AutoSelectSlacks
     - Set ``True`` to automatically select slack busbars in islands where the user has not manually specified a slack busbar.
   * - Boolean
     - InitFlatStart
     - Sets ``True`` to perform flat starts for all load flows until this parameter is reset to ``False``.
   * - Boolean
     - FSSetBusbarVoltages
     - Set ``True`` to reset all busbar voltages during a flat start.
   * - Boolean
     - FSIgnoreVoltageControlSettings
     - Set ``True`` to ignore transformer voltage control settings during a flat start.
   * - Float
     - FSVoltageMagnitudePU
     - Sets the busbar voltage magnitude in per unit during a flat start.
   * - Float
     - FSVoltageAngleDeg
     - Sets the busbar voltage angle in degrees during a flat start.
   * - Boolean
     - FSSetTransformerTaps
     - Set ``True`` to reset the transformer taps during a flat start.
   * - Boolean
     - FSIgnoreFixedTaps
     - Set ``True`` to ignore fixed tap positions during a flat start.
   * - Integer
     - FSNominalTaps
     - Set to 1 to specify that the transformer nominal tap position will be used during a flat start.
   * - Float
     - FSTapStartPC
     - Sets the tap position of transformers in percentage during a flat start.
   * - Boolean
     - FSSetInductionMachineSlips
     - Set ``True`` to force the induction motor slips to a specified value during a flat start.
   * - Float
     - FSSlipPC
     - Sets the induction motor slips in percentage during a flat start.
   * - Integer
     - ProfileUse
     -
        - 0 = Do not apply load and generator profiles
        - 1 = Apply load and generator profile category specified by the ``ProfileLoadCategory`` field
   * - String
     - ProfileLoadCategory
     - Pass a string representing the required load/generator profile category name to be used for the next load flow.
   * - Float
     - ProfileTimeSliceHrs
     - Pass a float representing the number of hours in each profile category.

IscAnalysisLF Class
--------------------

.. autoclass:: ipsa.IscAnalysisLF
   :members:
