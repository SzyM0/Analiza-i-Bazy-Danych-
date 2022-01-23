#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import random
from bubble import bubblesort


testdata = [[10 - i for i in range(10)],
            [random.randint(0, 100) for i in range(100)],
            [random.randint(-100, 100) for i in range(100)]]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    actual = bubblesort(sample)
    expected = sorted(sample)

    assert  all([a == b for a, b in zip(actual, expected)])