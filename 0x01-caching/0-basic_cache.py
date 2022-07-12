#!/usr/bin/env python3
""" Introducing the caching system """


class BasicCache(BaseCaching):
    def put(self, key, item):
        """ Assign to the dictionary """
        if key or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value from put """
        if key or self.cache_data(key) is None:
            return None
        return self.cache_data.get(key)
