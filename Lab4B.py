def lab4b():
    print("Welcome!")
    num = float(input("Please input a number: "))

    print(" ")

    print("What would you like to do to this number:")
    print("0) Get the additive inverse of the number")
    print("1) Get the reciprocal of the number")
    print("2) Square the number")
    print("3) Cube the number")
    print("4) Exit the program")

    user_input = int(input(""))

    if num == 0 and user_input == 1:
        print("Cannot divide by 0!")
        return

    if user_input == 0:
        print(f"The additive inverse of {num} is {-num}")

    elif user_input == 1:
        print(f"The reciprocal of {num} is {1/num}")

    elif user_input == 2:
        print(f"The square of {num} is {num**2}")

    elif user_input == 3:
        print(f"The cube of {num} is {num**3}")

    elif user_input == 4:
        print("Thank you, goodbye!")

    else:
        print("Invalid input, please try again!")
lab4b()

