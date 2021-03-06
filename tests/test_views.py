#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic_rest import views
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


@pytest.fixture
def basic_view():
    class BasicView(views.APIView):

        async def get(self, request):
            return 'Hello'

    return BasicView


class TestAPIView:

    @pytest.mark.asyncio
    def test_basic_view_get(self, api, basic_view, test_client):
        api.register_view('/testingmyself', basic_view)

        request, response = test_client.get('/testingmyself')
        assert response.status == 200



