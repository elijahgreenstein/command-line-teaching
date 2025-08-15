.. _cli-commands-clt-newcourse:

``clt newcourse``
============================================================

Summary
------------------------------------------------------------

Set up a new course in a directory.

Usage
------------------------------------------------------------

.. code-block:: console

   $ clt newcourse <directory>

Examples
------------------------------------------------------------

.. code-block:: console

   $ clt newcourse MATH101

Details
------------------------------------------------------------

CLT prompts the user for basic course information: API token, API URL, course unique identifier, default quiz times (unlock, deadline, and lock).

CLT then creates the named directory, a subdirectory for configuration files, a subdirectory for modules, and several configuration files: basic settings, a file containing the API token, and a default quiz description.

