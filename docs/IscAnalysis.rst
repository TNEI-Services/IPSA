IscAnalysis
============

There are separate classes for each analysis type, e.g. load flow, fault level and harmonic analysis.
The ``IscNetwork`` class provides functions to obtain an ``IscAnalysis`` instance for each analysis type,
for example ``GetAnalysisLF()`` returns an ``IscAnalysisLF`` object.
Motor start analysis options are provided under the fault level analysis class.

Analysis classes
-----------------

.. toctree::

    IscAnalysisLF
    IscAnalysisFL
    IscAnalysisHM
    IscAnalysisDCLF
    IscAnalysisAF