#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    Write a function that reads n lines of a text file (UTF8)
    and prints it to stdout.
    """
    with open(filename, mode='r') as myFile:
        if nb_lines <= 0:
            print(myFile.read(), end="")
            return
        linescnt = 0
        for lines in myFile:
            if linescnt < nb_lines:
                print(lines, end="")
            linescnt += 1
