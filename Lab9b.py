a = int(input("Enter size of list: "))
lst = list()
for i in range(a):
    val = int(input("Enter value: "))
    lst.append(val)
print("Original List =", lst)
_size = len(lst)
lst2 = []


def repeat(lst):
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if lst[i] == lst[j] and lst[i] not in lst2:
                lst2.append(lst[i])
    return lst2


repeat(lst)
lst2.sort()
print("Duplicates =", lst2)
