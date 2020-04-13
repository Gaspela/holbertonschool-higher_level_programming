#!/usr/bin/python3
# Function that finds a peak in a list of unsorted integers.


def find_peak(list_of_integers):

    """finds a peak in an unsorted list of integers"""
    num = list_of_integers
    if num != []:
        num.sort()
        return num[-1]
    else:
        return None
