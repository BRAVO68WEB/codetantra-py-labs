def makematrix(x, y):
    l = []
    for i in range(x):
        a = []
        for j in range(y):
            a.append(
                int(input("Entry in row: {} column: {}\n".format(i + 1,
                                                                 j + 1))))
        l.append(a)
    return l


print("Enter values for matrix - A")
m = int(input("Number of rows, m = "))
n = int(input("Number of columns, n = "))
A = makematrix(m, n)

print("Enter values for matrix - B")
p = int(input("Number of rows, m = "))
q = int(input("Number of columns, n = "))
B = makematrix(p, q)

print("Matrix - A =", A)
print("Matrix - B =", B)

C = []

for i in range(len(A)):
    a = []
    for j in range(len(B[0])):
        a.append(0)
    C.append(a)
if ((m + p) - (n + q)) >= 0:
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += (A[i][k]) * (B[k][j])
    print("Matrix - A * Matrix- B =", C)
else:
    print("Cannot multiply the two matrices. Incorrect dimensions.")
    print("Matrix - A * Matrix- B = None")
