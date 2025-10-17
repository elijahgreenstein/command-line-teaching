Explanation
============================================================

This page provides an overview of the background and assumptions that shaped the development of the CLT toolkit.

Background
------------------------------------------------------------

A basic predecessor of Command Line Teaching was developed by Elijah Greenstein while he was teaching university courses either remotely or in a hybrid format between 2020 and 2024. The tool was intended to facilitate teaching in an online environment by simplifying the process of uploading materials to the learning management system (`Canvas LMS <canvas_lms_>`_).

In 2025, the Python library was reorganized and packaged as "Command Line Teaching" for use by other instructors.

Assumptions and Goals
------------------------------------------------------------

Remote teaching tends to require instructors to rely on written materials to communicate course expectations, deadlines, content, and other information more than is the case for in-person teaching. This is particularly true for asynchronous learning. In an in-person setting, instructors can orally communicate the day's lesson plan and expectations, and they are available on site to direct (and redirect) students to tasks and learning activities. In contrast, in remote (and possibly asynchronous) settings, instructors rely more on course pages containing written instructions to provide instruction to students.

In an online setting, learning materials must therefore be organized such that students (who have other courses, obligations, and commitments) can quickly understand their tasks for a given day, week, or term, and efficiently access the materials required to accomplish those tasks.

Organizing Principles
------------------------------------------------------------

Command Line Teaching was developed under two organizing principles to accomplish the above goals:

**Modularity**
  Course materials should be organized into separate, meaningful modules. "Meaningful" means that instructors make deliberate decisions based on a clear logic about how to divide a course into units. Each module should be roughly comparable in scope.

  For example, a term might be organized into week-long modules, each organized around a specific theme. In each module, students engage with content focused on a common set of issues for a set amount of time.

**Consistency**
  The format and organization of learning materials should be consistent. This means that each module contains materials organized in a consistent order with a consistent appearance.

  For example, each module might begin with a page that lists tasks and deadlines, proceed to a quiz, and end with a writing activity.

**Modular** course design means that students can focus on a constrained set of tasks and content within a given time frame. **Consistent** course design means that students know where to look for information every time they engage with a module, and they become familiar with the steps required to complete each module.

The "Command Line Teaching" Approach
------------------------------------------------------------

Command Line Teaching is set up to simplify the creation of learning materials that satisfy the above principles.

The :ref:`cli-commands-clt-newcourse` command establishes a number of course settings, such as default quiz unlock and lock times, that facilitate **consistency** across course modules.

The :ref:`cli-commands-clt-addmod` command makes it simple to create new **modules** with a **consistent**, default set of course files (introduction page, quiz, and discussion board).

Writing in :ref:`Markdown <markdown>` leaves decision about style to the Canvas LMS, which ensures a **consistent** appearance. Every section heading, for example, appears the same.

The :ref:`cli-commands-clt-upmod` command requires users to prepare a complete **module** before uploading it to Canvas all at once (rather than in bits and pieces). This fosters deliberate decision-making about what to include in each **module**.

.. |clt-newcourse| replace:: ``clt newcourse``

.. include:: ../links.rst
