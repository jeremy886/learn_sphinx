.. meta::
   :description: Describe how to use RestructureText
   :keywords: rst

.. contents::


Tips
########################################


Text formatting
****************************************


Headings
========================================

* # with overline, for parts
* `*` with overline, for chapters
* = for sections
* `-` for subsections
* ^ for subsubsections
* “ for paragraphs


Lists
========================================

Hlist

.. hlist::
    :columns: 3

    * first item
    * second item
    * 3d item
    * 4th item
    * 5th item

Links
========================================

External links
----------------------------------------

This is a paragraph that contains a link to `Google`_.

.. _Google: https://www.google.com/

.. _internal-links:

Internal Links (Cross-referencing)
----------------------------------------


:ref:`reference-guide`

Tables
========================================

Simple table

========  ========  ========
Column A  Column B  Column C
========  ========  ========
row 1A    row 1B    row 1C
row 2A    row 2B    row 2C
========  ========  ========

Grid table

+----------+----------+----------+
| Column A | Column B | Column C |
+==========+==========+==========+
| row 1A   | row 1B   | row 1C   |
+----------+----------+----------+
| row 2A   | row 2B   | row 2C   |
+----------+----------+----------+

CSV table

.. csv-table::
   :header: "Column A", "Column B", "Column C"

   "row 1A", "row 1B", "row 1C"
   "row 2A", "row 2B", "row 2C"


Images
========================================

.. image:: https://openclipart.org/image/400px/191351


Maths
============================================================

Go to :ref:`math-eq`

Terms
========================================

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

Blocks
========================================

Literal Block
----------------------------------------
This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

Doctest  blocks
----------------------------------------

>>> 1 + 1
2


Raw HTML
================================================================================

.. raw:: html

    <h1> This is a HTML H1 heading</h1>
    <hr width=50 size=10>

Structure
********************************************************************************

TOC Tree
================================================================================

`Link <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

::

    .. toctree::

Include text
================================================================================

.. include:: small_note.txt


Meta data
================================================================================

Added but you can see it. It's shown in HTML source.

Example::

    .. meta::
       :http-equiv=Content-Type: text/html; charset=ISO-8859-1


Tags
================================================================================

.. .. only:: <expression>


Configuration
********************************************************************************

`Link <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-exclude_patterns>`_

To explore

*  exclude_patterns



