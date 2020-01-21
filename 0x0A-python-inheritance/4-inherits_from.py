#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    1. Returns TRUE if the object is an instance of a class that 
    inherited (directly or indirectly) from the specified class.
    2. 
    """
    return isinstance(obj, a_class) and not type(obj) == a_class
