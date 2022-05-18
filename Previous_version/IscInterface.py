from typing import List, overload


class IscInterface:
    """
    The main interface class used to access all other Ipsa objects and functions.
    """
    def ReadFile(self, strName: str):
        """
        Opens an Ipsa i2f file strName and returns an IscNetwork instance for that file.

        :param strName: The Ipsa i2f file that is going to be opened.
        :type strName: str
        :return: The IscNetwork instance for the strName file
        :rtype: IscNetwork
        """
        pass

    def ReadIpsa1File(self, strName: str):
        """
        Imports an Ipsa 1 (\*.iif) file strName and returns an IscNetwork instance for that file.

        :param strName: The Ipsa i2f file that is going to be imported.
        :type strName: str
        :return: The IscNetwork instance for the strName file
        :rtype: IscNetwork
        """
        pass

    def GetNetwork(self):
        """
        Returns an IscNetwork instance for the current Ipsa network.

        :return: The IscNetwork instance of the Ipsa network.
        :rtype: IscNetwork
        """
        pass

    def CloseNetwork(self) -> bool:
        """
        Closes the current network. Returns False if the network can’t be closed, e.g. if there is unsaved data.

        :return: Boolean denoting whether the network is closed.
        :rtype: bool
        """
        pass

    def GetDiagram(self, network, strName: str):
        """
        Returns an IscDiagram instance for the diagram with name strName contained in the network
        referred to by iscNetwork.

        :param network: The IscNetwork instance of the Ipsa network.
        :type network: IscNetwork
        :param strName: The name of the diagram.
        :type strName: str
        :return: The diagram of the Ipsa network.
        :rtype: IscDiagram
        """
        pass

    def CreateNewNetwork(
            self,
            dSystemBaseMVA: float,
            dFrequencyHz: float,
            bWithDiagram: bool,
            bIsDiagramSingleLine: bool,
            dGeoSceneScale: float,
            nSceneMeasurementUnit: int
    ) -> bool:
        """
        Creates a new Ipsa network based on the supplied parameters. Returns False if the network can’t be created.

        :param dSystemBaseMVA: The network base MVA.
        :type dSystemBaseMVA: float
        :param dFrequencyHz: The nominal network frequency in hertz.
        :type dFrequencyHz: float
        :param bWithDiagram: Denoting whether the diagram is required.
        :type bWithDiagram: bool
        :param bIsDiagramSingleLine: True if a normal single line diagram type is required,
            False if the diagram is a scaled geographic diagram.
        :type bIsDiagramSingleLine: bool
        :param dGeoSceneScale: The scaling factor used to locate or size network components on geographic diagrams.
        :type dGeoSceneScale: float
        :param nSceneMeasurementUnit: The unit used for the geographic scale.

            * 0 if Millimetres
            * 1 if Centimetres
            * 2 if Metres
            * 3 if Kilometres
            * 4 if Inches
            * 5 if Feet
            * 6 if Yards
            * 7 if Miles
        :type nSceneMeasurementUnit: int
        :return: Boolean denoting whether a network can be created.
        :rtype: bool
        """
        pass

    def MergeFile(self, sMergeName: str) -> bool:
        """
        Merges the Ipsa I2F file sMergeName into the current network.

        :param sMergeName: The name of the file being merged.
        :type sMergeName: str
        :return: Returns True if successful, False on merge failure.
        :rtype: bool
        """
        pass

    def ValidatedMergeFile(self, sMergeName: str) -> bool:
        """
        Performs a consistency check to determine if the Ipsa I2F file sMergeName can be merged into
        the current network. Use the GetFilingErrors() function to get details of the merge errors.

        :param sMergeName: The name of the file being merged.
        :type sMergeName: str
        :return: True if successful, False on merge failure.
        :rtype: bool
        """
        pass

    def GetFilingMessages(self) -> List[str]:
        """
        Returns a list of strings detailing the successful merge operations that occurred as a result of
        the ValidatedMergeFile function.

        :return: List of successful merge operations.
        :rtype: list(str)
        """
        pass

    def GetFilingErrors(self) -> List[str]:
        """
        Returns a list of strings detailing the failed merge operations that occurred as a result of
        the ValidatedMergeFile function.

        :return: List of failed merge operations.
        :rtype: list(str)
        """
        pass

    def WriteArea(self, nAreaUID: int, strName: str) -> bool:
        """
        Saves the area group nAreaUID as a new Ipsa i2f network file with the file name strName.
        The integer nAreaUID can be obtained using the IscGroup functions.
        The file is saved in the current working directory. The file name should include the .i2f extension

        :param nAreaUID: The area group UID.
        :type nAreaUID: int
        :param strName: The name of the output file containing the i2f network.
        :type strName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetAllDiagrams(self, network):
        """
        Returns a tuple of IscDiagram instances for the network referred to by IscNetwork.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :return: The network diagram.
        :rtype: tuple(IscDiagram)
        """
        pass

    def GetAllDiagramsNames(self, network) -> List[str]:
        """
        Returns a list of all the diagram names for the network referred to by IscNetwork.

        :param network: The Ipsa network.
        :type network: IscNetwork
        :return: List of diagram names.
        :rtype: list(str)
        """
        pass

    def PrintPDF(self, diagram, strFileName) -> None:
        """
        Print the IscDiagram instance to a PDF format file with name strFileName.

        :param diagram: The diagram of the Ipsa network.
        :type diagram: IscDiagram
        :param strFileName: The name of the pdf file.
        :type strFileName: str
        """
        pass

    @overload
    def GetLineLength(self, diagram, pComponent) -> float:
        """
        Returns the component length as drawn on the diagram.
        When used on geographic diagrams this function returns the physical as drawn line length.

        :param diagram: IscDiagram instance obtained from the GetDiagram function.
        :type diagram: IscDiagram
        :param pComponent: IscBranch instance returned by a GetBranch function.
        :type pComponent: IscBranch
        :return: The component length.
        :rtype: float
        """
        pass

    @overload
    def GetLineLength(self, diagram, nLineUID: int) -> float:
        """
        Returns the component length as drawn on the diagram.
        When used on geographic diagrams this function returns the physical as drawn line length.

        :param diagram: IscDiagram instance obtained from the GetDiagram function.
        :type diagram: IscDiagram
        :param nLineUID: The unique integer for the line.
        :type nLineUID: int
        :return: The component length.
        :rtype: float
        """
        pass

    def GetLineLength(self, diagram, nLineUID: int) -> float:
        """
        Returns the component length as drawn on the diagram.
        When used on geographic diagrams this function returns the physical as drawn line length.

        :param diagram: IscDiagram instance obtained from the GetDiagram function.
        :type diagram: IscDiagram
        :param pComponent: IscBranch instance returned by a GetBranch function.
        :type pComponent: IscBranch
        :param nLineUID: The unique integer for the line.
        :type nLineUID: int
        :return: The component length.
        :rtype: float
        """
        pass

    def MessageBox(self, strDialogTitle: str, strMessage: str) -> bool:
        """
        Display a message box with title specified by strDialogTitle and a message specified by strMessage.
        An OK button is provided for the user to dismiss the dialog.

        :param strDialogTitle: The title of the message box.
        :type strDialogTitle: str
        :param strMessage: The message displayed on the message box.
        :type strMessage: str
        :return: Boolean denoting whether a message box is created.
        :rtype: bool
        """
        pass

    def AskQuestion(self, strDialogTitle: str, strQuestion: str) -> bool:
        """
        Display a message box with a title and a question as shown below.

        :param strDialogTitle: The title of the message box.
        :type strDialogTitle: str
        :param strQuestion: The question displayed on the message box.
        :type strQuestion: str
        :return: True when the user clicks Yes, otherwise False.
        :rtype: bool
        """
        pass

    def AllowStackBarUpdates(self, bAllow: bool) -> None:
        """
        Setting bAllow to True prevents the Ipsa stack bar from updating during script execution.
        This can provide speed improvements since redrawing the stack bar is prevented.

        :param bAllow: Deciding whether the Ipsa stack bar can be updated during script execution.
        :type bAllow: bool
        """
        pass

    def GetDate(self) -> str:
        """
        Returns the date and time that Ipsa was launched, e.g. 06 Nov 2012 22:53:17.

        :return: The date in a string format.
        :rtype: str
        """
        pass

    def GetUser(self) -> str:
        """
        Returns the name of the current logged on user.

        :return: The name of the current logged on user.
        :rtype: str
        """
        pass

    def GetHost(self) -> str:
        """
        Returns the host name of the PC.

        :return: The host name of the PC.
        :rtype: str
        """
        pass

    def GetOrganisation(self) -> str:
        """
        Returns the company organisation data as set in network properties.

        :return: The company organisation data.
        :rtype: str
        """
        pass

    def GetNetworkTitle(self) -> str:
        """
        Returns the network title as set in network properties.

        :return: The network title.
        :rtype: str
        """
        pass

    def GetNetworkFileName(self) -> str:
        """
        Returns the filename of the current network.

        :return: The filename of the current network.
        :rtype: str
        """
        pass

    def GetFileName(self, strDialogTitle: str, strFileTypes: str) -> str:
        """
        Display the operating system File Open dialog to prompt the user to select a file.

        :param strDialogTitle: The title of the dialog itself.
        :type strDialogTitle: str
        :param strFileTypes: The file type filter.
        :type strFileTypes: str
        :return: String containing the file name and path selected by the user.
        :rtype: str
        """
        pass

    def GetDirectoryName(self, strDialogTitle: str) -> str:
        """
        Display the operating system Folder Selection dialog to prompt the user to select a folder.

        :param strDialogTitle: The title of the dialog itself.
        :type strDialogTitle: str
        :return: String containing the path selected by the user.
        :rtype: str
        """
        pass

    def GetVersion(self) -> str:
        """
        Returns the version number of IPSA software.

        :return: The version number.
        :rtype: str
        """
        pass

    def HasLoadFlow(self) -> bool:
        """
        Returns True if a load flow license is present.

        :return: Boolean denoting whether a load flow license is presented.
        :rtype: bool
        """
        pass

    def HasFaultLevel(self) -> bool:
        """
        Returns True if a fault level license is present.

        :return: Boolean denoting whether a fault level license is presented.
        :rtype: bool
        """
        pass

    def HasTransient(self) -> bool:
        """
        Returns True if a transient stability license is present.

        :return: Boolean denoting whether a transient stability license is presented.
        :rtype: bool
        """
        pass

    def HasProtection(self) -> bool:
        """
        Returns True if a protection analysis license is present.

        :return: Boolean denoting whether a protection analysis license is presented.
        :rtype: bool
        """
        pass

    def HasHarmonics(self) -> bool:
        """
        Returns True if a harmonics analysis license is present.

        :return: Boolean denoting whether a harmonics analysis license is presented.
        :rtype: bool
        """
        pass

    def HasUDM(self) -> bool:
        """
        Returns True if a UDM (User Defined Modelling) license is present.

        :return: Boolean denoting whether a UDM license is presented.
        :rtype: bool
        """
        pass

    def HasDC(self) -> bool:
        """
        Returns True if a DC component license is present.

        :return: Boolean denoting whether a DC component license is presented.
        :rtype: bool
        """
        pass

    def HasStaticCon(self) -> bool:
        """
        Returns True if a static converter license is present.

        :return: Boolean denoting whether a static converter license is presented.
        :rtype: bool
        """
        pass

    def HasTandemGen(self) -> bool:
        """
        Returns True if a tandem generator license is present.

        :return: Boolean denoting whether a tandem generator license is presented.
        :rtype: bool
        """
        pass

    def HasNonLinDevs(self) -> bool:
        """
        Returns True if a non-linear devices license is present.

        :return: Boolean denoting whether a non-linear devices license is presented.
        :rtype: bool
        """
        pass

    def HasAutomation(self) -> bool:
        """
        Returns True if an automation analysis license is present.

        :return: Boolean denoting whether an automation analysis license is presented.
        :rtype: bool
        """
        pass

    def IsLimitedSize(self) -> bool:
        """
        Returns True if the current license imposes a limit on the maximum number of busbars.

        :return: Boolean denoting whether the current license imposes a limit on the maximum number of busbars.
        :rtype: bool
        """
        pass

    def GetMaxBusbars(self) -> int:
        """
        Returns the maximum number of busbars if it is a limited busbar version, returns 0 if unlimited.

        :return: The maximum number of busbars if in limited busbar version, else 0.
        :rtype: int
        """
        pass

    def DisplayResultsTable(self, nTableType: int) -> None:
        """
        Displays the Ipsa results table which will contain the results of the last analysis.

        :param nTableType: Specify the type of table displayed:

            - ipsa.IscInterface.BusbarLF = busbar load flow results
            - ipsa.IscInterface.GeneratorLF = generator load flow results
            - ipsa.IscInterface.GridInfeedLF = grid infeed load flow results
            - ipsa.IscInterface.LoadLF = load object load flow results
            - ipsa.IscInterface.IMachineLF = motor load flow results
            - ipsa.IscInterface.StaticVCLF = SVC load flow results
            - ipsa.IscInterface.MechSwCapLF = switched capacitor load flow results
            - ipsa.IscInterface.UMachineLF = universal machine load flow results
            - ipsa.IscInterface.FilterLF = harmonic filter load flow results
            - ipsa.IscInterface.LineLF = branch load flow results
            - ipsa.IscInterface.TransformerLF = transformer load flow results
            - ipsa.IscInterface.ThreeWindingTransformerLF = 3 winding transformer load flow results
            - ipsa.IscInterface.BatteryLF = DC battery load flow results
            - ipsa.IscInterface.DCMachineLF = DC machine load flow results
            - ipsa.IscInterface.ConverterLF = AC-DC converter load flow results
            - ipsa.IscInterface.MGSetLF = motor- generator set load flow results
            - ipsa.IscInterface.BusbarFL = busbar fault level results
            - ipsa.IscInterface.GeneratorFL = generator fault level results
            - ipsa.IscInterface.GridInfeedFL = grid infeed fault level results
            - ipsa.IscInterface.LoadFL = load object fault level results
            - ipsa.IscInterface.IMachineFL = motor fault level results
            - ipsa.IscInterface.LineFL = branch fault level results
            - ipsa.IscInterface.TransformerFL = transformer fault level results
            - ipsa.IscInterface.ThreeWindingTransformerFL = 3 winding transformer fault level results
            - ipsa.IscInterface.BusbarHM = busbar harmonic analysis results
            - ipsa.IscInterface.GeneratorHM = generator harmonic analysis results
            - ipsa.IscInterface.LoadHM = load object harmonic analysis results
            - ipsa.IscInterface.IMachineHM = motor harmonic analysis results
            - ipsa.IscInterface.FilterHM = filter harmonic analysis results
            - ipsa.IscInterface.LineHM = branch harmonic analysis results
            - ipsa.IscInterface.TransformerHM = transformer harmonic analysis results
            - ipsa.IscInterface.ThreeWindingTransformerHM = 3 winding transformer harmonic analysis results
        :type: int
        """
        pass

    def GetResultsTableText(self, nTableType: int) -> str:
        """
        Returns the data contained in the results' table as a comma delimited string
        which can be pasted directly into a spreadsheet.

        :param nTableType: The type defined for the DisplayResultsTable function.
        :type nTableType: int
        :return: Data contained in the results' table.
        :rtype: str
        """
        pass

    def CloseResultsTable(self, nTableType: int) -> None:
        """
        Closes the results' table nTableType which is as defined for the DisplayResultsTable function.

        :param nTableType: The type defined for the DisplayResultsTable function.
        :type nTableType: int
        """
        pass

    def GetLogFileName(self) -> str:
        """
        Get the name of log file.

        :return: The name of the log file.
        :rtype: str
        """
        pass

    def DbgSetLogFileName(self, strName: str) -> None:
        """
        Set the name of the load flow log file to strName.
        If no file path is specified then the file is created in the Ipsa bin directory.

        :param strName: The name of the load flow log file.
        :type strName: str
        """
        pass

    def IsLogging(self) -> bool:
        """
        Checks whether a logging is in progress.

        :return: Returns True if logging is in progress.
        :rtype: bool
        """
        pass

    def DbgStartLogging(self) -> None:
        """Start logging of all analysis engine calls."""
        pass

    def DbgStopLogging(self) -> None:
        """Stop logging of all analysis engine calls."""
        pass
