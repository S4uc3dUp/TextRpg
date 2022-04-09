import os
import random
import sys

import Enemy
import Weapon
from Player import *

global enemy
global weapon


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
    start1()


def start1():
    clear()

    print("\n")
    print("Hero Name: %s " % Hero.name)
    print("Level: %i " % Hero.level)
    print("Experience: %i " % Hero.exp)
    print("Health: %i/%i " % (Hero.health, Hero.maxhealth))
    print("Gold: %d " % Hero.gold)
    print("Potions: %d " % Hero.potions)
    print("Attack: %i " % Hero.attack)
    print("Weapon: %s " % Hero.curweap)

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
    global weapon
    print("What do you want to equip?")
    for weapon in Hero.weap:
        print("%s " % weapon)
    print("b.) to go back")
    option = input(">> ")
    if option == Hero.curweap:
        print("you already have that weapon equipped")
        input(">> press enter to continue")
        equip()
    elif option == "b":
        pinventory()
    elif option in Hero.weap:
        Hero.curweap = option
        print("You have equipped %s" % option)
        input(">> press enter to continue ")
        equip()
    else:
        clear()
        print("you don't have %s in your inventory" % option)
        input(">> press enter to continue")
        start1()


def prefight():
    global enemy
    e_set = {'Goblin', 'Zombie', 'Skeleton'}
    enemylist = random.choice(tuple(e_set))

    if enemylist == 'Goblin':
        enemy = Enemy.Goblin
    elif enemylist == 'Zombie':
        enemy = Enemy.Zombie
    else:
        enemy = Enemy.Skeleton

    fight()


def fight():
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
        attack()
    elif option == "2":
        drinkpotion()
    elif option == "3":
        run()
    else:
        fight()


def attack():
    clear()
    p_attack = random.randint(0, Hero.base_attack + Hero.attack)
    e_attack = random.randint(0, enemy.attack)

    if p_attack == 0:
        print("You miss!")
    else:
        enemy.health -= p_attack
        print("You deal %i damage! " % p_attack)
    if enemy.health <= 0:
        win()

    if e_attack == 0:
        print("The enemy missed!")
    else:
        Hero.health -= e_attack
        print("The enemy deals %i damage" % e_attack)
    if Hero.health <= 0:
        dead()
    else:
        input(">> Press enter to continue")
        fight()


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


def run():
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
            dead()
        else:
            input(">> Press enter to continue ")
            fight()


def win():
    clear()
    e_droppotion = random.randint(1, 4)
    e_weapondrop = random.randint(1, 5)

    enemy.health = enemy.maxhealth
    Hero.gold += enemy.goldgain
    Hero.exp += enemy.expdrop

    print("you have defeated the %s" % enemy.name)
    print("you found %i gold!" % enemy.goldgain)
    print("You have gained %i experience" % enemy.expdrop)

    if Hero.level:
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

    if Hero.level == 2:
        print("you leveled up to 2!")

    input(">> Press enter to continue")
    start1()


def dead():
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
    print("\nType the word of the item you would like to buy")
    print("\nWhat would you like to buy?\n")

    print("Rusty Sword")
    print("Dagger")
    print("\nb.) Go Back")

    option = input(">> ")
    if option == "b":
        start1()

    if option in weapons:
        if Hero.gold >= weapons[option]:
            Hero.gold -= weapons[option]
            print("You have bought %s" % option)
            input(">> press enter to continue ")
            Hero.weap.append(option)
            start1()
        else:
            clear()
            print("you don't have enough gold")
            input(">> press enter to continue")
            store()
    else:
        clear()
        print("That item does not exist")
        input(">> press enter to continue")
        store()


def save():
    pass


def clear():
    os.system('cls')


main()
