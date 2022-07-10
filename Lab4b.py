n = int(input("Enter an integer: "))
a = 0
b = 1
count = 0
sum1 = 0
lst = list()
listfib = list()
listeven = list()
sum2 = 0
while count <= n:
    lst.append(sum1)
    count += 1
    a = b
    b = sum1
    sum1 = a + b
for j in lst:
    if j <= n:
        listfib.append(j)
for k in listfib:
    if k % 2 == 0:
        listeven.append(k)
for l in listeven:
    sum2 += l
print("The sum of even numbers of fibonacci sequence {} is: {}".format(
    listfib, sum2))
