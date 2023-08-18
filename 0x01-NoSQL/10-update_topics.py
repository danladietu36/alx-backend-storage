#!/usr/bin/env python3
""" A script that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """ Update Mongo document"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
