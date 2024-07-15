def letterPositions(phrase, letter):
    positions = []
    for index, char in enumerate(phrase):
        if char == letter:
            positions.append(index)
    return tuple(positions)

def main():
    phrase = input("Enter your phrase: ").lower()
    letter = input("Enter your letter: ").lower()
    positions = letterPositions(phrase, letter)
    print(f"{letter} appears inside your phrase in the following positions: {positions}")


main()
