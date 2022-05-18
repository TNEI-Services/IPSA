IscInterface
============

The ``IscInterface`` class is the main interface class used to access all other IPSA objects and functions. It **must** be created before any other references to IPSA objects. To create an instance from Python the following commands are required when running IPSA with the User Interface:

::

    # Run inside the IPSA User Interface
    import ipsa
    ipsascript = ipsa.GetScriptInterface()

The ``GetScriptInterface()`` returns an ``IscInterface`` instance which can then be used to access all other IPSA objects. The following sections provide the syntax for all other ``IscInterface`` functions.

Alternatively the following code returns the ``IscInterface`` object when IPSA is running without a User Interface:

::

    # Run with No User Interface
    import ipsa
    ipsascript = ipsa.IscInterface()

**The functions** ``IscInterface``  **and** ``GetScriptInterface``  **must only be called once for each running process.**
**Unexpected errors will occur if multiple calls to the above functions are made!**

Debugging Options
------------------

To aid the development of scripted applications a number of debugging functions have been provided. These functions allow logging and timing of the analysis routines by providing detailed information on the analysis settings and data loaded into the analysis engines. The example below shows the output generated from a ``DoLoadFlow()`` function on a small test network.

::

    IlfSetParameters: (100, 100, 0.01, 1,250,250,250,250,0, 0)
    IlfSetRunOpts: (0, 1, 1, 1, 1, 0, 1)
    IlfAddBusbarWithName: ([1]: <b>Busbar1</b> 0, 1, 0)
    IlfAddBusbarWithName: ([2]: <b>Busbar2</b> 0, 1, 2e-005)
    IlfAddUniversalMachine: (2, 0, 2, 0, 0)
    IlfAddGridInfeed: (1, 0, 1, -2, 4.00037e-005, 0.1, 0.1, 0.1, 0, 0, 0, 0)
    IlfAddBranch: (1, 2, 3, 0.0001, 0.001, 0)
    IlfSetSlkBus: (1, 1)
    IlfDoCalc: (4)
    IlfGetBusResults: (1, 1, 0, -0.000529898, -0.00267593)
    IlfGetBusResults: (2, 1, 1.99973e-005, 0.000265069, 0)
    IlfGetGridInfeedResults: (1, -2.00026, -0.00263594)
    IlfGetUMachResults: (1, 2, 0)
    IlfGetLineResults: (1, -1.99973, 3.99892e-005, -1.99973, -0)

IscInterface Class
-------------------

.. autoclass:: ipsa.IscInterface
   :members:
