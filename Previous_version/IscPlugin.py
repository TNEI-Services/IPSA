class IscPlugin:
    """
    The IscPlugin class provides access to an Ipsa plugin,
    to set and get data values and assign the plugin to a component.
    To use the functions in this section an IscPlugin plugin object must be created from the CreatePlugin function
    of the IscNetwork class.
    One such object should be created each time a plugin is to be assigned to a network component.
    """
    def SetName(self, strName: str) -> bool:
        """
        Sets the name as a string.

        :param strName: The selected string name.
        :type strName: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDValue(self, nFieldIndex: int) -> float:
        """
        Returns a double value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: str
        """
        pass

    def SetIValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the value for the enumerated field from an integer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetDValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the value for the enumerated field from a double.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetSValue(self, nFieldIndex: int, strValue: int) -> bool:
        """
        Sets the value for the enumerated field from a string.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetIntParameter(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the parameter for the field from an integer value. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetDoubleParameter(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the parameter for the field from a double value. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetBoolParameter(self, nFieldIndex: int, strValue: int) -> bool:
        """
        Sets the parameter for the field from a boolean value. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def GetIntParameter(self, nFieldIndex: int) -> int:
        """
        Returns an integer parameter for the enumerated field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDoubleParameter(self, nFieldIndex: int) -> float:
        """
        Returns a double parameter for the enumerated field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetBoolParameter(self, nFieldIndex: int) -> bool:
        """
        Returns a boolean parameter for the enumerated field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: bool
        """
        pass

    def GetIntOutput(self, nFieldIndex: int) -> int:
        """
        Returns the integer output of the plugin itself for the field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDoubleOutput(self, nFieldIndex: int) -> float:
        """
        Returns the double output of the plugin itself for the field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetBoolOutput(self, nFieldIndex: int) -> bool:
        """
        Returns the boolean output of the plugin itself for the field. The parameters are specific for the plugin object.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: bool
        """
        pass
