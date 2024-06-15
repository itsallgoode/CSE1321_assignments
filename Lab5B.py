def lab5b():

    value = int(input("Please enter a value for the size: "))
    char = "*"
    space = " "
    
    print(f"This is the requested {value}x{value} box:")

    for i in range(value):
        print(char * value)

    print(f"This is the requested right-facing {value}x{value} right-triangle:")

    for i in range(1, value+1):
        print(char * i)

    print(f"This is the requested left-facing {value}x{value} right-triangle:")

    for i in range(1, value+1):
        print(space * (value - i) + char * i)

lab5b()