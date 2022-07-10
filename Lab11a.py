m = int(input("Number of rows, m = "))
n = int(input("Number of columns, n = "))
l = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(
            int(input("Entry in row: {} column: {}\n".format(i + 1, j + 1))))
    l.append(a)
print(l)