a = int(input("Enter size of list: "))
l1 = list()
for i in range(a):
    ele = int(input("Enter value: "))
    l1.append(ele)
print("Original List =", l1)
l2 = l1[::-1]
print("Reversed List =", l2)
