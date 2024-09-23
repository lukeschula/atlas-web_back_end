#!/usr/bin/env python3
''' Helper Function Module '''


def index_range(page: int, page_size: int) -> tuple:
    '''return a tuple of size two'''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
