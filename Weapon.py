class Weapon:

    def __init__(self, name, value, damage, quantity):
        self.name = name
        self.value = value
        self.damage = damage
        self.quantity = quantity


Fist = Weapon(name='Fist', value=0, damage=0, quantity=0)
SmallKnife = Weapon(name='Small Knife', value=1, damage=1, quantity=1)
RustySword = Weapon(name='Rusty Sword', value=8, damage=3, quantity=1)
Dagger = Weapon(name='Dagger', value=20, damage=5, quantity=1)
