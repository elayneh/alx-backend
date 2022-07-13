#!/bin/usr/env python3
""" FIFO """
from ast import Return
from optparse import Values
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class to do with fifo ptinciple """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assign item to the cache data """
        if item and key:
            ky = self.get(key)
            if ky:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    dellist = list(self.cache_data.keys())[0]
                    del self.cache_data[dellist]
                    print("DISCARD {}", dellist)
            self.cache_data[key] = item

        def get(self, key):
            """
            Return:
                the key Values
            """
            return self.cache_data.get(key)
