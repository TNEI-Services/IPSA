*************************************
Key features of the IPSA 3 Series
*************************************

Key Features of IPSA 3.2
=============================
CIM integration to PyIPSA
----------------------------
CIM import and export has now been exposed to PyIPSA in ``IscInterface``. Additionally a new
CIM mRID generator has been created to populate the mRIDs for components currently lacking a CIM mRID mapping.
These generation functions are also accessible in PyIPSA in ``IscInterface``.

Scenarios
-----------
More scenarios functionality has been introduced. In particular, additional save file optimisations have been 
added in ``IscInterface`` to attempt to minimise the file size overhead of scenarios, and to allow areas/regions 
to be saved with only the relevant scenarios for that area. Additionally, users can now export selected 
scenarios into their own i3f files through overloads to the WriteFile and WriteArea functions.

Additionally, the scenarios interface is now more flexible, with a suite of new options in ``IscNetworkData`` to 
customise what information is tracked in scenarios and a new option in ``IscNetwork`` to set whether 
updating scenarios should change the scenario hierarchy.

Additional features
-----------------------
    - As part of a broader expansion to switchgear ratings and their integration into IPSA, circuit breakers (``IscCircuitBreaker``) now have accessible single phase ratings and short-time withstand current values that can can be used in fault analyses.
    - Users can now block the LDC contributions to load flow while the transformer flow is in reverse (through ``IscTransformer`` and ``IscAnalysisLF``).
    - Ability to parametrise asymmetric equivalent branches using ``ResistanceReversePU`` and ``ReactanceReversePU``.


Key Features of IPSA 3.1
=============================
G74 fault modelling
----------------------------------
Loads are now coupled with a fault mode that emulates induction machines based either on global settings
in ``IscAnalysisFL`` or individual impedence information in ``IscLoad``. Additionally a new option in 
``IscAnalysisFL`` allows the transformers to be forced to a maximum tap position to garner minimimum 
impedence for fault events.

Scenarios
-------------
New scenarios functionality has been added in ``IscNetwork`` to allow users to merge multiple scenarios 
simultaneously either by providing a list of scenarios to merge, or by setting a maximum date/scenario 
ID to merge up to. 
Additional functionality has been added to allow users to cascade changes to update not only the current 
scenario but also all of the current scenarios child scenarios.
Finally functionality to set the default "Fast Merge" options within the UI can be accessed through PyIPSA.

Additional features
-----------------------
    - Users can now run network reduction through PyIPSA (using ``IscNetwork.RunNetworkReduction`` in conjunction with ``IscAnalysisNR``).
    - Users can now set/unset the global override on data display styles through PyIPSA - selecting which diagram should provide the data display styles to be used across all diagrams.

Key features of IPSA 3.0
=============================

Boundaries and Network Reduction
-----------------------------------
New tool in IPSA to run a network reduction on the network based on a predefined boundary. These 
new boundaries can created and validated to define areas either from a predefined reduced area or by
explicitly definining the boundary busbars, validated to ensure no leakages will occur in the 
reduction. The ``IscBoundary`` class has been created to facilitate the creation, modification and 
validation of boundaries from PyIPSA. The ``IscEquivalentRadial`` and ``IscEquivalentBranch`` classes 
have been created to allow access to the equivalents created in the network reduction.

Scenarios
------------
A large expansion and enhancement of the previous "Versions" functionality of IPSA to Scenarios has 
occured. A full PyIPSA interface has been created within ``IscNetwork`` to allow the creation, 
deletion and modification of Scenarios as well as the comparison of Scenarios in the network. Scenarios 
have additionally been given description and date fields and brand new functionality has been included 
to Update scenarios, Merge scenarios and revert individual item modifications between one scenario and 
another. Additionally users may manage many of their Scenario UI options from the PyIPSA interface.

Advanced Feeder Analysis
----------------------------
New module in IPSA allowing for the creation and simple analysis of Feeder Groups. In particular, new
The tracing of feeder groups from feeder circuit breakers now possible through ``IscNetwork.RunFeederTrace``
and the examination of the feeder group properties and Customer Calculations are exposed to PyIPSA.
Feeder by feeder scaling has been added through the ``IscGroup`` instances.
Line Loading calculations have additionally been exposed to PyIPSA through ``GetLineLoadingPC`` on 
branch items and 3W transformers.

Geographic Map Diagrams
--------------------------
As part of the IPSA extension and refit of the Geographic map diagrams, the ability to create geographic 
map diagrams from PyIPSA and to modify their settings have all been added to ``IscDiagram``. This 
includes the ability to add and remove maps from Geographic diagram, set the geographic maps server 
and/or the style and calculate the lat-long positions from the diagram coordinates and vice versa.
Additionally, new functions to calculate the line length from Geographic diagrams (with or without Maps)
have been added to PyIPSA through ``IscDiagram.GetGeoLineLength``.

IscDrawTools
---------------
A new ``IscDrawTools`` class has been created in IPSA to allow for the modification of the default 
settings used when the User draws their network using the PolyDraw or new TreeDraw algorithm.

Draw Component Symbols
-------------------------
PyIPSA can now be used to draw Branches, Transformers, Breakers and Loads in each of the different draw 
styles selectable in the UI through new Draw functions in ``IscDiagram``.

Additional Fixes
-----------------------
Multiple new miscellaneous methods and corrections have been added to PyIPSA. These include, but are not limited to:  

    - Exposed more fault level results to PyIPSA for the ``IscSynMachine``, ``IscGridInfeed``, ``IscIndMachine`` and ``Isc3WTransformer``.
    - Extended data optimisations for ``IscTransformer`` and ``IscGridInfeed``
    - Creating PyIPSA objects will now ensure the provided UID matches the required item type.
    - PyIPSA draw functions will now connect branches to busbars graphically identically to the UI connections.
    - Generator scaling groups can now have their scaling factors managed through PyIPSA.
