def isValid(width, height):
    return (width + height) > 30

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def lab6a(width, height):
    if isValid(width, height):
        print("This is a valid rectangle.")
        print(f"The area is: {area(width, height)}")
        print(f"The perimeter is: {perimeter(width, height)}")
        print(" ") 
    else:        
        print("This is an invalid rectangle.")
        print(" ") 

if __name__ == "__main__":
    while True:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        lab6a(width, height)
        response = input("Do you want to enter another width and height (Y/N)?: ")
        print(" ") 
        if response == "N":
            print("Program Ends")
            break
