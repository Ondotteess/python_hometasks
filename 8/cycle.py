def cycle(iterable):
    while True:
        for x in iterable:
            yield x

def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break

    return res

print(take(cycle([1, 2, 3]), 10))

#   [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
