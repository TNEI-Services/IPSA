Changes from IPSA 2.10.0
=========================

Converter driven plant functionality
--------------------------------------------

Users in PyIPSA can co-opt the ``IscUMachine`` object to generate converter driven plants for inverter based generator fault calculations. This uses a parametrisation conforming to ERC G74/2 (more advanced functionality available in IPSA 2.10.1 UI). There is an additional flag in the fault level settings and additional data required in ``IscUMachine`` for this to work.

Choppers in PyIPSA
--------------------------------

The new DCDC Converter object is available through the ``IscChopper`` class which has full support for the load flow module through PyIPSA. 

Access DC load flow results data
------------------------------------------

In IPSA 2.10.0, we made strides to fixing the DC load flow module within PyIPSA. Now we have fully tested the functionality and also allowed it so that users can access the results in the same method as done in the standard AC load flow results framework. In each PyIPSA component, look at the methods of each class for more details!

Access to database entries via PyIPSA
---------------------------------------

In PyIPSA 2.10.1, users can populate the data of their inputted components via the database finally. This is done via the member functions owned by ``IscInterface``, such as ``OpenDBFromFile()``, ``GetDBNames()``, and ``PopulateDBEntry()`` via each specific network component. Users can also list the entire database entries from their loaded database.

Fixes to drawing functionality
--------------------------------------

The functions that ``CreateBusbarCircular()``, ``CreateBreaker()`` and ``DrawBreaker()`` have been built and fixed so that users do not have to rely on the UI to program circular busbars or circuit breakers.

DC Load Flow overloaded function
--------------------------------------

The DC load flow finally has its own unique function as ``IscNetwork::DoDCLoadFlow()`` which is a shorthand of the ``DoLoadFlow()`` alternative.

Additional fixes
--------------------------------------

The ability to access the send and receive ratings of a given branch have now been added back to the ``IscBranch`` object within PyIPSA. Also we have remapped the ``IscTransformer::Winding`` entry and the ``IscTransformer::VectorGroup`` entry together for longevity purposes and corrected the ``IscDCMachine::MechPowerMW`` bug.


