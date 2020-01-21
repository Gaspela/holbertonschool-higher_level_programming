#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    1.Returns TRUE if the object is an instance of, 
    or if the object is an instance of a class that inherited from, 
    the specified class. 
    2. Otherwise Faslse.
    """
    return isinstance(obj, a_class)
