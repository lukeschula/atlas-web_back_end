#!/usr/bin/env python3
'''MRU caching'''
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''Inherits from Base Class'''
    def __init__(self):
        '''Super class'''
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        '''Assign key to dict if = None.'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = next(reversed(self.order))
            del self.cache_data[discard]
            print(f'DISCARD: {discard}')
        self.cache_data[key] = item
        self.order[key] = True

    def get(self, key):
        '''Return the value'''
        if key is None or key not in self.cache_data:
            return None
        self.order.move_to_end(key)
        return self.cache_data[key]
