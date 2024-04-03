#!/usr/bin/env python3
"""
LFU caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    a class LFUCache that inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """
        initialization
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                min_frequency_keys = [k for k, v in self.frequency.items() if v == min_frequency]

                if len(min_frequency_keys) > 1:
                    lru_key = min_frequency_keys[0]
                    for k in min_frequency_keys:
                        if self.cache_data[k] < self.cache_data[lru_key]:
                            lru_key = k
                else:
                    lru_key = min_frequency_keys[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
                return self.cache_data[key]
        return None
