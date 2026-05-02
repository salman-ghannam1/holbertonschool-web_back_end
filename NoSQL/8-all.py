#!/usr/bin/env python3
"""
Module that provides a function to list all documents
in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Return a list of all documents in the collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents.
    """
    return list(mongo_collection.find())
