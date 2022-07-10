n = int(input("Enter size of int-list: "))
s = int(input("Enter size of string-list: "))
l1 = []
l2 = []
for i in range(1, n + 1):
    il = int(input("Enter int for int-list: "))
    l1.append(il)
for i in range(1, s + 1):
    sl = input("Enter string for string-list: ")
    l2.append(sl)
d = {}
for k in l1:
    for v in l2:
        d[k] = v
        l2.remove(v)
        break
print(str(d))