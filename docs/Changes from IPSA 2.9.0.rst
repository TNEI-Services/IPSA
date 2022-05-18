Changes from IPSA 2.9.0
========================

Setting licences from environment variables
--------------------------------------------

There is a new option, only available for IPSA Linux for now, in order to set a Sentinel LDK license in IPSA. It is now possible to set the Sentinel LDK license Key ID in an environmental variable, and PyIPSA will automatically check the environmental variable if no other license is set. This enables users to run PyIPSA from non-desktop environment operative systems. The environment variable to be set is **IPSALDKLICENSE** and it expects an 18-digit (or less) license Key ID. For more details contact *support@ipsa-power.com*.

Running ArcFlash through PyIPSA
--------------------------------

New infrastructure with ``IscAnalysisAF`` and the ``RunArcFlash()`` functionality enables users to execute network wide arc flash calculations with the new and improved Arc Flash engine. Users can now set parameters as they would in the UI, run a preliminary fault level to get the base bolted currents, and show a full network diagnosis for the flash incident energy details at all busbar sites.

Storage components and flip functionality
------------------------------------------

The new functionality whereby synchronous machines can behave like energy storage units has been transferred to PyIPSA. This means you can do local and global flip implementations on storages between import and export and hold all the technology/staging information in the ``IscSynMachine`` objects just as in the UI.

Standard  features updated
---------------------------

The following functionality has been updated and correctly mapped to PyIPSA:

•	``AutoSelectSlacks`` now correctly assigns the slacks before a load flow calculation.
•	The DC Load Flow module has been improved and efficiently mapped with the ``IscAnalysisDCLF`` class.
•	Users can now set the flat start with added flexibility and set the global busbar and branch overload limits from Python.
•	Customised contingencies can be designed using the ``CreateSpecificContingency`` function.

