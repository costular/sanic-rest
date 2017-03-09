#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from sanic import views

__author__ = 'costular'


@pytest.fixture
def basic_view():
    class BasicView(views.APIView):

        async def get(self, request):
            return 'Hello'

    return BasicView


class TestAPIView:

    @pytest.mark.asyncio
    async def test_basic_view_get(self, api, basic_view, test_client):
        api.register_view('/testingmyself', basic_view)

        request, response = test_client.get('/testingmyself')
        assert response.status == 200



