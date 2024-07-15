class Chair:
    numOfLegs = 4
    rolling = False
    material = 'Plastic'

def main():
    c1 = Chair()
    print("You are about to create a chair.")
    c1.numOfLegs = int(input("How many legs does your chair have: "))
    c1.rolling = input("Is your chair rolling (true/false): ").lower()
    c1.material = input("What is your chair made of: ")

    if c1.rolling == 'true':
        print(f"Your chair has {c1.numOfLegs} legs, is rolling, and is made of {c1.material}")
    else:
        print(f"Your chair has {c1.numOfLegs} legs, is not rolling, and is made of {c1.material}")

    print("This program is going to change that.")
    
    c1.numOfLegs = 4
    c1.rolling = False
    c1.material = "wood"

    if c1.rolling:
        print(f"Your chair has {c1.numOfLegs} legs, is rolling, and is made of {c1.material}")
    else:
        print(f"Your chair has {c1.numOfLegs} legs, is not rolling, and is made of {c1.material}")

main()

