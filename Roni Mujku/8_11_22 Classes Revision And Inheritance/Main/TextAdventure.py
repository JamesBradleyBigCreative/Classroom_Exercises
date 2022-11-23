from Characters import *
from gamefunctions import *
import random as rand

avatar = Player() # Initializing the users class

def Explore(isplaying): # Prompts the user to choose whether or not to 
    # explore a given location
    locations = ["You Have Found A Dungeon",
              "You Have Found An Forest",
              "You Have Found A Town",
              "You Have Found A Temple",
              "You Have Found A Ruin"] # Available Locations to explore
    while isplaying == True:

        Movement()

        shortcurrentlocation = Randomizer(locations,'S') # Randomly chooses a location

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
    single_loop = True
    while single_loop == True:
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
        print ("""
        __________________________  
        |  View Stats Press 'V'  |
        --------------------------
        """)
    
        Direction = input("")
        Direction = Direction.upper()

        if Direction == 'N':
            print("\nYou are heading North....\n")
            clear()
            single_loop = False

        elif Direction == 'E':
            print("\nYou are heading East....\n")
            clear()
            single_loop = False

        elif Direction == 'W':
            print("\nYou are heading West....\n")
            clear()
            single_loop = False

        elif Direction == 'S':
            print("\nYou are heading South....\n")
            clear()
            single_loop = False

        elif Direction == 'V':
            print(vars(avatar))

        elif Direction == 'Q':
            quit()

        else:
             print("\nError Wrong input")


def  indepthExplore(currentloc): # When the user chooses to explore a 
    # location deeper in Explore() this function is called
    # Randomly generates a event that happens to the user and runs 
    # correlating functions
    events = [f"In the {currentloc} you find a chest",
              f"In the {currentloc} you find an enemy encounter",
              f"In the {currentloc} you find nothing",
              f"In the {currentloc} you find treasure",
              f"In the {currentloc} you find a merchant",
              f"You enter the {currentloc}"
              ]

    print(f"\nYou delve deeper into the {currentloc}\n")

    #chosenevent = Randomizer(events,'L')
    chosenevent = events[4]
    # Randomly Chooses the event

    if chosenevent == events[0]:
        print(events[0])
        Chest()

    elif chosenevent == events[1]:
        print(events[1])
        chosenenemie = Randomizer(enemies,"L")
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
        Merchant()

    elif chosenevent == events[5]:
        print(events[5])
        Colosseum()
        
    # Calling the correlating functions according to the event generated

def Chest(): # When a user encounters a chest this function
   # randomly generates an item from the global dictionarys armour and weapons
    AorW = rand.randint(1,2)

    if AorW == 1:
        print("\nYou have found a weapon chest\n")
        print("And inside you find........\n")
        chosenWeapon = EquipmentRandomizer("weapon")
        avatar.attack += weapons[chosenWeapon]
        avatar.equipment_inventory.update({chosenWeapon: weapons[chosenWeapon]})
        print(f"Your attack has increased by {weapons[chosenWeapon]}\n")

    elif AorW == 2:
        print("\nYou have found a armour chest\n")
        print("And inside you find........\n")
        chosenArmour = EquipmentRandomizer("armour")
        avatar.defense += armour[chosenArmour]
        avatar.equipment_inventory[chosenArmour] = armour[chosenArmour]
        print(f"Your defense has increased by {armour[chosenArmour]}\n")


def Encounter(chosenenemie): # When the user finds an enemy 
    # this function runs the battle system
    enemieChoices = ["A","S","R"]
    print(f"\nYou encounter a {chosenenemie.name}!!!\n")
    print("Time To Fight")
    runned_away = None
    Flag = True
    while avatar.health > 0 and chosenenemie.health > 0 and Flag == True:
        Turn_over = False
        while Turn_over == False:
            # Turn based attack that loops until the enemy or the player dies or 
            # if the player or enemy run away
            print("""
             ______________________    ______________________
             |  Attack Press 'A'  |    |   Run Press 'R'    |
             ----------------------    ----------------------
                   
             ______________________    ______________________
             |  Block Press 'B'   |    |  Steal Press 'S'   |
             ----------------------    ----------------------

             ______________________    ______________________
             |View Stats Press 'V'|    | Use Item Press 'I' |
             ----------------------    ----------------------
            """)
            user_input= input("")
            user_input = user_input.upper()

            if user_input == 'A':
                print(f"\nYou have attacked the {chosenenemie.name}\n")
                chosenenemie.health -= avatar.attack
                print(f"\nYou have done {avatar.attack} damage\n")
                Turn_over = True

            elif user_input == 'B':
                print(f"\nYou put up your defense\n")
                Turn_over = True

            elif user_input == 'S':
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
                Turn_over = True

            elif user_input == 'R':
                ChanceofRun = [True,False]
                IsRun = rand.choices(ChanceofRun, weights = (75,25),k = 1)
                runned_away = IsRun[0]
                if runned_away == True:
                    print(f"You have ran away from the battle \n")
                    Flag = False
                else:
                    print(f"You failed to run away from the battle \n\n")
                Turn_over = True

            elif user_input == 'V':
                print(vars(avatar))

            elif user_input == 'I':
                print("\nYou open your bag and use a potion")
                temp = avatar.item_inventory.pop()
                avatar.health += temp
                print(f"\nYou healed {temp} HP")
                print(avatar.item_inventory)

            else:
                 print("Error Wrong input")
            #Players available battle options to choose

        enemieChoice = rand.choices(enemieChoices, weights = (50,10,10),k = 1)

        if enemieChoice[0] == "A":
            print(f"\n{chosenenemie.name} attacks you!!")

            if user_input == 'B' or user_input == 'b':
                extra_attack = chosenenemie.attack - avatar.defense
                if extra_attack < 0:
                    print(f"\nYou have taken 0 damage and succesfully"
                     " blocked the attack\n")
                else:
                    avatar.health -= extra_attack
                    print(f"\nYou have taken {extra_attack} damage and succesfully"
                         " blocked the attack\n")

                if avatar.health == 0 or avatar.health < 0:
                    print("YOU DIED")
                    quit()
            
            elif runned_away == True:
                Flag = False

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
        avatar.level_up(chosenenemie.exp)
        avatar.coins += chosenenemie.coins


    elif Flag == False:
        print("\nThe Battle ended abrubptly\n")

    elif avatar.health == 0 or avatar.health < 0:
            print("\nYOU DIED")
            quit()

    print(vars(avatar))


def Colosseum():

    print(f"\nInside you find a Colosseum\n")
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


def Merchant():
    print("\n'Hello traveller, Would you like to purchase some wares?'")
    print("\nThe merchant show you the 5 items he has for sale")
    wares = []
    for i in range (5):
        temp = (rand.randint(1,3))
        if temp == 1:
            wares.append(EquipmentRandomizer("weapon"))
        elif temp == 2:
            wares.append(EquipmentRandomizer("armour"))
        else:
            print("A Potion!!!\n")
            Potion = randint(30,55)
            wares.append(Potion)
    print(f"\nThe merchants wares are {wares}")
    correctinput = False
    while correctinput == False:
        try:
            Choice = int(input("Which ware do you buy 1,2,3,4 or 5: "))
            if isinstance(Choice,int) == False or Choice > 5 or Choice < 1:
                print("Error Wrong Input")
            else:
                correctinput = True
        except:
            print("Error input not int")

    Choice -= 1
    if avatar.coins < 15:
        print(f"\n'Sorry, {avatar.name}. I can't give credit. Come back when you're a little... mmmmm... richer!'")

    else:
        print(f"\nYou bought the {wares[Choice]} for 15 coins")

        if wares[Choice] in weapons:
            avatar.coins -= 15
            avatar.equipment_inventory.update({wares[Choice]:weapons[wares[Choice]]})
            print(avatar.equipment_inventory)
            avatar.attack += weapons[wares[Choice]]
        elif wares[Choice] in armour:
            avatar.coins -= 15
            avatar.equipment_inventory.update({wares[Choice]:armour[wares[Choice]]})
            print(avatar.equipment_inventory)
            avatar.defense += armour[wares[Choice]]
        elif isinstance(wares[Choice],int):
            avatar.coins -= 15
            avatar.item_inventory.append(wares[Choice])
            print(avatar.item_inventory)




