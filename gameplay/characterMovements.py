import pygame
import math
import player_utils
import projectile_utils
import boundary
import map_create
from projectile import NewProjectile
from player import NewPlayer
from gameplay_stage import GamePlayStage
import gameplay_stage

pygame.init()

# coin clip jpg is 1369p x 360p
# add lives and character stats in corner

MAP = 'map1'
arena = False

player1_character = 'fireball'
player2_character = 'throwing_knife'


game_over_font = pygame.font.SysFont('Veranda', 50)

running = True

current_stage = GamePlayStage('fireball', 'throwing_knife', MAP, arena)

while running:
    current_stage.updateGameplay()

pygame.quit()