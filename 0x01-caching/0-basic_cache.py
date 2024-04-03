#!/usr/bin/env python3
"""
Basic Dictionary
"""
from base_caching import BaseCaching


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
        if key is not None and item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
