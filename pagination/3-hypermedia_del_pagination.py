#!/usr/bin/env python3
'''Deletion-resilient hypermedia pagination'''

import csv
import math
from typing import List, Dict


class Server:
    '''Server class to paginate a database of popular baby names.'''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset'''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        '''Dataset indexed by sorting position'''
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Returns dictionary with values:'''
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.indexed_dataset()
        total = len(dataset)
        last_index = total - 1
        if index is None:
            index = 0
            return {
                "index": None,
                "next_index": None,
                "page_size": page_size,
                "data": []
            }
        next_index = min(index + page_size, last_index + 1)
        data = [dataset.get(i, []) for i in range(index, next_index)]
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data