#!/usr/bin/env python3
"""
Module that provides a function to insert
a document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: fields of the document to insert.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
