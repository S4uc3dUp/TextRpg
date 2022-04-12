import sys
import os
import random


class GameFlow:
    def __init__(self, hero, enemies, store):
        self.hero = hero
        self.enemies = enemies
        self.store = store
    
    def startMenu(self):
        print("Welcome To My Game!\n")
        print("1.) Start")
        print("2.) Load")
        print("3.) Exit")

        option = input(">> ")
        if option == "1":
            self.setHeroName()
        elif option == "2":
            pass
        elif option == "3":
            sys.exit()
        else:
            self.startMenu()
    
    def setHeroName(self):
        self.clear()
        print("\nHello, what is your name?")
        self.hero.name = input(">> ")
        self.hero.set_up_hero()
        self.mainMenu()


    def mainMenu(self):
        self.clear()
        print("\n")
        print(f"Hero Name: {self.hero.name}") 
        print(f"Level: {self.hero.base_level} ")
        print(f"Experience: {self.hero.exp}/{self.hero.max_exp}")
        print(f"Health: {self.hero.health}/{self.hero.maxhealth}")
        print(f"Gold: {self.hero.gold}")
        print(f"Potions: {len(self.hero.potions)}")
        print(f"Attack: {self.hero.attack_value}")
        print(f"Weapon: {self.hero.current_weapon.name}")

        print("\n")
        print("1:) Fight")
        print("2:) Inventory")
        print("3:) Store")
        print("4:) Save")
        print("5:) Exit")

        option = input(">> ")

        if option == "1":
            self.preFight()
        elif option == "2":
            self.inventoryMenu()
        elif option == "3":
            self.storeMenu()
        elif option == "4":
            self.save()
        elif option == "5":
            sys.exit()
        else:
            self.mainMenu()
    
    def inventoryMenu(self):
        self.clear()
        print("what do you want to do?")
        print("1.) Equip Weapon")
        print("b.) go back")
        option = input(">> ")
        if option == "1":
            self.equip()
        elif option == "b":
            self.mainMenu()
    
    def equip(self):
        self.clear()
        print("What do you want to equip?")
        for number, weapon in enumerate(self.hero.inventory):
            print(f"{number+1}:) {weapon.name}")
        print("b.) to go back")
        option = input(">> ")

        try:
            option = int(option)
            option -= 1
        except ValueError:
            pass

        if option == self.hero.current_weapon:
            print("you already have that weapon equipped")
            input(">> press enter to continue")
            self.equip()
        elif option == "b":
            self.inventoryMenu()
        elif option in range(len(self.hero.inventory)):
            self.hero.current_weapon = self.hero.inventory[option]
            self.hero.set_attack_value()
            print(f"You have equipped {self.hero.inventory[option].name}")
            input(">> press enter to continue ")
            self.equip()
        else:
            self.clear()
            print(f"you don't have {self.hero.inventory[option].name} in your inventory")
            input(">> press enter to continue")
            self.mainMenu()

    


    def getEnemy(self):
        enemy = random.choice(self.enemies)
        return enemy
    
    def preFight(self):
        while True:
            self.enemy = self.getEnemy()
            if self.enemy.min_hero_lvl > self.hero.base_level:
                pass
            else:
                break
        self.fight()
    
    def fight(self):
        self.clear()
        print(f"{self.hero.name} is fighting {self.enemy.name}")
        print(f"\n{self.hero.name}'s Health: {self.hero.health} / {self.hero.maxhealth}      {self.enemy.name}'s Health: {self.enemy.health} / {self.enemy.maxhealth}")

        print(f"Potions {len(self.hero.potions)} ")

        print("\n1.) Attack")
        print("2.) Drink Potion")
        print("3.) Run")

        option = input(">> ")

        if option == "1":
            self.attack()
        elif option == "2":
            self.drinkpotion()
        elif option == "3":
            self.run()
        else:
            self.fight()
    
    def attack(self):
        self.clear()
        p_attack = random.randint(0, self.hero.base_attack)
        e_attack = random.randint(0, self.enemy.attack)

        if p_attack == 0:
            print("You miss!")
        else:
            self.enemy.health -= p_attack
            print("You deal %i damage! " % p_attack)
        if self.enemy.health <= 0:
            self.win()

        if e_attack == 0:
            print("The enemy missed!")
        else:
            self.hero.health -= e_attack
            print("The enemy deals %i damage" % e_attack)
        if self.hero.health <= 0:
            self.dead()
        else:
            input(">> Press enter to continue")
            self.fight()

    def drinkpotion(self):
        self.clear()
        if len(self.hero.potions) == 0:
            print("You don't have any potions!")
            input(">> Press enter to continue")
            self.fight()
        elif len(self.hero.potions) >= 1:
            if self.hero.health < self.hero.maxhealth:
                potion = self.hero.potions.pop()
                self.hero.health += potion.hp_up
                #Hero.health = Hero.maxhealth
                print("You drink a potion!")
                #Hero.potions -= 1
                input(">> Press enter to continue")
                self.fight()

            if self.hero.health == self.hero.maxhealth:
                print("You already have full health")
                input(">> Press enter to continue")
                self.fight()
    
    def run(self):
        self.clear()
        run_num = random.randint(1, 3)

        if run_num == 1:
            print("You have successfully ran away!")
            input(">> Press enter to continue ")
            self.enemy.health = self.enemy.maxhealth
            self.mainMenu()
        else:
            print("you failed to get away!")

            e_attack = random.randint(self.enemy.attack / 2, self.enemy.attack)
            if e_attack == self.enemy.attack / 2:
                print("The enemy missed!")
            else:
                self.hero.health -= e_attack
                print("The enemy deals %i damage" % e_attack)

            if self.hero.health <= 0:
                self.dead()
            else:
                input(">> Press enter to continue ")
                self.fight()

    def win(self):
        self.clear()
        hero_level = self.hero.base_level

        # This is not a proper way to deal with probability (not in this case)
        # e_droppotion = random.randint(1, 4)
        # e_weapondrop = random.randint(1, 5)

        # First we get a random float from 0.0 to 1.0
        weapon_drop_chance = random.random()
        potion_drop_chance = random.random()

        self.enemy.health = self.enemy.maxhealth
        self.hero.gold += self.enemy.goldgain
        self.hero.exp += self.enemy.expdrop

        print(f"You have defeated the {self.enemy.name}")
        print(f"Enemy dropped {self.enemy.goldgain} gold!")
        print(f"You have gained {self.enemy.expdrop} experience")

        if len(self.enemy.weapondrop) > 0:
            if weapon_drop_chance > 0.10:
                weapon_dropped = random.choice(self.enemy.weapondrop)
                self.hero.inventory.append(weapon_dropped)
                print(f"Enemy dropped a {weapon_dropped.name}, added to inventory")
        
        if len(self.enemy.potiondrop) > 0:
            if potion_drop_chance > 0.10:
                potion_dropped = random.choice(self.enemy.potiondrop)
                self.hero.potions.append(potion_dropped)
                print(f"Enemy dropped a {potion_dropped.name} with {potion_dropped.hp_up} HP, saved to potions")

        self.hero.check_level_up()
        if hero_level != self.hero.base_level:
            print(f"you leveled up to level {self.hero.base_level}!")

        input(">> Press enter to continue")
        self.mainMenu()
    
    def dead(self):
        self.clear()
        g_amount = random.randint(1, 10)
        print("you have died")
        self.enemy.health = self.enemy.maxhealth
        self.hero.health = self.hero.maxhealth
        self.hero.gold -= g_amount

        if self.hero.gold >= 0:
            print("You lost %i gold" % g_amount)

            if self.hero.gold == 0:
                print("You lost all your gold")

        elif self.hero.gold < 0:
            print("You have no more gold")
            self.hero.gold = 0
        input(">> Press enter to continue")
        self.mainMenu()
    
    def storeMenu(self):
        self.clear()

        print("Welcome to the shop!")
        print("\nType the item number you would like to buy")
        print("\nWhat would you like to buy?\n")

        for number, item in enumerate(self.store['weapons']):
            print(f'{number+1}:) {item.name}')
        #print("Rusty Sword")
        #print("Dagger")
        print("\nb.) Go Back")

        option = input(">> ")

        try:
            option = int(option)
            option -= 1
        except ValueError:
            pass


        
        if option == "b":
            self.mainMenu()
        
        if option in range(len(self.store['weapons'])):
            print(f'You would like to buy: {self.store["weapons"][option].name}')
            print(f'Price: {self.store["weapons"][option].value}')
            print(f'Damage: {self.store["weapons"][option].damage}')
            yes = input('Type y or n (yes or no): ')

            if yes == 'y':
                if self.hero.gold >= self.store['weapons'][option].value:
                    self.hero.gold -= self.store['weapons'][option].value
                    print(f"You have bought {self.store['weapons'][option].name}")
                    input(">> press enter to continue ")
                    self.hero.inventory.append(self.store['weapons'][option])
                    self.mainMenu()
                else:
                    self.clear()
                    print("you don't have enough gold")
                    input(">> press enter to continue")
                    self.store()
            else:
                self.clear()
                self.store()

        else:
            #clear()
            print("That item does not exist")
            input(">> press enter to continue")
            self.store()



    def start(self):
        self.startMenu()

    def save(self):
        pass

    def load(self):
        pass


    @staticmethod
    def clear():
        os.system('cls')