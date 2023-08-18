#!/usr/bin/env python3
""" A script that returns the list of school having a specific topic"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    ''' function that returns the list of school having a specific topic'''
    return [i for i in mongo_collection.find({"topics": topic})]
