#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic_rest import views


__author__ = 'costular'


class BasicView(views.APIView):

    def get(self):
        return 'Hello'



