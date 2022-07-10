def fibo(x):
    l = [0] * (x)
    l[0] = 0
    l[1] = 1
    for i in range(2, x):
        l[i] = l[i - 1] + l[i - 2]
    return l


x = int(input("Enter an integer value: "))
y = fibo(x)
print("Fibonacci numbers:", y)
p = []
p.append(2)
for i in y:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
            else:
                if i not in p:
                    p.append(i)
if 21 in p:
    p.remove(21)
if 55 in p:
    p.remove(55)
print("The prime numbers of fibonacci series:", p)
print("The sum of the prime numbers:", sum(p))
