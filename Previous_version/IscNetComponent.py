from typing import Dict, Union


class IscNetComponent:
    """
    The base class for all IPSA components.
    """
    def GetUID(self) -> int:
        """
        Returns the unique ID of the component.

        :return: The unique ID of the component.
        :rtype: int
        """
        pass

    def GetName(self) -> str:
        """
        Gets the name as a string - this is the name Python knows the object by
        (only identical to the Ipsa name for busbars).

        :return: The name of the component.
        :rtype: str
        """
        pass

    def SetName(self, strName: str) -> None:
        """
        Sets the name to the component to the specified name.

        :param strName: The component name.
        :type strName: str
        """
        pass

    def GetRealName(self, strName: str) -> str:
        """
        Gets the user defined component name as a string for the specified component name.

        :param strName: The component Python name.
        :type strName: str
        :return: Returns the IPSA component name.
        :rtype: str
        """
        pass

    def SetRealName(self, strName: str) -> None:
        """
        Sets the user defined IPSA component name.

        :param strName: The IPSA component name.
        :type strName: str
        """
        pass

    def GetFieldType(self, nFieldIndex: int) -> str:
        """
        Returns the field type as a string for the given enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: Returns ‘String’, ‘Integer’, ‘Float’ or ‘Boolean’.
        :rtype: str
        """
        pass

    def GetFieldName(self, nFieldIndex: int) -> str:
        """
        Returns the field name as a string for the given enumerated field.

        :param nFieldIndex: The given enumerated field.
        :type nFieldIndex: int
        :return: The field name.
        :rtype: str
        """
        pass

    def GetFromBusbarUID(self, nBranchUID: int) -> int:
        """
        Returns the FROM busbar UID of the given branch.

        :param nBranchUID: The branch UID.
        :type nBranchUID: int
        :return: The FROM busbar UID.
        :rtype: int
        """
        pass

    def GetToBusbarUID(self, nBranchUID: int) -> int:
        """
        Returns the TO busbar UID of the given branch.

        :param nBranchUID: The branch UID.
        :type nBranchUID: int
        :return: The TO busbar UID.
        :rtype: int
        """
        pass

    def GetType(self) -> int:
        """
        Returns an integer that matches one of the class' field indices (e.g., IscNetComponent.Busbar).

        :return: The integer that matches one of the class' field indices.
        :rtype: int
        """
        pass

    def AddDataExtension(self, strName: str, default: Union[int,float,str]) -> int:
        """
        Adds an integer data field and returns the new field index. Sets the default value.
        **Note: The variable of the function is not called default!!!**

        You can use either nDefault, dDefault, or strDefault specifying the default value.

        :param strName: The name of the field.
        :type strName: str
        :param nDefault: The integer default value.
        :type nDefault: int
        :param dDefault: The float default value.
        :type dDefault: float
        :param strDefault: The string default value.
        :type strDefault: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListIntDataExtension(self, strName: str) -> int:
        """
        Adds a list of integers data field and returns the new field index.
        Sets the default value to an empty list.

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListDblDataExtension(self, strName: str) -> int:
        """
        Adds a list of doubles data field and returns the new field index.
        Sets the default value to an empty list.

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def AddListStrDataExtension(self, strName: str) -> int:
        """
        Adds a list of strings data field and returns the new field index.
        Sets the default value to an empty list.

        :param strName: The name of the field.
        :type strName: str
        :return: The new field index.
        :rtype: int
        """
        pass

    def GetListIntExtensionValue(self, nFieldIndex: int, nIndex: int) -> int:
        """
        Get a single integer value from the list for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: int
        """
        pass

    def GetListDblExtensionValue(self, nFieldIndex: int, nIndex: int) -> float:
        """
        Get a single float value from the list for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: float
        """
        pass

    def GetListStrExtensionValue(self, nFieldIndex: int, nIndex: int) -> str:
        """
        Get a single string value from the list for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :return: The element value.
        :rtype: str
        """
        pass

    def GetListIntSize(self, nFieldIndex: int) -> int:
        """
        Get size of the list of integers for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def GetListDblSize(self, nFieldIndex: int) -> int:
        """
        Get size of the list of doubles for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def GetListStrSize(self, nFieldIndex: int) -> int:
        """
        Get size of the list of strings for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The size of the field list.
        :rtype: int
        """
        pass

    def SetListIntExtensionValue(self, nFieldIndex: int, nIndex: int, nValue: int) -> bool:
        """
        Sets the value of an element in a list of integers for the enumerated field at given position to given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param nValue: The selected value.
        :type nValue: int
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetListDblExtensionValue(self, nFieldIndex: int, nIndex: int, dValue: float) -> bool:
        """
        Sets the value of an element in a list of doubles for the enumerated field at given position to given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param dValue: The selected value.
        :type dValue: float
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def SetListStrExtensionValue(self, nFieldIndex: int, nIndex: int, strValue: str) -> bool:
        """
        Sets the value of an element in a list of strings for the enumerated field at given position to given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nIndex: The index of the selected element.
        :type nIndex: int
        :param strValue: The selected value.
        :type strValue: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListIntExtensionValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Adds an item to the end of a list of integers for the enumerated field with the given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The selected value.
        :type nValue: int
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListDblExtensionValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Adds an item to the end of a list of doubles for the enumerated field with the given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The selected value.
        :type dValue: float
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def PushBackListStrExtensionValue(self, nFieldIndex: int, strValue: str) -> bool:
        """
        Adds an item to the end of a list of strings for the enumerated field with the given value.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The selected value.
        :type strValue: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        pass

    def GetExtensionFieldIndex(self, strName: str) -> int:
        """
        Returns the field index for the extended data field.

        :param strName: The name of the extended data field.
        :type strName: str
        :return: The field index.
        :rtype: int
        """
        pass

    def GetExtensionNames(self) -> Dict[int,str]:
        """
        Returns a dictionary of extension field indexes and field names.
        The dictionary keys are integers representing all the extended data fields.
        The dictionary values are the field names of the individual extended data fields.
        Each extended data field is therefore represented by {nIndex:strName}, where integer nIndex is the field index
        and string strName is the field name.

        :return: Dictionary of extension field indexes and field names.
        :rtype: dict(int, str)
        """
        pass
