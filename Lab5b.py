print("Enter strings contained name and dob with : seperated")
c = input().split(' ')
l = list(c)
print("The list:", l)
print("The list with join:", "---".join(l))
x1, x2 = l[0].split(':')
y1, y2 = l[1].split(':')
z1, z2 = l[2].split(':')
d = {}
d[x1] = x2
d[y1] = y2
d[z1] = z2
print("The sorted dictionary:", sorted(d.items()))
