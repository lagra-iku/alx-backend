#!/usr/bin/env python3
"""
LRU caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    a class LRUCache that inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """
        initialization
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            else:
                if key in self.cache_data:
                    self.access_order.remove(key)
                self.access_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            if key in self.cache_data:
                self.access_order.remove(key)
                self.access_order.append(key)
                return self.cache_data[key]
