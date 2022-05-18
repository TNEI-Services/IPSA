********************
Coding Requirements
********************

Importing IPSA
===============

All IPSA scripts should import the IPSA interface (``IscInterface``) using the import command near the start of the script. It is also recommended to import the print module which enables scripts to print directly to the IPSA progress window.

Starting from IPSA 2.3.2 there are two ways of launching IPSA 2, either from within IPSA 2 itself or from a separate Python process. The following code demonstrates how scripts should be written when launched from within IPSA 2. Refer to section 2.2.2 for details of running IPSA 2 from a separate Python process.

::

    # Initialise Scripting interface into IPSA+
    import ipsa
    # Get IPSA scripting instance
    ipsascript = ipsa.GetScriptInterface()

    print("Welcome to IPSA")

It is important to ensure that there is only one ``import ipsa`` statement in the full extent of the code. Calling ``import ipsa`` multiple times in the same Python session may result in unexpected errors.

IPSA unique identifiers and names
==================================

IPSA assigns all components and graphical objects a unique integer number called a UID, which is used for referencing the individual component. These UIDs can be seen in the IPSA i2f files and can also be used by scripts. Component classes include functions to obtain the UID and to perform operations, such as filtering results, using them.

The component UIDs provide the best method of referring to individual components in a script. The UID of an individual component will never change during the execution of the script. Since it is an integer it is also passed efficiently between different functions in the script. The component UIDs are normally obtained from functions such as ``GetBusbarUID()``.

Some functions return the IPSA object itself, such as ``GetBusbar()``, which are required when the script needs to read or write component data. Due to the way in which the Python IPSA interface works these objects are not guaranteed to refer to the same component. They exist only in the Python script and may be deleted or overwritten by IPSA. This typically occurs when the script calls a ``Get`` type function and the internal IPSA data maps are deleted and recreated. It is recommended that the objects returned by functions such as ``GetBusbar()`` are used immediately.

It is important to note that the UIDs are only unique across a single network. Different network files will use the same UIDs and therefore the UIDs must never be used to refer to components in multiple networks.

Some functions also accept and return Python names for IPSA network components, for example, the ``GetName()`` functions. These names are also unique and are in the following format:

::

    Busbar1			# busbar name
    Busbar1.Load		# radial component
    Busbar1.Busbar2.Branch	# branch component


Debugging Scripts
==================

When IPSA encounters an error in a script a traceback message is usually produced in the form shown below. This message is printed in the IPSA progress window and provides details of the error.

::

    [Nov 6 12 22:53:23] Traceback(most recent call last):
    File "C:/Program Files/IpsaPower/Ipsa 2.2/scripts/PyTester.py", line 18, in <module>
    gens = ipsa_network.GetIndMachines()
    AttributeError: 'NoneType' object has no attribute 'GetIndMachines'

This provides details of the line number and file name where the error was found, in this case line 18 in file PyTester.py. The error is reported as an ``AttributeError``, in the example above the ``ipsa_network`` variable does not have a function, or attribute, called ``GetIndMachines()``. More advanced debugging is also provided as described in the following section.

Debugging with an IDE
----------------------

IPSA 2 scripts can be debugged using an Integrated Development Environment such as Wing© available from `wingware.com`_. This allows developers to step through code line by line and examine variables as the script is run.

.. _wingware.com : http://wingware.com/

It is recommended that more complex scripts are developed using PyIPSA. This allows the users' script to be started from the IDE and code can then be stepped through as required.

Once the code has been debugged it can then be quickly converted to run from normal IPSA by changing the original IscInterface loading function.

Coding Methods
===============

Execution Speed
----------------

Complex scripts may have long execution times and some additional functions have been provided to reduce this time. These are summarised below:

•	``SetLoadPower()`` - changes the MW and MVAr of a load in the analysis engine only
•	``SetLoadStatus()`` - changes the MW and MVAr of a load in the analysis engine only
•	``SetGeneratorPower()`` - changes the MW and MVAr of a generator in the analysis engine only
•	``SetGeneratorStatus()`` - changes the MW and MVAr of a generator in the analysis engine only
•	``SetBranchStatus()`` - changes the MW and MVAr of a load in the analysis engine only
•	``DoLoadFlow()`` - This function includes an option to perform a load flow calculation based on the data currently in the engine
•	``SetEngineMessageSuppresion()`` - prevents the user interface displaying analysis engine messages
•	``AllowStackBarUpdates()`` - prevents the user interface from redrawing the stack bar

Memory Requirements
--------------------

Memory issues have been encountered when running a significant number of studies. For example, running many load flow studies on a network will slowly use up all the maximum allowable memory for the Python process, approximately 1.3Gb. This is understood to be a result of the Python garbage collection not releasing memory back to the operating system. To avoid this issue, it is possible to run scripted IPSA as a set of separate processes. Please contact `support@ipsa-power.com`_ for further details.

.. _support@ipsa-power.com: mailto:support@ipsa-power.com

Changing Data
--------------

Most of the objects are accessed via scripting, such as components, diagrams, analysis functions etc, have an associated set of data fields which the script can get and set, for example the nominal busbar voltage, the branch status or the load flow convergence tolerance. The majority of operations with components require the use of field values to access various data fields. There are four data types in common use, integers, strings, boolean variables and float numbers. There are therefore four functions to set and four functions to get these different data types from a component. Note that some functions may use lists of these types. The general get and set functions are as follows:

.. list-table::
   :widths: 25 25 25
   :header-rows: 1

   * - Get Functions
     - Set Functions
     - Python Data Type
   * - `GetBValue`
     - `SetBValue`
     - Boolean
   * - `GetDValue`
     - `SetDValue`
     - Float
   * - `GetIValue`
     - `SetIValue`
     - Integer
   * - `GetSValue`
     - `SetSValue`
     - String

Field indexes must be used to get and set specific items for a component. These indexes are defined for each component class and listed in the relevant sections. Field indexes are usually required in the following format, separated by dots:

•	Starting with the IPSA module name
•	Followed by the class name
•	Ending with the field name

The following example illustrates this:

::

    SetDValue(ipsa.IscBusbar.NomVoltkV, 33.0)   # Set the nominal busbar voltage
                                                # to 33kV
    GetDValue(ipsa.IscBusbar.NomVoltkV)         # Get the nominal bus voltage

The sample code below provides some simple examples.

::

    # Initialise Scripting interface into IPSA 2
    import ipsa
    ipsascript = ipsa.IscInterface()

    # load or create a new network
    ipsascript.ReadFile('Refinery.i2f')
    # return an IscNetwork instance representing the new network
    ipsa_network = ipsascript.GetNetwork()

    # Set data example
    busbar = ipsa_network.GetBusbar('SUB 2')
    # set the bus voltage
    busbar.SetDValue(ipsa.IscBusbar.NomVoltkV, 11.0)

    # get the nominal voltage at SUB 2
    dSub2Voltage = busbar.GetDValue(ipsa.IscBusbar.NomVoltkV)
    print("The voltage at SUB 2 is", dSub2Voltage, "kV")

Adding and Editing Components
------------------------------

In order to achieve optimum efficiency in terms of speed and memory usage, there are some simple recommendations regarding the execution order of statements. A common example is creating multiple components and editing the associated data. Due to the way IPSA refreshes its internal data the most efficient way to achieve this is to create all the new components first and then set the data.

IPSA creates internal data maps to store the component data accessed via scripting. These data maps must be rebuilt after components are added or deleted from the network. Changing component data does not require these maps to be rebuilt, but IPSA will automatically rebuild the maps if components have been added or deleted.

Therefore the most efficient way to add and edit components is to add all components first, then edit the component data. This will ensure that the data maps are only rebuilt once when a component is accessed to change its data. The ``Get`` functions have a ``bFetchFromSystem`` flag, setting this to ``True`` will force IPSA to rebuild its internal maps. Setting it to ``False`` will prevent these maps from being rebuilt unless required, i.e. they may still be rebuilt if components have been added or deleted.

For clarity no error checking is included in this example. For robust code, it is recommended that the return values of the various functions are checked to confirm they have executed correctly. For example, if IPSA fails to create one of the busbars then the following calls to set the voltages for that busbar will fail.

::

    # Initialise Scripting interface into IPSA
    import ipsa

    # create a new network
    ipsascript = ipsa.IscInterface()
    ipsascript.CreateNewNetwork(100.0, 50.0, True, True, 1.0, 1)

    # return an IscNetwork instance representing the new network
    ipsa_network = ipsascript.GetNetwork()

    # list of busbars and associated voltages to create
    busbar_list = ["Grid", "Substation", "Primary", "Secondary", "Customer"]
    busbar_voltages = [132.0, 33.0, 11.0, 11.0, 0.415]
    # create an empty list to store bus UIDs in
    busbar_uids = []

    # create all busbar objects and save UIDs
    for bus in busbar_list:
        uid = ipsa_network.CreateBusbar(bus)
        busbar_uids.append(uid)

    # add busbar voltages, need to access busbars using UIDs
    for index in range(len(busbar_uids)):
        busbar = ipsa_network.GetBusbar(busbar_uids[index])
        busbar.SetDValue(ipsa.IscBusbar.NomVoltkV, busbar_voltages[index])

Setting Analysis Engine Data
-----------------------------

Virtually all the functions presented in this manual operate on the main IPSA data model and therefore any changes can be saved within the network. There are a few functions which do not affect the main IPSA data model but change the data loaded into the calculation engine instead. These changes do not get reflected in the saved network or the network that a user would see in the User Interface. These functions allow simple changes to be made to improve calculation speed when undertaking large numbers of studies. For additional details see the IscAnalysis classes.
