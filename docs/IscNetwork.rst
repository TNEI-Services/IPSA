***********
IscNetwork
***********

This object provides the main access to an IPSA network. It is generally created as the result to a call to ``IscInterface().ReadFile(strName)``. This class provides functions to retrieve, create and delete network components, perform analysis and get network results.

Network Component Functions
============================

Various functions are provided to allow the creation, deletion and editing of network components. The ``Get``… functions return instances of the component objects, for example ``GetBusbar`` returns an ``IscBusbar`` instance. Once an ``IscBusbar`` instance is retrieved the busbar data can then be accessed as described in the ``IscBusbar`` section.

Component Access
-----------------

The dictionary keys are the Python script names of components whilst the values are the instances of components. The Python script name can be used to access individual components.

The example code below details how it is possible to iterate through all the components of a particular type in a network:

::

    # retrieve the busbar collection
    busbars = net.GetBusbars()
    # cycle each busbar, retrieve its name and voltage
    for bus in busbars.values():
       # do something with the bus
        name = bus.GetName()

Two functions are also provided to return dictionaries of the unique component IDs. The dictionary keys are the Python script names while the dictionary values are the integer IDs.

Setting ``bFetchFromSystem`` to ``True`` forces IPSA to rebuild its internal component data maps. Setting ``bFetchFromSystem`` to ``False`` will only rebuild the internal component data maps if components have been added or deleted since the last ``Get``… function call. If the script creates new data components during its execution then the internal component data maps will always be rebuilt and ``bFetchFromSystem`` can be ``True`` or ``False``.

Component Ratings
==================

Rating sets determine the thermal limits that branches and transformers can tolerate. Each component can be given a set of MVA or kA values which are checked after a load flow calculation to identify if the component is overloaded. In IPSA 1.x four rating sets were provided, namely Standard, Summer, Winter and Short. In IPSA 2 these rating sets are provided by default but users can add additional rating sets. The ratings sets defined by the user, either through the IPSA interface or via scripting, are stored with the network model.

The functions used to access the rating data have therefore been changed from IPSA 1.x in order to address the user-defined rating sets.


Profiles
=========

Profiles represent a set of categories with associated MW and MVAr values. Profiles can be assigned to loads, synchronous machines and universal machines. Each network can have any number of profiles which can used to provide absolute or scaled MW and MVAr values. Every load, generator and universal machine in the network can be assigned one of the profiles and load flow analysis or profile analysis can then be performed. Scaling profiles cannot be assigned to universal machines.

Refer to section 0 for the function to run a profile study.

Different types of profiles are represented by different classes as follows;

•	Actual load profile class - ``IscLoadProfilePQActual``
•	Scaled load profile class - ``IscLoadProfilePQScale``
•	Actual generator profile class - ``IscGeneratorProfilePQActual``
•	Scaled generator profile class - ``IscGeneratorProfilePQScale``
•	Actual universal machine profile class - ``IscUMachineProfilePQActual``

Add Profile Categories
-----------------------

Profiles comprise a number of categories and associated MW and MVAr values. Each category is simply a string which identifies the category name. Examples of profile categories could be:

•	Spring, Summer, Autumn, Winter
•	Normal, Max Load, Min Load, Emergency
•	00:00hrs, 01:00hrs, 02:00hrs, 03:00hrs etc.

The category names are only for user interaction and do not relate to other network components or analysis settings such as equipment ratings.

Add Profile Data
-----------------

Each profile category can be assigned a specific MW and MVAr load for the various profile types. The MW or MVAr value assigned to each category is either an actual value or a per unit scaling value depending on the profile type.

Add Profiles to Components
---------------------------

Once a profile has been created it can then be assigned to any number of individual loads, generators and universal machines in the network. The field index ``ProfileUID`` is set to assign a profile to a network load, generator or universal machine. This is detailed in the corresponding component sections and the code below illustrates the use of all the load profile functions.

::

    # define the categories and loads
    categories = {0:"00:00",
                  1:"06:00",
                  2:"12:00",
                  3:"18:00"}

    mw = {0: 0.8,
          1: 0.775,
          2: 0.75,
          3: 0.712}
    mvar = {0: 0.48,
            1: 0.465,
            2: 0.45,
            3: 0.4272}

    # create a load profile
    profileUID = ipsanetwork.CreateLoadProfilePQActual('Test Profile')

    # get the profile ID
    profile = ipsanetwork.GetLoadProfilePQActual(profileUID)

    # add the categories to the profile and set the data
    profile.SetCategoryNames(categories)
    profile.SetPMW(mw)
    profile.SetQMVAr(mvar)

    # finally assign the profile to all network loads
    loads = ipsa_network.GetLoads()
    for load in loads.values():
        load.SetIValue(ipsa.IscLoad.ProfileUID)

Running Profile Studies
------------------------

All categories in the selected profiles are run and the results are obtained from the functions provided in each component class. All profiles must have the same set of category names. The load flow solution parameters are set using the ``IscAnalysisLF`` class.


IscNetwork Class
=================

.. autoclass:: ipsa.IscNetwork
   :members:
