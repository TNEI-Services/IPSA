IscFaultFlow
=============

This class wraps the results from Fault Level analysis after running a fault-flow-on-all-busbars study. Each IscFaultFlow object represents either the flow results along a connected item on a busbar, or the flow results on a busbar node. 

Field Values
--------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscFaultFlow Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FaultedBusbarUID
     - The UID of the faulted busbar when this result is generated.
   * - String
     - FaultedBusbarName
     - The name of the faulted busbar when this result is generated.
   * - Integer
     - BusbarUID
     - The UID of the busbar this flow result is about (the result busbar).
   * - String
     - BusbarName
     - The name of the result busbar.
   * - Float
     - BusbarVoltkV
     - The nominal voltage of the result busbar.
   * - Integer
     - ItemUID
     - The UID of the item connected to the result busbar, the flow on which this row represents (the result item).
   * - String
     - ItemName
     - The name of the result item.
   * - String
     - ItemType
     - The type of the result item.
   * - String
     - Terminal
     - Text that indicates which end the flow results are on the result item. The text is either "From", "To", or "Three".
   * - Integer
     - RowType
     - The type of IscFaultFlow results. Note that a row can only be of one of the following types, and if the row is of the BusbarRow type, the fields about item are not meaningful.

        - 0 = IscFaultFlow.ItemRow, indicating this result is about flows along a connected item (radial, 2-port branch item, or 3-port item)
        - 1 = IscFaultFlow.BusbarRow, indicating this result is about the flows on a busbar.
   * - Boolean
     - HasBusbarResult
     - Indicates whether this Busbar has results from a successful fault level run.
   * - Float
     - IRedCompMVA
     - Fault flow MVA on the Red phase.
   * - Float
     - IRedCompkVA
     - Fault flow kVA on the Red phase.
   * - Float
     - IRedCompkA
     - Fault flow kA on the Red phase.
   * - Float
     - IRedCompA
     - Fault flow A on the Red phase.
   * - Float
     - IRedCompPUMVA
     - Fault flow MVA in per-unit on the Red phase.
   * - Float
     - AngRedCompDeg
     - Fault flow angle in degrees on the Red phase.
   * - Float
     - IYellCompMVA
     - Fault flow MVA on the Yellow phase.
   * - Float
     - IYellCompkVA
     - Fault flow kVA on the Yellow phase.
   * - Float
     - IYellCompkA
     - Fault flow kA on the Yellow phase.
   * - Float
     - IYellCompA
     - Fault flow A on the Yellow phase.
   * - Float
     - IYellCompPUMVA
     - Fault flow MVA in per-unit on the Yellow phase.
   * - Float
     - AngYellCompDeg
     - Fault flow angle in degrees on the Yellow phase.
   * - Float
     - IBlueCompMVA
     - Fault flow MVA on the Blue phase.
   * - Float
     - IBlueCompkVA
     - Fault flow kVA on the Blue phase.
   * - Float
     - IBlueCompkA
     - Fault flow kA on the Blue phase.
   * - Float
     - IBlueCompA
     - Fault flow A on the Blue phase.
   * - Float
     - IBlueCompPUMVA
     - Fault flow MVA in per-unit on the Blue phase.
   * - Float
     - AngBlueCompDeg
     - Fault flow angle in degrees on the Blue phase.
   * - Float
     - IPositiveCompMVA
     - Fault flow MVA on the Positive sequence.
   * - Float
     - IPositiveCompkVA
     - Fault flow kVA on the Positive sequence.
   * - Float
     - IPositiveCompkA
     - Fault flow kA on the Positive sequence.
   * - Float
     - IPositiveCompA
     - Fault flow A on the Positive sequence.
   * - Float
     - IPositiveCompPUMVA
     - Fault flow MVA in per-unit on the Positive sequence.
   * - Float
     - AngPositiveCompDeg
     - Fault flow angle in degrees on the Positive sequence.
   * - Float
     - INegativeCompMVA
     - Fault flow MVA on the Negative sequence.
   * - Float
     - INegativeCompkVA
     - Fault flow kVA on the Negative sequence.
   * - Float
     - INegativeCompkA
     - Fault flow kA on the Negative sequence.
   * - Float
     - INegativeCompA
     - Fault flow A on the Negative sequence.
   * - Float
     - INegativeCompPUMVA
     - Fault flow MVA in per-unit on the Negative sequence.
   * - Float
     - AngNegativeCompDeg
     - Fault flow angle in degrees on the Negative sequence.
   * - Float
     - IZeroCompMVA
     - Fault flow MVA on the Zero sequence.
   * - Float
     - IZeroCompkVA
     - Fault flow kVA on the Zero sequence.
   * - Float
     - IZeroCompkA
     - Fault flow kA on the Zero sequence.
   * - Float
     - IZeroCompA
     - Fault flow A on the Zero sequence.
   * - Float
     - IZeroCompPUMVA
     - Fault flow MVA in per-unit on the Zero sequence.
   * - Float
     - AngZeroCompDeg
     - Fault flow angle in degrees on the Zero sequence.
   * - Float
     - BusIACCompMVA
     - Fault flow MVA AC component of a result busbar.
   * - Float
     - BusIACCompkVA
     - Fault flow kVA AC component of a result busbar.
   * - Float
     - BusIACCompkA
     - Fault flow kA AC component of a result busbar.
   * - Float
     - BusIACCompA
     - Fault flow A AC component of a result busbar.
   * - Float
     - BusIACCompPUMVA
     - Fault flow MVA in per-unit AC component of a result busbar.
   * - Float
     - BusIDCCompMVA
     - Fault flow MVA DC component of a result busbar.
   * - Float
     - BusIDCCompkVA
     - Fault flow kVA DC component of a result busbar.
   * - Float
     - BusIDCCompkA
     - Fault flow kA DC component of a result busbar.
   * - Float
     - BusIDCCompA
     - Fault flow A DC component of a result busbar.
   * - Float
     - BusIDCCompPUMVA
     - Fault flow MVA in per-unit DC component of a result busbar.
   * - Float
     - BusI2harCompMVA
     - Fault flow MVA second harmonics component of a result busbar.
   * - Float
     - BusI2harCompkVA
     - Fault flow kVA second harmonics component of a result busbar.
   * - Float
     - BusI2harCompkA
     - Fault flow kA second harmonics component of a result busbar.
   * - Float
     - BusI2harCompA
     - Fault flow A second harmonics component of a result busbar.
   * - Float
     - BusI2harCompPUMVA
     - Fault flow MVA in per-unit second harmonics component of a result busbar.
   * - Float
     - BusDCTheveninXoverR
     - DC Thevenin X/R of a result busbar.
   * - Float
     - BusDCTheveninX
     - DC Thevenin X of a result busbar.
   * - Float
     - BusDCTheveninR
     - DC Thevenin R of a result busbar.
   * - Float
     - BusIRedCompMVA
     - Fault flow MVA of a result busbar on the Red phase.
   * - Float
     - BusIRedCompkVA
     - Fault flow kVA of a result busbar on the Red phase.
   * - Float
     - BusIRedCompkA
     - Fault flow kA of a result busbar on the Red phase.
   * - Float
     - BusIRedCompA
     - Fault flow A of a result busbar on the Red phase.
   * - Float
     - BusIRedCompPUMVA
     - Fault flow MVA in per-unit of a result busbar on the Red phase.
   * - Float
     - BusAngRedCompDeg
     - Fault flow angle in degrees of a result busbar on the Red phase.
   * - Float
     - BusIYellCompMVA
     - Fault flow MVA of a result busbar on the Yellow phase.
   * - Float
     - BusIYellCompkVA
     - Fault flow kVA of a result busbar on the Yellow phase.
   * - Float
     - BusIYellCompkA
     - Fault flow kA of a result busbar on the Yellow phase.
   * - Float
     - BusIYellCompA
     - Fault flow A of a result busbar on the Yellow phase.
   * - Float
     - BusIYellCompPUMVA
     - Fault flow MVA in per-unit of a result busbar on the Yellow phase.
   * - Float
     - BusAngYellCompDeg
     - Fault flow angle in degrees of a result busbar on the Yellow phase.
   * - Float
     - BusIBlueCompMVA
     - Fault flow MVA of a result busbar on the Blue phase.
   * - Float
     - BusIBlueCompkVA
     - Fault flow kVA of a result busbar on the Blue phase.
   * - Float
     - BusIBlueCompkA
     - Fault flow kA of a result busbar on the Blue phase.
   * - Float
     - BusIBlueCompA
     - Fault flow A of a result busbar on the Blue phase.
   * - Float
     - BusIBlueCompPUMVA
     - Fault flow MVA in per-unit of a result busbar on the Blue phase.
   * - Float
     - BusAngBlueCompDeg
     - Fault flow angle in degrees of a result busbar on the Blue phase.
   * - Boolean
     - BusG74CDPContributionsIncluded
     - Indicates whether CDP contribution is included.


IscFaultFlow Class
-----------------------

.. autoclass:: ipsa.IscFaultFlow
   :members:


