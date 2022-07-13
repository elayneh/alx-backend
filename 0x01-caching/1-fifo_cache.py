#!/usr/bin/env python3
""" FIFO """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Assign item to  self.cache_data """
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())[0]
                    del self.cache_data[keydel]
                    print("DISCARD: {}".format(keydel))

            self.cache_data[key] = item

    def get(self, key):
        """ Return value of the key """
        returned = self.cache_data.get(key)
        return returned
