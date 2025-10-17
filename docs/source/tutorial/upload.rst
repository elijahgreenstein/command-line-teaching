.. highlight:: none

Upload materials to Canvas
============================================================

In this final part of the tutorial, we will use the CLT toolkit to upload our teaching materials to Canvas LMS.

The upload tool
------------------------------------------------------------

Module upload is simple with the CLT ``upmod`` tool. Make sure that ``CLT101`` is the current working directory; then type this command and press ``enter``:

.. code-block:: bash

  clt -v upmod Week_01

We used the "verbose" option ``-v`` to make the ``upmod`` tool print messages about the upload process. If all settings are configured correctly, the following should print to the terminal:

.. code-block::

  Uploading module: 'Week_01'
  - Posting module ...
      - Status: 200
  - Posting item '1.1. Welcome to "CLT"!' ...
      - Status: 200
  - Posting item '1.2. Quiz' ...
      - Status: 200
  - Posting item '1.3. Discussion' ...
      - Status: 200
  - Moving item '1.1. Welcome to "CLT"!' ...
      - Status: 200
  - Moving item '1.2. Quiz' ...
      - Status: 200
  - Moving item '1.3. Discussion' ...
      - Status: 200
  - Adding questions to '1.2. Quiz' ...
      - Status: 200
      - Status: 200
      - Status: 200
  - Updating points for '1.2. Quiz' ...
      - Status: 200

Note the steps in the process:

* the ``upmod`` tool posts (creates) the module,
* the tool posts each module item (introduction page, quiz, and discussion),
* the tool moves each item to the new module,
* the tool adds questions to the quiz, and
* finally, the tool updates the quiz points.

.. note::

  A status code of ``200`` indicates success. Any other status code indicates a problem and a failure to post, move, or update the listed item.

  If an API request fails, first try a test run to identify possible issues. Replicate the command above but type ``-t`` before ``upmod``. Content for the expected API call will print to the terminal.

  If the problem is still unclear, replicate the above command but replace ``-v`` with ``-vv`` for additional messages. Each API response will print to the terminal.

Next steps
------------------------------------------------------------

Content uploads are as simple as that! For additional customization, refer to the :doc:`how-to guides <../navigation/howto>`:

* :doc:`../howto/course`
* :doc:`../howto/module`
* :doc:`../howto/quiz`

