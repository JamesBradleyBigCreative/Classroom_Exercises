from characters import *

player_1 = Player()
enemy_1 = Goblin()
enemy_2 = Hobgoblin()

def quit_game():
    end = input("are you sure you would like to quit? Y/N ? ")
    if end == "Y" or end == "y":
        print("game over.")
        quit()
    elif end == "N" or end == "n":
        isPlaying = True
        print("great.")
        



class scene():  
    scene1 = "You have discovered a Cave!" #Goblins or no goblins?
    scene2 = "You found an Apple Tree!" #health up !1!1
    scene3 = "You have discovered a home!" #attack up potion 
    scene4 = ""
    
randnum = randint(10,35)

def fight_scene():
     print(""" Choose an Attack Move: 
            A - Kick  B - Super Punch C - uppercut 
            """) 
     fight = input("Enter A, B or C: ")
     if fight == "a" or fight == "A":
       print("You have defeated the goblin! The enemy health  is now: " , enemy_1.health - 28)
     if fight == "B" or fight == "b":
       print("You have defeated the goblin!  The enemy health  is now: " , enemy_1.health - 40 )
     if fight == "c" or fight == "C":
       print( "oh no! the goblin bit you! your health is ", player_1.health - 15)
     else:
       print("the goblin attacked you. your health is now " , player_1.health - randnum)


        