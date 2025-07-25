"""Functions to load settings and content from files."""

import pathlib

from clteaching import objects, util


def load_user(token_path):
    """Load a user."""
    with open(token_path, encoding="utf-8") as f:
        user = objects.User(f.read().strip())
    return user


def load_course(cset, qdesc=None):
    """Load a course from a settings file and optional, default quiz description."""
    settings = util.load_yaml(cset)
    if qdesc:
        with open(qdesc, encoding="utf-8") as f:
            quiz_desc = util.md2html(qdesc, f.read(), get_meta=False)["body"]
        course = objects.Course(settings, quiz_desc)
    else:
        course = objects.Course(settings)
    return course


def load_page(pagepath):
    """Load a page from a Markdown file."""
    with open(pagepath, encoding="utf-8") as f:
        text = f.read()
    data = util.md2html(pagepath, text)
    title = data["meta"]["title"]
    body = data["body"]
    return objects.Page(title, body)


def load_disc(discpath, course):
    """Load a discussion from a Markdown file."""
    with open(discpath, encoding="utf-8") as f:
        text = f.read()
    data = util.md2html(discpath, text)
    title = data["meta"]["title"]
    body = data["body"]
    return objects.Discussion(title, body, course.disc)


def load_quiz(quizpath, course):
    """Load a quiz from a YAML file."""
    quiz = util.load_yaml(quizpath)
    title = quiz["title"]
    if quiz["description"]:
        body = util.md2html(quizpath, quiz["description"], get_meta=False)["body"]
    else:
        body = course.qdesc
    settings = course.quiz
    settings.update(quiz["times"])
    questions = []
    for qst in quiz["questions"]:
        qtext = qst["question"]
        qcor = qst["correct"] if "correct" in qst else None
        qinc = qst["incorrect"] if "incorrect" in qst else None
        qq = objects.QuizQuestion(qtext, qcor, qinc)
        questions.append(qq)
    return objects.Quiz(title, body, settings, questions)


def load_module(mod_dir, mset, course):
    """Load a module from a course configuration YAML file and module YAML file."""
    func = {
        "page": load_page,
        "quiz": load_quiz,
        "disc": load_disc,
    }
    mdir = pathlib.Path(mod_dir)
    mset = util.load_yaml(mdir / mset)
    items = []
    for item in mset["item_order"]:
        load_func = func[item[1]]
        if item[1] == "page":
            items.append(load_func(mdir / item[0]))
        else:
            items.append(load_func(mdir / item[0], course))
    mod = objects.Module(mset["title"], mset["position"], mset["module_name"], items)
    return mod
