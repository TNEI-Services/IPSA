IscCIMModelConfiguration
============================

The ``IscCIMModelConfiguration`` class provides access to the configurations used for CIM model import and export. The parameters can be get and set using this class.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscEquivalentBranch Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - ModelType
     - The CIM model type enum.
        - 1 - FullModel
        - 2 - Difference Model (currently unsupported in IPSA)
   * - Integer
     - CIMVersion
     - The CIM version used by the import or export.
        - 1 - CGMES
        - 2 - GB CIM
   * - String
     - FileDirFullPath
     - The path the CIM model is located. For import, this is the path where CIM files will be read from; for export, this is where CIM files will be saved.
   * - String
     - ZipFileFullPath
     - The path the zip file that is the CIM model. For import, the zip file will be the input; for export, the zip file is where CIM model will be saved.
   * - Boolean
     - UseZip
     - Whether the CIM model is in zip. If this is set to True, the ZipFileFullPath will be used to locate the CIM model, instead of the FileDirFullPath.
   * - List[Integer]
     - ProfileSet
     - The profiles used in this model. For import, this is the list of profiles that will be read; for export, this is the list of profiles that will be made from the IPSA model.
     The profiles are indicated by enums and the mappings are as follows:
        - 1 - EQBD
        - 2 - EQ
        - 3 - SC 
        - 4 - GL 
        - 5 - SSH 
        - 6 - TP 
        - 7 - SV 
        - 8 - DL 
        - 9 - DY 
        - 10 - SysCap 
        - 11 - SCR 

        Note that IPSA currently does not support GL and DY, and SysCap and SCR are only supported in GB CIM.
   * - String
     - ModelName
     - The model name string. In import, the model name is set as the network title in Network Properties. In export, this is used as the model name stem for the CIM XML files (the part before the profile name suffix).

   * - Integer
     - UseMode
     - This field indicates whether this CIM model configuration is used for import or export. The value cannot be set.

        - 1 = Import
        - 2 = Export


IscCIMModelConfiguration Class
---------------------------------

.. autoclass:: ipsa.IscCIMModelConfiguration
   :members:
