small_sandwiches = int(input("Enter the number of small sandwiches: "))
medium_sandwiches = int(input("Enter the number of medium sandwiches: "))
large_sandwiches = int(input("Enter the number of large sandwiches: "))
extra_large_sandwiches = int(input("Enter the number of extra-large sandwiches: "))

print(f"You've entered {small_sandwiches} small sandwiches.")
print(f"You've entered {medium_sandwiches} medium sandwiches.")
print(f"You've entered {large_sandwiches} large sandwiches.")
print(f"You've entered {extra_large_sandwiches} extra-large sandwiches.")

small_cook_time = small_sandwiches * 30
medium_cook_time = medium_sandwiches * 60
large_cook_time = large_sandwiches * 75
extra_large_cook_time = extra_large_sandwiches * 135

total_cook_minutes = (small_cook_time + medium_cook_time + large_cook_time + extra_large_cook_time) // 60

total_cook_seconds = (small_cook_time + medium_cook_time + large_cook_time + extra_large_cook_time) % 60
print(f"Total cooking time is {total_cook_minutes} minutes and {total_cook_seconds} seconds.")

