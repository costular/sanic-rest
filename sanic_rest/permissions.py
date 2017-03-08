#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'costular'


class BasePermission(object):
    """
    Base class for permissions
    """

    def has_permission(self, request, view):
        raise NotImplementedError("You must implement `has_permission` method.")


class AllowAny(BasePermission):

    def has_permission(self, request, view):
        return True
