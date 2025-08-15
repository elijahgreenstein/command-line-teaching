.. highlight: none

.. _markdown:

Markdown conventions used by the CLT toolkit
============================================================

The Command Line Teaching (CLT) toolkit uses a `Markdown-It-Py Markdown parser <markdown_it_py_>`_ to convert Markdown-formatted text to HTML. The parser is set up with the default ``commonmark`` configuration options, which conform to the `CommonMark <commonmark_>`_ Markdown specification, as well as the extensions discussed below.

Typography
------------------------------------------------------------

The Markdown-It-Py parser used by the CLT toolkit is set up with the typographic components ``smartquotes`` and ``replacements`` enabled. This means, for example, that two dashes ``--`` are converted to a single n-dash character (``&ndash;`` in HTML), and that vertical quotation marks are converted to left and right curved quotation marks. Refer to the `Markdown-It-Py documentation on typographic components <mditpy_typo_>`_ for details.

Tables
------------------------------------------------------------

The core `"tables" package <mditpy_tables_>`_ is enabled. Here is an example table:

.. code-block:: markdown

  | Header 1 | Header 2 |
  | -------- | -------- |
  | Cell 1A  | Cell 2A  |
  | Cell 1B  | Cell 2B  |

For more details, refer to the `GitHub documentation on tables <github_tables_>`_.

Plugin Extensions
------------------------------------------------------------

Several plugins from the separate `Markdown-It-Py Plugin Extensions <mdit_py_plugins_>`_ package are also enabled.

Footnotes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "`Footnotes <mditpyplugins_footnotes_>`_" plugin is enabled. Footnotes can be written as follows:

.. code-block:: markdown

   Statement of fact.[^1]

   [^1]: Footnote with supporting evidence.

Definition lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "`Definition Lists <mditpyplugins_def_>`_" plugin is enabled. Definition lists can be written in two ways:

.. code-block:: markdown

  First term
  : First paragraph of definition.

    Another paragraph.

  Second term
  ~ First paragraph of definition.
  ~ Second paragraph of definition.

Heading anchors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "`Heading Anchors <mditpyplugins_anchors_>`_" plugin is enabled with the maximum level set to the default ``2``. The Markdown-It-Py parser will automatically assign all level-two headings a unique id attribute based on the heading text. For example, the heading below will be rendered into HTML with the id ``a-great-heading``.

.. code-block:: markdown

  ## A Great Heading

.. include:: ../links.rst

