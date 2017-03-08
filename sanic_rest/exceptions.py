#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic_rest import status

__author__ = 'costular'


class BaseAPIException(Exception):
    """
    Base class for Sanic Rest exceptions
    """
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Internal Error'

    def __init__(self, status_code=None, message=None):
        if status_code:
            self.status_code = status_code

        if message:
            self.message = message

    def __str__(self):
        return '[{}] {}'.format(self.status_code, self.message)


class PermissionDenied(BaseAPIException):
    status_code = status.HTTP_403_FORBIDDEN


class NotFound(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND


class EntityTooLarge(BaseAPIException):
    status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE


class BadRequest(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST


class Unauthorized(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
