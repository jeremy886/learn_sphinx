.. contents::

Directives
################################################################################


Developing directives
********************************************************************************

* :doc:`sphinx:development/index`

Third Party Directives
********************************************************************************


Education
================================================================================

* :github:`executablebooks/sphinx-exercise`

Show time
********************************************************************************

Many directives
--------------------------------------------------------------------------------

how how to use then `include` and `math` directive



.. math::

  α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)


.. seealso:: This is a simple **seealso** note.



.. topic:: Your Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.


Substitution
----------------------------------------

I have to write a long text here. |longtext|

.. |longtext| replace:: This is a very very long text to include that can be very useful.

Comments
----------------------------------------

You cannot see comments.

.. This line will not be rendered.

..
   You can have multiline comments, by adding indented text blocks.
   This line will not be rendered.

   This is still a comment.

Admonition
----------------------------------------

.. attention:: complete your homework

.. caution:: get a good grade is the key

.. danger:: risk here

.. error:: when adding fractions, it's incorrect to just add the numerators and the denominators.

.. hint:: when adding fractions, make the denominators the same.

.. important:: what is the difference between fractions and ratios.

.. note::  This is a **note** box.

.. tip::
   Careful! Don't go overtime!

.. warning:: note the space between the directive and the text

.. tip:: Study everyday

.. admonition:: VSCode

    what is this?


Include external content
----------------------------------------

.. literalinclude:: conf.py
    :language: python
    :lines: 1, 3-5



Cross Reference
----------------------------------------

a reference can be used like :ref:`internal-links`

.. _reference-guide:

Reference Guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a reference use .. _reference:
#. Link to the reference anywhere using :ref:
