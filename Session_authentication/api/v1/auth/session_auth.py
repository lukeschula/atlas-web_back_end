#!/usr/bin/env python3
""" Task 1 - Session Auth """

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Task 2 - Create a Session """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for user_id """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Task 3 - Returns a User ID based on Session ID """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None

        user_id = SessionAuth.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """ Task 6 - Identifying User """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Task 8 - Logout """
        if request is None:
            return False

        cookie = self.session_cookie(request)
        if cookie is None:
            return False

        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return False

        del SessionAuth.user_id_by_session_id[cookie]
        return True