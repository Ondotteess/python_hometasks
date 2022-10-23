a = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Baranov": 99999, "Sidorov": 99999, "Fihtengolc": 12345, "Matanov": 55521}
b = {}

for value in a.values():
    c = [key for key, _value in a.items() if value == _value]
    b[value] = tuple(x for x in c)
    
print(b) #{97832: ('Ivanov', 'Kuznecov'), 55521: ('Petrov', 'Matanov'), 99999: ('Baranov', 'Sidorov'), 12345: ('Fihtengolc',)}
