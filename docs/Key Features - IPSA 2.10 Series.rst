Key features of the IPSA 2.10 Series
======================================

Key features of IPSA 2.10.3
-------------------------------
Network Capacity tool
--------------------------------
New module available to license in IPSA to run numerous load flows and find the violation capacity (over/under voltages, 
thermal overloads) caused by the addition of new capacity at every busbar.  
New ``IscNetworkCapacity`` class added to facilitate both modifying the settings for the network capacity tool (callable with 
``IscNetwork.DoNetworkCapacity``) and accessing the results. 

DC Load flow enhancement in PyIPSA
-------------------------------------------
Optimised and increased performance of the DC load flow functionality in PyIPSA.

Intertrips in PyIPSA
--------------------------------
New ``IscIntertrip`` class has been added. This allows users to create and modify intertrips from PyIPSA. Breakers that are part of 
intertrips will now obey the intertrip restrictions when their statuses are modified from PyIPSA. The documentation for all new PyIPSA
intertrip functionality can be found in the ``IscIntertrip`` part of the scripting reference.

Extended Data in PyIPSA
--------------------------------
Can now delete Extended data from PyIPSA. Additionally, can now add Boolean extended data fields from PyIPSA, and have increased access
to IscGroup extended data. 

Changing component connectivity in PyIPSA
----------------------------------------------
Functionality has been added to PyIPSA to allow for changes to be made to radial/branch connectivity analogously to that 
permitted through the IPSA UI. In particular, the new functions ``IscNetwork.ReverseBranch``, ``IscNetwork.SplitBranch`` and 
``IscNetwork.ChangeConnectivity`` have been added with documentation to explain the details of their functionality.

Additional Fixes
--------------------------------
Multiple new miscellaneous methods have been added to PyIPSA. These include, but are not limited to:  

    - IscNetwork.DeleteAllItems function to delete all components from a network from PyIPSA.
    - Get and Set List functions for components with field values corresponding to lists.
    - The ability to get components as dicts with the component UID as the key - e.g., ``IscNetwork.GetLoadUIDs``.
    - Numerous field values exposed to PyIPSA to allow for a wider range of component data to be accessed comparably to the UI data tables.


Key features of IPSA 2.10.2
------------------------------

Converter driven plant functionality
--------------------------------------------
Users in PyIPSA can co-opt the ``IscUMachine`` object to generate converter driven plants for inverter based generator fault calculations.
This uses a parametrisation conforming to ERC G74/2 (more advanced functionality available in IPSA 2.10.1 UI).
There is an additional flag in the fault level settings and additional data required in ``IscUMachine`` for this to work.
Now all the methods have been traced correctly and even allowed for advanced mode of CDP modelling.
Phase corrections that prioritise reactive power injection are also included and documented.

Groups in PyIPSA
--------------------------------
New functions for ``IscGroup`` have been added: ClearMembers, AddMember, RemoveMember, IsMember, CompareGroups, MergeGroups
all allowing for more detailed and flexible modelling of groups now directly with PyIPSA. These are all documented in the ``IscGroup`` part of the scripting reference.


Component Names in PyIPSA
--------------------------------
Component names can now be changed using the SetSValue functionality. Busbars can no longer have the same name which
resolves several bugs that were appearing via PyIPSA and will now force users not to do this (as in the user interface).


Documentation fixes
--------------------------------------
The documentation has been fully reviewed and should be up to date -- removing some non-existent functions and adding previously undocumented functions.
Additionally the read-the-docs can be accessed in an off line form by downloading a pdf from the readthedocs website, which has been aesthetically updated.


Additional fixes
--------------------------------------
Multiple new methods added in PyIPSA for access functions (inc. CreateBranch()).


Key features of IPSA 2.10.1
--------------------------------

Choppers in PyIPSA
--------------------------------

The DCDC Converter object is available through the ``IscChopper`` class which has full support for the load flow module through PyIPSA.
Several field types here have also been corrected from IPSA 2.10.1.

Access to database entries via PyIPSA
---------------------------------------

In PyIPSA 2.10.1, users can populate the data of their inputted components via the database finally. This is done via the member
functions owned by ``IscInterface``, such as ``OpenDBFromFile()``, ``GetDBNames()``, and ``PopulateDBEntry()`` via each specific network component.
Users can also list the entire database entries from their loaded database.

Fixes to drawing functionality
--------------------------------------

The functions that ``CreateBusbarCircular()``, ``CreateBreaker()`` and ``DrawBreaker()`` have been built and fixed so that
users do not have to rely on the UI to program circular busbars or circuit breakers.

Additional fixes
--------------------------------------

The ability to access the send and receive ratings of a given branch have now been added back to the ``IscBranch`` object within PyIPSA.
Also we have remapped the ``IscTransformer::Winding`` entry and the ``IscTransformer::VectorGroup`` entry together for longevity purposes
and corrected the ``IscDCMachine::MechPowerMW`` bug.

