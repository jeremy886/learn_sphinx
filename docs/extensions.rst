Extensions
########################################

Demonstration
********************************************************************************

.. toctree::
    :maxdepth: 3

    quiz

Built-in extensions
********************************************************************************

Add to conf.py::

    extensions = []

sphinx.ext.extlinks – Markup to shorten external links
================================================================================

Add to conf.py::

    extlinks = {'issue': ('https://github.com/sphinx-doc/sphinx/issues/%s', 'issue %s')}


sphinx.ext.autodoc – Include documentation from docstrings
================================================================================

In conf.py add::

    import os
    import sys
    sys.path.insert(0, os.path.abspath(".."))
    # 0 is the beginning
    # relative path to docs

sphinx.ext.intersphinx – Link to other projects’ documentation
================================================================================

`Intersphinx <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_

Add to conf.py::

    # intersphinx mapping
    intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

sphinx.ext.graphviz – Add Graphviz graphs
================================================================================

Install::

    scoop install graphviz
    dot -c
    pip install graphviz

.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }

.. graph:: foo

   "bar" -- "baz";

Clickable

.. graphviz::

     digraph example {
         a [label="sphinx", href="https://www.sphinx-doc.org", target="_top"];
         b [label="other"];
         a -> b;
     }

sphinx.ext.todo – Support for todo items
================================================================================

.. todo::
    - 🟩 Mercury
    - ✅ Venus


Third Party Extensions
****************************************

Text Utility
================================================================================

sphinx-copybutton
--------------------------------------------------------------------------------

Install::

    pip install sphinx-copybutton

Add to conf.py::

    extensions = [
    ...
    "sphinx_copybutton",
    ...
    ]


Embed
================================================================================

* https://github.com/shomah4a/sphinxcontrib.youtube

Diagram
================================================================================

* https://github.com/mgaitan/sphinxcontrib-mermaid
* https://github.com/Modelmat/sphinxcontrib-drawio
* https://github.com/blockdiag/sphinxcontrib-blockdiag
* https://github.com/clearlinux-pkgs/sphinxcontrib-blockdiag

Support Python Code
================================================================================
* https://github.com/ydcjeff/sphinxcontrib-playground
* https://github.com/sphinx-gallery/sphinx-gallery

Links References Indices
================================================================================
* https://pypi.org/project/toctree-plus/
* https://github.com/executablebooks/sphinx-external-toc
* https://github.com/haschdl/sphinx-tagtoctree

Changing Content Programmatically
================================================================================

* https://github.com/NextThought/sphinxcontrib-programoutput
* https://github.com/sphinx-contrib/datatemplates

Maths Support
================================================================================

write LaTeX math using `$$`
--------------------------------------------------------------------------------

* :github:`sympy/sphinx-math-dollar`

Install::

    pip install sphinx-math-dollar

* https://github.com/hagenw/sphinxcontrib-katex
* https://github.com/divi255/sphinxcontrib.asciinema

Edit conf.py::

    extensions = ['sphinx_math_dollar', 'sphinx.ext.mathjax']

    mathjax_config = {
        'tex2jax': {
            'inlineMath': [ ["\\(", "\\)"] ],
            'displayMath': [["\\[", "\\]"] ],
        },
    }


Fix::

    WARNING: mathjax_config/mathjax2_config does not work for the current MathJax version, use mathjax3_config instead


Issues

.. warning::

    quizdown stops working

Classroom
================================================================================

* https://github.com/bonartm/sphinxcontrib-quizdown

.. attention:: Consider just use Python's `Quizdown <https://github.com/jjfiv/quizdown>`_

Install::

    pip install git+git://github.com/bonartm/sphinxcontrib-quizdown

Setup::

    extensions = [
        ...,
        "sphinxcontrib.quizdown",
        ...
    ]


* https://github.com/coderefinery/sphinx-lesson

Easy editing
================================================================================

* https://github.com/sphinx-contrib/emojicodes

Publishing
================================================================================

* https://github.com/clearlinux-pkgs/sphinxcontrib-newsfeed

Parser Tools - Docutils
================================================================================

* https://github.com/executablebooks/MyST-Parser/blob/master/myst_parser/directives.py

Others
================================================================================

* https://github.com/useblocks/sphinxcontrib-needs

Github
********************************************************************************

Automation
================================================================================

* https://github.com/ammaraskar/sphinx-action