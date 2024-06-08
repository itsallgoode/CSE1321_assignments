
# Name: Charles Goode
# Section: E01

character = input("Enter a character to use: ")
diamond_width = int(input("Enter the diamond's width: "))

if diamond_width % 2 == 0:
    diamond_width += 1
    print(f"To make a diamond, we'll use {diamond_width} as the width instead.")

elif diamond_width < 3:
    print("Please enter a width of at least 3")
    diamond_width = int(input("Enter the diamond's width: "))

for i in range(diamond_width // 2 + 1):  # this divides the width by 2, rounds down, and adds 1. so with a width of 5, it will run 3 times, building the top half
    spaces = ' ' * (diamond_width // 2 - i)  # this divides the width by 2, rounds down, then subtracts 1 to use one less space per iteration
    chars = character * (2 * i + 1)  # this makes us start with one character on the first line, then adds 2 characters every line
    print(spaces + chars)

# Bottom half of the diamond
for i in range(diamond_width // 2 - 1, -1, -1):  # this makes the start value one step below the middle of the diamond, then subtracts 1 each time so the loop runs in reverse
    spaces = ' ' * (diamond_width // 2 - i)
    chars = character * (2 * i + 1)
    print(spaces + chars)
