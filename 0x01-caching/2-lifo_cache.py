#!/usr/bin/env python3
"""
LIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    a class LIFOCache that inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """
        initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
