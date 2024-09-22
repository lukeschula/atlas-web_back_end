#!/usr/bin/env python3
'''task 3'''

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Inherits from base class'''

    def __init__(self):
        '''Super Class'''
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        '''Store item in cache_data'''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usage_order.remove[key]
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lru_key = self.usage_order.pop(0)
                    del self.cache_data[lru_key]
                    print(f"DISCARD: {lru_key}")
                self.cache_data[key] = item
                self.usage_order.append(key)

    def get(self, key):
        '''Return value,
        move key to end,
        return none if key
        is none'''

        if key is None or key not in self.cache_data:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]