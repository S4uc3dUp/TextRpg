
from textrpg.store import Weapon

class Player:

    def __init__(self, name, maxhealth, health, base_attack, gold, base_level, exp):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.base_attack = base_attack
        self.attack_value = self.base_attack
        self.gold = gold
        #self.potions = potions
        self.inventory = []
        self.potions = []
        self.current_weapon = None
        self.base_level = base_level
        self.exp = exp
        self.max_exp = 8
    
    def set_up_hero(self):
        Fist = Weapon(name='Fist', value=0, damage=0, quantity=0)
        self.inventory.append(Fist)
        self.current_weapon = self.inventory[0]
    

    def check_level_up(self):
        if self.exp >= self.max_exp:
            self.base_level += 1
            self.max_exp = self.max_exp * 2

    # This is just 1 line with no repeating a code, which is how you should do it
    # Always make sure your code is DRY (dont repeat yourself)
    def set_attack_value(self):
        self.attack_value = self.base_attack + self.current_weapon.damage

    #@property
    #def attack(self):
    #    attack = self.base_attack
    #    if self.curweap == "Fist":
    #        attack += 0
    #
    #    if self.curweap == "Small Knife":
    #        attack += 2
    #
    #    if self.curweap == "Rusty Sword":
    #        attack += 4
    #
    #    if self.curweap == "Dagger":
    #        attack += 6
    #
    #    return attack

    #@property
    #def level(self):
    #    level = Hero.base_level
    #    if self.exp >= 8:
    #        level += 1
    #
    #    if self.exp >= 24:
    #        level += 1
    #
    #    if self.exp >= 40:
    #        level += 1
    #
    #    return level


Hero = Player('name', maxhealth=100, health=100, base_attack=10, gold=0, base_level=1, exp=0)
