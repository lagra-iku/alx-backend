#!/usr/bin/env python3
"""
 FIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """
        initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key, _ = next(iter(self.cache_data.items()))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
