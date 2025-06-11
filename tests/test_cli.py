"""Test CLI."""

import pathlib

import pytest
import yaml

from clteaching import objects, cli, util

from .fixtures import (
    ex_user,
    ex_course,
    ex_module,
)


FS = util.FileStructure()
DATADIR = pathlib.Path(__file__).parent / "data"
TEST101 = DATADIR / "TEST101"


@pytest.fixture
def ex_resp():
    """Example test run response from cli.upmod."""
    with open(DATADIR / "examples" / "example-resp.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f.read())
    return data


def test_load_mod(ex_user, ex_course, ex_module):
    """Test loading of user, course, and module."""
    cpath = TEST101
    mpath = TEST101 / FS.mod / "W01"
    user, course, mod = cli.load_mod(cpath, mpath)
    assert user.token == ex_user.token
    assert course.cname == ex_course.cname
    assert mod.mname == ex_module.mname


def test_upload_seq(ex_resp):
    """Test example response from cli.upmod."""
    cpath = TEST101
    mpath = TEST101 / FS.mod / "W01"
    user, course, mod = cli.load_mod(cpath, mpath)
    resp = cli.upload_seq(user, course, mod, 0, test=True)
    assert resp == ex_resp
