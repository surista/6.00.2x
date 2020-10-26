#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
              combo.append(items[j])
        yield combo

myItems = [1,2,3]
powerSet(myItems)

# def yieldAllCombos(items):
#     """
#       Generates all combinations of N items into two bags, whereby each
#       item is in one or zero bags.
#
#       Yields a tuple, (bag1, bag2), where each bag is represented as
#       a list of which item(s) are in each bag.
#     """
#     bag1, bag2 = [], []
#     for i in items:
