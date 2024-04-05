#!/usr/bin/env python3
"""
Simple Pagination
"""

import csv
import math
from typing import List, Dict, Tuple, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        a method named get_page that takes two integer arguments
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Any]:
        """
        a get_hyper method that takes the same arguments
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }


def index_range(page, page_size):
    """
    a func named index_range that takes two int args page and page_size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
