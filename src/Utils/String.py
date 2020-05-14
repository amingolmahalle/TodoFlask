def is_string_empty(mystring):
    assert isinstance(mystring, str)

    if len(mystring) == 0:
        return True
    else:
        return False
