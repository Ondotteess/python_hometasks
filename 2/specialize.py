def sumy(x, y):
    return x + y

def specialize(f1, *args, **kwargs):
    def f2(*_args, **_kwargs):
        return f1(*args, *_args, **kwargs, **_kwargs)
    return f2


just_two = specialize(sumy, 1, 1)
plus_one = specialize(sumy, y=1)

print(plus_one(x=10))    # 11
print(just_two())        # 2
