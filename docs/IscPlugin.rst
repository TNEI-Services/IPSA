IscPlugin
============

The ``IscPlugin`` class provides access to an IPSA plugin, to set and get data values and assign the plugin to a component. To use the functions in this section an ``IscPlugin`` plugin object must be created from the ``CreatePlugin`` function of the ``IscNetwork`` class. One such object should be created each time a plugin is to be assigned to a network component. The sequence of operations is as follows:

    1. Create an ``IscPlugin`` from the ``CreatePlugin`` function of ``IscNetwork``

        a. The plugin name should be obtained from the plugin documentation
    2. Set the ``ControlledUID`` field value to the UID of the component that the plugin is to be assigned to
    3. Set the ``Plugin`` field value of the component itself to the UID of the plugin created in step 1
    4. The plugin parameters can now be set using the normal ``SetIntParameterValue`` function calls etc

    a. Note that the ``Set...``/``Get...`` functions are used only to get and set ``IscPlugin`` **field values** such as ``Name`` and ``Type``

Refer to the documentation provided with each plugin to determine the usage and parameter values available.

Field Values
-------------

.. list-table:: **IscPlugin Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - ControlledUID
     - Gets the unique ID for controlled plugin.
   * - String
     - Name
     - Gets the plugin name.
   * - Integer
     - Type
     - Returns the type of the plugin, defined as follows:

        - 1 = Synchronous Machine AVR
        - 2 = Synchronous Machine Governor
        - 3 = DC Machine AVR
        - 4 = DC Machine Governor
        - 5 = Induction Machine D Axis AVR
        - 6 = Induction Machine Q Axis AVR
        - 7 = Induction Machine Governor
        - 8 = Synchronous Machine
        - 9 = DC Machine
        - 10 = AC/DC Converter
        - 11 = AC Converter Controller
        - 12 = DC Converter Controller
        - 13 = DC Non – Linear Devive
        - 14 = Universal Machine Active Power Controller
        - 15 = Universal Machine Reactive Power Controller
        - 16 = Induction Machine
        - 17 = Universal Machine
        - 18 = MSC Controller
        - 19 = SVC Controller
        - 20 = Transformer AVR
        - 21 = Network Controller
        - 30 = Line Dynamic Rating
        - 31 = Transformer Dynamic Rating
        - 32 = Transformer Reverse Rating
        - 50 = Battery Dynamic Model
   * - String
     - Model
     - Returns the model name of the plugin.

IscPlugin Class
----------------

.. autoclass:: ipsa.IscPlugin
   :members:
