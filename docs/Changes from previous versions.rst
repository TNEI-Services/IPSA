Changes from IPSA 2.10.1
=========================

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


Changes from IPSA 2.10.0
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

