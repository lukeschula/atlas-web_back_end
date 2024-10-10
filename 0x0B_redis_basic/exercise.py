#!/usr/bin/env python3
'''Module Documentation'''
import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Decorator to count calls to method'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''Stores the histor of inputs and outputs'''
    input_key = f'{method.__qualname__}:inputs'
    output_key = f'{method.__qualname__}:outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable):
    '''Retrieving lists'''
    redis = method.__self__._redis
    input_key = f'{method.__qualname__}:inputs'
    output_key = f'{method.__qualname__}:outputs'
    inputs = redis.lrange(input_key, 0, -1)
    outputs = redis.lrange(output_key, 0, -1)
    print(f'{method.__qualname__} was called {len(inputs)} times:')
    for input, output in zip(inputs, outputs):
        print(f'{method.__qualname__}(*{input.decode("utf-8")})\
              -> {output.decode("utf-8")}')


class Cache:
    '''Cache class documentation'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Generates a random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)  # stores data in redis using generated key
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        '''Retrieve data from redis'''
        data = self._redis.get(key)
        if key is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        '''Decode bytes to str'''
        return self.get(key, lambda k: k.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        '''Decode bytes to int'''
        return self.get(key, lambda k: int(k))

    def increment(self, key: str) -> int:
        '''Increment the value'''
        return self._redis.incr(key)
