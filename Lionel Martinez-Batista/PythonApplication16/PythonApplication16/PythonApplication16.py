class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

        #if user chooses ranger
chosenPlayer = Player("Ranger", 60)

chosenPlayer.health

class Scene:
    scene_1 = "gncbncgbjngvjvbjvb"


Ranger = {
    'Hp': 60,
    'AttackDmg': 70,
    'Speed': 80,
    'Range': 200,
    'CritMultiplyer': 3
    }
Tank = {
    'Hp': 250,
    'AttackDmg': 95,
    'Speed': 60,
    'Range': 10,
    'CritMultiplyer': 1.6
    }
Brawler = {
    'Hp': 100,
    'AttackDmg': 75,
    'Speed': 100,
    'Range': 50,
    'CritMultiplyer': 2.2
    }


print('Choose your class \n' 'Brawler: \n', Brawler ,'\n Ranger \n', Ranger,'\n Tank \n', Tank,'\n')


Class = input(": ")

if Class == 'Ranger' or Class == 'ranger':
    print('Your adventure starts with your bow... \n \n \n')
elif Class == 'Tank' or Class == 'tank':
    print('You take your shield and head on to adventure... \n \n \n')
elif Class == 'Brawler' or Class == 'brawler':
    print('You set to adventure with nothing but your fists to fend for yourself... \n \n \n')
else:
    print(' Class not available... \n \n \n yet \n \n \n')
    quit()
print('Generating story please wait... \n Tip: You shouldnt trust everything you see or hear...\n \n')
Choice1 = str(input('\n You find yourself in an intersection. \n A dense and dark forest to the right \n and a straight path to the mountains \n on the left \n where do you choose to go? \n right or left?  : '))




if Class == 'Ranger' or 'ranger' and  Choice1 == 'right' or 'Right':
    print('\n You enter the forest and encounter a dense atmosphere \n the silence is deafening and you feel eyes fixed on \n you as soon as you enter')
    RChoice2 = int(input(' You hear a scream in the distance but not too far, \n do you go investigate (1) or ignore and continue (2)? : '))
if RChoice2 == 2:
    int(input("You walk deeper into the forest ignoring the screams of anguish in the background where you encounter an old Cabin"))
if RChoice2 == 1:
    RChoice2A = int(input('\n You make your way in the direction of the noise and see three women. \n two of them are severely injured whilst the other one seems to be unscathed \n and standing in front of them with an evil grin on her face \n What will you do? wait patiently to see what happens (1) \n Take aim with your bow (2) \n Jump in peacefully and try to get insight on the situation (3): '))
    if RChoice2A == 1:
        print('\n You wait patiently to see what will happen and after a few seconds you witness the third woman turn into an abomination and before you had an opportunity to understand what you had seen, \n the creature pierces one of the women through her heart with spikes coming out of its body ')
        print('\n Status effect: In shock \n speed reduced by 10 points for 2 choices')
        print(Scene.scene_1)
        Ranger['Speed'] += 70
        print(' Your speed is now' ,Ranger['Speed']) #player.speed
        RChoice2A1 = int(input('\n What will you do? Take aim with your bow (1) \n Wait for the creature to leave (2) \n try to dash in, catch grab the woman and make a run for it (3): \n'))
        if RChoice2A1 == 1:
            print("You take aim to the monster's head...")
            print("Citical hit")
            print("200 - 210")
            print("The creature falls to the floor \n The woman noices you and thanks you")
            print("You escort the woman out of the forest")
            print("You head home with your head lowered as a life was lost due to your lack of action... \n \n Ranger Ending 1 'The Hero's guilty conscience'")
        elif RChoice2A1 == 2:
            print("You wait patiently, and left the woman to her fate, \n you cover your ears to not hear the slaughter and the screams being released by the poor woman /n after 10 solid minutes of torture, no more noise was heard \n Ranger Ending 5 'PG-16'")
        elif RChoice2A1 == 3:
            print("You ready to jump in and rescue the woman, \n you throw a rock in another direction to distract the creature and as soon as it's looked that way you make the run for it grabbing the woman on the go, \n the creature takes a while to notice you, long enough for you to gain distance but not enough to escape /n The creature impales right through bot you and the woman leaving you to bleed to death in the floor \n Ranger Ending 6 'Shocked'   ")
    elif RChoice2A == 2:
        print(" \n You take aim with your bow at the 3rd 'woman'...")
        print(" You hit the 'woman' with the arrow ")
        print(" 200 - 70")
        print(" The creature releases a demonic screech appearing to have come from within your nightmares")
        print(" You've been spotted, confrontation is inevitable")
        RChoice2A2 = int(input("\n The creature faces you with a hateful look on its face, waits patiently for your next move \n What will you do? \n Take aim with your bow (1) \n Relocate somewhere else to catch the creature off guard (2) \n Try to escape (3)"))
        if RChoice2A2 == 1:
            print("You take-")
            print("Before you had a chance to retract your bow the creature dashed at you with demonic speed \n and impaled you throught the chest with a spike coming out of its hand")
            print("Ranger ending 2 'Too slow'")
        elif RChoice2A2 == 2:
            print("You swiftly dash aside using trees and bushes at your advantage to distract the creature, \n it is now dishoriented")
            int(input("You climb a tree and the creature no longer knows where you are \n What will be your next course of action? Take aim with your bow (1) \n Remain hidden and wait for the creature to leave (2)"))
            print("You take aim with your bow...")
            print("Critical hit")
            print("130 - 210")
            print("The creature falls to the floor to never get back up again")
            print("The women thank you for saving them, you offer to accompany them out of the forest to ensure the were safe \n afterwards you head home with your head up feeling like the hero you are \n Ranger Ending 3 a 'Hero's duty'")
        elif RChoice2A2 == 3:
            print("You turn around to try to run away...")
            print("As soon as thecreature was out of your field of vision you saw your own beheaded body as the creature sliced your head clean off")
            print("Ranger Ending 4 'Coward's way out'")
