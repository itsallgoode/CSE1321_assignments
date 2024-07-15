def lab5b():
    value = int(input("Please enter a value for the size: "))
    char = "*"
    space = " "
    
    print(f" This is the requested {value}x{value} box:")
    for i in range(value):
        print(f" {char * value}")

    print(f" This is the right-facing {value}x{value} right-triangle:")
    for i in range(1, value + 1):
        print(f" {char * i}")

    print(f" This is the left-facing {value}x{value} right-triangle:")
    for i in range(1, value + 1):
        print(f" {space * (value - i)}{char * i}")

lab5b()

