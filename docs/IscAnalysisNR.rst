IscAnalysisNR
==============

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscAnalysisNR Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - ReductionAlgorithm
     - Network reduction algorithm option:

        - 0 = Ward equivalence
        - 1 = Extended ward equivalence
   * - Integer
     - BoundaryUID
     - UID of the boundary that defines the reduction.
   * - Boolean
     - AutomaticallySelectSlacks
     - If ``True`` automatically select slack busbars if equivalenced.
   * - Boolean
     - UseImpedanceCutOff
     - If ``True``, use the branch impedence cut off for reduction.
   * - Float
     - ImpedanceCutOffPU
     - The maximum branch impedence allowed in per unit.
   * - Integer
     - BoundaryRetentionMode
     - The mode for managing the boundary elements:

        - 0 = Retain boundary elements
        - 1 = Remove radial elements
   * - Integer
     - ACDCConversionMode
     - The mode of conversion for the AC/DC interface:

        - 0 = Largest power value
        - 1 = AC-DC radials
   * - Integer
     - YBusMatrixDecompositionRoutine
     - The matrix decomposition method used for the reduction:

        - 0 = LLT (simplicial)
        - 1 = LLDT (simplicial)
        - 2 = LU
   * - Boolean
     - EquivalentInjectionCutoff
     - If ``True``, filter out low MVA equivalent injections.
   * - Float
     - EquivalentInjCutoffMVA
     - The minimum equivalent injection retained power in MVA.
   * - Boolean
     - EquivalentBranchZCutoff
     - If ``True``, filter out high impedence equivalent branches.
   * - Float
     - EquivalentBrZCutoffPU
     - The maximum equivalent branch impedence in per unit.
   * - Integer
     - DrawEquivalents:
     - Logic for which equivalents are drawn:

        - 0 = Don't draw the equivalents
        - 1 = Draw the equivalent branches
        - 2 = Draw the equivalent branches and radials
   * - Boolean
     - DeleteBoundaryPostReduction
     - If ``True``, delete the used boundary after the reduction.
   * - Boolean
     - ExportNetworkPreReduction
     - If ``True``, export the existing network before the reduction.
   * - Integer
     - CatalogMode
     - The mode of the catalog distribution:

        - 0 = Do not expose the catalog
        - 1 = Distribute catalog generation equally
        - 2 = Weight catalog items by equivalent MW

IscAnalysisNR Class
--------------------

.. autoclass:: ipsa.IscAnalysisNR
   :members:
