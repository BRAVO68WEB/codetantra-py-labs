s = int(input("Enter size of list: "))
l = []
for i in range(1, s + 1):
    n = int(input("Enter value: "))
    l.append(n)
print("The sum of the given sequence {} is {}".format(l, sum(l)))
print("good bye..!")