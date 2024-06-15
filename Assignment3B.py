class Assignment3B:

    def quest():

        print("[Epic Quest Simulator]")
        mode1 = int(input("""Hello stranger! Do you have time to hear my tale?
1) Yes
2) No
"""))
        
        if mode1 == 2:
            print("Ah, then goodbye...")
            return
        elif mode1 == 1:
            mode2 = int(input("""Thank you! I come from the land of Pax Bisonica. Our country has been taken over by a cruel tyrant!
1) That’s awful!
2) What can I do?
"""))
            
            if mode2 == 1:
                print("Alas, it is truly terrible...")
                
            mode3 = int(input("""Please, you must journey to Pax Bisonica and free our country!
1) Okay
2) No
"""))
                
            if mode3 == 1:
                print("Hooray!")
            elif mode3 == 2:
                print("Then all is lost...")
        return
                

if __name__ == "__main__":
    Assignment3B.quest()
