#!/usr/bin/env python3
'''BasicCache module'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache class inherits from BaseCaching and provides simple'''

    def put(self, key, item):
        '''If key &item is not none set key to item'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Return item linked to key from cache_data '''

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
