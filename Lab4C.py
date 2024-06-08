

def main():
    
    print("Welcome!")
    balance = 1000
    print(f"You have ${balance} in your account.")

    while True:

        
        print(" ")
        print("Menu")
        print("0 – Make a deposit")
        print("1 – Make a withdrawal")
        print("2 – Display account value")
        print(" ")

        selection = int(input("Please make a selection: "))

        if selection == 0:
            deposit = float(input("How much would you like to deposit?: "))
            balance += deposit
            print(f"Your current balance is ${balance}")
        
        elif selection == 1:
            withdrawal = float(input("How much would you like to withdraw?: "))

            if withdrawal > balance:
                print("Not enough balance. Withdrawal canceled.")
                print(f"Your current balance is ${balance}")
            
            if withdrawal <= balance:
                balance -= withdrawal
                print(f"Your current balance is ${balance}")
        
        elif selection == 2:
            print(f"Your current balance is ${balance}")
        
        else:
            print("Invalid entry, please try again.")
        
        return_to_menu = input("Would you like to return to the main menu (Y/N)?: ").lower()

        if return_to_menu != "y":
            print("Thank you for banking with us!")
            break
main()