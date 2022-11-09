def start():
    inp_1 = input("Do you want to start, (yes/any other character to quit): ")
    if inp_1 == "yes":
        def intro():
            print("Let's start with your name: ")
            name = input("Enter name: ")        
        
    
            print("Welcome to the Adventure! As an avid player, you have decided to explore a small town near bye.  However, during your exploration, you find yourself lost. \n You can choose to walk in multiple directions to find a way out. ")
         
            print("Good luck, " ,name, ".")
 
        intro()   
        def Part1():
            directions = ["left","right","forward"]
            print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
            
            
            print("Options: left/right/backward/forward/back/front")
            userInput = input("Enter direction: ")
            while userInput in directions:
                if userInput == "left":
                    print("You walk down a path hoping to escape the forest you are in but reach a deadend and die to a banshee ")
                    input("press enter")
                elif userInput == "right":
                    print("you walk down a path way and during the walk you found a light which you think is your way out but instead leads you to a house which you decide to stay the night constantly in fear of your surroundings")
                    input("press enter")
                elif userInput == "forward" or "front":
                    print("You walk down the central path and.... YOU HAVE ESCAPED THE FOREST SAFELY!")
                    print("Continuing ...........")
                    input("Press enter")
                elif userInput == "backward" or "back" :
                    print("You find that this path leads into a dead end as you have taken a different path far away from the entrance and decide to go back")
                    input("press enter")
                else: 
                    print("Please enter a valid option.")

        def Part2():
            options = ["walk","wait for help","hitchhike","explore close by"]
            print("You have sucessfully escaped the forest(if you selectes the correct option) and find yourself outside with a large road")
            
            print("Options: walk/wait for help/hitchhike/explore close by")
            userInput = input("Enter option")
            while userInput in options:
                if userInput == "walk":
                    print("You have walked for a while and have died of starvation and dehydration as you have run out of resources ")
                    print("press enter")
                elif userInput == "wait for help":
                    print("You waited for days and it was worth it as your brother was searching for you for days and you both travel home together")
                    print("press enter")
                elif userInput == "hitchhike":
                    print("in despiration of trying to leave you hitchhike a random car which gets you kidnapped and never seen again")
                    print("press enter")
                elif userInput == "explore close by":
                    print("while you are thinking of a way to get home you explore in areas close to you which gives you more time but you still sadly die")



        Part2()          

            



        Part1()    
        
start()


