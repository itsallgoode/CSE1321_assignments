def allMath(number1, number2):
    addition = (number1 + number2)
    subtraction = (number1 - number2)
    multiplication = (number1 * number2)
    if number1 and number2 != 0:
        division = (number1 / number2)
    else:
        division = None
    if number1 and number2 != 0:
        floor_division = (number1 // number2)
    else:
        floor_division = None
    if number1 and number2 != 0:
        modulos = (number1 % number2)
    else:
        modulos = None
    power = (number1 ** number2)
    return addition, subtraction, multiplication, division, floor_division, modulos, power

def main():

    number1 = int(input("Enter your first number: "))
    print()
    number2 = int(input("Enter your second number: "))
    print()    
    result = allMath(number1, number2)
    print(f"Your resulting tuple is {result}")

main()