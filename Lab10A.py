def mailing_list():

    print("[Mailing List]")
    print()
    email_list = []
    while True:


        print("1 - Add email")
        print("2 - Delete email")
        print("3 - List all emails")
        print("4 - Quit")

        selection = int(input("Make your selection: "))
        print()



        if selection == 1:
            email = input("Enter the email to be added: ")
            email_list.append(email)
            print("Email added to mailing list.")
            print()
        
        if selection == 2:
            email_remove = input("Enter the email to be removed: ")
            if email_remove in email_list:
                email_list.remove(email_remove)
                print(f"{email_remove} has been removed from the mailing list.")
                print()

            else:
                print(f"No such email in mailing list: {email_remove}")
                print()
        
        if selection == 3:
            for emails in email_list:
                print(emails)
            print()
        
        if selection == 4:
            print("Shutting down...")
            break

mailing_list()
            

