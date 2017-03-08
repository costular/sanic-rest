#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

from sanic.views import HTTPMethodView
from sanic_rest.request import Request
from sanic_rest import exceptions


__author__ = 'costular'


class APIView(HTTPMethodView):

    permissions = ()
    authentication = None

    def get_permissions(self):
        return [permission() for permission in self.permissions]

    def check_permissions(self, request):
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                raise exceptions.PermissionDenied()

    def check_before_request(self, request):
        self.check_permissions(request)

    def dispatch_request(self, request, *args, **kwargs):
        request = Request(request)
        view = getattr(self, request.method.lower(), None)

        if not asyncio.iscoroutinefunction(view):
            raise TypeError("Methods must puy `async` before def reserved word. Like this -> async def my_method()")

        self.check_before_request(request)
        return view(request, *args, **kwargs)
