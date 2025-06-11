"""Representations of users, courses, modules, and module items."""

import pathlib
import urllib

import requests


# Give up requests after TIMEOUT seconds
TIMEOUT = 60


class User:
    """Representation of a user."""

    def __init__(self, token, courses=None):
        self.token = token
        self.auth = {"Authorization": f"Bearer {token}"}
        self.courses = courses

    def add_course(self, course):
        """Add a course to the user course dictionary."""
        if self.courses:
            self.courses[course.cname] = course
        else:
            self.courses = {course.cname: course}

    def create(self, course, item, test=False):
        """Create an item in the specified course."""
        path = course.get_path() / item.path
        url = course.url._replace(path=str(path)).geturl()
        iset = item.get_settings()
        if test:
            item.set_id("TEST_ID")
            return {"TEST_CREATE": {"URL": url, "-H": self.auth, "json": iset}}
        resp = requests.post(url, headers=self.auth, json=iset, timeout=TIMEOUT)
        item.set_id(resp.json()[item.id_name])
        return resp

    def move(self, course, module, item, pos, test=False):
        """Move an item in the specified course to a specific module."""
        path = course.get_path() / module.path / str(module.uid) / "items"
        url = course.url._replace(path=str(path)).geturl()
        params = {
            "module_item": {
                "type": item.itype,
                "position": pos,
                item.content_name: item.uid,
            }
        }
        if test:
            return {"TEST_MOVE": {"URL": url, "-H": self.auth, "json": params}}
        resp = requests.post(url, headers=self.auth, json=params, timeout=TIMEOUT)
        return resp

    def add_quiz_questions(self, course, quiz, test=False):
        """Add a question to a quiz in the specified course."""
        path = course.get_path() / quiz.path / str(quiz.uid) / "questions"
        url = course.url._replace(path=str(path)).geturl()
        resps = []
        for question in quiz.questions:
            params = question.get_json()
            if test:
                resps.append(
                    {"TEST_ADD_QUESTION": {"URL": url, "-H": self.auth, "json": params}}
                )
            else:
                resp = requests.post(
                    url, headers=self.auth, json=params, timeout=TIMEOUT
                )
                resps.append(resp)
        return resps

    def update_quiz_pts(self, course, quiz, test=False):
        """Update the points of a quiz in the specified course."""
        path = course.get_path() / quiz.path / str(quiz.uid)
        url = course.url._replace(path=str(path)).geturl()
        params = {"quiz": {"points_possible": len(quiz.questions)}}
        if test:
            return {"TEST_UPDATE_PTS": {"URL": url, "-H": self.auth, "json": params}}
        resp = requests.put(url, headers=self.auth, json=params, timeout=TIMEOUT)
        return resp


class Course:
    """Representation of a course."""

    modules = None

    def __init__(self, settings, qdesc=None):
        self.cname = settings["course"]["course_name"]
        self.uid = settings["course"]["course_id"]
        self.url = urllib.parse.urlparse(settings["course"]["course_url"])
        self.disc = settings["discussion"]
        self.quiz = settings["quiz"]
        self.qdesc = qdesc

    def add_mod(self, mod):
        """Add a module to the course dictionary of modules."""
        if self.modules:
            self.modules[mod.mname] = mod
        else:
            self.modules = {mod.mname: mod}

    def get_path(self):
        """Get the URL path as a pathlib.Path object."""
        return pathlib.Path(self.url.path) / "courses" / self.uid


class Module:
    """Representation of a module."""

    path = "modules"
    uid = None
    id_name = "id"

    def __init__(self, title, position, mname, items=None):
        self.title = title
        self.position = position
        self.mname = mname
        self.items = items

    def get_settings(self):
        """Get the module settings for API calls."""
        return {"module": {"name": self.title, "position": self.position}}

    def set_id(self, uid):
        """Set the unique identifier of the module."""
        self.uid = uid

    def add_item(self, item):
        """Add an item to the module."""
        if self.items:
            self.items.append(item)
        else:
            self.items = [item]


class Item:
    """Generic class for a item in a module."""

    settings = None
    param = None
    body_name = None
    uid = None

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def set_id(self, uid):
        """Set the unique identifier of the item."""
        self.uid = uid

    def get_settings(self):
        """Get the item settings for API calls."""
        settings = self.settings if self.settings else {}
        settings["title"] = self.title
        settings[self.body_name] = self.body
        settings = {self.param: settings} if self.param else settings
        return settings


class Page(Item):
    """Representation of a page."""

    itype = "Page"
    path = "pages"
    body_name = "body"
    param = "wiki_page"
    id_name = "url"
    content_name = "page_url"


class Discussion(Item):
    """Representation of a discussion board."""

    itype = "Discussion"
    path = "discussion_topics"
    body_name = "message"
    id_name = "id"
    content_name = "content_id"

    def __init__(self, title, body, settings):
        super().__init__(title, body)
        self.settings = settings


class Quiz(Item):
    """Representation of a quiz."""

    itype = "Quiz"
    path = "quizzes"
    body_name = "description"
    param = "quiz"
    id_name = "id"
    content_name = "content_id"

    def __init__(self, title, body, settings, questions):
        super().__init__(title, body)
        self.settings = settings
        self.questions = questions


class QuizQuestion:
    """Representation of a quiz question."""

    def __init__(self, question, correct=None, incorrect=None):
        self.question = question
        self.correct = correct
        self.incorrect = incorrect
        if not correct and not incorrect:
            self.type = "essay_question"
        elif len(correct) > 1:
            self.type = "multiple_answers_question"
        else:
            self.type = "multiple_choice_question"

    def get_json(self):
        """Get question JSON for API calls."""
        res = {
            "question_name": "Question",
            "question_type": self.type,
            "points_possible": 1,
            "question_text": self.question,
        }
        answers = []
        if self.correct:
            for answer in self.correct:
                answers.append({"answer_text": answer, "answer_weight": 100.0})
        if self.incorrect:
            for answer in self.incorrect:
                answers.append({"answer_text": answer, "answer_weight": 0.0})
        if answers:
            res["answers"] = answers
        else:
            pass
        return {"question": res}
