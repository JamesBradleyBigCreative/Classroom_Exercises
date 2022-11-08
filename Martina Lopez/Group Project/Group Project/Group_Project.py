import module1 as mod

def WelcomeScreen():
    isQuit = False
    while isQuit == False:
        print("""
        ___________________________                           ____________________
        | Mini Statement Press 'M'|                           | Balance Press 'B'|
        ---------------------------                           --------------------
    
        ______________________                                _______________
        | Withdrawl Press 'W'|                                | Transfer 'T'|
        ----------------------                                ---------------

        ____________________                                  _________________
        | Deposit Press 'D'|                                  | Quit Press 'Q'|
        --------------------                                  -----------------
        """)
        UserChoice = input("\nWhat Operation Do You Want To Perform: ")

        if UserChoice == 'M' or UserChoice == 'm':
            pass
        elif UserChoice == 'W' or UserChoice == 'w':
            pass
        elif UserChoice == 'D' or UserChoice == 'd':
            pass
        elif UserChoice == 'B' or UserChoice == 'b':
            pass
        elif UserChoice == 'T' or UserChoice == 't':
            pass
        elif UserChoice == 'Q' or UserChoice == 'q':
            print("\nQuitting from the terminal.....")
            isQuit = True


