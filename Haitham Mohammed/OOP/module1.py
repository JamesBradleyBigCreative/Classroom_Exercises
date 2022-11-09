class mov:
    def __init__(self, weapon, health, coins, xp):
        self.weapon = weapon
        self.health = health
        self.coins = coins
        self.xp = 100


    def description(self):
        return f"Your weapon is  {weapon}, and your health is {health}, You have {coins} coins, and {xp} xp"
     