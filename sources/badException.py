#! /usr/bin/python

from sys import stdin, argv, stderr, exit

# Error manager
class BadException(Exception):
    def __init__(self, message, errors = "BadException"):
        super().__init__(message)
        self.errors = errors