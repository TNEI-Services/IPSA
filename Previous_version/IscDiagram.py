from typing import List, overload


class IscDiagram:
    """
    The ``IscDiagram`` class provides access to graphical data on a single Ipsa diagram.
    These functions allow network components to be drawn, display options to be set and deleted.

    The creation of items on the diagram also creates the associated network components.
    The parameters of these components can then be set using the functions described for the particular component types.

    The origin for the co-ordinates is normally the top left corner of the diagram.
    Positive values of X are to the right whilst positive values of Y are down below the origin.
    """
    def GetName(self) -> str:
        """
        Returns the name of the diagram.

        :return: The name of the diagram.
        :rtype: str
        """
        pass

    def SetName(self, strName: str) -> None:
        """
        Sets the name of the diagram.

        :param strName: The name of the diagram.
        :type strName: str
        """
        pass

    def CreateBusbarPoint(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        A point busbar symbol is a small dot which does not resize as the diagram zoom level is changed.

        :param strName: The busbar name.
        :type strName: str
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def CreateBusbarJunction(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        A junction busbar symbol is the circular junction symbol.

        :param strName: The busbar name.
        :type strName: str
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def CreateBusbarHexagonal(self, strName: str, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        A hexagonal busbar symbol has six sides.

        :param strName: The busbar name.
        :type strName: str
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def CreateBusbarRectangular(self, strName: str, bHorizontal: bool, dX: float, dY: float) -> int:
        """
        Creates a new busbar component on the diagram.
        The rectangular symbol is the standard horizontal or vertical busbar.

        :param strName: The busbar name.
        :type strName: str
        :param bHorizontal: True draws a horizontal rectangular busbar, while False draws a vertical busbar.
        :type bHorizontal: bool
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: The unique ID of the new busbar.
        :rtype: int
        """
        pass

    def DrawBusbarPoint(self, nUID: int, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        A point busbar symbol is displayed as a small dot which does not resize as the diagram zoom level is changed.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarJunction(self, nUID: int, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        A junction busbar symbol is the solid circular junction symbol.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarHexagonal(self, nUID: int, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        The hexagonal symbol is the standard filled hexagonal busbar.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarRectangular(self, nUID: int, bHorizontal: bool, dSize: float, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        The rectangular symbol is the standard horizontal or vertical busbar.

        :param nUID: The busbar UID.
        :type nUID: int
        :param bHorizontal: True draws a horizontal rectangular busbar, while False draws a vertical busbar.
        :type bHorizontal: bool
        :param dSize: The length of the busbar symbol.
        :type dSize: float
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def DrawBusbarCircular(self, nUID: int, dSize: float, dX: float, dY: float) -> bool:
        """
        Draws an existing busbar component on the diagram as defined by the busbar UID.
        The circular symbol is the larger unfilled circle.

        :param nUID: The busbar UID.
        :type nUID: int
        :param dSize: The radius of the busbar symbol.
        :type dSize: float
        :param dX: The busbar x coordinate.
        :type dX: float
        :param dY: The busbar y coordinate.
        :type dY: float
        :return: Boolean denoting whether the busbar was drawn.
        :rtype: bool
        """
        pass

    def CreateLine(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        Creates a new branch component on the diagram.

        :param strName: The branch name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new branch.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    def DrawLine(self, nUID: int) -> bool:
        """
        Draws the symbol for the line identified by the unique ID.
        The line is drawn as a single segment between two busbars.
        The line must have been created using one of the following first:

            - IscDiagram.CreateLine
            - IscNetwork.CreateBranch
            - IscNetwork.CreateTransformer

        :param nUID: The line UID.
        :type nUID: int
        :return: Boolean denoting whether the line was drawn.
        :rtype: bool
        """
        pass

    def CreateTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        Creates a new transformer component on the diagram.

        :param strName: The branch name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new transformer.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    def DrawTransformer(self, nUID: int) -> bool:
        """
        Draws the symbol for the transformer identified by the unique ID.
        The line is drawn as a single segment between two busbars.
        The line must have been created using the following first:

            - IscNetwork.CreateTransformer

        :param nUID: The transformer UID.
        :type nUID: int
        :return: Boolean denoting whether the line was drawn.
        :rtype: bool
        """
        pass

    def CreateUnbalancedLine(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        Creates a new unbalanced line component on the diagram.

        :param strName: The unbalanced line name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new unbalanced line component.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    def CreateUnbalancedTransformer(self, strName: str, dXFrom: float, dYFrom: float, dXTo: float, dYTo: float) -> int:
        """
        Creates a new unbalanced transformer component on the diagram.

        :param strName: The unbalanced transformer name.
        :type strName: str
        :param dXFrom: The x coordinate of the busbar where the branch starts.
        :type dXFrom: float
        :param dYFrom: The y coordinate of the busbar where the branch starts.
        :type dYFrom: float
        :param dXTo: The x coordinate of the busbar where the branch ends.
        :type dXTo: float
        :param dYTo: The y coordinate of the busbar where the branch ends.
        :type dYTo: float
        :return: The unique positive ID of the new unbalanced transformer component.
            A negative value is returned if the “from” end busbar is not found,
            and zero is returned if the “to” end busbar is not found.
        :rtype: int
        """
        pass

    def AddPointToLine(self, nLineUID: int, dX: float, dY: float, bFromEnd: bool) -> bool:
        """
        Adds a knee point to the line identified by the unique ID.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param dX: The knee point x coordinate.
        :type dX: float
        :param dY: The knee point y coordinate.
        :type dY: float
        :param bFromEnd: If True then the knee point is added to the last segment, i.e. furthest from the From end.
            If False then the knee point is added to the first segment.
        :type bFromEnd: float
        :return: Boolean denoting whether the knee point was added.
        :rtype: bool
        """
        pass

    def RefreshLine(self, nLineUID: int) -> None:
        """
        Redraws the line identified by the line UID after knee points have been added.

        :param nLineUID: The line UID.
        :type nLineUID: int
        """
        pass

    def SplitBranch(self, nLineUID: int, nSection: int, dRatio: float, strName: str) -> int:
        """
        Splits a branch into two sections connected by a new busbar.

        :param nLineUID: The line UID.
        :type nLineUID: int
        :param nSection: Specifies which section of a multi-section branch is split.
            For branches with only one section then nSection should be set to 0.
        :type nSection: int
        :param dRatio: Specifies how the branch impedances are divided between the new branches.
            A value of 0.0 sets the split position to be at the “From” end whilst a value of 1.0 specifies the “To” end.
            Values between 0.0 and 1.0 split the branch in proportion.
            For multi-section branches dRatio splits the section identified by nSection.
        :type dRatio: float
        :param strName: The name of the busbar.
        :type strName: str
        :return: The UID of the new branch if it is greater than 0. ) if the branch has not been split.
            This is because there is a circuit breaker on the branch or the branch is drawn on more than one diagram.
        :rtype: int
        """
        pass

    def DrawUndrawnItemsAttachedToBusbar(self, nBusbarUID: int) -> None:
        """
        Draws items attached to the busbar identified by the busbar UID if they are not already drawn on the diagram.
        Note that this will draw branch items as well.

        :param nBusbarUID: The busbar UID.
        :type nBusbarUID: int
        """
        pass

    def DeleteItem(self, nUID: int) -> bool:
        """
        Deletes the graphic item identified by the ID. This may be a line, radial component or busbar.

        :param nUID: The graphical item UID.
        :type nUID: int
        :return: Denoting whether the item was deleted.
        :rtype: bool
        """
        pass

    @overload
    def GetLineLength(self, nUID: int) -> float:
        """
        Returns the component length for the graphic symbol on the current diagram.
        On geographic diagrams this function returns the actual line length,
        assuming that the diagram is correctly scaled.

        :param nUID: The line UID.
        :type nUID: int
        :return: The component length for the graphic symbol.
        :rtype: float
        """
        pass

    @overload
    def GetLineLength(self, pComponent) -> float:
        """
        Returns the component length for the graphic symbol on the current diagram.
        On geographic diagrams this function returns the actual line length,
        assuming that the diagram is correctly scaled.

        :param pComponent: The line IscBranch instance.
        :type pComponent: IscBranch
        :return: The component length for the graphic symbol.
        :rtype: float
        """
        pass

    def GetLineLength(self, pComponent) -> float:
        """
        Returns the component length for the graphic symbol on the current diagram.
        On geographic diagrams this function returns the actual line length,
        assuming that the diagram is correctly scaled.

        :param nUID: The line UID.
        :type nUID: int
        :param pComponent: The line IscBranch instance.
        :type pComponent: IscBranch
        :return: The component length for the graphic symbol.
        :rtype: float
        """
        pass

    def SetItemPenColour(self, nUID: int, nRed: int, nGreen: int, nBlue: int, nAlpha: int) -> bool:
        """
        Sets the outline colour of the diagram object.
        The colour is set by the RGB parameters.
        All colour parameters should be between 0 and 255.

        :param nUID: The diagraqm object UID.
        :type nUID: int
        :param nRed: The red colour.
        :type nRed: int
        :param nGreen: The green colour.
        :type nGreen: int
        :param nBlue: The blue colour.
        :type nBlue: int
        :param nAlpha: The transparency of the colour.
        :type nAlpha: int
        :return: Denoting whether the colour is set.
        :rtype: bool
        """
        pass

    def SetItemBrushColour(self, nUID: int, nRed: int, nGreen: int, nBlue: int, nAlpha: int) -> bool:
        """
        Sets the fill colour of the diagram object.
        The colour is set by the RGB parameters.
        All colour parameters should be between 0 and 255.

        :param nUID: The diagraqm object UID.
        :type nUID: int
        :param nRed: The red colour.
        :type nRed: int
        :param nGreen: The green colour.
        :type nGreen: int
        :param nBlue: The blue colour.
        :type nBlue: int
        :param nAlpha: The transparency of the colour.
        :type nAlpha: int
        :return: Denoting whether the colour is set.
        :rtype: bool
        """
        pass

    def MapToLatLong(self, fScreenX: float, fScreenY: float) -> List[float]:
        """
        Returns the latitude and longitude in decimal degrees of the screen position.
        The diagram is the one referenced by the IscDiagram object that the function is called on.
        The fScreenX and fScreenY parameters are relative to the nominal centre point of the screen,
        therefore calling this function with fScreenX = 0.0 and fScreenY = 0.0 returns the centre point of
        the background map in degrees.
        Note that the screen X is north/south and screen y is east/west.

        :param fScreenX: The x coordinate of the screen position.
        :type fScreenX: float
        :param fScreenX: The y coordinate of the screen position.
        :type fScreenX: float
        :return: The latitude and longitude of the screen position.
        :rtype: list(float)
        """
        pass

    def LatLongToMap(self, fN: float, fE: float) -> List[float]:
        """
        Returns the screen X and Y coordinates of the latitude and longitude.
        The fScreenX and fScreenY coordinates are relative to the nominal centre point of the screen
        which can be found by the MapToLatLong function.
        Note that the screen X is north/south and screen y is east/west.

        :param fN: The latitude.
        :type fN: float
        :param fE: The longitude.
        :type fE: float
        :return: The screen X and Y coordinates.
        :rtype: list(float)
        """
        pass

    def GetItemX(self, nUID: int) -> float:
        """
        Returns the screen X coordinate of the busbar.
        The screen co-ordinates are relative to the nominal centre point of the screen.

        :param nUID: The busbar UID.
        :type nUID: int
        :return: The screen X coordinate.
        :rtype: float
        """
        pass

    def GetItemY(self, nUID: int) -> float:
        """
        Returns the screen Y coordinate of the busbar.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The busbar UID.
        :type nUID: int
        :return: The screen Y coordinate.
        :rtype: float
        """
        pass

    def GetItemFromXPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen X coordinates of the FROM busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the FROM end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen X coordinates.
        :rtype: float
        """
        pass

    def GetItemFromYPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen Y coordinates of the FROM busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the FROM end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen Y coordinates.
        :rtype: float
        """
        pass

    def GetItemToXPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen X coordinates of the TO busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the TO end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen X coordinates.
        :rtype: float
        """
        pass

    def GetItemToYPoints(self, nUID: int) -> List[float]:
        """
        Returns a list of floats for the screen Y coordinates of the TO busbar point, the middle point of the line and
        all knee points lying on the branch between these two points.
        The coordinates are for the TO end of the line.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen Y coordinates.
        :rtype: float
        """
        pass

    def CreateAnnotation(self, strName: str, strAnnotationText: str, dX: float, dY: float) -> int:
        """
        Creates a new diagram annotation.
        The screen coordinates are relative to the nominal centre point of the screen.

        :param strName: The strName is not used and can be an empty string.
        :type strName: str
        :param strAnnotationText: The text to be displayed on the diagram.
            The text string can include simple html for text formatting.
        :type strAnnotationText: str
        :param dX: The x coordinate of the diagram.
        :type dX: float
        :param dY: The y coordinate of the diagram.
        :type dY: float
        :return: The diagram annotation.
        :rtype: int
        """
        pass

    def PrintPDF(self, strFileName: str) -> None:
        """
        Print the diagram to a PDF file.

        :param nUID: The line UID.
        :type nUID: int
        :return: The screen Y coordinate.
        :rtype: float
        """
        pass
