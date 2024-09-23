#!/usr/bin/env python3
""" Task 3 - Auth Class """

import os
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authorization Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Defines which routes require authorization """

        if not excluded_paths:
            return True

        if path is None or excluded_paths is None:
            return True

        if path in excluded_paths:
            return False

        new_path = path.rstrip("/")

        new_paths = [path.rstrip("/") for path in excluded_paths]

        if new_path in new_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns None - Requests """
        if request is None:
            return None

        header = request.headers.get("Authorization")

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None - Requests """

        return None

    def session_cookie(self, request=None):
        """ Task 4 - Session Cookies """
        if request is None:
            return None
        _my_session_id = os.getenv("SESSION_NAME")
        return request.cookies.get(_my_session_id)