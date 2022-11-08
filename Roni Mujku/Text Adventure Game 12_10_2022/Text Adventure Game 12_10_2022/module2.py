import module1 as mod
import random as rand
import sys as system

avatar = mod.Player("Avatar",100,0,20,20,{})

weapons = {"Blunt Sword": 10,"Common Sword": 20,"Uncommon Sword":50,"Rare Sword":100,"Legendary Sword":200,
           "Blunt Dagger": 5,"Common Dagger": 10,"Uncommon Dagger":25,"Rare Dagger":50,"Legendary Dagger":100,
           "Broken Hammer": 20,"Common Hammer": 40,"Uncommon Hammer":100,"Rare Hammer":200,"Legendary Hammer":400,}

armour = {"Wooden Armour": 10,"Common Armour": 20,"Uncommon Armour": 50,"Rare Armour":100,"Legendary Armour":200,}

Slime = mod.Player("Slime",10,10,10,10,{})
Wild_Dog = mod.Player("WildDog",50,20,20,20,{})
Bandit = mod.Player("Bandit",100,50,50,50,{})
Demon_Knight = mod.Player("Demon_Knight",200,100,100,100,{})

enemies = [Slime,Wild_Dog,Bandit,Demon_Knight]


def Movement():
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
    elif Direction == 'E' or Direction == 'e':
        print("\nYou are heading East....\n")
    elif Direction == 'W' or Direction == 'w':
        print("\nYou are heading West....\n")
    elif Direction == 'S' or Direction == 's':
        print("\nYou are heading South....\n")
    elif Direction == 'Q' or Direction == 'q':
        quit()
    else:
         print("Error Wrong input")

def  indepthExplore(currentloc):
    events = [f"In the {currentloc} you find a chest",
              f"In the {currentloc} you find an enemy encounter",
              f"In the {currentloc} you find nothing",
              f"In the {currentloc} you find treasure",
              ]

    print(f"\nYou delve deeper into the {currentloc}\n")

    temp = rand.randint(0,len(events)-1)

    chosenevent = events[temp]

    if chosenevent == events[0]:
        Chest()
    elif chosenevent == events[1]:
        Encounter()
    elif chosenevent == events[2]:
        print("You Found Nothing Continue...\n")
    else:
        print("\nYou found treasure\n")
        coinsfound = rand.randint(0,100)
        print(f"You Got {coinsfound} coins!!!\n")
        avatar.coins += coinsfound


def Explore(isplaying):
    locations = ["You Have Found A Dungeon",
              "You Have Found An Forest",
              "You Have Found A Town",
              "You have Found A Temple"]
    while isplaying == True:

        Movement()

        X = rand.randint(0,len(locations)-1)
        print(locations[X])
        temp = locations[X].split(" ")
        shortcurrentlocation = temp[4]
        print("\nDo you wish to explore this area further or keep moving:\n")
        Choice = input("Press 'Y' to explore further or Press 'N' to keep moving or Press 'Q' to Quit: \n")
        if Choice == 'Y' or Choice == 'y':
            indepthExplore(shortcurrentlocation)
        elif Choice == 'N' or Choice == 'n':
            Movement()
        elif Choice == 'Q' or Choice == 'q':
            quit()
        else:
            print("Error Wrong input")

def Chest():
    AorW = rand.randint(1,2)

    if AorW == 1:
        print("\nYou have found a weapons chest\n")
        print("And inside you find........\n")
        temp = rand.choices(list(weapons), weights = (50,25,15,10,5,50,25,15,10,5,50,25,15,10,5,),k = 1)
        chosenWeapon =  temp[0]
        print(f"A {chosenWeapon}!!\n")
        avatar.attack += weapons[chosenWeapon]

        avatar.inventory.update({chosenWeapon: weapons[chosenWeapon]})

        print(f"Your attack has increased by {weapons[chosenWeapon]}\n")

    elif AorW == 2:
        print("\nYou have found a armour chest\n")
        print("And inside you find........\n")

        temp = rand.choices(list(armour), weights = (45,25,15,10,5),k = 1)
        chosenArmour = temp[0]
        print(f"A {chosenArmour}!!\n")
        avatar.defense += armour[chosenArmour]

        avatar.inventory[chosenArmour] = armour[chosenArmour]

        print(f"Your defense has increased by {armour[chosenArmour]}\n")

def Encounter():
    temp = rand.randint(0,len(enemies)-1)
    chosenenemie = enemies[temp]
    enemieChoices = ["A","S","R"]
    print(f"\nYou have encouter a {chosenenemie.name}!!!\n")
    print("Time To Fight")
    Flag = True
    while avatar.health > 0 and chosenenemie.health > 0 and Flag == True:

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
                print(f"You have stolen {chosenenemie.coins} from the {chosenenemie.name}\n")
                avatar.coins += chosenenemie.coins
            else:
                print(f"You failed to steal {chosenenemie.coins} from the {chosenenemie.name}\n")

        elif user_input == 'R' or user_input == 'r':
            ChanceofRun = [True,False]
            IsRun = rand.choices(ChanceofRun, weights = (75,25),k = 1)
            if IsRun[0] == True:
                print(f"You have ran away from the battle \n")
                Flag = False
                quit()
            else:
                print(f"You failed to run away from the battle \n\n")

        else:
             print("Error Wrong input")

        enemieChoice = rand.choices(enemieChoices, weights = (50,10,10),k = 1)
        if enemieChoice[0] == "A":
            print(f"\n{chosenenemie.name} attacks you!!")
            if user_input == 'B' or user_input == 'b':
                extraAttack = chosenenemie.attack - avatar.defense
                avatar.health -= extraAttack
                print(f"\nYou have taken {extraAttack} damage and succesfully blocked the attack\n")
                if avatar.health == 0 or avatar.health < 0:
                    print("YOU DIED")
                    quit()
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
                print(f"{chosenenemie.name} failed to steal {avatar.coins} from you\n")

        elif enemieChoice[0] == "R":
            ChanceofRun = [True,False]
            IsRun = rand.choices(ChanceofRun, weights = (25,75),k = 1)
            if IsRun[0] == True:
                print(f"{chosenenemie.name} has ran away from the battle \n")
                Flag = False
            else:
                print(f"{chosenenemie.name} failed to run away from the battle \n")

        elif avatar.health == 0 or avatar.health < 0:
            print("YOU DIED")
            quit()

    if chosenenemie.health == 0 or chosenenemie.health < 0:
        print("You Won The Battle\n")

    elif Flag == False:
        print("The Battle ended abrubptly")

    elif avatar.health == 0 or avatar.health < 0:
            print("YOU DIED")
            quit()