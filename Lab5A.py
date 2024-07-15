def lab5a():

    print("Please enter 10 numbers and this program will display the largest.")
    nums = []
    for i in range(1, 11):
        num = int(input(f"Please enter number {i}: "))
        nums.append(num)


    print(" ")
    print(f"The largest number was {sorted(nums)[-1]}")

lab5a()