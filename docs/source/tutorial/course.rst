.. highlight:: none

Set up a new course
============================================================

In this part of the tutorial, we will use the CLT command line interface (CLI) to set up a new course: "CLT101 -- Introduction to Command Line Teaching."

Preparation
------------------------------------------------------------

We will need an access token to make API calls to Canvas. Follow the `Canvas instructions <canvas_token_>`_ to generate an access token. We will use the token shortly.

Next, determine the API URL for your institution. The URL should end with the path ``/api/v1``. Be prepared to copy this URL.

Finally, change into a directory to hold your courses.

Create a new course
------------------------------------------------------------

We are now ready to set up a new course. We can access the CLT toolkit with the command ``clt``, followed by the name of a "tool." To create a new course, we use the ``newcourse`` tool followed by the name of a directory. For this tutorial, we will set up our new course in a directory named ``CLT101``. Type the following command and press ``enter``:

.. code-block:: bash

  clt newcourse CLT101

You will now be asked a series of questions:

``> Enter API token``
  Copy the access token that you generated on Canvas, paste it here, and press ``enter``.

``> Enter API URL:``
  Copy the API URL for your institution, paste it here, and press ``enter``.

``> Enter course unique identifier:``
  Open your course on Canvas. The URL will end with the path ``/courses/<UID>``. Find the identifier after ``courses`` (in place of ``<UID>``), copy it, paste it here, and press ``enter``.

``> Enter quiz unlock time:``
  The ``newcourse`` tool will set up a default time to unlock each module quiz. Enter the default unlock time in Coordinated Universal Time (UTC), in the format ``HH:MM:SS``. For example, let's say that we want our quizzes to unlock at 10:00 AM Pacific Daylight Time (PDT). PDT is seven hours behind UTC, so type ``17:00:00`` and press ``enter``.

``> Enter quiz deadline:``
  The ``newcourse`` tool will set up a default deadline for each module quiz. Let's say that we want students to complete the quizzes by 11:00:00 AM PDT, one hour after quizzes unlock. Type ``18:00:00`` and press ``enter``.

``> Enter quiz lock time:``
  Students will not be able to access quizzes after the lock time. Let's give students an extra 30 minutes to submit a late quiz. Type ``18:30:00`` and press ``enter``.

The ``newcourse`` tool will now create a new directory, ``CLT101``, containing several sub-directories and configuration files.

File structure
------------------------------------------------------------

Let's explore the files and directories set up with the ``newcourse`` tool::

  CLT101/
      _conf/
          quiz-desc.md
          settings.yaml
          token
      modules/

The ``_conf`` directory contains our course configuration files. We will edit a few of them to finalize our course set up.

The ``modules`` directory will hold our course modules. We will set up a new module in the :doc:`next tutorial <module>`.

Default quiz description
------------------------------------------------------------

We can edit ``CLT101/_conf/quiz-desc.md`` to prepare a default quiz description. We will format the quiz description following the `CommonMark <commonmark_>`_ Markdown specification. (Refer to the :doc:`Markdown reference <../reference/markdown>` for additional details about the Markdown parser used by the CLT toolkit.) Open ``quiz-desc.md``, delete any text, and add the following::

  ## Overview

  This is an open-book quiz:

  - You **may** refer to course materials and notes.
  - You **may not** ask classmates for help.

  ## Deadline

  Submit your quiz by 11:00 AM.

Notice that we have used a level-two heading for our first heading: ``## Overview``. Level-one ``<h1>`` tags are reserved for webpage titles, so we will use level-two headings for the top-level headings in the body of our content.

Save and close ``quiz-desc.md``. CLT tools will use the above description for each quiz, unless we provide an alternative description. Refer to the :doc:`guide to quizzes <../howto/quiz>` for details about quiz customization.

Token
------------------------------------------------------------

Your Canvas access token was written to ``CLT101/_conf/token``. If your access token changes, you can replace the token in this file.

.. danger::

  Do not make the access token public. Do not use Command Line Teaching on a shared computer where others can access your ``token`` file. If you use Git for version control for your course, add ``token`` to your ``.gitignore`` file.

Next steps
------------------------------------------------------------

Now that we know how to set up a course with the ``newcourse`` tool, we can move on to the :doc:`next tutorial <module>`. For additional details about how to customize your course, refer to the :doc:`guide to course settings <../howto/course>`.

.. include:: ../links.rst

