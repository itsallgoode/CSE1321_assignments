

def main():

    print('[FYE Level Map Creator]')
    width = int(input("Enter a level map width: "))
    height = int(input("Enter a level map height: "))

    map = [["_"] * width for _ in range(height)]
    draw_map(map)
    print()
    while True:
        print("Options")
        print("1. Clear Level")
        print("2. Add Platform")
        print("3. Add items")
        print("4. Quit")
        option = int(input("Enter a choice: "))
        print()

        if option == 1:
            clear_level(map, width, height)
        if option == 2:
            add_platform(map, width, height)
        if option == 3:
            add_items(map, width, height)
        if option == 4:
            draw_map(map)
            print()
            print("Goodbye!")
            break


def draw_map(map):
    for level in map:
        print(''.join(level))

def clear_level(map, width, height):
    print("[Clear Level]")
    for i in range(height):
        for j in range(width):
            map[i][j] = "_"
    draw_map(map)

def add_platform(map, width, height):
    print("[Add Platform]")
    x = int(input("Enter X Coordinate: "))
    y = int(input("Enter Y coordinate: "))
    length = int(input("Enter Length: "))
    if x >= height or y + length > width:
        print("This platform won't fit in the level!")
    else:
        for i in range(length):
            map[y][x + i] = '='
    draw_map(map)

def add_items(map, width, height):
    print("[Add Item]")
    x = int(input("Enter X Coordinate: "))
    y = int(input("Enter Y coordinate: "))
    if x > height or y > width:
        print("This is not a valid location!")
    else:
        map[y][x] = 'P'
    draw_map(map)
main()

