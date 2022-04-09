class Enemy:

    def __init__(self, name, maxhealth, health, attack, goldgain, potiondrop, weapondrop, expdrop):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.attack = attack
        self.goldgain = goldgain
        self.potiondrop = potiondrop
        self.weapondrop = weapondrop
        self.expdrop = expdrop


Goblin = Enemy(name='Goblin', maxhealth=1, health=1, attack=4, goldgain=3, potiondrop=1, weapondrop=1, expdrop=2)
Zombie = Enemy(name='Zombie', maxhealth=2, health=2, attack=6, goldgain=5, potiondrop=0, weapondrop=0, expdrop=5)
Skeleton = Enemy(name='Skeleton', maxhealth=5, health=5, attack=8, goldgain=10, potiondrop=1, weapondrop=0, expdrop=8)
