IscAnalysisHM
==============

Field Values
-------------

.. list-table:: **IscAnalysisHM Field Values**
   :widths: 2 5 15
   :class: tight-table
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - HarmonicStudyType
     - Type of harmonic study. Should be one of:

        - 0 = Harmonic voltage penetration
        - 1 = Harmonic voltage waveform
        - 2 = Harmonic impedance scan
   * - Integer
     - FundamentalTHD
     - Use fundamental voltage for THD calculation.
   * - Integer
     - MinimumHarmonicOrder
     - Minimum harmonic order.
   * - Integer
     - MaximumHarmonicOrder
     - Maximum harmonic order.
   * - Integer
     -
        HarmonicWaveformBusbar
        HarmonicWaveformBusbar2
        HarmonicWaveformBusbar3
        HarmonicWaveformBusbar4
        HarmonicWaveformBusbar5
        HarmonicWaveformBusbar6
     - Busbar to produce waveform for. Up to six busbars can be specified.
   * - Integer
     - HarmonicSequence
     - Sequence network to use for harmonics.

        - 0 = Zero sequence impedance used for triplen orders, positive sequence impedances used for all others
        - 1 = Only the positive sequence network impedances are used
        - 2 = Only the zero sequence network impedances are used
   * - Integer
     - HarmonicUseLongLines
     - Global override using long lines.
   * - Integer
     - HarmonicGlobalLineModel
     - Global override line model. One of the following:

        - 0 = Polynomial resistance model
        - 1 = Resistance square root model
        - 2 = Constant X/R model
   * - Integer
     - HarmonicGlobalTransformerModel
     - Global override transformer model. One of the following:

        - 0 = Polynomial resistance mode
        - 1 = Resistance square root model
        - 2 = Constant X/R model
   * - Integer
     - HarmonicGlobalShuntModel
     - Global override shunt model. One of the following:

        - 0 = Use default resistance to give X/R = 2000.0 if no resistance passed
        - 1 = Ideal shunt with no resistance
   * - Integer
     - HarmonicGlobalLoadModel
     - Global override load model. One of the following:

        - 0 = Series RX model
        - 1 = Parallel RX 1 model
        - 2 = Parallel RX 2 model
        - 3 = X plus parallel RX model
   * - Float
     - HarmonicOffNominalFrequencyHz
     - Off-nominal frequency (Hz).
   * - Integer
     - HarmonicOnlyScanResonant
     - Only scan harmonic resonant zones in detail.
   * - Float
     - HarmonicScanStepSizePU
     - Step size for harmonic sensitivity scans (pu).
   * - Integer
     - HarmonicPlotVoltageType
     - Plot the harmonic voltage as it varies with harmonic order. Should be one of:

        - 0 = Plot voltage waveform
        - 1 = Plot harmonic voltages as a bar chart
   * - Integer
     - HarmonicPlotImpedanceType
     - Plot the harmonic impedance as it varies with harmonic order. Should be one of:

        - 0 = Z - Plot the total impedance.
        - 1 = R - Plot the resistance.
        - 2 = X - Plot the reactance.
   * - Boolean
     - HarmonicPlotSeparateFundamental
     - If this option is selected then the fundamental waveform will be plotted separately from the harmonics waveform. If this option is not selected then the waveforms will be superimposed.
   * - Boolean
     - HarmonicPlotZ
     - If this option is ``True`` then the harmonic impedance Z will be plotted.
   * - Boolean
     - HarmonicPlotR
     - If this option is ``True`` then the harmonic resistance waveform will be plotted.
   * - Boolean
     - HarmonicPlotX
     - If this option is ``True`` then the harmonic reactance waveform will be plotted.
   * - Boolean
     - HarmonicPlotUseLogarithmic
     - If this option is ``True`` then plot axes will be logarithmic.
   * - Boolean
     - HarmonicPlotUseFrequency
     - If this option is ``True`` then the harmonics impedance will be plotted against frequency in Hertz, else it will be plotted against the harmonic order.
   * - Boolean
     - HarmonicPlotUseOhms
     - If this option is ``True`` then the impedance plot will be in per unit ohms on the system base, else it will be in actual Ohms.

IscAnalysisHM Class
--------------------

.. autoclass:: ipsa.IscAnalysisHM
   :members:
