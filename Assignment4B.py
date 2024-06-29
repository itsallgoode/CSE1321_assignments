
def input_message():
    print("Enter your message:")
    phrase = input()
    phrase = phrase.upper()
    offset = int(input("Enter the offset value: "))
    print()
    if check_message(phrase, offset):
        encoded_message = encode_message(phrase, offset)
        print("Your secret message is...")
        print(encoded_message)
    else:
        print("Sorry, we can only process messages with letters and spaces, and the offset must be between 0 and 26.")
    end_message()

def check_message(phrase, offset):
    if offset <= 0 or offset >= 26:
        return False
    for char in phrase:
        if not (char.isalpha() or char.isspace()):
            return False
    return True

def encode_message(phrase, offset):
    secret_message = []
    for letter in phrase:
        if letter.isspace():
            secret_message.append(letter)
        else:
            number = ord(letter)
            new_number = (number - ord('A') + offset) % 26 + ord('A')
            encoded_phrase = chr(new_number)
            secret_message.append(encoded_phrase)
    return "".join(secret_message)

def end_message():
    question = input("Do you want to encrypt another message?: ").upper()
    if question == "Y":
        input_message()
    else:
        print()
        print("Closing out...")
        return

if __name__ == "__main__":
    input_message()
    







