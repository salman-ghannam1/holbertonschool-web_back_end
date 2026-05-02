#!/usr/bin/env python3
"""
Module that provides a function to update
school topics in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of all school documents
    matching the given name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): school name to update.
        topics (list): list of topics.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
