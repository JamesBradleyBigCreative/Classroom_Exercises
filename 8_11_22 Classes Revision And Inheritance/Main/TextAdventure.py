from Characters import *
import random as rand


avatar = Player() # Initializing the users class

clear = "\n" * 100 # Clears the terminal

# Dictionary of available weapons that can be collected in the game
weapons = {"Blunt Sword": 10,"Common Sword": 20,"Uncommon Sword":50,
           "Rare Sword":100,"Legendary Sword":200,
           "Blunt Dagger": 5,"Common Dagger": 10,"Uncommon Dagger":25,
           "Rare Dagger":50,"Legendary Dagger":100,
           "Broken Hammer": 20,"Common Hammer": 40,"Uncommon Hammer":100,
           "Rare Hammer":200,"Legendary Hammer":400,}

# Dictionary of available armour that can be collected in the game
armour = {"Wooden Armour": 10,"Common Armour": 20,"Uncommon Armour": 50,
          "Rare Armour":100,"Legendary Armour":200,}

# List of Available Enemy types
enemies = [Slime(),WildDog(),Goblin(),Bandit(),HobGoblin(),DemonKnight()]


def Explore(isplaying): # Prompts the user to choose whether or not to 
    # explore a given location
    locations = ["You Have Found A Dungeon",
              "You Have Found An Forest",
              "You Have Found A Town",
              "You Have Found A Temple",
              "You Have Found A Colosseum"] # Available Locations to explore
    while isplaying == True:

        Movement()

        X = rand.randint(0,len(locations)-1)
        print(locations[X])
        temp = locations[X].split(" ")
        shortcurrentlocation = temp.pop() # Randomly chooses a location

        print("\nDo you wish to explore this area further or keep moving:\n")
        Choice = input("Press 'Y' to explore further or Press"
        " 'N' to keep moving or Press 'Q' to Quit: ")

        if Choice == 'Y' or Choice == 'y':
            indepthExplore(shortcurrentlocation)

        elif Choice == 'N' or Choice == 'n':
            print(f"\nYou Have Decided to keep moving"
            f" and ignore the {shortcurrentlocation}\n")

        elif Choice == 'Q' or Choice == 'q':
            quit()

        else:
            print("\nError Wrong input")
        # Users Options

def Movement(): # Allows user to decide what direction to move
    print("Enter the Direction You Wish to Go Or Press 'Q' to quit")

    print("""
          _______     
          |  N  |     
          -------     
                   
     _______    _______
     |  W  |    |  E  |
     -------    -------

          _______
          |  S  |
          -------
    """)
    
    Direction = input("")

    if Direction == 'N' or Direction == 'n':
        print("\nYou are heading North....\n")
        print(clear)

    elif Direction == 'E' or Direction == 'e':
        print("\nYou are heading East....\n")
        print(clear)

    elif Direction == 'W' or Direction == 'w':
        print("\nYou are heading West....\n")
        print(clear)

    elif Direction == 'S' or Direction == 's':
        print("\nYou are heading South....\n")
        print(clear)

    elif Direction == 'Q' or Direction == 'q':
        quit()

    else:
         print("Error Wrong input")


def  indepthExplore(currentloc): # When the user chooses to explore a 
    # location deeper in Explore() this function is called
    # Randomly generates a event that happens to the user and runs 
    # correlating functions
    events = [f"In the {currentloc} you find a chest",
              f"In the {currentloc} you find an enemy encounter",
              f"In the {currentloc} you find nothing",
              f"In the {currentloc} you find treasure",
              f"You enter the {currentloc}"
              ]

    print(f"\nYou delve deeper into the {currentloc}\n")

    temp = rand.randint(0,len(events)-1)
    chosenevent = events[temp]
    # Randomly Chooses the event

    if chosenevent == events[0]:
        print(events[0])
        Chest()

    elif chosenevent == events[1]:
        print(events[1])
        temp = rand.randint(0,len(enemies)-1)
        chosenenemie = enemies[temp]
        Encounter(chosenenemie)

    elif chosenevent == events[2]:
        print(events[2])
        print("You Found Nothing Continue...\n")

    elif chosenevent == events[3]:
        print(events[3])
        coinsfound = rand.randint(0,100)
        print(f"You Got {coinsfound} coins!!!\n")
        avatar.coins += coinsfound

    elif chosenevent == events[4]:
        print(events[4])
        print(f"\nInside the {currentloc} you find a Colosseum\n")
        print("""
        Colosseum Rules And Reward
        --------------------------
         Survive the onslaught of 
                 enemies
           Maximum Of 10 Enemies
        --------------------------
            REWARD: 1000 Coins
        """)

        try:
            number_of_enemies = int(input(
                "How many enemies do you dare to challenge: "))

        except:
            print("Error Invalid Input")
            return None
        
        generated_list = GenerateEnemyList(number_of_enemies,enemies)

        for i in range(len(generated_list)):
            Encounter(generated_list[i])
            print("NEXT ENEMY INCOMING")

    # Calling the correlating functions according to the event generated








def Chest(): # When a user encounters a chest this function
   # randomly generates an item from the global dictionarys armour and weapons
    AorW = rand.randint(1,2)

    if AorW == 1:
        print("\nYou have found a weapons chest\n")
        print("And inside you find........\n")
        temp = rand.choices(list(weapons), weights =
        (50,25,15,10,5,50,25,15,10,5,50,25,15,10,5,),k = 1)
        # Choices selects items on a list randomly but with weighted probability 
        chosenWeapon =  temp[0]
        print(f"A {chosenWeapon}!!\n")
        avatar.attack += weapons[chosenWeapon]

        avatar.inventory.update({chosenWeapon: weapons[chosenWeapon]})

        print(f"Your attack has increased by {weapons[chosenWeapon]}\n")

    elif AorW == 2:
        print("\nYou have found a armour chest\n")
        print("And inside you find........\n")

        temp = rand.choices(list(armour), weights = (45,25,15,10,5),k = 1)
        # Choices selects items on a list randomly but with weighted probability 
        chosenArmour = temp[0]
        print(f"A {chosenArmour}!!\n")
        avatar.defense += armour[chosenArmour]

        avatar.inventory[chosenArmour] = armour[chosenArmour]

        print(f"Your defense has increased by {armour[chosenArmour]}\n")

def Encounter(chosenenemie): # When the user finds an enemy 
    # this function runs the battle system
    enemieChoices = ["A","S","R"]
    print(f"\nYou encouter a {chosenenemie.name}!!!\n")
    print("Time To Fight")
    runned_away = None
    Flag = True
    while avatar.health > 0 and chosenenemie.health > 0 and Flag == True:
        # Turn based attack that loops until the enemy or the player dies or 
        # if the player or enemy run away
        print("""
              ______________________     
              |  Attack Press 'A'  |     
              ----------------------     
                   
         _____________________    ______________________
         |  Block Press 'B'  |    |  Steal Press 'S'  |
         ---------------------    ----------------------

              ___________________
              |  Run Press 'R'  |
              -------------------
        """)
        user_input= input("")
        if user_input == 'A' or user_input == 'a':
            print(f"\nYou have attacked the {chosenenemie.name}\n")
            chosenenemie.health -= avatar.attack
            print(f"\nYou have done {avatar.attack} damage\n")

        elif user_input == 'B' or user_input == 'b':
            print(f"\nYou put up your defense\n")

        elif user_input == 'S' or user_input == 's':
            print(f"\nYou attempt to steal from the {chosenenemie.name}\n")
            ChanceofSteal = [True,False]
            IsStolen = rand.choices(ChanceofSteal, weights = (25,75),k = 1)
            if IsStolen[0] == True:
                print(f"You have stolen {chosenenemie.coins}"
                     " from the {chosenenemie.name}\n")
                avatar.coins += chosenenemie.coins
            else:
                print(f"You failed to steal {chosenenemie.coins}"
                     " from the {chosenenemie.name}\n")

        elif user_input == 'R' or user_input == 'r':
            ChanceofRun = [True,False]
            IsRun = rand.choices(ChanceofRun, weights = (75,25),k = 1)
            runned_away = IsRun[0]
            if runned_away == True:
                print(f"You have ran away from the battle \n")
                Flag = False
            else:
                print(f"You failed to run away from the battle \n\n")

        else:
             print("Error Wrong input")
        #Players available battle options to choose

        enemieChoice = rand.choices(enemieChoices, weights = (50,10,10),k = 1)

        if enemieChoice[0] == "A":
            print(f"\n{chosenenemie.name} attacks you!!")

            if user_input == 'B' or user_input == 'b':
                extraAttack = chosenenemie.attack - avatar.defense
                avatar.health -= extraAttack
                print(f"\nYou have taken {extraAttack} damage and succesfully"
                     " blocked the attack\n")

                if avatar.health == 0 or avatar.health < 0:
                    print("YOU DIED")
                    quit()
            
            elif runned_away == True:
                pass

            else:
                avatar.health -= chosenenemie.attack
                print(f"\nYou have taken {chosenenemie.attack} damage")
                if avatar.health == 0 or avatar.health < 0:
                    print("YOU DIED")
                    quit()

        elif enemieChoice[0] == "S":
            print(f"\n{chosenenemie.name} tries to steal from you!!")
            ChanceofSteal = [True,False]
            IsStolen = rand.choices(ChanceofSteal, weights = (15,85),k = 1)

            if IsStolen[0] == True:
                print(f"You have lost {avatar.coins} coins\n")
                chosenenemie.coins += avatar.coins

            else:
                print(f"{chosenenemie.name} failed to steal"
                     f" {avatar.coins} from you\n")

        elif enemieChoice[0] == "R":
            ChanceofRun = [True,False]
            IsRun = rand.choices(ChanceofRun, weights = (25,75),k = 1)

            if IsRun[0] == True:
                print
                (f"\n{chosenenemie.name} has ran away from the battle \n")
                Flag = False
            else:
                print(f"\n{chosenenemie.name} failed to run"
                     " away from the battle \n")

        elif avatar.health == 0 or avatar.health < 0:
            print("\nYOU DIED")
            quit()

    if chosenenemie.health == 0 or chosenenemie.health < 0:
        print("\nYou Won The Battle\n")

    elif Flag == False:
        print("\nThe Battle ended abrubptly\n")

    elif avatar.health == 0 or avatar.health < 0:
            print("\nYOU DIED")
            quit()

    print(vars(avatar))
