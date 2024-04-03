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
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.access_order:
                self.access_order.append(key)
            else:
                self.access_order.append(
                    self.access_order.pop(self.access_order.index(key)))
            if len(self.access_order) > BaseCaching.MAX_ITEMS:
                discard = self.access_order.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is not None:
            if key in self.cache_data:
                # Update access order
                self.access_order.remove(key)
                self.access_order.append(key)
                return self.cache_data[key]
        return None
