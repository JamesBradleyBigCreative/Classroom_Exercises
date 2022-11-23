import random as rand
from Characters import *

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


def Randomizer(list1,splitter):# Randomly chooses a location

    X = rand.randint(0,len(list1)-1)
    if splitter == 'S':
        print(list1[X])
        temp = list1[X].split(" ")
        y = temp.pop()
        return y
    elif splitter == 'L':
        y = list1[X]
        return y

def YesOrNo():
    pass

def GenerateEnemyList(number_of_enemies,enemy_list):
    generated_list = []

    try:
        # Asking user for number of enemies to generate
        number_of_enemies = int(number_of_enemies)
    except:
        print("Error Invalid Input")
        return None
    # Error Handling if the user doesnt input an integer

    if number_of_enemies <= 10 and number_of_enemies > 0:
        for i in range(number_of_enemies): # Populates the enemy list with how
           #many enemies are specified
            x = choices(list(enemy_list), weights = 
                    (30,25,20,15,10,5),k = 1)
            x = x[0]

            if x.name == "Slime":
                generated_list.append(Slime())

            elif x.name == "Goblin":
                generated_list.append(Goblin())

            elif x.name == "Hobgoblin":
                generated_list.append(HobGoblin())

            elif x.name == "Wild Dog":
                generated_list.append(WildDog())

            elif x.name == "Bandit":
                generated_list.append(Bandit())

            elif x.name == "Demon Knight":
                generated_list.append(DemonKnight())
    else:
        print("Error Invalid Number of Enemies")
        return None

    return generated_list

def clear():
    print("\n" * 100)
    # Clears the terminal

def EquipmentRandomizer(equip_type):
    # Randomizer for equipment

    if equip_type == "weapon":
        temp = rand.choices(list(weapons), weights =
        (50,25,15,10,5,50,25,15,10,5,50,25,15,10,5,),k = 1)
        # Choices selects items on a list randomly but with weighted probability 
        chosenWeapon =  temp[0]
        print(f"A {chosenWeapon}!!\n")
        return chosenWeapon
        

    elif equip_type == "armour":
        temp = rand.choices(list(armour), weights = (45,25,15,10,5),k = 1)
        # Choices selects items on a list randomly but with weighted probability 
        chosenArmour = temp[0]
        print(f"A {chosenArmour}!!\n")
        return chosenArmour