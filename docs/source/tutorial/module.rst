.. highlight:: none

Set up a new module
============================================================

In this part of the tutorial, we will use the CLT toolkit to add a new module to our course.

Add a module
------------------------------------------------------------

Change into the ``CLT101`` directory; then type this command and press ``enter``:

.. code-block:: bash

  clt addmod Week_01

You will now be asked a series of questions:

``> Enter module title:``
  The name of the module as it will appear in Canvas. Type ``Example module`` and press ``enter``.

``> Enter module position:``
  This is the position among the modules on Canvas. Let's assume that we want to keep an information module at the top of our list of modules. ``Week_01`` will, therefore, be our second module. Type ``2`` and press ``enter``.

``> Enter module prefix:``
  The CLT ``addmod`` tool automatically prefixes the title of each item in the module (page, quiz, discussion) with a number. This is our first content module, so type ``1`` and press ``enter``.

``> Enter quiz date:``
  The CLT ``addmod`` tool automatically creates a quiz. Enter the quiz date in the format ``YYYY-MM-DD``. For example, type ``2025-05-01`` and press ``enter``.

The CLT ``addmod`` tool will now create a new directory, ``Week_01``, and several files in it.

File structure
------------------------------------------------------------

Let's explore the files set up in ``CLT101/modules/Week_01``::

  CLT101/
      _conf/
      modules/
          Week_01/
              _conf.yaml
              disc.md
              intro.md
              quiz.yaml

The CLT ``addmod`` tool wrote module settings to ``_conf.yaml``. Refer to the :doc:`guide to module settings <../howto/module>` to learn how to customize these settings.

The CLT ``addmod`` tool also prepared three files for our module content in the following default order:

#. ``intro.md``: an introduction page
#. ``quiz.yaml``: a quiz
#. ``disc.md``: a discussion board

We will edit these files in the :doc:`next tutorial <content>`.

Next steps
------------------------------------------------------------

Now that we have files in our module, we can learn how to add content in the :doc:`next tutorial <content>`. For additional details about how to customize a module, refer to the :doc:`guide to module settings <../howto/module>`.

