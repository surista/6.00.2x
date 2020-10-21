#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""

class Food(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return getValue() / getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories)+ '>'


def buildMenu(names, values, calories):
    """ names, values calories lists of same length
    name a list of strings
    values and calories lists of numbers
    returns list of food"""
    menu = [(Food(names[i]), values[i], calories[i]) for i in range(len(values))]
    #
    # for i in range(len(values)):
    #     menu.append(Food(names[i], values[i], calories[i]))

    return menu

def greedy(items, maxCost, keyFunction):
    """assume slist of imte,s maxCost >=0
    keyFunction maps elements of items to numbers"""

    itemsCopy = sorted(items, key = keyFunction, reverse=True)