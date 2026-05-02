#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def count_logs(collection):
    """
    Return the total number of logs.
    """
    return collection.count_documents({})


def count_method(collection, method):
    """
    Return the number of documents with a specific method.
    """
    return collection.count_documents({"method": method})


def count_status_checks(collection):
    """
    Return the number of status check documents.
    """
    return collection.count_documents({
        "method": "GET",
        "path": "/status"
    })


if __name__ == "__main__":
    client = MongoClient()
    nginx_collection = client.logs.nginx

    print("{} logs".format(count_logs(nginx_collection)))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            count_method(nginx_collection, method)
        ))

    print("{} status check".format(
        count_status_checks(nginx_collection)
    ))
