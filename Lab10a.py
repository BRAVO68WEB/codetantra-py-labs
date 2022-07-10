from itertools import accumulate

a = int(input("Enter size of list: "))
lst = list()
lst2 = list()
for i in range(a):
    ele = int(input("Enter value: "))
    lst.append(ele)
print("Original List =", lst)
lst2 = [*accumulate(lst, lambda a, b: a * b)]
print("Cumulative Product List =", lst2)
