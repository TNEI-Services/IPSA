IscProtectionDevice
====================

The ``IscProtectionDevice`` class provides access to a single protection device, such as a relay, allowing data to be set and cleared.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscProtectionDevice Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - String
     - Name
     - Gets and sets the name of the protection device.
   * - Integer
     - Status
     - Status. Note this is the status of the device itself and currently always should be in. The status of the protection container the device lies within can be found through the auxiliary function (with get/set functions for a block). The Status for the device cannot be set.

        - 0 = Switched in
        - -1 = Switched out
   * - String
     - DeviceManufacturer
     - Gets the name of the manufacturer for the relay assigned to the protection device. Cannot be set.
   * - String
     - DeviceFamily
     - Gets the name of the relay family for the relay assigned to the protection device. Cannot be set.
   * - String
     - DeviceDBName
     - Gets the data base name of the relay assigned to the protection device. Cannot be set.
   * - String
     - DeviceVersion
     - Gets the version text of the relay assigned to the protection device. Cannot be set.
   * - String
     - DeviceComments
     - Gets the comments for the relay assigned to the protection device.
   * - Float
     - OCNominalCurrentA
     - Gets the UID nominal operating current of the relay in Amps. Cannot be set.
   * - String
     - BlockName
     - Gets the name of a block. Use with the `GetBlockSValue` function. Cannot be set.
   * - Integer
     - BlockStatus
     - Gets the status of a block. Use with the `GetBlockIValue` or `SetBlockIValue` function.
   * - Float
     - CurrentMultiplier
     - Gets the status of a block. Use with the `GetBlockIValue` or `SetBlockIValue` function. This field is only avaiable for a block of type ProtBlockConstantCurrent, ProtBlockGivenPointsAdjust, or ProtBlockIDMT.
   * - List[String]
     - CurrentMultiplierRange
     - Current multiplier range of a block. Use with the `GetBlockListSValue` function. Cannot be set. This field is only avaiable for a block of type ProtBlockConstantCurrent, ProtBlockGivenPointsAdjust, or ProtBlockIDMT.
   * - List[String]
     - CurrentOperatingRangePC
     - Current operating range percentage of a block. Use with the `GetBlockListSValue` function. Cannot be set. This field is only avaiable for a block of type ProtBlockConstantCurrent, ProtBlockGivenPointsAdjust, or ProtBlockPickAndDelay.
   * - Float
     - TimeSettingS
     - Time setting in seconds. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockConstantTime.
   * - Float
     - TimeRangeS
     - Time range in seconds. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockConstantTime.
   * - Float
     - TimeMultiplier
     - Time multiplier. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockGivenPointsAdjust or ProtBlockIDMT.
   * - List[String]
     - TimeMultiplierRange
     - Time multiplier range of a block. Use with the `GetBlockListSValue` function. Cannot be set. This field is only avaiable for a block of type ProtBlockGivenPointsAdjust, or ProtBlockIDMT.
   * - Integer
     - IDMTCurveType
     - Curve type of an IDMT Block. Use with the `GetBlockIValue` or `SetBlockIValue` function. This field is only avaiable for a block of type ProtBlockIDMT.
     The curve type enum value and name are mapped as follows:
       - 1 - IEC standard
       - 2 - IEC Very
       - 3 - IEC Extremely
       - 4 - ANSI Moderately
       - 5 - ANSI Very
       - 6 - ANSI Extremely
       - 7 - AREVA Short
       - 8 - AREVA Long
       - 9 - CO Short
       - 10 - CO Long
       - 11 - IEC Long
       - 12 - IEC Short
       - 13 - SEL Moderately
       - 14 - SEL Standard
       - 15 - SEL Very
       - 16 - SEL Extremely
       - 17 - SEL Short

   * - Float
     - PickUpCurrent
     - Pick up current for a PickAndDelay block. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockPickAndDelay.
   * - List[String]
     - PickUpCurrentRange
     - Pick up current range. Use with the `GetBlockListSValue` function. Cannot be set. This field is only avaiable for a block of type ProtBlockPickAndDelay.
   * - Float
     - TimeDelayS
     - Time delay in seconds. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockPickAndDelay.
   * - List[String]
     - TimeDelayRangeS
     - Time delay range in seconds. Use with the `GetBlockListSValue` or `SetBlockListSValue` function. This field is only avaiable for a block of type ProtBlockPickAndDelay.
   * - Float
     - TimeDelayCurrentMultiplier
     - Time delay current multipler. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockPickAndDelay.     
   * - Float
     - TimeDelaySlope
     - Time delay slope. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockPickAndDelay.      
   * - Float
     - ResetTimeS
     - Reset time in seconds. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockTransientDisc.     
   * - Float
     - ResetPercentage
     - Reset percentage. Use with the `GetBlockDValue` or `SetBlockDValue` function. This field is only avaiable for a block of type ProtBlockTransientDisc.        




IscProtectionDevice Class
--------------------------

.. autoclass:: ipsa.IscProtectionDevice
   :members:
