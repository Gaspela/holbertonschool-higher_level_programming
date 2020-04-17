#!/usr/bin/python3
# Takes in a URL, sends a request and
# Displays the value of the X-Request-Id variable found.
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        data = response.info()
    print(dict(data).get("X-Request-Id"))
