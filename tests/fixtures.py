"""Fixtures for tests."""

import pathlib

import pytest
import yaml

from clteaching import objects

DATADIR = pathlib.Path(__file__).parent / "data"
TEST101 = DATADIR / "TEST101"


@pytest.fixture
def ex_user():
    """Example user."""
    return objects.User("12345ABCDE")


@pytest.fixture
def ex_course():
    """Example course, with settings and default quiz description."""
    with open(TEST101 / "_conf" / "settings.yaml", encoding="utf-8") as f:
        settings = yaml.safe_load(f.read())
    with open(DATADIR / "examples" / "example-qdesc.html", encoding="utf-8") as f:
        qdesc = f.read()
    return objects.Course(settings, qdesc)


@pytest.fixture
def ex_module():
    """Example module."""
    return objects.Module("A test module", 3, "W01")


@pytest.fixture
def ex_page():
    """Example page."""
    return objects.Page(
        "1.1. Introduction",
        '<h2 id="overview">Overview</h2>\n<p>This is a test module.</p>\n',
    )


@pytest.fixture
def ex_disc():
    """Example discussion."""
    with open(DATADIR / "examples" / "example-disc.html", encoding="utf-8") as f:
        body = f.read()
    settings = {
        "discussion_type": "threaded",
        "published": False,
    }
    return objects.Discussion("1.3. Discussion", body, settings)


@pytest.fixture
def ex_questions():
    """Example quiz questions."""
    q1 = objects.QuizQuestion(
        "What are the correct answers?",
        correct=["Answer 1", "Answer 2"],
        incorrect=["Answer 3", "Answer 4"],
    )
    q2 = objects.QuizQuestion("Write about a test case.")
    return (q1, q2)


@pytest.fixture
def ex_quiz(ex_questions):
    """Example quiz."""
    with open(TEST101 / "_conf" / "settings.yaml", encoding="utf-8") as f:
        cset = yaml.safe_load(f.read())
    with open(TEST101 / "modules" / "W01" / "quiz.yaml", encoding="utf-8") as f:
        quiz = yaml.safe_load(f.read())
    with open(DATADIR / "examples" / "example-qdesc.html", encoding="utf-8") as f:
        qdesc = f.read()
    title = quiz["title"]
    body = qdesc
    settings = cset["quiz"]
    settings.update(quiz["times"])
    return objects.Quiz(title, body, settings, ex_questions)
