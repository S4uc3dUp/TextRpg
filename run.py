from textrpg.game_flow import GameFlow
from textrpg.player import Hero
from textrpg.enemies import enemies
from textrpg.store import store

game = GameFlow(hero=Hero, enemies=enemies, store=store)

game.start()