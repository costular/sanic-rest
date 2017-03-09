#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from sanic import Sanic
from sanic_rest import SanicRest

__author__ = 'costular'


@pytest.fixture
def app():
    return Sanic(__name__)


@pytest.fixture
def api(app):
    return SanicRest(app)


@pytest.fixture
def test_client(app):
    return app.test_client
