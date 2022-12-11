def coroutine(f):
    def inner():
        ret = f()
        next(ret)
        return ret

    return inner

@coroutine
def storage():
    values = set()
    was_there = False
    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
print(st.send(0)) # False
print(st.send(0)) # True
