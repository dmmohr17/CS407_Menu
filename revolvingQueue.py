import pygame
import numpy as np
import revolvingQueue_utils

pygame.init()

WIDTH = 500
HEIGHT = 500
GRAY = (34, 34, 34)
WHITE = (255, 255, 220)
BLACK = (0, 0, 0)
SHEAR_X = 0.0
SHEAR_Y = 0.1

SCALE_INT = 150

my_font = pygame.font.SysFont('Veranda', 30)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pick Arena")

medieval_town_background_image = pygame.image.load('image_reference/background/medieval_town_background.jpg').convert_alpha()

object_list = []
scaled_sheared_list = []

#for i in range(5):

currentMap = 'map1'

#store maps and current positions. Shift left will subtract 1, shift right will add 1. Only 1-5 will be rendered
map_image_list = [
    {"name": "Town Hall", "idx": 0, "image": medieval_town_background_image},
    {"name": "map2", "idx": 1, "image": medieval_town_background_image},
    {"name": "Town Hall", "idx": 2, "image": medieval_town_background_image},
    {"name": "map4", "idx": 3, "image": medieval_town_background_image},
    {"name": "map5", "idx": 4, "image": medieval_town_background_image}
]


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            
            if event.key == pygame.K_RIGHT:
                revolvingQueue_utils.shift_right(map_image_list)
                print("shift right")
            if event.key == pygame.K_LEFT:
                revolvingQueue_utils.shift_left(map_image_list)
                print("shift left")
        
    if currentMap == 'map1':
        text_surface = my_font.render('Town Hall', True, (0, 0, 0))
    screen.fill(WHITE)
    
    revolvingQueue_utils.render_maps(screen, map_image_list, object_list, my_font)

    pygame.display.flip()