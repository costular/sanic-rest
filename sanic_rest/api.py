#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'costular'


class API(object):

    def __init__(self, app):
        if app:
            self.app = app

    def init_app(self, app):
        self.app = app

    def register_view(self, view, urls=(), *args, **kwargs):
        if not self.app:
            self.throw_app_none()
        self._register_view(self.app, view, urls)

    def _register_view(self, app, view, urls=(), *args, **kwargs):
        view_func = view.as_view()

        if len(urls) < 1:
            raise ValueError("You must give one valid URL at least.")

        for url in urls:
            self.app.add_route(view_func, url)

    def throw_app_none(self):
        raise ValueError("`app` must be a valid Sanic instance")
