s1 = input("enter the matrix: ")
s1 = s1.split("|")

matrix = []

for s2 in s1:
    s2 = s2.split()
    for i in range(len(s2)):
        s2[i] = float(s2[i])
    matrix.append(s2)

print(matrix[1][2])
