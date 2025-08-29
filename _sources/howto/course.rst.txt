.. highlight:: none

How to customize course settings
============================================================

Setup
------------------------------------------------------------

Use the ``newcourse`` tool to create a new course:

.. code-block:: bash

   clt newcourse <NAME>

Answer the questions. After the ``newcourse`` tool creates course files, open ``<NAME>/_conf/settings.yam``.

Default settings
------------------------------------------------------------

The default settings are shown below, where ``<USER>`` represents user responses to the ``newcourse`` prompts:

.. code-block:: yaml

  course:
    course_name: "<NAME>"
    course_id: "<USER>"
    course_url: <USER>
  discussion:
    discussion_type: threaded
    published: false
  quiz:
    hide_results: always
    quiz_type: assignment
    shuffle_answers: true
  times:
    unlock_at: "<USER>"
    due_at: "<USER>"
    lock_at: "<USER>"

Change discussion settings
------------------------------------------------------------

Default settings for discussion boards follow ``discussion``. The `Canvas API documentation <canvas_api_>`_ provides details about other options for "`Discussion Topics <canvas_api_disc_>`_." Follow `YAML <yaml_>`_ syntax to add other parameters.

Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

  discussion:
    discussion_type: threaded
    published: false
    require_initial_post: true
    sort_order: asc

With these settings, the CLT ``upmod`` tool will upload discussions that

#. are "threaded,"
#. remain unpublished after upload (instructors will need to publish them manually on Canvas),
#. require students to make a post before viewing other posts, and
#. are sorted in "ascending" order.

.. note::

  Boolean options take values ``true`` or ``false``. One-word strings do not need to be placed in quotation marks (``string``). Strings with punctuation should be placed in quotation marks (``"string: punctuation"``) to ensure correct parsing.

Change quiz settings
------------------------------------------------------------

Default quiz settings follow ``quiz``. The `Canvas API documentation <canvas_api_>`_ provides details about other options for "`Quizzes <canvas_api_quiz_>`_." Follow `YAML <yaml_>`_ syntax to add other parameters.

Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

  quiz:
    hide_results: always
    quiz_type: practice_quiz
    shuffle_answers: true
    time_limit: 5
    one_question_at_a_time: true

With these settings, the CLT ``upmod`` tool will upload quizzes that

#. hide results,
#. are practice quizzes rather than assignments,
#. shuffle answers,
#. impose a five-minute time limit,
#. and require students to answer questions one at a time.

Change quiz times
------------------------------------------------------------

Edit the times following ``unlock_at``, ``due_at``, and ``lock_at`` to change the default quiz times.

.. note::

   This may be necessary during a term due to changes to/from daylight savings time.

.. include:: ../links.rst

