#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    """
    Write a function that creates
    an Object from a “JSON file”.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.loads(myFile.read())
