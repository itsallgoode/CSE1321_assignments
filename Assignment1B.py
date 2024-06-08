import math

print("First color")
r_1 = int(input("R: "))
g_1 = int(input("G: "))
b_1 = int(input("B: "))
print(" ")
print("Second color")
r_2 = int(input("R: "))
g_2 = int(input("G: "))
b_2 = int(input("B: "))

distance = math.sqrt((r_2 - r_1) ** 2 + (g_2 - g_1) ** 2 + (b_2 - b_1) ** 2)

print(float(distance))
