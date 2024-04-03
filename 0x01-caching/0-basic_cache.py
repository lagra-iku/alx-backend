#!/usr/bin/env python3
"""
Basic Dictionary
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a class BasicCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        initialization
        """
        super().__init__()

    def put(self, key, item):
        """

        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """

        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
