def friend_list():

    print("[Friend List]")
    print()
    friends = []

    while True:

        print("1 - Add friend")
        print("2 - List friends")
        print("3 - Quit")
        selection = int(input("Make your selection: "))
        print()

        if selection == 1:
            friend_info = []
            name = input("Enter your friend's name: ")
            friend_info.append(name)
            age = input("Enter your friend's age: ")
            friend_info.append(age)
            friends.append(friend_info)
            print("Friend added")
            print()
        
        if selection == 2:
            for friend in friends:
                print(f"Name: {friend[0]}, Age: {friend[1]}")
            print()

        if selection == 3:
            print("Shutting down...")
            print()
            break

friend_list()