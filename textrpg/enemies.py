
from textrpg.store import Dagger, RustySword, SmallKnife, HealthPotion10

class Enemy:

    def __init__(self, name, maxhealth, health, attack, goldgain, potiondrop, weapondrop, expdrop, min_hero_lvl):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.attack = attack
        self.goldgain = goldgain
        self.potiondrop = potiondrop
        self.weapondrop = weapondrop
        self.expdrop = expdrop
        self.min_hero_lvl = min_hero_lvl


Goblin = Enemy(name='Goblin', maxhealth=1, health=1, attack=4, goldgain=3, potiondrop=[], weapondrop=[], expdrop=2, min_hero_lvl=1)
Zombie = Enemy(name='Zombie', maxhealth=2, health=2, attack=6, goldgain=5, potiondrop=[HealthPotion10], weapondrop=[RustySword], expdrop=5, min_hero_lvl=1)
Skeleton = Enemy(name='Skeleton', maxhealth=5, health=5, attack=8, goldgain=10, potiondrop=[HealthPotion10], weapondrop=[SmallKnife], expdrop=8, min_hero_lvl=1)

GoldGoblin = Enemy(name='Gold Goblin', maxhealth=10, health=10, attack=10, goldgain=5, potiondrop=[], weapondrop=[SmallKnife], expdrop=5, min_hero_lvl=4)
GoldZombie = Enemy(name='Gold Zombie', maxhealth=20, health=20, attack=15, goldgain=10, potiondrop=[HealthPotion10], weapondrop=[SmallKnife], expdrop=10, min_hero_lvl=4)
GoldSkeleton = Enemy(name='Gold Skeleton', maxhealth=50, health=50, attack=20, goldgain=30, potiondrop=[HealthPotion10], weapondrop=[RustySword, Dagger], expdrop=30, min_hero_lvl=4)

enemies = [Goblin, Zombie, Skeleton, GoldGoblin, GoldZombie, GoldSkeleton]
