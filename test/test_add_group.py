# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.appolication import Application


@pytest.fixture
def app (request):
    fixture = Application ()
    request.addfinalizer (fixture. destroy)
    return fixture


def test_add_group(app):
    app.session.login( username = "admin", password = "secret")
    app.creat_group(Group(name = "test1", header = "reew", footer = "fdsf"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username = "admin", password = "secret")
    app.creat_group(Group(name = "", header = "", footer = ""))
    app.session.logout()
