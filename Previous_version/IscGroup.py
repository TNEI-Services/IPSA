from typing import List


class IscGroup:
    """
    The IscGroup class provides access to an Ipsa group to set and get group members.
    """
    def GetUID(self) -> int:
        """
        Returns the UID of the group.

        :return: The group UID.
        :rtype: int
        """
        pass

    def GetName(self) -> str:
        """
        Returns the user defined group name as a string.

        :return: The user defined group name.
        :rtype: str
        """
        pass

    def SetName(self, strName: str) -> None:
        """
        Sets the name as a string.

        :param strName: The selected string name.
        :type strName: str
        """
        pass

    def GetGroupType(self) -> int:
        """
        Returns the type of the group where:

            - 0 = No group type
            - 1 = Area type group – contains all busbars in an area
            - 2 = Mixed item group
            - 3 = Load scaling group
            - 4 = Load transfer group
            - 5 = Protection device group
            - 8 = Generator scaling group
            - 9 = Region group
            - 10 = Transformer group (master slave operation)

        :return: The group type.
        :rtype: int
        """
        pass

    def GetMembers(self) -> List[int]:
        """
        Returns a list containing the UIDs of the components in the group.

        :return: The UIDs of the components in the group.
        :rtype: list(int)
        """
        pass

    def SetMembers(self, nUIDs: List[int]) -> None:
        """
        Sets the group members to the list of component integers.
        This replaces any existing members with the supplied list of UIDs.

        :param nUIDs: List of component integers.
        :type nUIDs: list(int)
        """
        pass

    def GetLoadScalingReal(self) -> float:
        """
        Returns the per unit scaling factor for the active power load.

        :return: The per unit scaling factor for the active power load.
        :rtype: float
        """
        pass

    def GetLoadScalingReactive(self) -> float:
        """
        Returns the per unit scaling factor for the reactive power load.

        :return: The per unit scaling factor for the reactive power load.
        :rtype: float
        """
        pass

    def SetLoadScaling(self, fMW: float, fMVAr: float) -> bool:
        """
        Sets the per unit scaling factors for the active and reactive parts of the load.

        :param fMW: The active part of the load.
        :type fMW: float
        :param fMVAr: The reactive part of the load.
        :type fMVAr: float
        :return: True if successful.
        :rtype: bool
        """
        pass
