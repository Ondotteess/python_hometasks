x = int(input('enter the num: '))
result = x & 1
x >>= 1
while (x != -1 and x != 0):
    if x & 1:
        result += 1
    x >>= 1
print(result + (x & 1))