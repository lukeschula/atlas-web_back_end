#!/usr/bin/env python3
'''Password Encryption Module'''

import typing
import bcrypt


def hash_password(password: str) -> bytes:
    '''Returns a hashed, salted password'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Validates hashed password '''
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False