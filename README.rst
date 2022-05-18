Read the Docs for PyIPSA
=========================

Project enabling the User to use the scripting manual in a html format.

How to run it
--------------

    1. Select the Run/Run... option from the menu
    2. Select Edit configurations
        a. Click Add new configuration and choose shell script
        b. Change the script PATH to: C:\Users\{USERNAME}\{PATH_TO_PyIPSA}\PyIPSA\docs\make.bat
        c. Change the script options to: html
        d. Change the Working directory to: C:/Users/{USERNAME}/{PATH_TO_PyIPSA}/PyIPSA
        e. Press apply, then close the window by pressing OK.
        f. Press run.
        g. If errors are appearing, write the commands given below in the Terminal:
            - pip install sphinx
            - pip install sphinx-rtd-theme

To look for the html version go to docs/build/html and open index.html

Files
------

All classes and functions documentation are stored in ipsa.py.

In docs/source reside all rst files containing the data that sphinx and read the docs need to convert the manual into html file.