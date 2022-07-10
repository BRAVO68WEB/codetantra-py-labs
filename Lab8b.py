import statistics

x = int(input("Enter size of list: "))
l = [0] * x
for i in range(x):
    l[i] = int(input("Enter integer value: "))
print("Mean of list:", statistics.mean(l))
print("Median of list:", statistics.median(l))
print("Mode of list:", statistics.mode(l))
print("Standard deviation of list:", statistics.stdev(l))
print("Variance of list:", statistics.variance(l))
