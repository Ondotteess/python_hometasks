a = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Baranov": 99999, "Sidorov": 99999, "Fihtengolc": 12345, "Matanov": 55521}
b = {}
c = set()

for s in a.items():
    if s[1] in c:
        b[s[1]] = tuple(x for x in a.keys() if a[x] == s[1])
    else:
        b[s[1]] = s[0]

    c.add(s[1])

print(b)