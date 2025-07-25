"""Tests of utility functions."""

import pathlib

import pytest

from clteaching import util

DATADIR = pathlib.Path(__file__).parent / "data"


@pytest.fixture
def example_md():
    """Open example Markdown file and return text."""
    with open(DATADIR / "examples" / "example.md", encoding="utf-8") as f:
        md = f.read()
    return md


@pytest.fixture
def example_md_meta():
    """Example Markdown metadata, raw."""
    return {"title": "A Markdown example"}


@pytest.fixture
def example_html():
    """Example HTML."""
    with open(DATADIR / "examples" / "example.html", encoding="utf-8") as f:
        html = f.read()
    return html


def test_md2html(example_md, example_md_meta, example_html):
    """Test Markdown to HTML conversion."""
    data_meta = util.md2html("example.md", example_md, get_meta=True)
    assert data_meta["meta"] == example_md_meta
    assert data_meta["body"] == example_html
    data_no_meta = util.md2html("example.md", example_md, get_meta=False)
    assert data_no_meta["meta"] is None
    assert data_no_meta["body"] == example_html
