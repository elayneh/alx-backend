#!/usr/bin/env python3
"""  Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class that inherits from the BaseCaching """

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return linked value """
        if key or self.cache_data.get[key] is None:
            return None
        return self.cache_data.get[key]
