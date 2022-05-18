IscBusbar
============

The ``IscBusbar`` class provides access to an IPSA busbar, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. list-table:: **IscBusbar Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - String
     - Name
     - Gets the busbar name.
   * - Float
     - NomVoltkV
     - Nominal bus voltage in kV
   * - Integer
     - ControlType
     - Gets the type of busbar, e.g. slack, PV, PQ, etc.

        - 0 = No voltage control at bus
        - 1 = Slack busbar
        - 2 = Real power and voltage control by generator
        - 3 = No longer used
        - 4 = No longer used
        - 5 = Voltage controlled by transformer
        - 6 = No longer used
        - 7 = Multiple types of voltage control, i.e. generator and transformer
        - 8 = Voltage controlled by remote PV generator
        - 9 = Voltage controlled by local switched capacitor
        - 10 = Voltage controlled by remote switched capacitor
   * - Float
     - VoltPU
     - Gets the voltage magnitude in per unit.
   * - Float
     - VoltAngleRad
     - Gets the voltage angle in radians.
   * - String
     - Comment
     - Gets the comments.
   * - Integer
     - ArcBusbarConfiguration
     - Specific busbar configuration for this bus according to the definitions penned out by IEEE-1584 standard:

        - 0 = Unknown
        - 1 = VCB (vertical closed box)
        - 2 = VCBB (vertical closed bolted box)
        - 3 = HCB (horizontal closed box)
        - 4 = VOA (vertical open air box)
        - 5 = HOA (horizontal open air box)
   * - Float
     - ArcEnclosureWidthMM
     - Width of the busbar enclosure for the arcflash in mm.
   * - Float
     - ArcEnclosureHeightMM
     - Height of the busbar enclosure for the arcflash in mm.
   * - Float
     - ArcEnclosureDepthMM
     - Depth of the busbar enclosure for the arcflash in mm.
   * - Float
     - ArcConductorGapMM
     - Air gap between the conductors that the arc flash jumps across in mm.
   * - Float
     - ArcWorkingDistanceMM
     - Working distance for the bus container in mm.

IscBusbar Class
----------------

.. autoclass:: ipsa.IscBusbar
   :members:
