def sumy(*args):
    res = 0
    for i in args:
        res += i
    return res

def specialize(f1, *args1):
    def f2(*args2):
        return f1(*args1, *args2)
    return f2

plus_one = specialize(sumy, 1)
just_two = specialize(sumy, 1, 1)

print(plus_one(10))    # 11
print(just_two())      # 2
