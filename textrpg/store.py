class Weapon:
    def __init__(self, name, value, damage, quantity):
        self.name = name
        self.value = value
        self.damage = damage
        self.quantity = quantity


class Potion:
    def __init__(self, name, value, hp_up):
        self.name = name
        self.value = value
        self.hp_up = hp_up

HealthPotion10 = Potion('Health potion', 1, 10)



SmallKnife = Weapon(name='Small Knife', value=1, damage=1, quantity=1)
RustySword = Weapon(name='Rusty Sword', value=8, damage=3, quantity=1)
Dagger = Weapon(name='Dagger', value=20, damage=5, quantity=1)

store_weapons = [SmallKnife, RustySword, Dagger]

store = {
    'weapons': store_weapons,
    'potions': [HealthPotion10]
}
