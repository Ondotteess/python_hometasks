import functools

def deprecated(func=None, since=None, will_be_removed=None):
    
    if func is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)
    
    def inner(*args, **kwargs):

        if since: first = f"Warning: {func.__name__} is deprecated since version {since}."
        else: first = f"Warning: {func.__name__} is deprecated."

        if will_be_removed: second = f" It will be renoved in version {will_be_removed}."
        else: second = " It will be renoved in future versions."

        print(first + second)

        return func(*args, **kwargs)

    return inner

@deprecated
def sumy(a, b):
    return a+b

@deprecated(since="1.5.2")
def _sumy(first, *args):
    ret = first
    for x in args:
        ret+=x
    return ret

@deprecated(since="0.0.0", will_be_removed="0.0.1")
def two():
    return 2

print(sumy(1, 2), end='\n\n')                               #  Warning: sumy is deprecated. It will be removed in future versions.                        3
print(_sumy('p', 'y' ,'t', 'h', 'o', 'n'), end='\n\n')      #  Warning: _sumy is deprecated since version 1.5.2. It will be removed in future versions.   python
print(two())                                                #  Warning: two is deprecated since version 0.0.0. It will be removed in version 0.0.1.       2
