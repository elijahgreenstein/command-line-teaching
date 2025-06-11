How to customize quizzes
============================================================

Default quizzes
------------------------------------------------------------

The default quiz created by the CLT ``addmod`` tool is as follows:

.. code-block:: yaml

  title: "1.2. Quiz"
  description: null
  times:
    unlock_at: "2025T123Z"
    due_at: "2025T123Z"
    lock_at: "2025T123Z"
  questions:
    - question: "What is ..."
      correct:
        - "Answer 1"
        - "Answer 2"
      incorrect:
        - "Answer 3"
        - "Answer 4"
    - question: "Write about ..."

As seen above, a CLT quiz requires a ``title``, ``description``, ``times``, and a list of ``questions``. 

Quiz description
------------------------------------------------------------

The CLT ``upmod`` tool will use the default quiz description in ``<COURSE>/_conf/quiz-desc.md`` when ``description`` is set to ``null``.

To add a multi-line description to a quiz, follow the YAML "`literal style <yaml_literal_>`_". Replace ``description: null`` with ``description: |``, then write the custom description below. Each line of the custom description must begin with two spaces.

Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Markdown-formatted description:

.. code-block:: markdown

  # Overview

  This is a unique quiz description.

  - A list
  - of items

Markdown-formatted description as part of a YAML-formatted quiz:

.. code-block:: yaml

  description: |
    # Overview

    This is a unique quiz description.

    - A list
    - of items
  times:

Quiz times
------------------------------------------------------------

CLT quizzes require three times: ``unlock_at``, ``due_at``, and ``lock_at``. Each time must follow the format ``<DATE>T<TIME>Z``. Note the letter ``T`` between the date and time and the letter ``Z`` after the time. The date must follow the format ``YYYY-MM-DD`` (year-month-day) and the time must follow the format ``HH:MM:SS`` (hour:minute:second).

Quiz questions
------------------------------------------------------------

Refer to :ref:`Part 4 of the tutorial <tutorial-content-quizzes>` for details about how to add, remove, and reorder questions.

.. include:: ../links.rst

