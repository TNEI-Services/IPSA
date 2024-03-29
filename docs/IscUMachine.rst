IscUMachine
============

The ``IscUMachine`` class provides access to an IPSA universal machine, to set and get data values and to retrieve load flow results.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscUMachine Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - FromUID
     - Gets the unique ID for busbar.
   * - String
     - BusName
     - Gets the busbar name.
   * - String
     - Name
     - Gets the universal machine name.
   * - Integer
     - Status
     - Status:

        - 0 = Switched in
        - -1 = Switched out
   * - Float
     - RealMW
     - Gets and sets the real power output in MW.
   * - Float
     - ReactiveMVAr
     - Gets and sets the reactive power output in MVAr.
   * - Float
     - RatingMVA
     - Gets and sets the apparent power generated by the machine.
   * - Integer
     - ProfileUID
     - Gets and sets the UID of the profile applied to the universal machine. Set to 0 to not use any profiles.
   * - Integer
     - PluginID
     - Gets and sets the ID of the plugin applied to the universal machine. Set to 0 to not use any profiles.
   * - Boolean
     - ConverterDrivenPlant
     - ``True`` if the universal machine is being used as a Converter Driven Plant (G74/2)
   * - Integer
     - CDPMethodType
     - The CDP current-output mode

        - 0 = Simple
        - 1 = Advanced
   * - Integer
     - CDPVoltageInterpolation
     - The CDP voltage interpolation scheme

        - 0 = Linear
        - 1 = Cubic
   * - Float
     - CDPKFactor
     - The K factor co-efficient that determines the strength of the current injection contributions (only valid between 0 and 10).
   * - Float
     - CDPMaxISync
     - Maximum synchronous value for the current injected given the time domains.
   * - Float
     - CDPMaxITrans
     - Maximum transient value for the current injected given the time domains.
   * - Float
     - CDPMaxISubTrans
     - Maximum subtransient value for the current injected given the time domains.
   * - Float
     - CDPTimeConstantTransientMs
     - Time constant value in ms for the transient window duration.
   * - Float
     - CDPTimeConstantSubTransientMs
     - Time constant value in ms for the subtransient window duration.
   * - Boolean
     - CDPPhaseCorrections
     - Switch for the CDP functionality of the universal machine that forces the phase correction of the injected current to be in
       quadrature with the pre-fault voltage. This 'prioritises' reactive power injection at the CDP injection site. In advanced mode,
       when this is disabled it will adopt the phase of the active-reactive current phasor. In simple mode, when this is disabled it
       will be in phase with the retained voltage.

IscUMachine Class
------------------

.. autoclass:: ipsa.IscUMachine
   :members:
