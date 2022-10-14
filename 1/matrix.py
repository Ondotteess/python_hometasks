s1 = input("enter the matrix: ")    # 1 2 3 | 4 5 6 | 7 8 9 
s1 = s1.split("|")

matrix = []

for s2 in s1:
    s2 = s2.split()
    for i in range(len(s2)):
        s2[i] = float(s2[i])
    matrix.append(s2)

print(matrix[1][2])    # 6.0
