"""Tests of loader functions."""

import pathlib

from clteaching import objects, loaders, util

from .fixtures import (
    ex_user,
    ex_course,
    ex_module,
    ex_page,
    ex_disc,
    ex_questions,
    ex_quiz,
)

FS = util.FileStructure()
DATADIR = pathlib.Path(__file__).parent / "data"
TEST101 = DATADIR / "TEST101"


def test_load_user(ex_user):
    """Test loading of user."""
    res = loaders.load_user(TEST101 / FS.token)
    assert res.token == ex_user.token
    assert res.auth == ex_user.auth


def test_load_course(ex_course):
    """Test loading of course."""
    res = loaders.load_course(TEST101 / FS.cset, TEST101 / FS.qdesc)
    assert res.uid == ex_course.uid
    assert res.url == ex_course.url
    assert res.disc == ex_course.disc
    assert res.quiz == ex_course.quiz
    assert res.qdesc == ex_course.qdesc
    assert res.get_path() == ex_course.get_path()


def test_load_page(ex_page):
    """Test loading of page."""
    res = loaders.load_page(TEST101 / FS.get_intro("W01"))
    assert res.itype == "Page"
    assert res.path == "pages"
    assert res.body_name == "body"
    assert res.param == "wiki_page"
    assert res.id_name == "url"
    assert res.content_name == "page_url"
    assert res.title == ex_page.title
    assert res.body == ex_page.body


def test_load_disc(ex_disc):
    """Test loading of discussion."""
    course = loaders.load_course(TEST101 / FS.cset)
    discpath = TEST101 / FS.get_disc("W01")
    res = loaders.load_disc(discpath, course)
    assert res.itype == "Discussion"
    assert res.path == "discussion_topics"
    assert res.body_name == "message"
    assert res.param is None
    assert res.id_name == "id"
    assert res.content_name == "content_id"
    assert res.title == ex_disc.title
    assert res.body == ex_disc.body
    assert res.get_settings() == ex_disc.get_settings()


def test_load_quiz(ex_quiz):
    """Test loading of quiz."""
    course = loaders.load_course(TEST101 / FS.cset, TEST101 / FS.qdesc)
    quizpath = TEST101 / FS.get_quiz("W01")
    res = loaders.load_quiz(quizpath, course)
    assert res.itype == "Quiz"
    assert res.path == "quizzes"
    assert res.body_name == "description"
    assert res.param == "quiz"
    assert res.id_name == "id"
    assert res.content_name == "content_id"
    assert res.title == ex_quiz.title
    assert res.body == ex_quiz.body
    assert res.get_settings() == ex_quiz.get_settings()
    assert len(res.questions) == len(ex_quiz.questions)
    for idx, val in enumerate(res.questions):
        res_question = val
        check_question = ex_quiz.questions[idx]
        assert res_question.question == check_question.question
        assert res_question.correct == check_question.correct
        assert res_question.incorrect == check_question.incorrect


def test_load_module(ex_module):
    """Test loading of module and assorted items."""
    course = loaders.load_course(TEST101 / FS.cset)
    moddir = TEST101 / FS.mod / "W01"
    res = loaders.load_module(moddir, FS.mset, course)
    assert res.title == ex_module.title
    assert res.position == ex_module.position
    assert res.path == "modules"
    assert res.uid is None
    assert res.id_name == "id"
    new_id = "123456"
    res.set_id(new_id)
    assert res.uid == new_id
    assert isinstance(res.items[0], objects.Page)
    assert isinstance(res.items[1], objects.Quiz)
    assert isinstance(res.items[2], objects.Discussion)
