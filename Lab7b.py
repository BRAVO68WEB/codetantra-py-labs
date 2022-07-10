fname = input("Enter file name: ")
file = open(fname, 'r')
nl = nw = nc = 0
for line in file:
    words = line.split()
    nl += 1
    nw += len(words)
    nc += len(line)
file.close
print("Lines =", nl)
print("words =", nw)
print("Characters =", nc)
