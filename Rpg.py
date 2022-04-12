import os
import random
import sys

# I have made a new folder inside called "textrpg" which has __init__.py script
# This tells python that folder is a module and you can freely import from it

from textrpg import enemies
#from textrpg import Weapon

# Never use import *, this will probably give you more trouble than anything
# Import just object you want to manipulate in this case its Hero, which is an instance of class Player

from textrpg.store import store_weapons
from textrpg.player import Hero 
from textrpg.enemies import enemies

#global enemy
#global weapon


def main():
    print("Welcome To My Game!\n")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")

    option = input(">> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        main()


def start():
    clear()
    print("\nHello, what is your name?")
    Hero.name = input(">> ")
    Hero.set_up_hero()
    start1()


def start1():
    #clear()

    # There are easyer way to format a string

    #print("\n")
    #print("Hero Name: %s " % Hero.name)
    #print("Level: %i " % Hero.level)
    #print("Experience: %i " % Hero.exp)
    #print("Health: %i/%i " % (Hero.health, Hero.maxhealth))
    #print("Gold: %d " % Hero.gold)
    #print("Potions: %d " % Hero.potions)
    #print("Attack: %i " % Hero.attack)
    #print("Weapon: %s " % Hero.curweap)

    print("\n")
    print(f"Hero Name: {Hero.name}") 
    print(f"Level: {Hero.base_level} ")
    print(f"Experience: {Hero.exp}/{Hero.max_exp}")
    print(f"Health: {Hero.health}/{Hero.maxhealth}")
    print(f"Gold: {Hero.gold}")
    print(f"Potions: {Hero.potions}")
    print(f"Attack: {Hero.attack_value}")
    print(f"Weapon: {Hero.current_weapon.name}")

    print("\n")
    print("1:) Fight")
    print("2:) Inventory")
    print("3:) Store")
    print("4:) Save")
    print("5:) Exit")

    option = input(">>")
    if option == "1":
        prefight()
    elif option == "2":
        pinventory()
    elif option == "3":
        store()
    elif option == "4":
        save()
    elif option == "5":
        sys.exit()
    else:
        start1()


def pinventory():
    clear()
    print("what do you want to do?")
    print("1.) Equip Weapon")
    print("b.) go back")
    option = input(">> ")
    if option == "1":
        equip()
    elif option == "b":
        start1()


def equip():
    clear()
    #global weapon
    print("What do you want to equip?")
    for number, weapon in enumerate(Hero.inventory):
        print(f"{number+1}:) {weapon.name}")
    print("b.) to go back")
    option = input(">> ")

    try:
        option = int(option)
        option -= 1
    except ValueError:
        pass

    if option == Hero.current_weapon:
        print("you already have that weapon equipped")
        input(">> press enter to continue")
        equip()
    elif option == "b":
        pinventory()
    elif option in range(len(Hero.inventory)):
        Hero.current_weapon = Hero.inventory[option]
        Hero.set_attack_value()
        print(f"You have equipped {Hero.inventory[option].name}")
        input(">> press enter to continue ")
        equip()
    else:
        clear()
        print(f"you don't have {Hero.inventory[option].name} in your inventory")
        input(">> press enter to continue")
        start1()


def get_enemy():
    enemy = random.choice(enemies)
    return enemy

def prefight():
    while True:
        enemy = get_enemy()
        if enemy.min_hero_lvl > Hero.base_level:
            pass
        else:
            break

#
#    if enemylist == 'Goblin':
#        enemy = Enemy.Goblin
#    elif enemylist == 'Zombie':
#        enemy = Enemy.Zombie
#    else:
#        enemy = Enemy.Skeleton
#
    fight(enemy)


def fight(enemy):
    clear()
    print("%s is fighting %s " % (Hero.name, enemy.name))
    print("\n%s's Health: %d / %d      %s's Health: %i / %i" % (Hero.name, Hero.health, Hero.maxhealth,
                                                                enemy.name, enemy.health, enemy.maxhealth))

    print("Potions %i " % Hero.potions)

    print("\n1.) Attack")
    print("2.) Drink Potion")
    print("3.) Run")

    option = input(">> ")

    if option == "1":
        attack(enemy)
    elif option == "2":
        drinkpotion()
    elif option == "3":
        run(enemy)
    else:
        fight(enemy)


def attack(enemy):
    clear()
    p_attack = random.randint(0, Hero.base_attack)
    e_attack = random.randint(0, enemy.attack)

    if p_attack == 0:
        print("You miss!")
    else:
        enemy.health -= p_attack
        print("You deal %i damage! " % p_attack)
    if enemy.health <= 0:
        win(enemy)

    if e_attack == 0:
        print("The enemy missed!")
    else:
        Hero.health -= e_attack
        print("The enemy deals %i damage" % e_attack)
    if Hero.health <= 0:
        dead(enemy)
    else:
        input(">> Press enter to continue")
        fight(enemy)


def drinkpotion():
    clear()
    if Hero.potions == 0:
        print("You don't have any potions!")
        input(">> Press enter to continue")
        fight()
    elif Hero.potions >= 1:
        if Hero.health < Hero.maxhealth:
            Hero.health += 50
            Hero.health = Hero.maxhealth
            print("You drink a potion!")
            Hero.potions -= 1
            input(">> Press enter to continue")
            fight()

        if Hero.health == Hero.maxhealth:
            print("You already have full health")
            input(">> Press enter to continue")
            fight()


def run(enemy):
    clear()
    run_num = random.randint(1, 3)

    if run_num == 1:
        print("You have successfully ran away!")
        input(">> Press enter to continue ")
        enemy.health = enemy.maxhealth
        start1()
    else:
        print("you failed to get away!")

        e_attack = random.randint(enemy.attack / 2, enemy.attack)
        if e_attack == enemy.attack / 2:
            print("The enemy missed!")
        else:
            Hero.health -= e_attack
            print("The enemy deals %i damage" % e_attack)

        if Hero.health <= 0:
            dead(enemy)
        else:
            input(">> Press enter to continue ")
            fight()


def win(enemy):
    clear()
    hero_level = Hero.base_level
    e_droppotion = random.randint(1, 4)
    e_weapondrop = random.randint(1, 5)

    enemy.health = enemy.maxhealth
    Hero.gold += enemy.goldgain
    Hero.exp += enemy.expdrop

    print("you have defeated the %s" % enemy.name)
    print("you found %i gold!" % enemy.goldgain)
    print("You have gained %i experience" % enemy.expdrop)

    if Hero.base_level:
        if enemy.name == "Skeleton":
            if e_droppotion == 1:
                Hero.potions += e_droppotion
                print("you have found %i potion" % e_droppotion)
            if enemy.name == "Goblin":
                if e_droppotion == 1:
                    Hero.potions += e_droppotion
                    print("you have found %i potion" % e_droppotion)
                if e_weapondrop == 2:
                    Hero.weap.append(Weapon.SmallKnife.name)
                    print("you found a %s " % Weapon.SmallKnife.name)

    Hero.check_level_up()
    if hero_level != Hero.base_level:
        print(f"you leveled up to {Hero.base_level}!")

    input(">> Press enter to continue")
    start1()


def dead(enemy):
    clear()
    g_amount = random.randint(1, 10)
    print("you have died")
    enemy.health = enemy.maxhealth
    Hero.health = Hero.maxhealth
    Hero.gold -= g_amount

    if Hero.gold >= 0:
        print("You lost %i gold" % g_amount)

        if Hero.gold == 0:
            print("You lost all your gold")

    elif Hero.gold < 0:
        print("You have no more gold")
        Hero.gold = 0
    input(">> Press enter to continue")
    start1()


def store():
    clear()

    print("Welcome to the shop!")
    print("\nType the item number you would like to buy")
    print("\nWhat would you like to buy?\n")

    for number, item in enumerate(store_weapons):
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
        start1()
    
    if option in range(len(store_weapons)):
        print(f'You would like to buy: {store_weapons[option].name}')
        print(f'Price: {store_weapons[option].value}')
        print(f'Damage: {store_weapons[option].damage}')
        yes = input('Type y or n (yes or no): ')

        if yes == 'y':
            if Hero.gold >= store_weapons[option].value:
                Hero.gold -= store_weapons[option].value
                print(f"You have bought {store_weapons[option].name}")
                input(">> press enter to continue ")
                Hero.inventory.append(store_weapons[option])
                start1()
            else:
                clear()
                print("you don't have enough gold")
                input(">> press enter to continue")
                store()
        else:
            clear()
            store()

    else:
        #clear()
        print("That item does not exist")
        input(">> press enter to continue")
        store()


def save():
    pass


def clear():
    os.system('cls')


main()