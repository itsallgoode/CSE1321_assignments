import random

class Assignment3A:
    
    def __init__(self):

        print("[Mathletes Game]")
        mode = int(input("Choose a game mode (0=Easy, 1=Hard): "))

        if mode == 0:
            self.EasyMode()
        elif mode == 1:
            self.HardMode()
        else:
            print("Invalid mode. Please try again.")
            exit()

    def EasyMode(self):
        print("Playing on easy mode, huh? Okay!")
        while True:
            for i in range(1, 4):
                i1 = random.randint(-10, 10)
                i2 = random.randint(-10, 10)
                print(f"Q{i}. {i1} * {i2} = ?")
                ans = i1 * i2
                ans1 = int(input(""))
                if ans1 == ans:
                    print("Correct!")
                else:
                    print("Incorrect! Try again.")
                    ans2 = int(input(""))
                    if ans2 == ans:
                        print("Correct!")
                    else:
                        print("Incorrect! Try again.")
                        ans3 = int(input(""))
                        if ans3 == ans:
                            print("Correct!")
                        else:
                            print("Incorrect!")
                            print("Game over...")
                            return
            print("You win!")
            return
                        
    def HardMode(self):
        print("So, you want a challenge? Okay!")

        while True:
            for i in range(1, 7):
                i1 = random.randint(-255, 255)
                i2 = random.randint(-255, 255)
                print(f"Q{i}. {i1} * {i2} = ?")
                ans = i1 * i2
                ans1 = int(input(""))
                if ans1 == ans:
                    print("Correct!")
                else:
                    print("Incorrect!")
                    print("Game over...")
                    return
            print("You win!")
            return
    
if __name__ == "__main__":
    Assignment3A()