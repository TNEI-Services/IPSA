Using Python with IPSA
=======================

Background
-----------
Python is a high level, general-purpose programming language. It has a simple syntax and programmes written in Python can run on many different platforms. The main features of Python include:

•	**Interpreted:** Code is processed by the interpreter at runtime, saving you the task of compiling and linking it.
•	**Dynamically typed:** There is no need for variable or argument declarations.
•	**Object Orientated:** Supports for user-defined classes and inheritance.
•	**Interactive:** Python contains an interactive prompt which is useful for testing short pieces of code.
•	**Automatic Memory Management:** Python handles memory management automatically, freeing you from the need to think about allocating and freeing memory in your code.
•	**Easy to use and quick to develop code:** Because it is a high-level language with an elegant syntax Python is easy to learn and the built-in data types and features such as lists and dictionaries enable quick code development.
•	**Mature:** Python is a mature, stable and well-documented language.
•	**Extendable:** New modules can be added in a compiled language such as C++ or C. Python programming interfaces can be incorporated into applications (e.g. IPSA).
•	**Interface and Existing Toolboxes:** Many useful modules already exist that can be freely downloaded, for example, to enable interaction with Microsoft Office programmes like Excel. Toolboxes are available that allow the creation of graphical user interfaces. Libraries like SciPy, NumPy and Matplotlib allow python to be used effectively within the scientific community.
•	**Free:** Python is available under an open source license and is free to both download and include in an application.

Python is a versatile programming language for power system engineers as they can clearly coordinate instructions for their analysis software, especially for computationally intensive tasks. For example, embedding power systems software with additional economical analysis data requires iterative and recursive tool design. 
IPSA 2 contains application programming interfaces to Python making Python a good choice to automate analysis using power systems analysis software. 
 
If you're interested in finding out about more sophisticated tools and applications of IPSA with embedding Python, please contact the Solutions team at `support@ipsa-power.com`_.

.. _support@ipsa-power.com: mailto:support@ipsa-power.com

Configuration
--------------
This guide provides a full reference to IPSA objects and their methods that are exposed through the Python API. Our Python engine API is referred to as PyIPSA. All Python scripts run through IPSA internally benefit from IPSA's internal Python interpreter.

PyIPSA 2.10.3 uses Python 3.11 and we only offer a 64 bit application as of 2023. Note that since Python developed Python 3.9, embedded C applications have to be constructed for Python with the version that is required for users. 
Therefore if you use an alternative version of Python 3, the PyIPSA 2.10.3 installation will not work. 
Please contact `support@ipsa-power.com`_ if there are serious problems with this configuration.

.. _support@ipsa-power.com: mailto:support@ipsa-power.com