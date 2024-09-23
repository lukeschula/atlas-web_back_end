#!/usr/bin/env python3
'''Module doc hash password'''
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    '''Hashes password'''
    byte_repr = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=15)
    return bcrypt.hashpw(byte_repr, salt)


def _generate_uuid() -> str:
    '''Str representation of the new uuid'''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Register user'''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            passwd = _hash_password(password)
            new_usr = self._db.add_user(email, passwd)
            return new_usr

    def valid_login(self, email: str, password: str) -> bool:
        '''Checks if valid login'''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        '''returns the session id'''
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''Finds user by session id'''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''Destroy session'''
        self._db.update_user(user_id=user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        '''Generate reset password token'''
        try:
            user = self._db.find_user_by(email=email)
            user.reset_token = _generate_uuid()
            return user.reset_token
        except NoResultFound:
            raise ValueError('No user found')

    def update_password(self, reset_token: str, password: str) -> None:
        '''Update password'''
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            user.hashed_password = _hash_password(password)
            user.reset_token = None
        except NoResultFound:
            raise ValueError('No user found')
