import random
def main():
    throws = ['Rock', 'Paper', 'Scissors']


    games = int(input("How many games do you want to play? "))
    history = []

    for num in range(1, games+1):
        human = input(f"Round {num}: What do you want to throw? ").capitalize()
        computer = random.choice(throws)
        print(f"Computer threw {computer.upper()}!")
        rounds = [human, computer]
        history.append(rounds)
        
    print("Game Over...")
    print()
    print("Here's the recap:")

    for num, round in enumerate(history, start=1):
            
            if round[0] == 'Paper' and round[1] == 'Scissors':
                print(f"Computer won Round {num} with Scissors")
            if round[0] == 'Paper' and round[1] == 'Rock':
                print(f"Player won Round {num} with Paper")
            if round[0] == 'Paper' and round[1] == 'Paper':
                print(f"Tied on Round {num} with Paper")

            if round[0] == 'Rock' and round[1] == 'Paper':
                print(f"Computer won Round {num} with Paper")
            if round[0] == 'Rock' and round[1] == 'Scissors':
                print(f"Player won Round {num} with Rock")
            if round[0] == 'Rock' and round[1] == 'Rock':
                print(f"Tied on Round {num} with Rock")

            if round[0] == 'Scissors' and round[1] == 'Paper':
                print(f"Player won Round {num} with Scissors")
            if round[0] == 'Scissors' and round[1] == 'Rock':
                print(f"Computer won Round {num} with Rock")
            if round[0] == 'Scissors' and round[1] == 'Scissors':
                print(f"Tied on Round {num} with Scissors")

main()
