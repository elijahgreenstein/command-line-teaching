"""Utility functions."""

import pathlib

from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.anchors import anchors_plugin
import yaml


class FileStructure:
    """Representation course and module file structures."""

    course = pathlib.Path("_conf")
    mod = pathlib.Path("modules")
    cset = course / "settings.yaml"
    qdesc = course / "quiz-desc.md"
    token = course / "token"
    mset = "_conf.yaml"
    intro = "intro.md"
    quiz = "quiz.yaml"
    disc = "disc.md"

    def get_mset(self, modname):
        "Get path to module settings." ""
        return self.mod / modname / self.mset

    def get_intro(self, modname):
        "Get path to module default introduction page."
        return self.mod / modname / self.intro

    def get_quiz(self, modname):
        "Get path to module default quiz."
        return self.mod / modname / self.quiz

    def get_disc(self, modname):
        "Get path to module default discussion."
        return self.mod / modname / self.disc


class UserInput:
    """Representation of prompts for user input."""

    course_prompts = {
        "token": "> Enter API token: ",
        "course_url": "> Enter API URL: ",
        "course_id": "> Enter course unique identifier: ",
        "unlock_at": "> Enter quiz unlock time: ",
        "due_at": "> Enter quiz deadline: ",
        "lock_at": "> Enter quiz lock time: ",
    }
    mod_prompts = {
        "title": "> Enter module title: ",
        "position": "> Enter module position: ",
        "prefix": "> Enter module prefix: ",
        "date": "> Enter quiz date: ",
    }

    course_conf = None
    mod_conf = None

    def __init__(self, name):
        self.name = name

    def get_course_input(self):
        """Get user input for course configuration settings."""
        self.course_conf = {}
        for key, val in self.course_prompts.items():
            self.course_conf[key] = input(val)
        self.course_conf["course_name"] = self.name

    def get_mod_input(self):
        """Get user input for module configuration settings."""
        self.mod_conf = {}
        for key, val in self.mod_prompts.items():
            self.mod_conf[key] = input(val)
        self.mod_conf["module_name"] = self.name

    def add_mod_conf(self, new_conf):
        """Add configuration settings to module settings."""
        self.mod_conf.update(new_conf)


class Logger:
    """Log messages at different levels of verbosity."""

    def __init__(self, verbosity):
        self.verbosity = verbosity
        self.msgs = {
            "newcourse": "Creating new course: '{course}'",
            "addmod": "Adding a module: '{mod}'",
            "upmod": "Uploading module: '{mod}'",
            "create_dir": "- Creating directories:",
            "create_files": "- Creating files from templates:",
            "create": "    - {name}",
            "upmod_mod": "- Posting module ...",
            "upmod_item": "- Posting item '{item}' ...",
            "upmod_move": "- Moving item '{item}' ...",
            "status": "    - Status: {status}",
            "details": "    - Details: {resp}",
            "upmod_add_qst": "- Adding question to '{item}' ...",
            "upmod_update_pts": "- Updating points for '{item}' ...",
        }

    def log(self, level, message):
        """Print message if verbosity level is sufficiently high."""
        if self.verbosity >= level:
            print(message)
        else:
            pass

    def set_verbosity(self, new_verb):
        """Update the verbosity level."""
        self.verbosity = new_verb


def md2html(text):
    """Convert Markdown to HTML."""
    md = (
        MarkdownIt("commonmark", {"typographer": True})
        .enable(["replacements", "smartquotes", "table"])
        .use(footnote_plugin)
        .use(deflist_plugin)
        .use(anchors_plugin)
    )
    return md.render(text)


def split_yaml_body(fname, text):
    """Split YAML metadata block from body text of Markdown file."""
    lines = text.strip().split("\n")
    complete_yaml = False
    meta = []
    if lines[0] == "---":
        idx = 1
        while idx < len(lines):
            if lines[idx] == "---":
                complete_yaml = True
                break
            meta.append(lines[idx])
            idx += 1
        if complete_yaml:
            meta = "\n".join(meta)
            body = "\n".join(lines[idx + 1 :])
            return meta.strip(), body.strip()
        raise ValueError(f"{fname} does not contain a complete YAML metadata block.")
    raise ValueError(f"{fname} does not begin with a YAML metadata block.")


def load_yaml(file):
    """Load a YAML file."""
    with open(file, encoding="utf-8") as f:
        text = f.read()
    return yaml.safe_load(text)
