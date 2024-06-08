print("[How far your donation goes]")

print(" ")

soup = int(input("How many cans of soups? "))
rice = int(input("How many bags of rice? "))
vegetables = int(input("How many cans of vegetables? "))
pb = int(input("How many cans of peanut butter? "))

print(" ")

soup_people = soup * 2
rice_people = rice * 4
veg_people = vegetables * 3.5
pb_people = pb * 7

total_people = soup_people + rice_people + veg_people + pb_people

print(f"Your donation will help feed {total_people} people!")
print(f"{soup_people} people with the {soup} can(s) of soup")
print(f"{rice_people} people with the {rice} bag(s) of rice")
print(f"{veg_people} people with the {vegetables} can(s) of vegetables")
print(f"{pb_people} people with the {pb} can(s) of peanut butter")
