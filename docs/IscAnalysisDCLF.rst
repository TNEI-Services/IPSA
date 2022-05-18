IscAnalysisDCLF
================

Field Values
-------------

.. list-table:: **IscAnalysisDCLF Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Boolean
     - CalculateNodalTLF
     - If this option is selected then the nodal transmission loss factors will be calculated for the network.
   * - Integer
     - BranchLossEstimationMethod
     - Type of method used to estimate the losses in the branches in the network. Should be one of:

        - 0 = None (i.e. no branch losses)
        - 1 = PI-model. This estimates the branch losses by placing a real power load at either end of every branch for which a resistance value has been provided.
   * - Float
     - InductionMachineEfficiencyPC
     - The efficiency of all induction machines in percent. This will be used to estimate the electrical power to the machines from the machines mechanical output power.
   * - Boolean
     - OnlyLargestIsland
     - If this option is selected then only the largest island in the network will be included in the DC load flow.
   * - Boolean
     - NoPhaseShift
     - Do not apply phase shifts to DC load flow. **Note this flag is for future use!**

        False = Use phase shifting in DCload flow
        True = No phase shifting
   * - Boolean
     - UseLoadScaling
     - Enable scaling of loads in the DC load flow calculation.
   * - Float
     - RealLoadScale
     - Per unit factor used to scale all real loads (default = 1.0).
   * - Integer
     - WhichImpedance
     - The default setting is 0 which will use the normal resistance value for branches when performing calculations. Set this value to 1 to use the minimum resistance value for branches when performing calculations.
   * - Boolean
     - AutoSelectSlacks
     - Set ``True`` to automatically select slack busbars in islands where the user has not manually specified a slack busbar.


IscAnalysisDCLF Class
----------------------

.. autoclass:: ipsa.IscAnalysisDCLF
   :members:
