# Command Line Teaching

Command Line Teaching (CLT) is a Python library that enables instructors to develop course materials quickly and upload them to [Canvas LMS by Instructure](https://www.instructure.com/canvas) through API calls---all from the command line.

Refer to the CLT documentation for detailed instructions. Basic usage described below.

## Installation

CLT requires an installation of [Python](https://www.python.org). First install Python; then use the command below to install the CLT Python package with `pip`:

```
pip install git+https://github.com/elijahgreenstein/command-line-teaching.git
```

`pip` will also install the following dependencies:

- `jinja2` ([Jinja](https://jinja.palletsprojects.com/en/stable/))
- `markdown-it-py` ([markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/using.html))
- `mdit_py_plugins` ([Markdown-It-Py Plugin Extensions](https://mdit-py-plugins.readthedocs.io/en/latest/))
- `pyyaml` ([PyYAML](https://pyyaml.org))
- `requests` ([Requests](https://docs.python-requests.org/en/latest/index.html))

## Command line interface

We can access the CLT toolkit with the `clt` command followed by the name of a "tool."

To set up a new course, navigate to a directory of your choice. Then use the `newcourse` tool as follows:

```
clt newcourse TEST101
```

Answer the questions that follow to set up a new course in `TEST101`. To set up a new module in your course, change into the `TEST101` directory and use the `addmod` tool:

```
cd TEST101
clt addmod Week01
```

Answer the questions and the `addmod` tool will create a directory with default files: introduction page, quiz, and discussion board. Edit the files in `TEST101/Week01` (`intro.md`, `quiz.yaml`, and `disc.md`) to add your course content.

To upload the contents of a module to Canvas, use the `upmod` tool:

```
clt upmod Week01
```

The `upmod` tool will create a new module in Canvas, convert the content in `TEST101/Week01` to HTML, and upload that content to Canvas. It's that simple.

