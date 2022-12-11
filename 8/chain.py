def chain(*args):
    res = []
    for x in args:
        res += x

    for x in res:
        yield x

it = range(3, 0, -1)

print(chain([1, 2, 3], it ,['a', 'b', 'c']))

