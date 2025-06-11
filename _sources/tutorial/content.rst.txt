.. highlight:: none

Prepare module content
============================================================

In this tutorial, we will add content to the files created by the ``addmod`` tool.

.. _introduction-page:

Introduction page
------------------------------------------------------------

Open ``intro.md``. It should contain the following text:

.. code-block::

  ---
  title: "1.1. Introduction"
  ---

As you can see, the file contains `YAML-formatted <yaml_>`_ metadata between the lines containing three hyphens (``---``). The title for the page must appear here. Notice that the CLT ``addmod`` tool provided a default title with a prefix, ``1.1.``. This communicates that the introduction is the first item in the first content module. Let's edit our title and add some content as follows:

.. code-block::

  ---
  title: "1.1. Welcome to \"CLT\"!"
  ---

  # Welcome to CLT 101!

  This week we will learn about Command Line Teaching.

Recall that we used the `CommonMark <commonmark_>`_ Markdown syntax when we drafted the default quiz description in :doc:`Part 2 of the tutorial <course>`. We must also follow this Markdown syntax to format course pages and :ref:`discussion board prompts <discussion-boards>`. Refer to the :doc:`Markdown reference <../markdown>` for additional details about the Markdown parser used by the CLT toolkit.

.. note::

  Notice that we have placed the title text inside quotation marks and that we have escaped quotation marks that are part of the text (``\"CLT\"``). Enclose all titles in quotation marks to ensure that CLT tools parse the text correctly.

Save and close the file.

.. _tutorial-content-quizzes:

Quizzes
------------------------------------------------------------

Open ``quiz.yaml``. It should contain this `YAML-formatted <yaml_>`_ text:

.. code-block:: yaml

  title: "1.2. Quiz"
  description: null
  times:
    unlock_at: "2025-05-01T17:00:00Z"
    due_at: "2025-05-01T18:00:00Z"
    lock_at: "2025-05-01T18:30:00Z"
  questions:
    - question: "What is ..."
      correct:
        - "Answer 1"
        - "Answer 2"
      incorrect:
        - "Answer 3"
        - "Answer 4"
    - question: "Write about ..."

Notice that the title, ``1.2. Quiz``, indicates that this is the second item in the first content module.

Quiz settings
------------------------------------------------------------

Recall that we set default unlock times, deadlines, and lock times for quizzes when we created our course with the ``newcourse`` tool in the :doc:`second tutorial <course>`. Notice that the CLT ``addmod`` tool combined those times with our quiz date, ``2025-05-01``, to create date-time strings that the Canvas API can parse.

Additionally notice that the quiz ``description`` is set to ``null``. The CLT toolkit will, therefore, use the default quiz description in ``CLT101/_conf/quiz-desc.md`` when we upload the quiz to Canvas in the :doc:`next tutorial <upload>`. Refer to the :doc:`guide to quizzes <../howto/quiz>` to learn how to customize the quiz description for an individual quiz.

Quiz questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default quiz template contains two questions. Note the structure of each question:

- Each question follows the ``questions:`` line.
- Each question begins with ``- question:``, which is offset by two spaces.
- Question text is enclosed in quotation marks and follows ``- question:``.

CLT tools can handle three kinds of questions:

- Questions without answers are treated as *essay questions*. The second question in the template is an essay question.
- Questions with only one correct answer are treated as *multiple choice questions*. The template above does not contain a multiple choice question.
- Questions with more than one correct answer are treated as *multiple answers questions*. The first question in the template is a multiple answers question.

Notice that answers are divided into two groups: ``correct`` and ``incorrect``. Both of these words are preceded by four spaces to align with the word ``question`` and both are followed by a colon ``:`` character.

Answers follow either ``correct`` or ``incorrect``. Each answer text is preceded by six spaces, a hyphen ``-``, and another space. Each answer is enclosed in quotation marks.

Let's add some questions to our quiz. We will first add a multiple choice question. Remove the text beneath ``questions:`` and add the following:

.. code-block:: yaml

  questions:
    - question: "Which tool creates a module?"
      correct:
        - "addmod"
      incorrect:
        - "newcourse"
        - "upmod"

This question has only one correct answer; it will be treated as a multiple choice question.

Now let's add a multiple answers question and an essay question:

.. code-block:: yaml

  questions:
    - question: "Which tool creates a module?"
      correct:
        - "addmod"
      incorrect:
        - "newcourse"
        - "upmod"
    - question: "What are the default module items?"
      correct:
        - "pages"
        - "quizzes"
        - "discussions"
      incorrect:
        - "assignments"
    - question: "What do you like about the CLT tools?"

The second question has three correct answers; it will bee treated as a multiple answers question. The final question does not have answers listed; it will be treated as an essay question.

Save and close the file.

.. _discussion-boards:

Discussion boards
------------------------------------------------------------

Finally, let's update our discussion board. Open ``disc.md``. It should contain this text:

.. code-block::

  ---
  title: "1.3. Discussion"
  ---

Notice that the discussion also begins with `YAML-formatted <yaml_>`_ metadata and that the title indicates that this is the third item in the first content module.

As with the :ref:`introduction page <introduction-page>`, we can add Markdown-formatted text to this file below the metadata:

.. code-block::

  ---
  title: "1.3. Discussion"
  ---

  # Overview

  Discuss:

  1. how to create a new course with CLT; and
  1. how to add a module to your course.

Save and close the file.

Next steps
------------------------------------------------------------

Now that our module has some content, we can upload it to Canvas in the :doc:`next tutorial <upload>`.

.. include:: ../links.rst


