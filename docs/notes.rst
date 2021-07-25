Notes
#################################################

Quickstart
****************************************

Infrastructure
========================================

`Docutils <https://docutils.sourceforge.io/docs/ref/rst/directives.html#include>`_

Step
========================================

#. pip install Sphinx
#. sphinx-quickstart
#. sphinx-build -b linkcheck . _build/linkcheck

Tools
****************************************

sphinx-autobuild
========================================

`sphinx-autobuild <https://github.com/executablebooks/sphinx-autobuild>`_

::

    pip install sphinx-autobuild
    # cd to above docs directory
    sphinx-autobuild docs docs/_build/html
    # or
    sphinx-autobuild . _build/html