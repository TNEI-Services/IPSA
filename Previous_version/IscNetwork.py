from typing import Dict, List, Tuple, overload


class IscNetwork:
    """
    Class providing the main access to an Ipsa network.
    """
    def SetBusbarSlack(self, strBusbar: str) -> None:
        """
        Sets the busbar as the slack busbar for a particular part of the network.

        :param strBusbar: The Python busbar name which is returned by IscNetComponent.GetName().
        :type strBusbar: str
        """
        pass

    def RefreshSystem(self) -> None:
        """
        Forces Ipsa to rebuild its internal component data maps.
        This function can be used if the network has been modified outside of scripting while a script is running.
        """
        pass

    def WriteFile(self, strName: str) -> bool:
        """
        Saves the current network file at the path and the file name.

        :param strName: The file name.
        :type strName: str
        :return: Denoting whether the file is saved.
        :rtype: bool
        """
        pass

    def WriteArea(self, nAreaUID: int, strName: str) -> bool:
        """
        Saves the area group UID as a new Ipsa i2f network file.
        The file is saved in the current working directory.
        The file name should include the .i2f extension.

        :param nAreaUID: The area group UID. nAreaUID can be obtained using the IscGroup functions.
        :type strName: int
        :param strName: The file name.
        :type strName: str
        :return: Denoting whether the file is saved.
        :rtype: bool
        """
        pass

    def MergeFile(self, strMergeName: str) -> bool:
        """
        Merges the file into the current network file.

        :param strMergeName: The merged file name.
        :type strMergeName: str
        :return: Denoting whether the file is successfully saved.
        :rtype: bool
        """
        pass

    def ValidatedMergeFile(self, strMergeName: str) -> bool:
        """
        Performs a consistency check to determine if the Ipsa I2F file can be merged into the current network.
        Use the GetFilingErrors() function to get details of the merge errors.

        :param strMergeName: The merged file name.
        :type strMergeName: str
        :return: Denoting whether the file is successfully saved.
        :rtype: bool
        """
        pass

    def CommitVersion(self, strVersionName: str) -> int:
        """
        Creates a new network version which includes all non-versioned network changes.

        :param strVersionName: The new network version name.
        :type strVersionName: str
        :return: An integer representing the version ID.
        :rtype: int
        """
        pass

    def GetVersionUuid(self, nVersion: int) -> str:
        """
        Returns a unique string (UUID) representing the version name for the given version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: The version name.
        :rtype: str
        """
        pass

    def SetToVersion(self, nVersion: int) -> bool:
        """
        Selects the version of the current network.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: Denoting whether the version is successfully set or whether it does not exist.
        :rtype: bool
        """
        pass

    def CreateChangeFile(self, nVersion: int, strMergeName: str) -> bool:
        """
        Creates an Ipsa merge file based on the network differences between the given version and the current version.

        :param nVersion: The selected version.
        :type nVersion: int
        :param strMergeName: The merged file name.
        :type strMergeName: str
        :return: Denoting whether the file is successfully created.
        :rtype: bool
        """
        pass

    def GetCurrentVersion(self) -> int:
        """
        Returns the current working version. Any changes to the network are made to this version.

        :return: The current version.
        :rtype: int
        """
        pass

    def GetParentVersion(self, nVersion: int) -> int:
        """
        Returns the parent version for the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: The parent version.
        :rtype: int
        """
        pass

    def GetVersionDiffAdded(self, nVersion: int) -> List[int]:
        """
        Returns a list of component UIDs which have been added to the network in the current selected version and
        that were not in the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: List of component UIDs.
        :rtype: int
        """
        pass

    def GetVersionDiffChanged(self, nVersion: int) -> List[int]:
        """
        Returns a list of component UIDs which have been edited in the current selected version compared to
        the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: List of component UIDs.
        :rtype: int
        """
        pass

    def GetVersionDiffDeleted(self, nVersion: int) -> List[int]:
        """
        Returns a list of component UIDs which have been deleted from the network in the current selected version and
        that were in the selected version.

        :param nVersion: The selected version.
        :type nVersion: int
        :return: List of component UIDs.
        :rtype: int
        """
        pass

    def ResetResults(self) -> None:
        """Reset all analysis results."""
        pass

    def GetLastSuccessfulAutomationUID(self) -> int:
        """
        Returns the integer UID of the last successful automation study.

        :return: The last successful automation study UID.
        :rtype: int
        """
        pass

    def GetLastSuccessfulContingencyUID(self) -> int:
        """
        Returns the integer UID of the last successful contingency study.

        :return: The last successful contingency study UID.
        :rtype: int
        """
        pass

    def GetNumberOfIslands(self) -> int:
        """
        Returns the number of islands.

        :return: The number of islands.
        :rtype: int
        """
        pass

    def GetIslandsUIDs(self) -> Dict[str, List[int]]:
        """
        Returns a dictionary of integer busbar nUIDs belonging to the islands.
        The keys are the island slack busbar names or the first busbar names if no slack busbar is set for that island.

        :return: The busbars belonging to each island.
        :rtype: dict(str,list(int))
        """
        pass

    def GetNoSlackIslandsUIDs(self) -> Dict[str, List[int]]:
        """
        Returns a dictionary of integer busbar UIDs belonging to islands with no slack busbars.
        The keys are the first busbar names.

        :return: The busbars with no slack belonging to each island.
        :rtype: dict(str,list(int))
        """
        pass

    def GetNoGeneratorIslandsUIDs(self) -> Dict[str, List[int]]:
        """
        Returns a dictionary of integer busbar UIDs belonging to the islands with no generators or grid infeeds.
        The keys are the island slack busbar names or the first busbar names if no slack busbar is set for that island.

        :return: The busbars with no generators or grid infeeds belonging to each island.
        :rtype: dict(str,list(int))
        """
        pass

    def GetBusbars(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of busbars. The keys are the busbar names.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of busbars.
        :rtype: dict(str,IscBusbar)
        """
        pass

    def GetBusbarsOrderedByVoltage(self, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of busbar UIDs, sorted in ascending order of voltage and then by busbar name.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Tuple of busbars UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedBranches(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of branch UIDs attached to the busbar specified by busbar UID.
        Only branches are returned, not transformers.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Tuple of busbars UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedTransformers(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of transformer UIDs attached to the busbar specified by busbar UID.
        Only transformers are returned, not branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Tuple of transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttached3WTransformers(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of 3-winding transformer UIDs attached to the busbar specified by busbar UID.
        Only 3-winding transformers are returned, not 2-winding transformers or branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Tuple of 3-winding transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBusbarAttachedUnbalancedBranches(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of unbalanced branch UIDs attached to the busbar specified by busbar UID.
        Only unbalanced branches are returned, not unbalanced transformers.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Tuple of unbalanced branch UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetBranches(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscBranch instances.
        Key values (sPyName) are the Python names and the associated values are IscBranch instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of branches.
        :rtype: dict(str,IscBranch)
        """
        pass

    def GetBusbarAttachedUnbalancedTransformers(self, nBusbarUID: int, bFetchFromSystem: bool) -> Tuple[int]:
        """
        Returns a tuple of unbalanced transformer UIDs attached to the busbar specified by busbar UID.
        Only unbalanced transformers are returned, not unbalanced branches.

        :param nBusbarUID: The selected busbar UID.
        :type nBusbarUID: int
        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Tuple of unbalanced transformer UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetTransformers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscTransformer instances.
        Keys (sPyName) are the Python names and the associated values are IscTransformer instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of transformers.
        :rtype: dict(str,IscTransformer)
        """
        pass

    def Get3WTransformers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of Isc3WTransformer instances.
        Keys (sPyName) are the Python names and the associated values are Isc3WTransformer instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of 3WTransformers.
        :rtype: dict(str,Isc3WTransformer)
        """
        pass

    def GetLoads(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscLoad instances.
        Keys (sPyName) are the Python names and the associated values are IscLoad instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of loads.
        :rtype: dict(str,IscLoad)
        """
        pass

    def GetSynMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscSynMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscSynMachine instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of synchronous machines.
        :rtype: dict(str,IscSynMachine)
        """
        pass

    def GetGridInfeeds(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscGridInfeed instances.
        Keys (sPyName) are the Python names and the associated values are IscGridInfeed instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of grid infeeds.
        :rtype: dict(str,IscGridInfeed)
        """
        pass

    def GetFilters(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscFilter instances.
        Keys (sPyName) are the Python names and the associated values are IscFilter instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of filters.
        :rtype: dict(str,IscFilter)
        """
        pass

    def GetIndMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscIndMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscIndMachine instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of induction machines.
        :rtype: dict(str,IscIndMachine)
        """
        pass

    def GetMechSwCapacitors(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscMechSwCapacitor instances.
        Keys (sPyName) are the Python names and the associated values are IscMechSwCapacitor instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of mechanical switch capacitors.
        :rtype: dict(str,IscMechSwCapacitor)
        """
        pass

    def GetStaticVCs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscStaticVC instances.
        Keys (sPyName) are the Python names and the associated values are IscStaticVC instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of static var compensators.
        :rtype: dict(str,IscStaticVC)
        """
        pass

    def GetUMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscUMachine instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of universal machines.
        :rtype: dict(str,IscUMachine)
        """
        pass

    def GetHarmonics(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscHarmonic instances.
        Keys (sPyName) are the Python names and the associated values are IscHarmonic instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of harmonics.
        :rtype: dict(str,IscHarmonic)
        """
        pass

    def GetCircuitBreakers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscCircuitBreaker instances.
        Keys (sPyName) are the Python names and the associated values are IscCircuitBreaker instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of circuit breakers.
        :rtype: dict(str,IscCircuitBreaker)
        """
        pass

    def GetBatteries(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscBattery instances.
        Keys (sPyName) are the Python names and the associated values are IscBattery instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of batteries.
        :rtype: dict(str,IscBattery)
        """
        pass

    def GetDCMachines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscDCMachine instances.
        Keys (sPyName) are the Python names and the associated values are IscDCMachine instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of DC machines.
        :rtype: dict(str,IscDCMachine)
        """
        pass

    def GetConverters(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscConverter instances.
        Keys (sPyName) are the Python names and the associated values are IscConverter instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of converters.
        :rtype: dict(str,IscConverter)
        """
        pass

    def GetMGSets(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscMGSet instances.
        Keys (sPyName) are the Python names and the associated values are IscMGSet instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of MG sets.
        :rtype: dict(str,IscMGSet)
        """
        pass

    def GetProtectionDevices(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscProtectionDevice instances.
        Keys (sPyName) are the Python names and the associated values are IscProtectionDevice instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of protection devices.
        :rtype: dict(str,IscProtectionDevice)
        """
        pass

    def GetUnbalancedLoads(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUnbalancedLoad instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedLoad instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced loads.
        :rtype: dict(str,IscUnbalancedLoad)
        """
        pass

    def GetUnbalancedLines(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUnbalancedLine instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedLine instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced lines.
        :rtype: dict(str,IscUnbalancedLine)
        """
        pass

    def GetUnbalancedTransformers(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscUnbalancedTransformer instances.
        Keys (sPyName) are the Python names and the associated values are IscUnbalancedTransformer instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of unbalanced transformers.
        :rtype: dict(str,IscUnbalancedTransformer)
        """
        pass

    def GetVoltageRegulators(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscVoltageRegulator instances.
        Keys (sPyName) are the Python names and the associated values are IscVoltageRegulator instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of voltage regulators.
        :rtype: dict(str,IscVoltageRegulator)
        """
        pass

    def GetAnnotations(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of IscAnnotation instances.
        Keys (sPyName) are the Python names and the associated values are IscAnnotation instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of annotations.
        :rtype: dict(str,IscAnnotation)
        """
        pass

    def GetGroups(self):
        """
        Returns a dictionary of IscGroup instances.
        Keys (sPyName) are the Python names and the associated values are IscGroup instances.

        :return: Dictionary of groups.
        :rtype: dict(str,IscGroup)
        """
        pass

    def GetGroupsForItem(self, nUID: int) -> Tuple[int]:
        """
        Returns a tuple containing the group UIDs for each group that the component UID is a member of.

        :param nUID: Component UID.
        :type nUID: int
        :return: Tuple of group UIDs.
        :rtype: tuple(int)
        """
        pass

    def GetPlugins(self):
        """
        Returns a dictionary of IscPlugin instances.
        Keys (sPyName) are the Python names and the associated values are IscPlugin instances.

        :return: Dictionary of plugins.
        :rtype: dict(str,IscPlugin)
        """
        pass

    def GetBusbarUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all busbar UIDs in the network.
        The keys are the integer UIDs and the values are the IscBusbar instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of all busbar UIDs.
        :rtype: dict(int,IscBusbar)
        """
        pass

    def GetProtectionDeviceUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all protection device UIDs in the network.
        The keys are the integer UIDs and the values are the IscProtectionDevice instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of all protection devices UIDs.
        :rtype: dict(int,IscProtectionDevice)
        """
        pass

    def TraceBusbarUIDs(self, nBranchUID: int, bOpenBreakers: bool, nGroupUID: int) -> List[int]:
        """
        Performs a network trace to identify all busbars that are connected to the selected branch.
        The network trace stops when it reaches any busbar that is a member of the group of the selected group UID or
        when it reaches a transformer.

        :param nBranchUID: The selected branch UID.
        :type nBranchUID: int
        :param bOpenBreakers: If True then the trace also stops if it finds an open circuit breaker.
        :type bOpenBreakers: bool
        :param nGroupUID: The selected group UID.
        :type nGroupUID: int
        :return: List of all busbar UIDs found by the trace.
        :rtype: list(int)
        """
        pass

    def GetBusbarSlacks(self) -> List[str]:
        """
        Returns a list of all the busbar names contained in the network busbar slack list.

        :return: List of busbar names.
        :rtype: list(str)
        """
        pass

    @overload
    def GetBusbar(self, nUID: int):
        """
        Returns an IscBusbar instance for the busbar identified by the UID.

        :param nUID: The selected busbar UID.
        :type nUID: int
        :return: The busbar instance or None if such is not found.
        :rtype: IscBusbar
        """
        pass

    @overload
    def GetBusbar(self, strPythonName: str):
        """
        Returns an IscBusbar instance for the busbar identified by the Python name.

        :param strPythonName: The selected busbar name.
        :type strPythonName: str
        :return: The busbar instance or None if such is not found.
        :rtype: IscBusbar
        """
        pass

    def GetBusbar(self, strPythonName: str):
        """
        Returns an IscBusbar instance for the busbar identified by the UID or the Python name.

        You can use either nUID specifying the busbar UID, or strPythonName specifying its name.

        :param nUID: The selected busbar UID.
        :type nUID: int
        :param strPythonName: The selected busbar name.
        :type strPythonName: str
        :return: The busbar instance or None if such is not found.
        :rtype: IscBusbar
        """
        pass

    @overload
    def GetBranch(self, nUID: int):
        """
        Returns an IscBranch instance for the branch identified by the UID.

        :param nUID: The selected branch UID.
        :type nUID: int
        :return: The branch instance or None if such is not found.
        :rtype: IscBranch
        """
        pass

    @overload
    def GetBranch(self, strPythonName: str):
        """
        Returns an IscBranch instance for the branch identified by the Python name.

        :param strPythonName: The selected branch name.
        :type strPythonName: str
        :return: The branch instance or None if such is not found.
        :rtype: IscBranch
        """
        pass

    def GetBranch(self, strPythonName: str):
        """
        Returns an IscBranch instance for the branch identified by the UID or the Python name.

        You can use either nUID specifying the branch UID, or strPythonName specifying its name.

        :param nUID: The selected branch UID.
        :type nUID: int
        :param strPythonName: The selected branch name.
        :type strPythonName: str
        :return: The branch instance or None if such is not found.
        :rtype: IscBranch
        """
        pass

    @overload
    def GetTransformer(self, nUID: int):
        """
        Returns an IscTransformer instance for the transformer identified by the UID.

        :param nUID: The selected transformer UID.
        :type nUID: int
        :return: The transformer instance or None if such is not found.
        :rtype: IscTransformer
        """
        pass

    @overload
    def GetTransformer(self, strPythonName: str):
        """
        Returns an IscTransformer instance for the transformer identified by the Python name.

        :param strPythonName: The selected transformer name.
        :type strPythonName: str
        :return: The transformer instance or None if such is not found.
        :rtype: IscTransformer
        """
        pass

    def GetTransformer(self, strPythonName: str):
        """
        Returns an IscTransformer instance for the transformer identified by the UID or the Python name.

        You can use either nUID specifying the transformer UID, or strPythonName specifying its name.

        :param nUID: The selected transformer UID.
        :type nUID: int
        :param strPythonName: The selected transformer name.
        :type strPythonName: str
        :return: The transformer instance or None if such is not found.
        :rtype: IscTransformer
        """
        pass

    @overload
    def Get3WTransformer(self, nUID: int):
        """
        Returns an Isc3WTransformer instance for the three winding transformer identified by the UID.

        :param nUID: The selected three winding transformer UID.
        :type nUID: int
        :return: The three winding transformer instance or None if such is not found.
        :rtype: Isc3WTransformer
        """
        pass

    @overload
    def Get3WTransformer(self, strPythonName: str):
        """
        Returns an Isc3WTransformer instance for the three winding transformer identified by the Python name.

        :param strPythonName: The selected three winding transformer name.
        :type strPythonName: str
        :return: The three winding transformer instance or None if such is not found.
        :rtype: Isc3WTransformer
        """
        pass

    def Get3WTransformer(self, strPythonName: str):
        """
        Returns an Isc3WTransformer instance for the three winding transformer identified by the UID or the Python name.

        You can use either nUID specifying the three winding transformer UID, or strPythonName specifying its name.

        :param nUID: The selected three winding transformer UID.
        :type nUID: int
        :param strPythonName: The selected three winding transformer name.
        :type strPythonName: str
        :return: The three winding transformer instance or None if such is not found.
        :rtype: Isc3WTransformer
        """
        pass

    @overload
    def GetLoad(self, nUID: int):
        """
        Returns an IscLoad instance for the load identified by the UID.

        :param nUID: The selected load UID.
        :type nUID: int
        :return: The load instance or None if such is not found.
        :rtype: IscLoad
        """
        pass

    @overload
    def GetLoad(self, strPythonName: str):
        """
        Returns an IscLoad instance for the load identified by the Python name.

        :param strPythonName: The selected load name.
        :type strPythonName: str
        :return: The load instance or None if such is not found.
        :rtype: IscLoad
        """
        pass

    def GetLoad(self, strPythonName: str):
        """
        Returns an IscLoad instance for the load identified by the UID or the Python name.

        You can use either nUID specifying the load UID, or strPythonName specifying its name.

        :param nUID: The selected load UID.
        :type nUID: int
        :param strPythonName: The selected load name.
        :type strPythonName: str
        :return: The load instance or None if such is not found.
        :rtype: IscLoad
        """
        pass

    @overload
    def GetSynMachine(self, nUID: int):
        """
        Returns an IscSynMachine instance for the synchronous machine identified by the UID.

        :param nUID: The selected synchronous machine UID.
        :type nUID: int
        :return: The synchronous machine instance or None if such is not found.
        :rtype: IscSynMachine
        """
        pass

    @overload
    def GetSynMachine(self, strPythonName: str):
        """
        Returns an IscSynMachine instance for the synchronous machine identified by the Python name.

        :param strPythonName: The selected synchronous machine name.
        :type strPythonName: str
        :return: The synchronous machine instance or None if such is not found.
        :rtype: IscSynMachine
        """
        pass

    def GetSynMachine(self, strPythonName: str):
        """
        Returns an IscSynMachine instance for the synchronous machine identified by the UID or the Python name.

        You can use either nUID specifying the synchronous machine UID, or strPythonName specifying its name.

        :param nUID: The selected synchronous machine UID.
        :type nUID: int
        :param strPythonName: The selected synchronous machine name.
        :type strPythonName: str
        :return: The synchronous machine instance or None if such is not found.
        :rtype: IscSynMachine
        """
        pass

    @overload
    def GetGridInfeed(self, nUID: int):
        """
        Returns an IscGridInfeed instance for the grid infeed identified by the UID.

        :param nUID: The selected grid infeed UID.
        :type nUID: int
        :return: The grid infeed instance or None if such is not found.
        :rtype: IscGridInfeed
        """
        pass

    @overload
    def GetGridInfeed(self, strPythonName: str):
        """
        Returns an IscGridInfeed instance for the grid infeed identified by the Python name.

        :param strPythonName: The selected grid infeed name.
        :type strPythonName: str
        :return: The grid infeed instance or None if such is not found.
        :rtype: IscGridInfeed
        """
        pass

    def GetGridInfeed(self, strPythonName: str):
        """
        Returns an IscGridInfeed instance for the grid infeed identified by the UID or the Python name.

        You can use either nUID specifying the grid infeed UID, or strPythonName specifying its name.

        :param nUID: The selected grid infeed UID.
        :type nUID: int
        :param strPythonName: The selected grid infeed name.
        :type strPythonName: str
        :return: The grid infeed instance or None if such is not found.
        :rtype: IscGridInfeed
        """
        pass

    @overload
    def GetIndMachine(self, nUID: int):
        """
        Returns an IscIndMachine instance for the induction motor identified by the UID.

        :param nUID: The selected induction motor UID.
        :type nUID: int
        :return: The induction motor instance or None if such is not found.
        :rtype: IscIndMachine
        """
        pass

    @overload
    def GetIndMachine(self, strPythonName: str):
        """
        Returns an IscIndMachine instance for the induction motor identified by the Python name.

        :param strPythonName: The selected induction motor name.
        :type strPythonName: str
        :return: The induction motor instance or None if such is not found.
        :rtype: IscIndMachine
        """
        pass

    def GetIndMachine(self, strPythonName: str):
        """
        Returns an IscIndMachine instance for the induction motor identified by the UID or the Python name.

        You can use either nUID specifying the induction motor UID, or strPythonName specifying its name.

        :param nUID: The selected induction motor UID.
        :type nUID: int
        :param strPythonName: The selected induction motor name.
        :type strPythonName: str
        :return: The induction motor instance or None if such is not found.
        :rtype: IscIndMachine
        """
        pass

    @overload
    def GetFilter(self, nUID: int):
        """
        Returns an IscFilter instance for the harmonic filter identified by the UID.

        :param nUID: The selected harmonic filter UID.
        :type nUID: int
        :return: The harmonic filter instance or None if such is not found.
        :rtype: IscFilter
        """
        pass

    @overload
    def GetFilter(self, strPythonName: str):
        """
        Returns an IscFilter instance for the harmonic filter identified by the Python name.

        :param strPythonName: The selected harmonic filter name.
        :type strPythonName: str
        :return: The harmonic filter instance or None if such is not found.
        :rtype: IscFilter
        """
        pass

    def GetFilter(self, strPythonName: str):
        """
        Returns an IscFilter instance for the harmonic filter identified by the UID or the Python name.

        You can use either nUID specifying the harmonic filter UID, or strPythonName specifying its name.

        :param nUID: The selected harmonic filter UID.
        :type nUID: int
        :param strPythonName: The selected harmonic filter name.
        :type strPythonName: str
        :return: The harmonic filter instance or None if such is not found.
        :rtype: IscFilter
        """
        pass

    @overload
    def GetMechSwCapacitor(self, nUID: int):
        """
        Returns an IscMechSwCapacitor instance for the mechanically switched capacitor identified by the UID.

        :param nUID: The selected mechanically switched capacitor UID.
        :type nUID: int
        :return: The mechanically switched capacitor instance or None if such is not found.
        :rtype: IscMechSwCapacitor
        """
        pass

    @overload
    def GetMechSwCapacitor(self, strPythonName: str):
        """
        Returns an IscMechSwCapacitor instance for the mechanically switched capacitor identified by the Python name.

        :param strPythonName: The selected mechanically switched capacitor name.
        :type strPythonName: str
        :return: The mechanically switched capacitor instance or None if such is not found.
        :rtype: IscMechSwCapacitor
        """
        pass

    def GetMechSwCapacitor(self, strPythonName: str):
        """
        Returns an IscMechSwCapacitor instance for the mechanically switched capacitor identified by
        the UID or the Python name.

        You can use either nUID specifying the mechanically switched capacitor UID,
        or strPythonName specifying its name.

        :param nUID: The selected mechanically switched capacitor UID.
        :type nUID: int
        :param strPythonName: The selected mechanically switched capacitor name.
        :type strPythonName: str
        :return: The mechanically switched capacitor instance or None if such is not found.
        :rtype: IscMechSwCapacitor
        """
        pass

    @overload
    def GetStaticVC(self, nUID: int):
        """
        Returns an IscStaticVC instance for the static VAR compensator identified by the UID.

        :param nUID: The selected static VAR compensator UID.
        :type nUID: int
        :return: The static VAR compensator instance or None if such is not found.
        :rtype: IscStaticVC
        """
        pass

    @overload
    def GetStaticVC(self, strPythonName: str):
        """
        Returns an IscStaticVC instance for the static VAR compensator identified by the Python name.

        :param strPythonName: The selected static VAR compensator name.
        :type strPythonName: str
        :return: The static VAR compensator instance or None if such is not found.
        :rtype: IscStaticVC
        """
        pass

    def GetStaticVC(self, strPythonName: str):
        """
        Returns an IscStaticVC instance for the static VAR compensator identified by the UID or the Python name.

        You can use either nUID specifying the static VAR compensator UID, or strPythonName specifying its name.

        :param nUID: The selected static VAR compensator UID.
        :type nUID: int
        :param strPythonName: The selected static VAR compensator name.
        :type strPythonName: str
        :return: The static VAR compensator instance or None if such is not found.
        :rtype: IscStaticVC
        """
        pass

    @overload
    def GetBranchGetUMachine(self, nUID: int):
        """
        Returns an IscUMachine instance for the universal machine identified by the UID.

        :param nUID: The selected universal machine UID.
        :type nUID: int
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    @overload
    def GetBranchGetUMachine(self, strPythonName: str):
        """
        Returns an IscUMachine instance for the universal machine identified by the Python name.

        :param strPythonName: The selected universal machine name.
        :type strPythonName: str
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    def GetBranchGetUMachine(self, strPythonName: str):
        """
        Returns an IscUMachine instance for the universal machine identified by the UID or the Python name.

        You can use either nUID specifying the universal machine UID, or strPythonName specifying its name.

        :param nUID: The selected universal machine UID.
        :type nUID: int
        :param strPythonName: The selected universal machine name.
        :type strPythonName: str
        :return: The universal machine instance or None if such is not found.
        :rtype: IscUMachine
        """
        pass

    @overload
    def GetHarmonic(self, nUID: int):
        """
        Returns an IscHarmonic instance for the harmonic source identified by the UID.

        :param nUID: The selected harmonic source UID.
        :type nUID: int
        :return: The harmonic source instance or None if such is not found.
        :rtype: IscHarmonic
        """
        pass

    @overload
    def GetHarmonic(self, strPythonName: str):
        """
        Returns an IscHarmonic instance for the harmonic source identified by the Python name.

        :param strPythonName: The selected harmonic source name.
        :type strPythonName: str
        :return: The harmonic source instance or None if such is not found.
        :rtype: IscHarmonic
        """
        pass

    def GetHarmonic(self, strPythonName: str):
        """
        Returns an IscHarmonic instance for the harmonic source identified by the UID or the Python name.

        You can use either nUID specifying the harmonic source UID, or strPythonName specifying its name.

        :param nUID: The selected harmonic source UID.
        :type nUID: int
        :param strPythonName: The selected harmonic source name.
        :type strPythonName: str
        :return: The harmonic source instance or None if such is not found.
        :rtype: IscHarmonic
        """
        pass

    @overload
    def GetCircuitBreaker(self, nUID: int):
        """
        Returns an IscCircuitBreaker instance for the circuit breaker identified by the Python name.

        :param nUID: The selected circuit breaker UID.
        :type nUID: int
        :return: The circuit breaker instance or None if such is not found.
        :rtype: IscCircuitBreaker
        """
        pass

    @overload
    def GetCircuitBreaker(self, strPythonName: str):
        """
        Returns an IscCircuitBreaker instance for the circuit breaker identified by the Python name.

        :param strPythonName: The selected circuit breaker name.
        :type strPythonName: str
        :return: The circuit breaker instance or None if such is not found.
        :rtype: IscCircuitBreaker
        """
        pass

    def GetCircuitBreaker(self, strPythonName: str):
        """
        Returns an IscCircuitBreaker instance for the circuit breaker identified by the UID or the Python name.

        You can use either nUID specifying the circuit breaker UID, or strPythonName specifying its name.

        :param nUID: The selected circuit breaker UID.
        :type nUID: int
        :param strPythonName: The selected circuit breaker name.
        :type strPythonName: str
        :return: The circuit breaker instance or None if such is not found.
        :rtype: IscCircuitBreaker
        """
        pass

    @overload
    def GetBattery(self, nUID: int):
        """
        Returns an IscBattery instance for the DC battery identified by the UID.

        :param nUID: The selected DC battery UID.
        :type nUID: int
        :return: The DC battery instance or None if such is not found.
        :rtype: IscBattery
        """
        pass

    @overload
    def GetBattery(self, strPythonName: str):
        """
        Returns an IscBattery instance for the DC battery identified by the Python name.

        :param strPythonName: The selected DC battery name.
        :type strPythonName: str
        :return: The DC battery instance or None if such is not found.
        :rtype: IscBattery
        """
        pass

    def GetBattery(self, strPythonName: str):
        """
        Returns an IscBattery instance for the DC battery identified by the UID or the Python name.

        You can use either nUID specifying the DC battery UID, or strPythonName specifying its name.

        :param nUID: The selected DC battery UID.
        :type nUID: int
        :param strPythonName: The selected DC battery name.
        :type strPythonName: str
        :return: The DC battery instance or None if such is not found.
        :rtype: IscBattery
        """
        pass

    @overload
    def GetDCMachine(self, nUID: int):
        """
        Returns an IscDCMachine instance for the DC machine identified by the UID.

        :param nUID: The selected DC machine UID.
        :type nUID: int
        :return: The DC machine instance or None if such is not found.
        :rtype: IscDCMachine
        """
        pass

    @overload
    def GetDCMachine(self, strPythonName: str):
        """
        Returns an IscDCMachine instance for the DC machine identified by the Python name.

        :param strPythonName: The selected DC machine name.
        :type strPythonName: str
        :return: The DC machine instance or None if such is not found.
        :rtype: IscDCMachine
        """
        pass

    def GetDCMachine(self, strPythonName: str):
        """
        Returns an IscDCMachine instance for the DC machine identified by the UID or the Python name.

        You can use either nUID specifying the DC machine UID, or strPythonName specifying its name.

        :param nUID: The selected DC machine UID.
        :type nUID: int
        :param strPythonName: The selected DC machine name.
        :type strPythonName: str
        :return: The DC machine instance or None if such is not found.
        :rtype: IscDCMachine
        """
        pass

    @overload
    def GetConverter(self, nUID: int):
        """
        Returns an IscConverter instance for the AC/DC convertor identified by the UID.

        :param nUID: The selected AC/DC convertor UID.
        :type nUID: int
        :return: The AC/DC convertor instance or None if such is not found.
        :rtype: IscConverter
        """
        pass

    @overload
    def GetConverter(self, strPythonName: str):
        """
        Returns an IscConverter instance for the AC/DC convertor identified by the Python name.

        :param strPythonName: The selected AC/DC convertor name.
        :type strPythonName: str
        :return: The AC/DC convertor instance or None if such is not found.
        :rtype: IscConverter
        """
        pass

    def GetConverter(self, strPythonName: str):
        """
        Returns an IscConverter instance for the AC/DC convertor identified by the UID or the Python name.

        You can use either nUID specifying the AC/DC convertor UID, or strPythonName specifying its name.

        :param nUID: The selected AC/DC convertor UID.
        :type nUID: int
        :param strPythonName: The selected AC/DC convertor name.
        :type strPythonName: str
        :return: The AC/DC convertor instance or None if such is not found.
        :rtype: IscConverter
        """
        pass

    @overload
    def GetMGSet(self, nUID: int):
        """
        Returns an IscMGSet instance for the motor generator set identified by the UID.

        :param nUID: The selected motor generator set UID.
        :type nUID: int
        :return: The motor generator set instance or None if such is not found.
        :rtype: IscMGSet
        """
        pass

    @overload
    def GetMGSet(self, strPythonName: str):
        """
        Returns an IscMGSet instance for the motor generator set identified by the Python name.

        :param strPythonName: The selected motor generator set name.
        :type strPythonName: str
        :return: The motor generator set instance or None if such is not found.
        :rtype: IscMGSet
        """
        pass

    def GetMGSet(self, strPythonName: str):
        """
        Returns an IscMGSet instance for the motor generator set identified by the UID or the Python name.

        You can use either nUID specifying the motor generator set UID, or strPythonName specifying its name.

        :param nUID: The selected motor generator set UID.
        :type nUID: int
        :param strPythonName: The selected motor generator set name.
        :type strPythonName: str
        :return: The motor generator set instance or None if such is not found.
        :rtype: IscMGSet
        """
        pass

    @overload
    def GetVoltageRegulator(self, nUID: int):
        """
        Returns an IscVoltageRegulator instance for the voltage regulator identified by the UID.

        :param nUID: The selected voltage regulator UID.
        :type nUID: int
        :return: The voltage regulator instance or None if such is not found.
        :rtype: IscVoltageRegulator
        """
        pass

    @overload
    def GetVoltageRegulator(self, strPythonName: str):
        """
        Returns an IscVoltageRegulator instance for the voltage regulator identified by the Python name.

        :param strPythonName: The selected voltage regulator name.
        :type strPythonName: str
        :return: The voltage regulator instance or None if such is not found.
        :rtype: IscVoltageRegulator
        """
        pass

    def GetVoltageRegulator(self, strPythonName: str):
        """
        Returns an IscVoltageRegulator instance for the voltage regulator identified by the UID or the Python name.

        You can use either nUID specifying the voltage regulator UID, or strPythonName specifying its name.

        :param nUID: The selected voltage regulator UID.
        :type nUID: int
        :param strPythonName: The selected voltage regulator name.
        :type strPythonName: str
        :return: The voltage regulator instance or None if such is not found.
        :rtype: IscVoltageRegulator
        """
        pass

    @overload
    def GetProtectionDevice(self, nUID: int):
        """
        Returns an IscProtectionDevice instance for the protection device identified by the UID.

        :param nUID: The selected protection device  UID.
        :type nUID: int
        :return: The protection device instance or None if such is not found.
        :rtype: IscProtectionDevice
        """
        pass

    @overload
    def GetProtectionDevice(self, strPythonName: str):
        """
        Returns an IscProtectionDevice instance for the protection device identified by the Python name.

        :param strPythonName: The selected protection device name.
        :type strPythonName: str
        :return: The protection device instance or None if such is not found.
        :rtype: IscProtectionDevice
        """
        pass

    def GetProtectionDevice(self, strPythonName: str):
        """
        Returns an IscProtectionDevice instance for the protection device identified by the UID or the Python name.

        You can use either nUID specifying the protection device UID, or strPythonName specifying its name.

        :param nUID: The selected protection device  UID.
        :type nUID: int
        :param strPythonName: The selected protection device name.
        :type strPythonName: str
        :return: The protection device instance or None if such is not found.
        :rtype: IscProtectionDevice
        """
        pass

    @overload
    def GetAnnotation(self, nUID: int):
        """
        Returns an IscAnnotation instance for the diagram annotation identified by the UID.

        :param nUID: The selected diagram annotation UID.
        :type nUID: int
        :return: The diagram annotation instance or None if such is not found.
        :rtype: IscAnnotation
        """
        pass

    @overload
    def GetAnnotation(self, strPythonName: str):
        """
        Returns an IscAnnotation instance for the diagram annotation identified by the Python name.

        :param strPythonName: The selected diagram annotation name.
        :type strPythonName: str
        :return: The diagram annotation instance or None if such is not found.
        :rtype: IscAnnotation
        """
        pass

    def GetAnnotation(self, strPythonName: str):
        """
        Returns an IscAnnotation instance for the diagram annotation identified by the UID or the Python name.

        You can use either nUID specifying the diagram annotation UID, or strPythonName specifying its name.

        :param nUID: The selected diagram annotation UID.
        :type nUID: int
        :param strPythonName: The selected diagram annotation name.
        :type strPythonName: str
        :return: The diagram annotation instance or None if such is not found.
        :rtype: IscAnnotation
        """
        pass

    @overload
    def GetGroup(self, nUID: int):
        """
        Returns an IscGroup instance for the group identified by the UID.

        :param nUID: The selected group UID.
        :type nUID: int
        :return: The group instance or None if such is not found.
        :rtype: IscGroup
        """
        pass

    @overload
    def GetGroup(self, strPythonName: str):
        """
        Returns an IscGroup instance for the group identified by the Python name.

        :param strPythonName: The selected group name.
        :type strPythonName: str
        :return: The group instance or None if such is not found.
        :rtype: IscGroup
        """
        pass

    def GetGroup(self, strPythonName: str):
        """
        Returns an IscGroup instance for the group identified by the UID or the Python name.

        You can use either nUID specifying the group UID, or strPythonName specifying its name.

        :param nUID: The selected group UID.
        :type nUID: int
        :param strPythonName: The selected group name.
        :type strPythonName: str
        :return: The group instance or None if such is not found.
        :rtype: IscGroup
        """
        pass

    @overload
    def GetPlugin(self, nUID: int):
        """
        Returns an IscPlugin instance for the plugin identified by the UID.

        :param nUID: The selected plugin UID.
        :type nUID: int
        :return: The plugin instance or None if such is not found.
        :rtype: IscPlugin
        """
        pass

    @overload
    def GetPlugin(self, strPythonName: str):
        """
        Returns an IscPlugin instance for the plugin identified by the Python name.
        :param strPythonName: The selected plugin name.
        :type strPythonName: str
        :return: The plugin instance or None if such is not found.
        :rtype: IscPlugin
        """
        pass

    def GetPlugin(self, strPythonName: str):
        """
        Returns an IscPlugin instance for the plugin identified by the UID or the Python name.

        You can use either nUID specifying the plugin UID, or strPythonName specifying its name.

        :param nUID: The selected plugin UID.
        :type nUID: int
        :param strPythonName: The selected plugin name.
        :type strPythonName: str
        :return: The plugin instance or None if such is not found.
        :rtype: IscPlugin
        """
        pass

    def GetUnbalancedLoad(self, nUID: int):
        """
        Returns an IscUnbalancedLoad instance for the unbalanced load identified by the UID or the Python name.

        :param nUID: The selected unbalanced load UID.
        :type nUID: int
        :return: The unbalanced load instance or None if such is not found.
        :rtype: IscUnbalancedLoad
        """
        pass

    def GetUnbalancedLine(self, nUID: int):
        """
        Returns an IscUnbalancedLine instance for the unbalanced line identified by the UID or the Python name.

        :param nUID: The selected unbalanced line UID.
        :type nUID: int
        :return: The unbalanced line instance or None if such is not found.
        :rtype: IscUnbalancedLine
        """
        pass

    def GetUnbalancedTransformer(self, nUID: int):
        """
        Returns an IscUnbalancedTransformer instance for the unbalanced transformer identified by
        the UID or the Python name.

        :param nUID: The selected unbalanced transformer UID.
        :type nUID: int
        :return: The unbalanced transformer instance or None if such is not found.
        :rtype: IscUnbalancedTransformer
        """
        pass

    def GetNetworkData(self):
        """
        Returns an IscNetworkData instance of the network.
        The IscNetworkData object provides access to network wide properties such as the base MVA.

        :return: A network data instance of the network.
        :rtype: IscNetworkData
        """
        pass

    def GetBusbarUID(self, strName: str) -> int:
        """
        Returns the UID of a busbar with the given name.

        :param strName: The selected busbar name.
        :type strName: str
        :return: The busbar UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetBranchUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a branch with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected branch name.
        :type strName: str
        :return: The branch UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetBranchUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all branch UIDs in the network.
        The keys are the integer UIDs and the values are the IscBranch instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of all branches.
        :rtype: dict(int,IscBranch)
        """
        pass

    @overload
    def GetBranchUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns all branches connecting two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: List of branch UIDs.
        :rtype: list(int)
        """
        pass

    def GetBranchUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns a dictionary of all branch UIDs in the network if bFetchFromSystem is specified.
        The keys are the integer UIDs and the values are the IscBranch instances.

        Returns all branches connecting two busbars that are specified by their UIDs if nFromID and nToID are specified.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: Dictionary of all branches.
        :rtype: dict(int,IscBranch)
        :return: List of branch UIDs.
        :rtype: list(int)
        """
        pass

    def GetTransformerUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a transformer with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected transformer name.
        :type strName: str
        :return: The transformer UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def GetTransformerUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all transformer UIDs in the network.
        The keys are the integer UIDs and the values are the IscTransformer instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of all transformer UIDs.
        :rtype: dict(int,IscTransformer)
        """
        pass

    @overload
    def GetTransformerUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns all transformers connecting two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: List of transformers UIDs.
        :rtype: list(int)
        """
        pass

    def GetTransformerUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns a dictionary of all transformer UIDs in the network if bFetchFromSystem is specified.
        The keys are the integer UIDs and the values are the IscTransformer instances.

        Returns all transformers connecting two busbars that are specified by their UIDs if nFromID and
        nToID are specified.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: Dictionary of all transformer UIDs.
        :rtype: dict(int,IscTransformer)
        :return: List of transformers UIDs.
        :rtype: list(int)
        """
        pass

    def Get3WTransformerUID(self, nFromID: int, nToID: int, nTeritaryID: int, strName: str) -> int:
        """
        Returns the UID of a 3 winding transformer with the given name between three busbars that are specified
        by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param nTeritaryID: The UID of the Teritary busbar.
        :type nTeritaryID: int
        :param strName: The selected 3 winding transformer name.
        :type strName: str
        :return: The 3 winding transformer UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    @overload
    def Get3WTransformerUIDs(self, bFetchFromSystem: bool):
        """
        Returns a dictionary of all busbar UIDs in the network.
        The keys are the integer UIDs and the values are the IscBusbar instances.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :return: Dictionary of all 3WTransformers.
        :rtype: dict(int,Isc3WTransformer)
        """
        pass

    @overload
    def Get3WTransformerUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns all 3 winding transformers connecting two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: List of 3 winding transformers UIDs.
        :rtype: list(int)
        """
        pass

    def Get3WTransformerUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns a dictionary of all busbar UIDs in the network if bFetchFromSystem is specified.
        The keys are the integer UIDs and the values are the IscBusbar instances.

        Returns all 3 winding transformers connecting two busbars that are specified by their UIDs if nFromID and
        nToID are specified.

        :param bFetchFromSystem: Setting bFetchFromSystem to True forces Ipsa to rebuild
            its internal component data maps.
            Setting bFetchFromSystem to False will only rebuild the internal component data maps if
            components have been added or deleted since the last Get… function call.
            If the script creates new data components during its execution then the internal component data maps
            will always be rebuilt and bFetchFromSystem can be True or False.
        :type bFetchFromSystem: bool
        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: Dictionary of all 3WTransformers.
        :rtype: dict(int,Isc3WTransformer)
        :return: List of 3 winding transformers UIDs.
        :rtype: list(int)
        """
        pass

    def GetLoadUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a load with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected load name.
        :type strName: str
        :return: The load UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetLoadUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all loads connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of load UIDs.
        :rtype: list(int)
        """
        pass

    def GetSynMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a synchronous machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected synchronous machine name.
        :type strName: str
        :return: The synchronous machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetSynMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all synchronous machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of synchronous machine UIDs.
        :rtype: list(int)
        """
        pass

    def GetGridInfeedUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a grid infeed with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected grid infeed name.
        :type strName: str
        :return: The grid infeed UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetGridInfeedUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all grid infeeds connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of grid infeed UIDs.
        :rtype: list(int)
        """
        pass

    def GetIndMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of an induction machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected induction machine name.
        :type strName: str
        :return: The induction machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetIndMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all induction machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of induction machine UIDs.
        :rtype: list(int)
        """
        pass

    def GetFilterUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a filter with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected filter name.
        :type strName: str
        :return: The filter UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetFilterUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all filters connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of filter UIDs.
        :rtype: list(int)
        """
        pass

    def GetMechSwCapacitorUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a mechanically switched capacitor with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected mechanically switched capacitor name.
        :type strName: str
        :return: The mechanically switched capacitor UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetMechSwCapacitorUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all mechanically switched capacitors connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of mechanically switched capacitor UIDs.
        :rtype: list(int)
        """
        pass

    def GetStaticVCUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a static VAr compensator with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected static VAr compensator name.
        :type strName: str
        :return: The static VAr compensator UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetStaticVCUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all static VAr compensators connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of static VAr compensator UIDs.
        :rtype: list(int)
        """
        pass

    def GetUMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a universal machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected universal machine name.
        :type strName: str
        :return: The universal machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetUMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all universal machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of universal machine UIDs.
        :rtype: list(int)
        """
        pass

    def GetHarmonicUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a harmonic source with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected harmonic source name.
        :type strName: str
        :return: The harmonic source UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetHarmonicUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all harmonic sources connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of harmonic source UIDs.
        :rtype: list(int)
        """
        pass

    def GetCircuitBreakerUID(self, nBranchOrTxID: int, nClosestBusbarUID: int) -> int:
        """
        Returns the UID of a circuit breaker located on the branch or transformer specified by its UID.
        The From or To end of the branch is specified by the nClosestBusbarUID parameter.

        :param nBranchOrTxID: The UID of the branch or the transformer.
        :type nBranchOrTxID: int
        :param nClosestBusbarUID: Identifies the busbar at either the From or To end.
        :type nClosestBusbarUID: int
        :return: The circuit breaker UID, 0 if no matches.
        :rtype: int
        """
        pass

    def GetFromCircuitBreakerUID(self, nBranchOrTxID: int) -> int:
        """
        Returns the UID of a circuit breaker located on the "From" end of the branch or transformer
        specified by its UID.

        :param nBranchOrTxID: The UID of the branch or the transformer.
        :type nBranchOrTxID: int
        :return: The circuit breaker UID, 0 if no matches.
        :rtype: int
        """
        pass

    def GetToCircuitBreakerUID(self, nBranchOrTxID: int) -> int:
        """
        Returns the UID of a circuit breaker located on the "To" end of the branch or transformer
        specified by its UID.

        :param nBranchOrTxID: The UID of the branch or the transformer.
        :type nBranchOrTxID: int
        :return: The circuit breaker UID, 0 if no matches.
        :rtype: int
        """
        pass

    def GetBatteryUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a battery with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected battery name.
        :type strName: str
        :return: The battery UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetBatteryUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all batteries connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of battery UIDs.
        :rtype: list(int)
        """
        pass

    def GetDCMachineUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of a DC Machine with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected DC Machine name.
        :type strName: str
        :return: The DC Machine UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetDCMachineUIDs(self, nBusID: int) -> List[int]:
        """
        Returns all DC Machines connected to the busbars specified by the given UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :return: List of DC Machine UIDs.
        :rtype: list(int)
        """
        pass

    def GetConverterUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a converter with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected converter name.
        :type strName: str
        :return: The converter UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetConverterUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns all converters connected between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: List of converter UIDs.
        :rtype: list(int)
        """
        pass

    def GetMGSetUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of a motor/generator with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected motor/generator name.
        :type strName: str
        :return: The motor/generator UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetMGSetUIDs(self, nFromID: int, nToID: int) -> List[int]:
        """
        Returns all motors/generators connected between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :return: List of motor/generator UIDs.
        :rtype: list(int)
        """
        pass

    def GetUnbalancedLoadUID(self, nBusID: int, strName: str) -> int:
        """
        Returns the UID of an unbalanced load with specified name at busbar specified by its UID.

        :param nBusID: The UID of the busbar.
        :type nBusID: int
        :param strName: The selected unbalanced load name.
        :type strName: str
        :return: The unbalanced load UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetUnbalancedLineUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of an unbalanced line with the given name between two busbars that are specified by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected unbalanced line name.
        :type strName: str
        :return: The unbalanced line UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetUnbalancedTransformerUID(self, nFromID: int, nToID: int, strName: str) -> int:
        """
        Returns the UID of an unbalanced transformer with the given name between two busbars that are specified
        by their UIDs.

        :param nFromID: The UID of the From busbar.
        :type nFromID: int
        :param nToID: The UID of the To busbar.
        :type nToID: int
        :param strName: The selected unbalanced transformer name.
        :type strName: str
        :return: The unbalanced transformer UID, 0 if no matches or -N if we have N matches.
        :rtype: int
        """
        pass

    def GetVoltageRegulatorUID(self, nBranchID: int) -> int:
        """
        Returns the UID of a voltage regulator at branch specified by its UID.

        :param nBranchID: The UID of the branch.
        :type nBranchID: int
        :return: The voltage regulator UID.
        :rtype: int
        """
        pass

    def GetProfileUID(self, nUID: int) -> int:
        """
        Returns the integer UID of the profile for the component UID.

        :param nUID: The UID of component. nUID may be the UID of a load, generator, grid infeed or Universal Machine.
        :type nUID: int
        :return: The profile for the component UID, 0 if the component nUID does not have a profile assigned to it,
        or if nUID is not a load, generator, grid infeed or universal machine.
        :rtype: int
        """
        pass

    def CreateBusbar(self, strName: str) -> int:
        """
        Returns the UID for the newly created busbar.

        **Warning: It is up to the script to ensure that the busbar name is unique.**


        :param strName: The branch name string if required.
        :type strName: str
        :return: The UID for the newly created busbar, 0 on failure.
        :rtype: int
        """
        pass

    def CreateBusbarNoGraphics(self, strName: str):
        """
        Returns an IscBusbar object for the newly created busbar.

        **Warning: It is up to the script to ensure that the busbar name is unique.**


        :param strName: The busbar name string if required.
        :type strName: str
        :return: The IscBusbar object for the newly created busbar.
        :rtype: IscBusbar
        """
        pass

    @overload
    def CreateBranch(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created branch.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The branch name string if required.
        :type strName: str
        :return: The UID for the newly created branch, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateBranch(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscBranch object for the newly created branch.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The branch name string if required.
        :type strName: str
        :return: The IscBranch object for the newly created branch.
        :rtype: IscBranch
        """
        pass

    def CreateBranch(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscBranch object for the newly created branch.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The branch name string if required.
        :type strName: str
        :return: The UID for the newly created branch, 0 on failure.
        :rtype: int
        :return: The IscBranch object for the newly created branch.
        :rtype: IscBranch
        """
        pass

    @overload
    def CreateTransformer(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The transformer name string if required.
        :type strName: str
        :return: The UID for the newly created transformer, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscTransformer object for the newly created transformer.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The transformer name string if required.
        :type strName: str
        :return: The IscTransformer object for the newly created transformer.
        :rtype: IscTransformer
        """
        pass

    def CreateTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscTransformer object for the newly created transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The transformer name string if required.
        :type strName: str
        :return: The UID for the newly created transformer, 0 on failure.
        :rtype: int
        :return: The IscTransformer object for the newly created transformer.
        :rtype: IscTransformer
        """
        pass

    @overload
    def Create3WTransformer(self, nFromBusbarUID: int, nToBusbarUID: int, nTeritaryBusUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created 3-winding transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param nTeritaryBusUID: The "Teritary" busbar UID.
        :type nTeritaryBusUID: int
        :param strName: The 3-winding transformer name string if required.
        :type strName: str
        :return: The UID for the newly created 3-winding transformer, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def Create3WTransformer(self, pFromBusbar, pToBusbar, pTeritaryBus, strName: str):
        """
        Returns an Isc3WTransformer object for the newly created 3-winding transformer.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param pTeritaryBus: The "Teritary" busbar.
        :type pTeritaryBus: IscBusbar
        :param strName: The 3-winding transformer name string if required.
        :type strName: str
        :return: The Isc3WTransformer object for the newly created 3-winding transformer.
        :rtype: Isc3WTransformer
        """
        pass

    def Create3WTransformer(self, pFromBusbar, pToBusbar, pTeritaryBus, strName: str):
        """
        Returns the UID or an Isc3WTransformer object for the newly created 3-winding transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param nTeritaryBusUID: The "Teritary" busbar UID.
        :type nTeritaryBusUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param pTeritaryBus: The "Teritary" busbar.
        :type pTeritaryBus: IscBusbar
        :param strName: The 3-winding transformer name string if required.
        :type strName: str
        :return: The UID for the newly created 3-winding transformer, 0 on failure.
        :rtype: int
        :return: The Isc3WTransformer object for the newly created 3-winding transformer.
        :rtype: Isc3WTransformer
        """
        pass

    @overload
    def CreateLoad(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The load name string if required.
        :type strName: str
        :return: The UID for the newly created load, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateLoad(self, pAtBusbar, strName: str):
        """
        Returns an IscLoad object for the newly created load.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The load name string if required.
        :type strName: str
        :return: The IscLoad object for the newly created load.
        :rtype: IscLoad
        """
        pass

    def CreateLoad(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscLoad object for the newly created load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The load name string if required.
        :type strName: str
        :return: The UID for the newly created load, 0 on failure.
        :rtype: int
        :return: The IscLoad object for the newly created load.
        :rtype: IscLoad
        """
        pass

    @overload
    def CreateIndMachine(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created induction machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The induction machine name string if required.
        :type strName: str
        :return: The UID for the newly created induction machine, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateIndMachine(self, pAtBusbar, strName: str):
        """
        Returns an IscIndMachine object for the newly created induction machine.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The induction machine name string if required.
        :type strName: str
        :return: The IscIndMachine object for the newly created induction machine.
        :rtype: IscIndMachine
        """
        pass

    def CreateIndMachine(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscIndMachine object for the newly created induction machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The induction machine name string if required.
        :type strName: str
        :return: The UID for the newly created induction machine, 0 on failure.
        :rtype: int
        :return: The IscIndMachine object for the newly created induction machine.
        :rtype: IscIndMachine
        """
        pass

    @overload
    def CreateSynMachine(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created synchronous machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The synchronous machine name string if required.
        :type strName: str
        :return: The UID for the newly created synchronous machine, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateSynMachine(self, pAtBusbar, strName: str):
        """
        Returns an IscSynMachine object for the newly created synchronous machine.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The synchronous machine name string if required.
        :type strName: str
        :return: The IscSynMachine object for the newly created synchronous machine.
        :rtype: IscSynMachine
        """
        pass

    def CreateSynMachine(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscSynMachine object for the newly created synchronous machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The synchronous machine name string if required.
        :type strName: str
        :return: The UID for the newly created synchronous machine, 0 on failure.
        :rtype: int
        :return: The IscSynMachine object for the newly created synchronous machine.
        :rtype: IscSynMachine
        """
        pass

    @overload
    def CreateGridInfeed(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created grid infeed.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The grid infeed name string if required.
        :type strName: str
        :return: The UID for the newly created grid infeed, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateGridInfeed(self, pAtBusbar, strName: str):
        """
        Returns an IscGridInfeed object for the newly created grid infeed.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The grid infeed name string if required.
        :type strName: str
        :return: The IscGridInfeed object for the newly created grid infeed.
        :rtype: IscGridInfeed
        """
        pass

    def CreateGridInfeed(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscGridInfeed object for the newly created grid infeed.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The grid infeed name string if required.
        :type strName: str
        :return: The UID for the newly created grid infeed, 0 on failure.
        :rtype: int
        :return: The IscGridInfeed object for the newly created grid infeed.
        :rtype: IscGridInfeed
        """
        pass

    @overload
    def CreateFilter(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created filter.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The filter name string if required.
        :type strName: str
        :return: The UID for the newly created filter, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateFilter(self, pAtBusbar, strName: str):
        """
        Returns an IscFilter object for the newly created filter.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The filter name string if required.
        :type strName: str
        :return: The IscFilter object for the newly created filter.
        :rtype: IscFilter
        """
        pass

    def CreateFilter(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscFilter object for the newly created filter.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The filter name string if required.
        :type strName: str
        :return: The UID for the newly created filter, 0 on failure.
        :rtype: int
        :return: The IscFilter object for the newly created filter.
        :rtype: IscFilter
        """
        pass

    @overload
    def CreateHarmonic(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created harmonic source.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The harmonic source name string if required.
        :type strName: str
        :return: The UID for the newly created harmonic source, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateHarmonic(self, pAtBusbar, strName: str):
        """
        Returns an IscHarmonic object for the newly created harmonic source.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The harmonic source name string if required.
        :type strName: str
        :return: The IscHarmonic object for the newly created harmonic source.
        :rtype: IscHarmonic
        """
        pass

    def CreateHarmonic(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscHarmonic object for the newly created harmonic source.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The harmonic source name string if required.
        :type strName: str
        :return: The UID for the newly created harmonic source, 0 on failure.
        :rtype: int
        :return: The IscHarmonic object for the newly created harmonic source.
        :rtype: IscHarmonic
        """
        pass

    @overload
    def CreateDCMachine(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created DC machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The DC machine name string if required.
        :type strName: str
        :return: The UID for the newly created DC machine, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateDCMachine(self, pAtBusbar, strName: str):
        """
        Returns an IscDCMachine object for the newly created DC machine.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The DC machine name string if required.
        :type strName: str
        :return: The IscDCMachine object for the newly created DC machine.
        :rtype: IscDCMachine
        """
        pass

    def CreateDCMachine(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscDCMachine object for the newly created DC machine.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The DC machine name string if required.
        :type strName: str
        :return: The UID for the newly created DC machine, 0 on failure.
        :rtype: int
        :return: The IscDCMachine object for the newly created DC machine.
        :rtype: IscDCMachine
        """
        pass

    @overload
    def CreateConverter(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created AC/DC converter.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The AC/DC converter name string if required.
        :type strName: str
        :return: The UID for the newly created AC/DC converter, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateConverter(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscConverter object for the newly created AC/DC converter.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The AC/DC converter name string if required.
        :type strName: str
        :return: The IscConverter object for the newly created AC/DC converter.
        :rtype: IscConverter
        """
        pass

    def CreateConverter(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscConverter object for the newly created AC/DC converter.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The AC/DC converter name string if required.
        :type strName: str
        :return: The UID for the newly created AC/DC converter, 0 on failure.
        :rtype: int
        :return: The IscConverter object for the newly created AC/DC converter.
        :rtype: IscConverter
        """
        pass

    @overload
    def CreateMGSet(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created motor/generator set.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The motor/generator set name string if required.
        :type strName: str
        :return: The UID for the newly created motor/generator set, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateMGSet(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscMGSet object for the newly created motor/generator set.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The motor/generator set name string if required.
        :type strName: str
        :return: The IscMGSet object for the newly created motor/generator set.
        :rtype: IscMGSet
        """
        pass

    def CreateMGSet(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscMGSet object for the newly created motor/generator set.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The motor/generator set name string if required.
        :type strName: str
        :return: The UID for the newly created motor/generator set, 0 on failure.
        :rtype: int
        :return: The IscMGSet object for the newly created motor/generator set.
        :rtype: IscMGSet
        """
        pass

    @overload
    def CreateVoltageRegulator(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created voltage regulator.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The UID for the newly created voltage regulator, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateVoltageRegulator(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscVoltageRegulator object for the newly created voltage regulator.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The IscVoltageRegulator object for the newly created voltage regulator.
        :rtype: IscVoltageRegulator
        """
        pass

    def CreateVoltageRegulator(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscVoltageRegulator object for the newly created voltage regulator.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The voltage regulator name string if required.
        :type strName: str
        :return: The UID for the newly created voltage regulator, 0 on failure.
        :rtype: int
        :return: The IscVoltageRegulator object for the newly created voltage regulator.
        :rtype: IscVoltageRegulator
        """
        pass

    @overload
    def CreateUnbalancedLoad(self, nAtBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created unbalanced load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param strName: The unbalanced load name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced load, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateUnbalancedLoad(self, pAtBusbar, strName: str):
        """
        Returns an IscUnbalancedLoad object for the newly created unbalanced load.

        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The unbalanced load name string if required.
        :type strName: str
        :return: The IscUnbalancedLoad object for the newly created unbalanced load.
        :rtype: IscUnbalancedLoad
        """
        pass

    def CreateUnbalancedLoad(self, pAtBusbar, strName: str):
        """
        Returns the UID or an IscUnbalancedLoad object for the newly created unbalanced load.

        :param nAtBusbarUID: The busbar UID.
        :type nAtBusbarUID: int
        :param pAtBusbar: The busbar.
        :type pAtBusbar: IscBusbar
        :param strName: The unbalanced load name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced load, 0 on failure.
        :rtype: int
        :return: The IscUnbalancedLoad object for the newly created unbalanced load.
        :rtype: IscUnbalancedLoad
        """
        pass

    @overload
    def CreateUnbalancedLine(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created unbalanced line.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The unbalanced line name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced line, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateUnbalancedLine(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscUnbalancedLine object for the newly created unbalanced line.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced line name string if required.
        :type strName: str
        :return: The IscUnbalancedLine object for the newly created unbalanced line.
        :rtype: IscUnbalancedLine
        """
        pass

    def CreateUnbalancedLine(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscUnbalancedLine object for the newly created unbalanced line.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced line name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced line, 0 on failure.
        :rtype: int
        :return: The IscUnbalancedLine object for the newly created unbalanced line.
        :rtype: IscUnbalancedLine
        """
        pass

    @overload
    def CreateUnbalancedTransformer(self, nFromBusbarUID: int, nToBusbarUID: int, strName: str) -> int:
        """
        Returns the UID for the newly created unbalanced transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param strName: The unbalanced transformer name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced transformer, 0 on failure.
        :rtype: int
        """
        pass

    @overload
    def CreateUnbalancedTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns an IscUnbalancedTransformer object for the newly created unbalanced transformer.

        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced transformer name string if required.
        :type strName: str
        :return: The IscUnbalancedTransformer object for the newly created unbalanced transformer.
        :rtype: IscUnbalancedTransformer
        """
        pass

    def CreateUnbalancedTransformer(self, pFromBusbar, pToBusbar, strName: str):
        """
        Returns the UID or an IscUnbalancedTransformer object for the newly created unbalanced transformer.

        :param nFromBusbarUID: The "From" busbar UID.
        :type nFromBusbarUID: int
        :param nToBusbarUID: The "To" busbar UID.
        :type nToBusbarUID: int
        :param pFromBusbar: The "From" busbar.
        :type pFromBusbar: IscBusbar
        :param pToBusbar: The "To" busbar.
        :type pToBusbar: IscBusbar
        :param strName: The unbalanced transformer name string if required.
        :type strName: str
        :return: The UID for the newly created unbalanced transformer, 0 on failure.
        :rtype: int
        :return: The IscUnbalancedTransformer object for the newly created unbalanced transformer.
        :rtype: IscUnbalancedTransformer
        """
        pass

    def CreateGroup(self, strName: str, nGroupType: int) -> int:
        """
        Create a new empty group of components and returns the group UID.
        Group types:

            - 0 = No group type
            - 1 = Area type group (contains all busbars in an area)
            - 2 = Mixed item group
            - 3 = Load scaling group
            - 4 = Load transfer group
            - 5 = Protection device group

        :param strName: The group name.
        :type strName: str
        :param nGroupType: The group type.
        :type nGroupType: int
        :return: The group UID, 0 on failure.
        :rtype: int
        """
        pass

    def CreateGroupNoGraphics(self, strName: str, nGroupType: int):
        """
        Create a new empty group of components and returns the group object.
        Group types:

            - 0 = No group type
            - 1 = Area type group (contains all busbars in an area)
            - 2 = Mixed item group
            - 3 = Load scaling group
            - 4 = Load transfer group
            - 5 = Protection device group

        :param strName: The group name.
        :type strName: str
        :param nGroupType: The group type.
        :type nGroupType: int
        :return: The IscGroup object.
        :rtype: IscGroup
        """
        pass

    def CreatePlugin(self, nCompUID: int, sPluginName: str, sName: str) -> int:
        """
        Returns the UID for the newly created plugin.
        A different plugin UID is required for each component with a plugin,
        therefore this function should be used every time a plugin is assigned to a component,
        even if the same type of plugin is being assigned.

        :param nCompUID: The UID of the component to which the plugin is to be assigned to.
        :type nCompUID: int
        :param sPluginName: The name of the plugin itself, for example ‘Constant Current Load’.
        :type sPluginName: str
        :param sName: The user defined plugin name or empty string.
        :type sName: str
        :return: The plugin UID, 0 on failure.
        :rtype: int
        """
        pass

    def DeleteBusbar(self, pBusbar) -> bool:
        """
        Deletes a busbar by passing the IscBusbar object for deletion.

        :param pBusbar: The IscBusbar object for deletion.
        :type pBusbar: IscBusbar
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteBranch(self, pBranch) -> bool:
        """
        Deletes a branch by passing the IscBranch object for deletion and all the circuit breakers attached to it.

        :param pBranch: The IscBranch object for deletion.
        :type pBranch: IscBranch
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteTransformer(self, pTransformer) -> bool:
        """
        Deletes a transformer by passing the IscTransformer object for deletion.

        :param pTransformer: The IscTransformer object for deletion.
        :type pTransformer: IscTransformer
        :return: True if successful.
        :rtype: bool
        """
        pass

    def Delete3WTransformer(self, p3WTransformer) -> bool:
        """
        Deletes a 3-winding transformer by passing the Isc3WTransformer object for deletion.

        :param p3WTransformer: The Isc3WTransformer object for deletion.
        :type p3WTransformer: Isc3WTransformer
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteLoad(self, pLoad) -> bool:
        """
        Deletes a load by passing the IscLoad object for deletion.

        :param pLoad: The IscLoad object for deletion.
        :type pLoad: IscLoad
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteSynMachine(self, pSynMachine) -> bool:
        """
        Deletes a synchronous machine by passing the IscSynMachine object for deletion.

        :param pSynMachine: The IscSynMachine object for deletion.
        :type pSynMachine: IscSynMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteIndMachine(self, pIndMachine) -> bool:
        """
        Deletes an induction machine by passing the IscIndMachine object for deletion.

        :param pIndMachine: The IscIndMachine object for deletion.
        :type pIndMachine: IscIndMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGridInfeed(self, pGridInfeed) -> bool:
        """
        Deletes a grid infeed by passing the IscSynMachine object for deletion.

        :param pGridInfeed: The IscSynMachine object for deletion.
        :type pGridInfeed: IscSynMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteFilter(self, pFilter) -> bool:
        """
        Deletes a filter by passing the IscFilter object for deletion.

        :param pFilter: The IscFilter object for deletion.
        :type pFilter: IscFilter
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteMechSwCapacitor(self, pMechSwCapacitor) -> bool:
        """
        Deletes a mechanical switched capacitor by passing the IscMechSwCapacitor object for deletion.

        :param pMechSwCapacitor: The IscMechSwCapacitor object for deletion.
        :type pMechSwCapacitor: IscMechSwCapacitor
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteStaticVC(self, pStaticVC) -> bool:
        """
        Deletes a synchronous machine by passing the IscStaticVC object for deletion.

        :param pStaticVC: The IscStaticVC object for deletion.
        :type pStaticVC: IscStaticVC
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUMachine(self, pUMachine) -> bool:
        """
        Deletes an universal machine by passing the IscUMachine object for deletion.

        :param pUMachine: The IscUMachine object for deletion.
        :type pUMachine: IscUMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteHarmonic(self, pHarmonic) -> bool:
        """
        Deletes a harmonic source by passing the IscHarmonic object for deletion.

        :param pHarmonic: The IscHarmonic object for deletion.
        :type pHarmonic: IscHarmonic
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteCircuitBreaker(self, pCircuitBreaker) -> bool:
        """
        Deletes a circuit breaker by passing the IscCircuitBreaker object for deletion.

        :param pCircuitBreaker: The IscCircuitBreaker object for deletion.
        :type pCircuitBreaker: IscCircuitBreaker
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteBattery(self, pBattery) -> bool:
        """
        Deletes a battery by passing the IscBattery object for deletion.

        :param pBattery: The IscBattery object for deletion.
        :type pBattery: IscBattery
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteDCMachine(self, pDCMachine) -> bool:
        """
        Deletes a DC machine by passing the IscDCMachine object for deletion.

        :param pDCMachine: The IscDCMachine object for deletion.
        :type pDCMachine: IscDCMachine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteConverter(self, pConverter) -> bool:
        """
        Deletes a converter by passing the IscConverter object for deletion.

        :param pConverter: The IscConverter object for deletion.
        :type pConverter: IscConverter
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteMGSet(self, pMGSet) -> bool:
        """
        Deletes a motor/generator set by passing the IscMGSet object for deletion.

        :param pMGSet: The IscMGSet object for deletion.
        :type pMGSet: IscMGSet
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteVoltageRegulator(self, pVoltageRegulator) -> bool:
        """
        Deletes a voltage regulator by passing the IscVoltageRegulator object for deletion.

        :param pVoltageRegulator: The IscVoltageRegulator object for deletion.
        :type pVoltageRegulator: IscVoltageRegulator
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteAnnotation(self, pAnnotation) -> bool:
        """
        Deletes an annotation by passing the IscAnnotation object for deletion.

        :param pAnnotation: The IscAnnotation object for deletion.
        :type pAnnotation: IscAnnotation
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUnbalancedLoad(self, pUnbalancedLoad) -> bool:
        """
        Deletes an unbalanced load by passing the IscUnbalancedLoad object for deletion.

        :param pUnbalancedLoad: The IscUnbalancedLoad object for deletion.
        :type pUnbalancedLoad: IscUnbalancedLoad
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUnbalancedLine(self, pUnbalancedLine) -> bool:
        """
        Deletes an unbalanced line by passing the IscUnbalancedLine object for deletion.

        :param pUnbalancedLine: The IscUnbalancedLine object for deletion.
        :type pUnbalancedLine: IscUnbalancedLine
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUnbalancedTransformer(self, pUnbalancedTransformer) -> bool:
        """
        Deletes an unbalanced transformer by passing the IscUnbalancedTransformer object for deletion.

        :param pUnbalancedTransformer: The IscUnbalancedTransformer object for deletion.
        :type pUnbalancedTransformer: IscUnbalancedTransformer
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGroup(self, pGroup) -> bool:
        """
        Deletes a group by passing the IscGroup object for deletion.

        :param pGroup: The IscGroup object for deletion.
        :type pGroup: IscGroup
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeletePlugin(self, pPlugin) -> bool:
        """
        Deletes a plugin by passing the IscPlugin object for deletion.

        :param pPlugin: The IscPlugin object for deletion.
        :type pPlugin: IscPlugin
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteBusBarSlack(self, strBusbar: str) -> bool:
        """
        Deletes a slack busbar from the network busbar slack list.
        **It does not delete the busbar in the same way as DeleteBusbar(pBusbar)**,
        instead it uses the busbar name for deletion.

        :param strBusbar: The slack busbar name.
        :type strBusbar: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetRatingIndex(self, strName: str) -> int:
        """
        Returns an integer representing the rating set for a specified name.

        :param strName: The specified name.
        :type strName: str
        :return: The rating set index, or -1 if no rating set with that name exists in the network.
        :rtype: int
        """
        pass

    def GetBranchRatingName(self, nIndex: int) -> str:
        """
        Returns the name representing the rating set identified by an index.

        :param nIndex: The specified index.
        :type nIndex: int
        :return: The rating set name, or empty set if no rating set with that index exists in the network.
        :rtype: str
        """
        pass

    def SetRatingName(self, nIndex: int, strName: str) -> None:
        """
        Sets the name of the rating set identified by an index to specified name.
        If the rating set name does not exist it will be created by the function.

        :param nIndex: The specified index.
        :type nIndex: int
        :param strName: The specified name.
        :type strName: str
        """
        pass

    def SetLimitsForOverloadChecks(self, dMaxVoltsPU: float, dMinVoltsPU: float, nRatingIndex: int, strDiagram: str)\
            -> None:
        """
        Sets the limits for overload checking on diagrams.

        :param dMaxVoltsPU: The maximum voltage in per unit.
        :type dMaxVoltsPU: float
        :param dMinVoltsPU: The minimum voltage in per unit.
        :type dMinVoltsPU: float
        :param nRatingIndex: The index of the rating set to be used for the thermal overload checks.
        :type nRatingIndex: int
        :param strDiagram: The name of the diagram that these limits will be applied to.
        :type strDiagram: str
        """
        pass

    def CreateLoadProfilePQActual(self, strName: str) -> int:
        """
        Returns the load profile UID representing a load profile which uses actual MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The load profile UID, 0 if a load profile cannot be created.
        :rtype: int
        """
        pass

    def CreateLoadProfilePQActualNoGraphics(self, strName: str):
        """
        Returns an IscLoadProfilePQActual object representing a load profile
        which uses actual MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQActual object.
        :rtype: IscLoadProfilePQActual
        """
        pass

    def CreateGeneratorProfilePQActual(self, strName: str) -> int:
        """
        Returns the generator profile UID representing a generator profile which uses actual MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The generator profile UID, 0 if a generator profile cannot be created.
        :rtype: int
        """
        pass

    def CreateGeneratorProfilePQActualNoGraphics(self, strName: str):
        """
        Returns an IscGeneratorProfilePQActual object representing a generator profile
        which uses actual MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQActual object.
        :rtype: IscGeneratorProfilePQActual
        """
        pass

    def CreateUMachineProfilePQActual(self, strName: str) -> int:
        """
        Returns the universal machine profile UID representing a universal machine profile which uses actual
        MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The universal machine profile UID, 0 if a universal machine profile cannot be created.
        :rtype: int
        """
        pass

    def CreateUMachineProfilePQActualNoGraphics(self, strName: str):
        """
        Returns an IscUMachineProfilePQActual object representing a universal machine profile
        which uses actual MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscUMachineProfilePQActual object.
        :rtype: IscUMachineProfilePQActual
        """
        pass

    def CreateLoadProfilePQScale(self, strName: str) -> int:
        """
        Returns the load profile UID representing a load which scales the existing MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The load profile UID, 0 if a generator profile cannot be created.
        :rtype: int
        """
        pass

    def CreateLoadProfilePQScaleNoGraphics(self, strName: str):
        """
        Returns an IscLoadProfilePQScale object representing a load profile
        which scales the existing MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQScale object.
        :rtype: IscLoadProfilePQScale
        """
        pass

    def CreateGeneratorProfilePQScale(self, strName: str) -> int:
        """
        Returns the generator profile UID representing a generator which scales the existing MW and MVAr values.
        No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: The generator profile UID, 0 if a generator profile cannot be created.
        :rtype: int
        """
        pass

    def CreateGeneratorProfilePQScaleNoGraphics(self, strName: str):
        """
        Returns an IscGeneratorProfilePQScale object representing a generator profile
        which scales the existing MW and MVAr values. No checking is made on duplicate profile names.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQScale object.
        :rtype: IscGeneratorProfilePQScale
        """
        pass

    def GetLoadProfilePQActuals(self):
        """
        Returns a dictionary of all IscLoadProfilePQActual objects in the network for actual load profiles.
        The keys are the profile UIDs and the values are the IscLoadProfilePQActual objects.

        :return: A dictionary of all IscLoadProfilePQActual objects in the network for actual load profiles.
        :rtype: dict(int,IscIscLoadProfilePQActual)
        """
        pass

    def GetGeneratorProfilePQActuals(self):
        """
        Returns a dictionary of all IscGeneratorProfilePQActual objects in the network for actual generator profiles.
        The keys are the profile UIDs and the values are the IscGeneratorProfilePQActual objects.

        :return: A dictionary of all IscGeneratorProfilePQActual objects in the network for actual generator profiles.
        :rtype: dict(int,IscGeneratorProfilePQActual)
        """
        pass

    def GetUMachineProfilePQActuals(self):
        """
        Returns a dictionary of all IscUMachineProfilePQActual objects in the network for actual universal machine
        profiles.
        The keys are the profile UIDs and the values are the IscUMachineProfilePQActual objects.

        :return: A dictionary of all IscUMachineProfilePQActual objects in the network for actual universal machine
        profiles.
        :rtype: dict(int,IscUMachineProfilePQActual)
        """
        pass

    def GetLoadProfilePQScales(self):
        """
        Returns a dictionary of all IscLoadProfilePQScale objects in the network for scaled load profiles.
        The keys are the profile UIDs and the values are the IscLoadProfilePQScale objects.

        :return: A dictionary of all IscLoadProfilePQScale objects in the network for scaled load profiles.
        :rtype: dict(int,IscLoadProfilePQScale)
        """
        pass

    def GetGeneratorProfilePQScales(self):
        """
        Returns a dictionary of all IscGeneratorProfilePQScale objects in the network for scaled generator profiles.
        The keys are the profile UIDs and the values are the IscGeneratorProfilePQScale objects.

        :return: A dictionary of all IscGeneratorProfilePQScale objects in the network for scaled generator profiles.
        :rtype: dict(int,IscGeneratorProfilePQScale)
        """
        pass

    def GetLoadProfilePQActual(self, strName: str):
        """
        Returns an IscLoadProfilePQActual object for the actual MW/MVAr load profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQActual object for the actual MW/MVAr load profile.
        Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQActual
        """
        pass

    def GetGeneratorProfilePQActual(self, strName: str):
        """
        Returns an IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQActual object for the actual MW/MVAr generator profile.
        Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQActual
        """
        pass

    def GetUMachineProfilePQActual(self, strName: str):
        """
        Returns an IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile with
        a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscUMachineProfilePQActual object for the actual MW/MVAr universal machine profile.
        Returns None if a profile cannot be found.
        :rtype: IscUMachineProfilePQActual
        """
        pass

    def GetLoadProfilePQScale(self, strName: str):
        """
        Returns an IscLoadProfilePQScale object for the scaled MW/MVAr load profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscLoadProfilePQScale object for the scaled MW/MVAr load profile.
        Returns None if a profile cannot be found.
        :rtype: IscLoadProfilePQScale
        """
        pass

    def GetGeneratorProfilePQScale(self, strName: str):
        """
        Returns an IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile with a specified name.

        :param strName: The profile name.
        :type strName: str
        :return: IscGeneratorProfilePQScale object for the scaled MW/MVAr generator profile.
        Returns None if a profile cannot be found.
        :rtype: IscGeneratorProfilePQScale
        """
        pass

    def DeleteLoadProfilePQActual(self, pProfile) -> bool:
        """
        Deletes the actual load profile from the network by passing an IscLoadProfilePQActual object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscLoadProfilePQActual
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteLoadProfilePQScale(self, pProfile) -> bool:
        """
        Deletes the scaled load profile from the network by passing an IscLoadProfilePQScale object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscLoadProfilePQScale
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGeneratorProfilePQActual(self, pProfile) -> bool:
        """
        Deletes the actual generator profile from the network by passing an IscGeneratorProfilePQActual object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscGeneratorProfilePQActual
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteGeneratorProfilePQScale(self, pProfile) -> bool:
        """
        Deletes the scaled generator profile from the network by passing an IscGeneratorProfilePQScale object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscGeneratorProfilePQScale
        :return: True if successful.
        :rtype: bool
        """
        pass

    def DeleteUMachineProfilePQActual(self, pProfile) -> bool:
        """
        Deletes the actual universal machine profile from the network by passing an IscUMachineProfilePQActual object.

        :param pProfile: The profile to be deleted.
        :type pProfile: IscUMachineProfilePQActual
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetCategoryNames(self, dicCategories: Dict[int, str]) -> None:
        """
        Sets up the profile categories for the profile instance.
        The dictionary should comprise a set of integer keys and string values.
        The string values are used as the individual category labels whilst the integer keys are only used internally.
        It is recommended that the keys are numbered sequentially starting from 0.

        For example, passing the following dictionary to an IscLoadProfilePQActual instance would add 3 categories to
        the profile with the strings as the categories:

        categories = {0: "00:00", 1: "00:30", 2: "01:00"}

        :param dicCategories: The profile categories for the profile instance.
        :type dicCategories: dict(int,str)
        """
        pass

    def SetPMW(self, dictCategoryToMW: Dict[int, float]) -> None:
        """
        Assigns MW values to the profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MW data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For scaling profiles the values are the per unit scaling values.
        For example, passing the following dictionary to an IscLoadProfilePQActual instance would set the MW data:

        dictCategoryToMW = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMW: MW values to the profile categories.
        :type dictCategoryToMW: dict(int,float)
        """
        pass

    def SetQMVAr(self, dictCategoryToMVAr: Dict[int, float]) -> None:
        """
        Assigns MVAr values to the profile categories.
        The dictionary should comprise a set of integer keys and float values.
        The float values are the MVAr data values whilst the integer keys should be identical to those
        being used when defining the categories.
        For scaling profiles the values are the per unit scaling values.
        For example, passing the following dictionary to an IscLoadProfilePQActual instance would set the MVAr data:

        dictCategoryToMVAr = {0: 1.23, 1: 3.73, 2: 5.67}

        :param dictCategoryToMVAr: MVAr values to the profile categories.
        :type dictCategoryToMVAr: dict(int,float)
        """
        pass

    def RunProfile(self) -> int:
        """
        Runs the profile study. Returns the number of profile categories which have been run.

        :return: The number of profile categories which have been run.
        :rtype: int
        """
        pass

    def GetAllDiagrams(self):
        """
        Returns a list of IscDiagram objects for the network.

        :return: List of IscDiagram objects for the network.
        :rtype: list(IscDiagram)
        """
        pass

    def GetAllDiagramsNames(self) -> List[str]:
        """
        Returns a list of the names of the diagrams for the network.

        :return: The names of the diagrams for the network.
        :rtype: list(str)
        """
        pass

    def GetAnalysisLF(self):
        """
        Returns an IscAnlaysisLF object which can be used to get and set the load flow analysis parameters.

        :return: IscAnlaysisLF object.
        :rtype: IscAnlaysisLF
        """
        pass

    def SetResultsForTheseUIDs(self, nUIDs: int) -> None:
        """
        This function restricts the number of results that are returned from the load flow calculation engine to Python
        in order to reduce the execution time.
        Call this function before DoLoadFlow() or DoSimpleLoadFlow().

        :param nUIDs: The component UIDs.
        :type nUIDs: int
        """
        pass

    def DoLoadFlow(self, bNoEngineLoad: bool, bDontUpdateData: bool) -> bool:
        """
        Performs a load flow calculation.

        :param bNoEngineLoad: If False (default), loads the engine from the Ipsa model before doing a load flow calculation. If True, skips the load from the Ipsa model and uses whatever network is currently loaded in the engine.
        :type bNoEngineLoad: bool
        :param bDontUpdateData: If False (default), allows the load flow results being written back to the network model data (e.g. Busbar voltages and angles). If True, skips this stage, so the network model remains the same as it was loaded. **Note that calling the function with no arguments is allowed and works as if it has been called with bNoEngineLoad and bDontUpdateData set to False.**
        :type bDontUpdateData: bool
        :return: True if the load flow converges, False on a non-convergence.
        :rtype: bool
        """
        pass

    def DoSimpleLoadFlow(self):
        """
        Performs a load flow calculation without prompting the user to confirm analysis options.
        Identical to the DoLoadFlow(False, False) call with no user interaction.

        :return: True if the load flow converges, False on a non-convergence.
        :rtype: bool
        """
        pass

    def SetBranchStatus(self, nUID: int, nStatus: int) -> None:
        """
        Changes the status of the branch UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the branch status
        does not need to be stored with the network.

        :param nUID: The branch UID.
        :type nUID: int
        :param nStatus: The status.
        :type nStatus: int
        """
        pass

    def SetLoadStatus(self, nUID: int, nStatus: int) -> None:
        """
        Changes the status of the load UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the load status
        does not need to be stored with the network.

        :param nUID: The load UID.
        :type nUID: int
        :param nStatus: The status.
        :type nStatus: int
        """
        pass

    def SetLoadPower(self, nUID: int, dMW: float, dMVAr: float) -> None:
        """
        Changes the power of the load UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the load power
        does not need to be stored with the network.

        :param nUID: The load UID.
        :type nUID: int
        :param dMW: The MW power.
        :type dMW: float
        :param dMVAr: The MVAr power.
        :type dMVAr: float
        """
        pass

    def SetGeneratorStatus(self, nUID: int, nStatus: int) -> None:
        """
        Changes the status of the generator UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the generator status
        does not need to be stored with the network.

        :param nUID: The generator UID.
        :type nUID: int
        :param nStatus: The status.
        :type nStatus: int
        """
        pass

    def SetGeneratorPower(self, nUID: int, dMW: float, dMVAr: float) -> None:
        """
        Changes the power of the generator UID in the calculation engine.
        This is a convenience function which can be used when performance is important and the generator power
        does not need to be stored with the network.

        :param nUID: The generator UID.
        :type nUID: int
        :param dMW: The MW power.
        :type dMW: float
        :param dMVAr: The MVAr power.
        :type dMVAr: float
        """
        pass

    def GetLoadFlowMessage(self) -> str:
        """
        Returns the last load flow engine message.

        :return: The last load flow engine message.
        :rtype: str
        """
        pass

    def SetEngineMessageSuppression(self, nLevel: int) -> None:
        """
        Sets the verbosity of the load flow messages that are generated in the Ipsa progress window.
        This can provide a speed improvement for complex scripts

            - 0 = Displays all messages
            - 1 = Shows only error messages
            - 2 = Shows no engine error messages

        :param nLevel: The verbosity of the load flow messages.
        :type nLevel: int
        """
        pass

    def GetLFSummaryResults(self) -> None:
        """
        Call this function to obtain the load flow summary results.
        """
        pass

    def GetHighestBusbarVoltagePU(self) -> float:
        """
        Returns the highest busbar voltage in per unit.

        :return: The highest busbar voltage in per unit.
        :rtype: float
        """
        pass

    def GetLowestBusbarVoltagePU(self) -> float:
        """
        Returns the lowest busbar voltage in per unit. GetLFSummaryResults()must be called first.

        :return: The lowest busbar voltage in per unit.
        :rtype: float
        """
        pass

    def GetTotalGenerationOutputMW(self) -> float:
        """
        Returns the total network generation, excluding slack generators, in MW.
        GetLFSummaryResults() must be called first.

        :return: The total network generation, excluding slack generators, in MW.
        :rtype: float
        """
        pass

    def GetTotalGenerationOutputMVAr(self) -> float:
        """
        Returns the total network generation, excluding slack generators, in MVAr.
        GetLFSummaryResults() must be called first.

        :return: The total network generation, excluding slack generators, in MVAr.
        :rtype: float
        """
        pass

    def GetTotalLoadInputMW(self) -> float:
        """
        Returns the total network load in MW. GetLFSummaryResults() must be called first.

        :return: The total network load in MW.
        :rtype: float
        """
        pass

    def GetTotalLoadInputMVAr(self) -> float:
        """
        Returns the total network load in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network load in MVAr.
        :rtype: float
        """
        pass

    def GetTotalInductionInputMW(self) -> float:
        """
        Returns the total network induction motor load in MW. GetLFSummaryResults() must be called first.

        :return: The total network induction motor load in MW.
        :rtype: float
        """
        pass

    def GetTotalInductionInputMVAr(self) -> float:
        """
        Returns the total network induction motor load in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network induction motor load in MVAr.
        :rtype: float
        """
        pass

    def GetSlackOutputMW(self) -> float:
        """
        Returns the total network slack generation in MW. GetLFSummaryResults() must be called first.

        :return: The total network slack generation in MW.
        :rtype: float
        """
        pass

    def GetSlackOutputMVAr(self) -> float:
        """
        Returns the total network slack generation in MVAr. GetLFSummaryResults() must be called first.

        :return: The total network slack generation in MVAr.
        :rtype: float
        """
        pass

    def GetNumberOutsideLimits(self) -> int:
        """
        Returns the number of busbars outside voltage limits plus the number of overloaded branches and transformers.

        :return: The number of busbars outside voltage limits plus the number of overloaded branches and transformers.
        :rtype: int
        """
        pass

    def GetOutsideLimitText(self) -> str:
        """
        Returns a string detailing the busbar, branch or transformer with the most excessive overload/overvoltage
        in percentage terms. GetNumberOutsideLimits() must be called first.
        The name returned is the Python name of the component, e.g. Busbar1.Busbar2.Transformer

        :return: A string detailing the busbar, branch or transformer with the most excessive overload/overvoltage
        in percentage terms.
        :rtype: str
        """
        pass

    def AreLFLimitsIdentical(self) -> bool:
        """
        Returns True if the LF limits are identical.

        :return: True if the LF limits are identical.
        :rtype: bool
        """
        pass

    def SaveLFState(self) -> int:
        """
        Saves the current LF state and returns a state handle to restore it with.

        :return: State handle to restore the current LF state.
        :rtype: int
        """
        pass

    def RestoreLFState(self, nStateIndex: int) -> bool:
        """
        Restore the LF state. This function can fail if the number of items in a network is different from
        when the state was saved, which can happen in a subtle way if zero impedance branches are switched in or out.

        :param nStateIndex: The state index.
        :type nStateIndex: int
        :return: True if the restore operation succeeded.
        :rtype: bool
        """
        pass

    def DeleteAllLFStates(self) -> None:
        """
        Delete all LF saved states.
        """
        pass


    def GetBusbarsOutsideLimits(self) -> Dict[int, bool]:
        """
        Returns a dictionary of busbar UIDs that are outside voltage limits for the previous load flow study.

        :return: A dictionary of busbar UIDs that are outside voltage limits for the previous load flow study.
        :rtype: dict(int,bool)
        """
        pass

    def GetBranchesOutsideLimits(self) -> Dict[int, bool]:
        """
        Returns a dictionary of branch UIDs that are above their ratings for the previous load flow study.

        :return: A dictionary of branch UIDs that are above their ratings for the previous load flow study.
        :rtype: dict(int,bool)
        """
        pass

    def GetTransformersOutsideLimits(self) -> Dict[int, bool]:
        """
        Returns a dictionary of transformer UIDs that are above their ratings for the previous load flow study.

        :return: A dictionary of transformer UIDs that are above their ratings for the previous load flow study.
        :rtype: dict(int,bool)
        """
        pass

    def GetAnalysisFL(self):
        """
        Returns an IscAnlaysisFL object which can be used to get and set the fault level analysis parameters.

        :return: IscAnlaysisFL object.
        :rtype: IscAnlaysisFL
        """
        pass

    def DoFaultLevel(self) -> bool:
        """
        Performs a fault level calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def DoIECFaultLevel(self) -> bool:
        """
        Performs an IEC 60909 fault calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetAnalysisHM(self):
        """
        Returns an IscAnlaysisHM object which can be used to get and set the load flow analysis parameters.

        :return: IscAnlaysisHM object.
        :rtype: IscAnlaysisHM
        """
        pass

    def DoHarmPenetration(self) -> bool:
        """
        Performs a harmonic penetration calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def DoHarmSensitivity(self) -> bool:
        """
        Performs a harmonic voltage sensitivity calculation.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def RunContingency(self, nUID: int, bUseProfiles: bool) -> None:
        """
        Performs the contingency study identified by the integer UID.

        :param nUID: The contingency study UID.
        :type nUID: int
        :param bUseProfiles: If False then the contingency study is performed using the standard load and generator data.
        If True then the contingency study is performed using load and generator profiles assigned in the network.
        In this instance the switching operation is performed first followed by a load flow calculation for
        all of the profile categories.
        :type bUseProfiles: bool
        """
        pass

    def CreateContingency(self, nDepth: int, bExtendToBreakers: bool) -> None:
        """
        Creates a new contingency study and returns the UID of the study created.
        The depth of the study is configured as follows:
            - 1 = N - 1
            - 2 = N - 2
            - 3 = N - 3
            - 4 = N - 1 - 1

        :param nDepth: The depth of the study.
        :type nDepth: int
        :param bExtendToBreakers: If False then individual branches and transfers are switched out during the study.
        If True then the nearest circuit breakers are switched out allowing multiple components to be switched
        for each study.
        :type bExtendToBreakers: bool
        """
        pass

    def GetStudies(self, nReportType: int) -> List[str]:
        """
        Returns a list of strings containing the individual automation or contingency study titles.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :return: The individual automation or contingency study titles.
        :rtype: list(str)
        """
        pass

    def GetStudyRowTitles(self, nReportType: int) -> str:
        """
        Returns a string in html format for the table header row associated with the automation or contingency results.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :return: String in html format.
        :rtype: str
        """
        pass

    def GetStudyRowOutput(self, nReportType: int, strStudyTitle: str) -> str:
        """
        Returns a string in html format for the table rows associated with the specified automation or contingency
        study.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :param strStudyTitle: The specified automation or contingency study.
        :type strStudyTitle: str
        :return: String in html format.
        :rtype: str
        """
        pass

    def GetStudyIDs(self, nReportType: int) -> List[int]:
        """
        Returns a list containing the individual automation or contingency study IDs.

        Automation studies:
            - 100 = All studies in the order run
            - 101 = All solved studies in the order run
            - 102 = All solved studies listed by severity of overload
            - 103 = All solved studies listed by the number of items exceeding limits
            - 104 = All studies that failed to solve

        Contingency studies:
            - 120 = All studies in the order run
            - 121 = All solved studies in the order run
            - 122 = All solved studies listed by severity of overload
            - 123 = All solved studies listed by the number of items exceeding limits
            - 124 = All studies that failed to solve

        :param nReportType: The index denoting an automation or a contingency study.
        :type nReportType: int
        :return: The individual automation or contingency study IDs.
        :rtype: list(int)
        """
        pass

    def GetContingencyStudyItemResults(self, nStudyID: int) -> List[int]:
        """
        Returns a list of integers containing the study result IDs for the contingency study ID.
        Each switching operation in a contingency study may produce a number of constraints.
        Each constraint can be examined using the result IDs returned by this function.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The study result IDs for the contingency study ID.
        :rtype: list(int)
        """
        pass

    def GetStudyProfileIndex(self, nStudyID: int) -> int:
        """
        Returns the profile category index associated with the contingency or automation study.
        This is used to identify which profile category is associated with the study ID.

        :param nStudyID: The study ID.
        :type nStudyID: int
        :return: The profile category index associated with the contingency or automation study.
        :rtype: int
        """
        pass

    def GetStudyItemsSwitchedOutUIDs(self, nStudyID: int) -> List[int]:
        """
        Returns a list of integers containing the component UIDs for switched out components in contingency study ID.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The component UIDs for switched out components in contingency study ID.
        :rtype: list(int)
        """
        pass

    def GetContingencyStudyResultMagnitude(self, nStudyID: int, nResultID: int) -> float:
        """
        Returns the result magnitude for the result ID in contingency study ID.
        The nResultID is obtained from the GetContingencyStudyItemResults function.
        For busbars the return value is the per unit busbar voltage.
        For branches and transformers the return value is the largest power flow in MVA.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :param nResultID: The result ID.
        :type nResultID: int
        :return: The result magnitude for the result ID in contingency study ID.
        :rtype: float
        """
        pass

    def GetContingencyStudyDynamicallyOverloadedUIDs(self, nStudyID: int) -> List[int]:
        """
        Returns a list of integers which represent lines which are overloaded due to the action
        of a dynamic rating plugin.
        Dynamic rating plugins can be used to model the thermal response of OHLs,
        transformers and cables and provide ratings which are based on these models.
        The normal Ipsa rating of a component is overridden if it has a dynamic rating plugin applied.
        In this case this function returns the UIDs of all such overloaded components in contingency study ID.

        :param nStudyID: The contingency study ID.
        :type nStudyID: int
        :return: The lines which are overloaded due to the action of a dynamic rating plugin.
        :rtype: list(int)
        """
        pass

    def GetContingencyBranchRatingIndex(self) -> int:
        """
        Returns the Ipsa rating index of the rating set used during the contingency study.

        :return: The Ipsa rating index.
        :rtype: int
        """
        pass

    def RunReliability(self) -> bool:
        """
        Performs the reliability study on the current network.

        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetReliabilityCI(self) -> float:
        """
        Returns the customer interruptions (CI) for the full network.

        :return: The customer interruptions (CI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityCML(self) -> float:
        """
        Returns the customer minutes lost (CMLs) for the full network.

        :return: The customer minutes lost (CMLs) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilitySAIFI(self) -> float:
        """
        Returns the system average interruption frequency index (SAIFI) for the full network.

        :return: The system average interruption frequency index (SAIFI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASIFI(self) -> float:
        """
        Returns the average service interruption frequency index (ASIFI) for the full network.

        :return: The average service interruption frequency index (ASIFI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilitySAIDI(self) -> float:
        """
        Returns the system average interruption duration index (SAIDI) for the full network.

        :return: The system average interruption duration index (SAIDI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityCAIDI(self) -> float:
        """
        Returns the customer average interruption duration index (CAIDI) for the full network.

        :return: The customer average interruption duration index (CAIDI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASIDI(self) -> float:
        """
        Returns the average system interruption duration index (ASIDI) for the full network.

        :return: The average system interruption duration index (ASIDI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASAI(self) -> float:
        """
        Returns the average service availability index (ASAI) for the full network.

        :return: The average service availability index (ASAI) for the full network.
        :rtype: float
        """
        pass

    def GetReliabilityASUI(self) -> float:
        """
        Returns the average service unavailability index (ASUI) for the full network.

        :return: The average service unavailability index (ASUI) for the full network.
        :rtype: float
        """
        pass

    def GetBusbarsWithArcFlashResults(self) -> List[int]:
        """
        Returns a list of busbar UIDs which have arc flash results.
        This is then used to get arc flash results for individual busbars.

        :return: Busbar UIDs which have arc flash results.
        :rtype: list(int)
        """
        pass

    def GetArcFlashReportText(self, nUID: int) -> str:
        """
        Returns a string containing the arc flash result for the busbar identified by the UID.

        :param nUID: The busbar ID.
        :type nUID: int
        :return: The average service unavailability index (ASUI) for the full network.
        :rtype: str
        """
        pass
