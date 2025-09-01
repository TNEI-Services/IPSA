Key features of the IPSA 3 Series
======================================

Key features of IPSA 3.0
-------------------------------

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
