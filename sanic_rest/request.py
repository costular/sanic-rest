#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'costular'


DEFAULT_HTTP_CONTENT_TYPE = "application/octet-stream"


class Request(object):
    """
    Wrapper of request class
    """

    def __init__(self, request):
        self.request = request

    @property
    def content_type(self):
        return self.request.headers.get('Content-Type', DEFAULT_HTTP_CONTENT_TYPE)

    @property
    def query_params(self):
        return self.request.args()

    @property
    def json(self):
        return self.request.json()

    @property
    def post(self):
        return self.request.form()

    @property
    def files(self):
        return self.request.files()
