#!/usr/bin/env python3
""" A python script that inserts a new document in a collection based on kwargs
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    '''function that inserts a new document in a collection based on kwargs'''
    if not mongo_collection and kwargs:
        return None
    return mongo_collection.insert(kwargs)
