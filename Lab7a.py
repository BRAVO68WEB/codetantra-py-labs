a = input("Enter file name: ")
for line in reversed(list(open(a))):
    print(line.rstrip())
