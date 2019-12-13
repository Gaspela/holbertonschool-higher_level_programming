#!/usr/bin/python3
from dynamic import argv


def principal():
    res = 0
    for i in range(1, len(argv)):
        res += int(argv[i])
    print(sum)

if __name__ == "__main__":
    principal()
