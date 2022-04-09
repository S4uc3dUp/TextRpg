global player
weapons = {"Rusty Sword": 8, "Dagger": 20}


class Player:

    def __init__(self, name, maxhealth, health, base_attack, gold, potions, base_level, exp):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.base_attack = base_attack
        self.gold = gold
        self.potions = potions
        self.weap = []
        self.curweap = "Fist"
        self.base_level = base_level
        self.exp = exp

    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Fist":
            attack += 0

        if self.curweap == "Small Knife":
            attack += 2

        if self.curweap == "Rusty Sword":
            attack += 4

        if self.curweap == "Dagger":
            attack += 6

        return attack

    @property
    def level(self):
        level = Hero.base_level
        if self.exp >= 8:
            level += 1

        if self.exp >= 24:
            level += 1

        if self.exp >= 40:
            level += 1

        return level


Hero = Player('name', maxhealth=100, health=100, base_attack=10, gold=0, potions=0, base_level=1, exp=0)
