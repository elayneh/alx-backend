#!/usr/bin/env python3
""" FIFO cache management policy in python """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class tha inherits from the BaseCaching and do some thing """

    def __init__(self):
        super().__init__()
        self.lkey = ''

    def put(self, key, item):
        """ Assign self.cache_data to item """
        if item and key is not None:
            self.cache_data[key] = item
            if len(self.cache_data >= BaseCaching.MAX_ITEMS):
                print("DISCARD {}".format(self.lkey))
                self.cache_data.pop(self.lkey)
            self.lkey = key

    def get(self, key):
        """ Returns linked value """
        if key and self.cache_data.get(key):
            return self.cache_data[key]
        else:
            return None
