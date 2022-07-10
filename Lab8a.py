a = (input("Enter x, y, r of ball-1: "))
b = (input("Enter x, y, r of ball-2: "))
lst1 = a.split(' ')
lst2 = b.split(' ')
for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
for j in range(len(lst2)):
    lst2[j] = int(lst2[j])
rad = lst1[2] + lst2[2]
dis = ((lst1[0] - lst2[0])**2 + (lst1[1] - lst2[1])**2)**0.5
if (rad > dis):
    print("True - Balls are colliding")
else:
    print("False - Balls are not colliding")
