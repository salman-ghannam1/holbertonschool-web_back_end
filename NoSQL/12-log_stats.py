#!/usr/bin/env python3
"""
Script that provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def print_method_stats(collection, method):
    """
    Print the number of logs for one HTTP method.
    """
    count = collection.count_documents({"method": method})
    print("\tmethod {}: {}".format(method, count))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    print_method_stats(collection, "GET")
    print_method_stats(collection, "POST")
    print_method_stats(collection, "PUT")
    print_method_stats(collection, "PATCH")
    print_method_stats(collection, "DELETE")

    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print("{} status check".format(status_count))
