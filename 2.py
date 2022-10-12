arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = ['rtbtr', 'rbtr', 4123, True, '32cc3e']
arr3 = []

for i in range(min(len(arr1), len(arr2))):
    arr3.append((arr1[i], arr2[i]))

print(arr3)