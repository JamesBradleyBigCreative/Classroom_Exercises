
from codecs import namereplace_errors


class player:
    def __innit__ (self,coins,health,name):
        self.coins = coins
        self.health = health
        self.name = name

class scene:
    scene_1 = "While on your journey you have stumbled across a coin"
    scene_2 = "You have come across a foe"
    scene_3 = "You have found a a heart"
    scene_4 = "You were robbed!"

class batman:
    coins = 999999999999
    health = 100000
    name = "Batman"
    
    scene_1 = "You are fighting joker and all of a sudden you get hit with dynamite"
    scene_2 = "You land a heavy hit on joker and follow up with the batarang"
    scene_3 = ""
