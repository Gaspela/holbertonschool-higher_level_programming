#!/usr/bin/python3
class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """prints the list"""
        print(sorted(self))
