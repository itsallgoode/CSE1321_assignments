def isValid(width, height):
    return (width + height) > 30

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def lab6a():
    while True:
        width = float(input("Enter a width: "))
        height = float(input("Enter a height: "))

        if isValid(width, height):
            print("This is a valid rectangle.")
            print(f"The area is: {area(width, height)}")
            print(f"The perimeter is: {perimeter(width, height)}")
        else:
            print("This is an invalid rectangle.")

        print(" ")
        response = input("Do you want to enter another width and height (Y/N)?: ").upper()
        print(" ")

        if response == "N":
            break
lab6a()