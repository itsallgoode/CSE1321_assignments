def lab5a():

    print("Please enter 10 numbers and this program will display the largest.")

    for i in range(1, 11):
        num = int(input(f"Please enter number {i}: "))
        if i == 1:
            largest = num
        elif num > largest:
            largest = num
    print(" ")
    print(f"The largest number was {largest}")

lab5a()