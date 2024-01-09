IscBusbar
============

The ``IscBusbar`` class provides access to an IPSA busbar, to set and get data values and to retrieve load flow and fault level results.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscBusbar Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
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
   * - Integer
     - Type
     - Gets the physical type of busbar e.g. straight joint, mains joint etc.

        - 0 = Unset
        - 1 = Straight joint
        - 2 = Mains joint
        - 3 = Service cable joint
        - 4 = Service termination joint
        - 5 = Overhead termination joint
        - 6 = Ground mounted substation node
   * - Float
     - VoltPU
     - Gets the voltage magnitude in per unit.
   * - Float
     - VoltAngleRad
     - Gets the voltage angle in radians.
   * - String
     - Comment
     - Gets and sets the comments.
   * - Float
     - FaultMakePeakkA
     - The rated asymmetric peak make current in kA at half a cycle.
       These must be accessed through the GetFaultDValue/SetFaultDValue functions.
   * - Float
     - FaultBreakRMSkA
     - The rated RMS symmetric break rating in kA at the break time specified.
       These must be accessed through the GetFaultDValue/SetFaultDValue functions.
   * - Float
     - FaultBreakTimemS
     - The time in milliseconds for which the Break ratings are given.
       These must be accessed through the GetFaultDValue/SetFaultDValue functions.
   * - Float
     - FaultBreakDCPC
     - The rated DC break current as a percentage of the rated symmetric break current.
       These must be accessed through the GetFaultDValue/SetFaultDValue functions.
   * - Float
     - FaultNomCurrentkA
     - A value designating the "standard" current at which the busbar operates.
       These must be accessed through the GetFaultDValue/SetFaultDValue functions.
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
   * - Integer
     - ArcIEEEStandard
     - The IEEE-1584 standard for conduction arc flash studies. Users can toggle between the two for comparative studies:

        - 0 = 2002
        - 1 = 2018
   * - Integer
     - ArcEnclosure
     - A 2002 IEEE-1584 legacy parameter. The type of busbar enclosure:

        - 0 = None or open
        - 1 = Box
   * - Integer
     - ArcEquipmentType
     - A 2002 IEEE-1584 legacy parameter. The specific type of busbar:

        - 0 = Not set
        - 1 = Open air
        - 2 = Switchgear
        - 3 = MCC and panels
        - 4 = Cable
   * - Boolean
     - ArcUngrounded
     - A 2002 IEEE-1584 legacy parameter. ``True`` if the busbar is ungrounded.

IscBusbar Class
----------------

.. autoclass:: ipsa.IscBusbar
   :members:
