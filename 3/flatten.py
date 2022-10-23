def checkArr(a):
    for x in a:
        if isinstance(x, list):
            return False
    return True

def _flatten(a):
    __a = a
    while True:
        _a = []
        for x in __a:
            if isinstance(x, int): _a.append(x)
            else: 
                _a = _a + x
        __a = _a

        if checkArr(__a):
            return __a

def flatten(a, depth=-1):
    __a = a
    i = 1
    while True:
        _a = []
        for x in __a:
            if isinstance(x, int): _a.append(x)
            else: 
                _a = _a + x
        __a = _a
        if checkArr(__a) or i == depth:
            return __a
        i += 1
        

a = [1, 2, [4, 5], [6, [7]], 8]

print(flatten(a, depth=1))  #  [1, 2, 4, 5, 6, [7], 8]
print(_flatten(a))          #  [1, 2, 4, 5, 6, 7, 8]
