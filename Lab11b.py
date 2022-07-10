def makematrix(m, n):
    l = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(
                int(input("Entry in row: {} column: {}\n".format(i + 1,
                                                                 j + 1))))
        l.append(a)
    return l


m = int(input("Number of rows for matrix - A, m = "))
n = int(input("Number of columns for matrix - A, n = "))
p = int(input("Number of rows for matrix - B, p = "))
q = int(input("Number of columns for matrix - B, q = "))
if m == p and n == q:
    print("Enter values for matrix - A")
    A = makematrix(m, n)
    print("Enter values for matrix - B")
    B = makematrix(p, q)
    C = []
    for i in range(m):
        a = []
        for j in range(q):
            a.append(0)
        C.append(a)
        for i in range(len(C)):
            for j in range(len(C[0])):
                C[i][j] = A[i][j] + B[i][j]
    print("Matrix a =", A)
    print("Matrix b =", B)
    print("Addition of two matrices =", C)
else:
    print("Addition is not possible")
