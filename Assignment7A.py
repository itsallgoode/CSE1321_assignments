from FSAfile import FSA

def main():
    
    print("[Finite State Automata]")
    initial_state = int(input("What state do you want to start at? "))
    fsa = FSA(initial_state)

    while True:
        print()
        print("What will you do?")
        print(">Go to next state")
        print(">End")
        answer = input().upper()
        print()

        if answer == "Go to next state".upper():
            current_state = fsa.goToNextState()
            print(f"You're now at state {current_state}")

        elif answer == "End".upper():
            if fsa.end():
                print("The FSA has shut down.")
                break
            else:
                print("You can't stop here; you can only stop at state 3.")
        
        else:
            print("[Invalid command!]")

main()