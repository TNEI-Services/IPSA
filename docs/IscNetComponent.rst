IscNetComponent
================

The ``IscNetComponent`` class is the base class for all IPSA components. All functions that are exposed (described below) are accessible via the derived component classes. The functions in this section should therefore be used in conjunction with one of the IPSA component classes, e.g. for accessing busbar data the following code would be used:

::

    busbar = ipsa_network.GetBusbar(“Busbar1”)
    nBusbarUID = busbar.GetUID()

Extension Data
---------------

It is possible to add extension data to an object of any type. The definitions of the data extension fields are held as static data associated with the component, i.e. all components of the same type have the same extension data fields. The actual field values on each component are stored with the component.

All extension data is handled transparently by the IPSA filing modules and is not currently used for analysis by IPSA. All extension data fields are persistent when filed.

The field names for extended data fields **must not** contain spaces. Only alphanumeric characters and underscores are permitted.

Field Values
-------------
Below is a list of the field values for IscNetComponent which map each derived component object to a field value, sometimes used within the code.

.. tabularcolumns:: |\Y{0.3}|\Y{0.5}|
.. list-table:: **IscNetComponent Field Values - Types**
   :widths: 5, 5
   :class: tight-table, longtable
   :header-rows: 1

   * - Field Name
     - PyIPSA class
   * - Unknown
     - An unknown IscNetComponent object
   * - Busbar
     - IscBusbar
   * - Load
     - IscLoad
   * - Generator
     - IscSynMachine
   * - IndMachine
     - IscIndMachine
   * - Harmonic
     - IscHarmonic
   * - HarmonicFilter
     - IscFilter
   * - MechSwCapacitor
     - IscMechSwCapacitor
   * - StaticVArC
     - IscStaticVC
   * - Battery
     - IscBattery
   * - DCMachine
     - IscDCmachine
   * - UniMachine
     - IscUMachine
   * - GridInfeed
     - IscGridInfeed
   * - Line
     - IscBranch
   * - Transformer
     - IscTransformer
   * - ThreeWTransformer
     - Isc3WTransformer
   * - ACDCConverter
     - IscConverter
   * - DCDCConverter
     - IscChopper
   * - MGset
     - IscMGset
   * - UniversalBranch
     - (Not mapped to PyIPSA)
   * - UnbalancedLoad
     - IscUnbalancedLoad
   * - UnbalancedLine
     - IscUnbalancedLine
   * - UnbalancedTransformer
     - IscUnbalancedTransformer
   * - AVR
     - (Not mapped to PyIPSA)
   * - Governor
     - (Not mapped to PyIPSA)
   * - DCConverterCtl
     - (Not mapped to PyIPSA)
   * - ACConverterCtl
     - (Not mapped to PyIPSA)
   * - DCMachineCtl
     - (Not mapped to PyIPSA)
   * - PluginModel
     - IscPlugin
   * - CircuitBreaker
     - IscCircuitBreaker
   * - SeriesRegulator
     - IscVoltageRegulator
   * - ProtectionContainer
     - (Not mapped to PyIPSA)
   * - ProtectionMonitorCT
     - (Not mapped to PyIPSA)
   * - ProtectionDevice
     - IscProtectionDevice
   * - EquivalentBoundary
     - IscBoundary
   * - EquivalentBranch
     - IscEquivalentBranch
   * - EquivalentRadial
     - IscEquivalentRadial
   * - Annotation
     - IscAnnotation
   * - AnalysisLF
     - IscAnalysisLF
   * - AnalysisFL
     - IscAnalysisFL
   * - AnalysisMS
     - (Not mapped to PyIPSA)
   * - AnalysisBD
     - (Not mapped to PyIPSA)
   * - AnalysisTS
     - (Not mapped to PyIPSA)
   * - AnalysisHM
     - IscAnalysisHM
   * - AnalysisProt
     - (Not mapped to PyIPSA)
   * - AnalysisNR
     - IscAnalysisNR
   * - AnalysisAF
     - IscAnalysisAF
   * - AnalysisUnb
     - (Not mapped to PyIPSA)
   * - AnalysisDCLF
     - (Not mapped to PyIPSA)
   * - AnalysisRel
     - (Not mapped to PyIPSA)
   * - Automation
     - (Not mapped to PyIPSA)
   * - Contingency
     - (Not mapped to PyIPSA)
   * - Study
     - (Not mapped to PyIPSA)
   * - Intertrip
     - IscIntertrip
   * - Network
     - IscNetwork
   * - ResultsDisplayStyle
     - (Not mapped to PyIPSA)
   * - ResultsDisplayLF
     - (Not mapped to PyIPSA)
   * - SQL
     - (Not mapped to PyIPSA)
   * - NetworkCapacity
     - IscNetworkCapacity
   * - DrawTools
     - (Not mapped to PyIPSA)
   * - Staging
     - (Not mapped to PyIPSA)

IscNetComponent Class
----------------------
.. autoclass:: ipsa.IscNetComponent
   :members:
