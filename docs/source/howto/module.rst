.. highlight:: none

How to customize module settings
============================================================

This guide shows you how to customize the organization of files in your module.

Setup
------------------------------------------------------------

Set up a new module with the ``addmod`` tool (replace ``<MODULE>`` with the module directory name):

.. code-block:: bash

  clt addmod <MODULE>

Answer the questions; the ``addmod`` tool will create the files listed under ``<MODULE>``:

.. code-block::

  <COURSE>/
      modules/
          <MODULE>/
              _conf.py
              disc.md
              intro.md
              quiz.yaml

Default settings
------------------------------------------------------------

The ``addmod`` tool sets up the default module settings in ``<MODULE>/_conf.py``. Default settings appear as below, where ``<USER>`` represents user replies to ``addmod`` prompts:

.. code-block:: yaml

  module_name: "<MODULE>"
  title: "<USER>"
  position: <USER>
  item_order:
    - [intro.md, page]
    - [quiz.yaml, quiz]
    - [disc.md, disc]

Default module files
------------------------------------------------------------

By default, the ``addmod`` tool creates three files for course content:

#. ``intro.md``: an introduction page
#. ``quiz.yaml``: a quiz
#. ``disc.md``: a discussion board


Remove an item
------------------------------------------------------------

The CLT ``upmod`` tool will only upload files named in the list under ``item_order``. To remove an item from the module, delete the corresponding line.

Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

  item_order:
    - [intro.md, page]
    - [disc.md, disc]

With the above settings, the ``upmod`` tool will only upload the introduction page and discussion board prompt. The ``upmod`` tool will ignore all other files in ``modules/<MODULE>``.

Reorder the items
------------------------------------------------------------

The ``upmod`` tool will order the content on Canvas in the order the files appear under ``item_order``. Reorder the list before any upload to Canvas to determine the order of items uploaded with ``upmod``.

.. code-block:: yaml

  item_order:
    - [disc.md, disc]
    - [quiz.yaml, quiz]
    - [intro.md, page]

With the above settings, the ``upmod`` tool will order the items in the module as follows: first a discussion board, then a quiz, last a page.

.. note::

  The ``addmod`` tool prefixes the title of each default item with a numeric code that follows the default order. Edit the title in each file to correspond to the new order. For example, change ``1.3. Discussion`` to ``1.1. Discussion``. Alternatively, remove the prefix: ``Discussion``.

Add items
------------------------------------------------------------

The ``upmod`` tool will upload all files in ``modules/<MODULE>`` listed under ``item_order``. To add a new file, add an entry to the list. Write the entry with the form ``- [<FILE_NAME>, <ITEM_TYPE>``.

Write the file name in ``modules/<MODULE>`` in place of ``<FILE_NAME>``. Write the type of the item in place of ``<ITEM_TYPE>``. The CLT toolkit supports three item types: ``page``, ``quiz``, or ``disc`` (discussion).

Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

  item_order:
    - [welcome.md, page]
    - [notes.md, page]
    - [discussion.md, disc]
    - [check.yaml, quiz]
    - [thoughts.md, disc]
    - [review.yaml, quiz]
    - [handout.md, page]

With the above settings, the ``upmod`` tool will upload three pages, two discussions, and two quizzes to Canvas with the ``upmod`` command. Note that the names of the files do not correspond to the default names (``intro.md``, ``quiz.yaml``, and ``disc.md``). The ``upmod`` tool can upload files with any name, as long as (1) the file appears under ``item_order``, (2) the type of the file follows the file name, and (3) the file exists in ``modules/<MODULE>``.


