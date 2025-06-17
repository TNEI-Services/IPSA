IscDrawTools
================

The IscDrawTools class provides access to settings used when running the PolyDraw or TreeDraw algorithms.

Field Values
-------------

.. tabularcolumns:: |\Y{0.15}|\Y{0.25}|\Y{0.6}|
.. list-table:: **IscDrawTools Field Values**
   :widths: 2 5 15
   :class: tight-table, longtable
   :header-rows: 1

   * - Type
     - Field Name
     - Description
   * - Integer
     - DrawAlgorithm
     - The chosen algorithm to use:

        - 0 = PolyDraw
        - 1 = TreeDraw
   * - Integer
     - PolyDrawBusbarType
     - The style of drawn busbars in the PolyDraw algorithm:

        - 0 = Horizontal
        - 1 = Vertical
        - 2 = Junction
        - 3 = Circular
        - 4 = Haxagonal
   * - Integer
     - PolyDrawBusbarSize
     - The size of drawn busbars in the PolyDraw algorithm.
   * - Double
     - PolyDrawStartingX
     - The starting X position for the PolyDraw algorithm. This is recommended to be larger than 100.
   * - Double
     - PolyDrawStartingY
     - The starting Y position for the PolyDraw algorithm. This is recommended to be larger than 100.
   * - Double
     - PolyDrawGridSize
     - The island grid size used in the PolyDraw algorithm. This is recommended to be larger than 200.
   * - Double
     - PolyDrawIslandSeparation
     - The island separation used in the PolyDraw algorithm. This is recommended to be larger than 0.
   * - Double
     - PolyDrawEnlargementConst
     - The enlargement constant used in the PolyDraw algorithm. This is recommended to be larger than 0.
   * - Integer
     - TreeDrawInitialBusbarUID
     - The UID of the starting busbar for the TreeDraw algorithm. If unset this will return -1.
   * - Integer
     - TreeDrawBusbarType
     - The style of drawn busbars in the TreeDraw algorithm:

        - 0 = Horizontal
        - 1 = Vertical
        - 2 = Junction
        - 3 = Circular
        - 4 = Haxagonal
   * - Integer
     - TreeDrawBusbarSize
     - The size of drawn busbars in the TreeDraw algorithm.
   * - Double
     - TreeDrawStartingX
     - The starting X position for the TreeDraw algorithm. This is recommended to be larger than 100.
   * - Double
     - TreeDrawStartingY
     - The starting Y position for the TreeDraw algorithm. This is recommended to be larger than 100.
   * - Integer
     - TreeDrawOrder
     - The number of drawn busbar levels in the TreeDraw algorithm.
   * - Boolean
     - TreeDrawUnlimited
     - If True, the TreeDraw algorithm will draw all reachable busbars.
   * - Boolean
     - TreeDrawShowProgMsgs
     - If True, the TreeDraw algorithm will show a detailed report of the drawing process.
   * - Boolean
     - TreeDrawRedrawAll
     - If True, the TreeDraw algorithm will remove all items from the diagram, and redraw items according to the algorithm.
            If False, it will only draw undrawn connected sections from the starting busbar.
   * - Boolean
     - DrawIncludeLoads
     - If True, connected loads will be drawn by both algorithms, otherwise they will be ignored.
   * - Boolean
     - DrawIncludeGens
     - If True, connected synchronous machines will be drawn by both algorithms, otherwise they will be ignored.
   * - Boolean
     - DrawIncludeInfeeds
     - If True, connected infeeds will be drawn by both algorithms, otherwise they will be ignored.
   * - Boolean
     - DrawIncludeIMs
     - If True, connected induction machines will be drawn by both algorithms, otherwise they will be ignored.
   * - Boolean
     - DrawIncludeOtherRadials
     - If True, all other connected radials will be drawn by both algorithms, otherwise they will be ignored.
   * - Boolean
     - DrawIncludeBreakers
     - If True, circuit breakers on drawn branch items will be drawn by both algorithms, otherwise they will be ignored.
   * - Boolean
     - DrawIncludeProtContainers
     - If True, protection containers on drawn branch items will be drawn by both algorithms, otherwise they will be ignored.
   * - Boolean
     - DrawIncludeOtherInlines
     - If True, all other inlines on drawn branch items will be drawn by both algorithms, otherwise they will be ignored.
	
IscDrawTools Class
-----------------

.. autoclass:: ipsa.IscDrawTools
   :members:
