#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import  List, Tuple

zz = [100 - i for i in range(100)]


def bubblesort(array: List[int]) -> List[int]:
    n = len(array)

    while n > 0:
        sorted = False
        for j in range(1, n):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                sorted = True
        n -= 1
        if sorted is False:
            return array
    return array




