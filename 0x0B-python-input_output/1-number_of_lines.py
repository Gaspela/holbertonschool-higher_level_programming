#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    Write a function that returns the
    number of lines of a text file.
    """
    with open(filename, encoding="utf-8") as myFile:

        linescnt = 0

        for line in myFile:
            linescnt += 1

        return linescnt
