a = int(input("Enter size of list: "))
l1 = list()
l3 = list()
for i in range(a):
    ele = int(input("Enter value: "))
    l1.append(ele)
print("Original List =", l1)
l2 = set(l1)
for j in l1:
    if j in l2:
        l3.append(j)
        l2.remove(j)
print("Unique elements =", l3)
