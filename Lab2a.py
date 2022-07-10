import math

x1 = int(input("Enter the x coordinate of first point: "))
y1 = int(input("Enter the y coordinate of first point: "))
x2 = int(input("Enter the x coordinate of second point: "))
y2 = int(input("Enter the y coordinate of second point: "))
r = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance is:", r)
