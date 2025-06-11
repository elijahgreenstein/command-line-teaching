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
    return 'title: "A Markdown example"'


@pytest.fixture
def example_md_body(example_md):
    """Example Markdown body."""
    lines = example_md.split("\n")
    body = "\n".join(lines[3:]).strip()
    return body


@pytest.fixture
def example_html():
    """Example HTML."""
    with open(DATADIR / "examples" / "example.html", encoding="utf-8") as f:
        html = f.read()
    return html


def test_split_yaml_body(example_md, example_md_meta, example_md_body):
    """Test function to split YAML metadata block from body text."""
    meta, body = util.split_yaml_body("example.md", example_md)
    assert meta == example_md_meta
    assert body == example_md_body


def test_md2html(example_md, example_html):
    """Test Markdown to HTML conversion."""
    _, body = util.split_yaml_body("example.md", example_md)
    assert util.md2html(body) == example_html
