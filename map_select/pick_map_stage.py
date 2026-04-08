import pygame
import numpy as np
import map_select.revolvingQueue_utils
import time;
from gameplay.gameplay_stage import GamePlayStage

class PickMapStage:
    def __init__(self, arena, lives, two_player):
        pygame.init()
        pygame.mixer.init()

        self.arena = arena
        self.lives = lives
        self.two_player = two_player

        self.WIDTH = 800
        self.HEIGHT = 500
        self.GRAY = (34, 34, 34)
        self.WHITE = (255,255,255)
        self.CREME = (255, 255, 220)
        self.PINK = (220, 180, 160)
        self.BLACK = (0, 0, 0)
        self.SHEAR_X = 0.0
        self.SHEAR_Y = 0.1
        self.SCALE_INT = 150

        self.flipped = False
        self.check_ready = False

        self.my_font = pygame.font.Font("pick_characters/DIMIS___.TTF", 50)
        self.stage_font = pygame.font.Font("pick_characters/DIMIS___.TTF", 30)
        self.instruction_font = pygame.font.SysFont('Veranda', 20)
        self.ready_font = pygame.font.Font("pick_characters/DIMIS___.TTF", 200)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pick Arena")

        self.object_list = []
        self.scaled_sheared_list = []

        self.mostRecentDirection = -1

        self.load_assets()
        
    
    def load_assets(self):

        self.waffle_background_image = pygame.image.load('image_reference/background/waffle.jpg').convert_alpha()
        self.shelby_background_image = pygame.image.load('image_reference/background/shelby.jpg').convert_alpha()
        self.bdenny_map_background_image = pygame.image.load('image_reference/background/bdenny.jpg').convert_alpha()
        self.quad_map_background_image = pygame.image.load('image_reference/stage_select/quad.png').convert_alpha()
        self.rounders_map_background_image = pygame.image.load('image_reference/background/rounders.jpg').convert_alpha()

        self.map_image_list = [
            {"name": "Waffle House", "idx": 0, "image": self.waffle_background_image, "size": "Small", "elevation": "None", "dynamic": "Yes"},
            {"name": "Shelby Hall", "idx": 1, "image": self.shelby_background_image, "size": "Medium", "elevation": "Minimal", "dynamic": "No"},
            {"name": "Bryant-Denny Stadium", "idx": 2, "image": self.bdenny_map_background_image, "size": "Large", "elevation": "None", "dynamic": "Yes"},
            {"name": "The Quad ", "idx": 3, "image": self.quad_map_background_image, "size": "Large", "elevation": "None", "dynamic": "No"},
            {"name": "Rounders", "idx": 4, "image": self.rounders_map_background_image, "size": "Medium", "elevation": "Minimal", "dynamic": "Yes"}
        ]
        self.map_pointer_index = next(
            (i for i, m in enumerate(self.map_image_list) if m["name"] == "Bryant-Denny Stadium"),
            None
        )

        self.click_sound = pygame.mixer.Sound("image_reference/sounds/click.mp3")
        self.card_flip_sound = pygame.mixer.Sound("image_reference/sounds/cardFlip.mp3")
        self.select_sound = pygame.mixer.Sound("image_reference/sounds/select.mp3")
        self.elephant_sound = pygame.mixer.Sound("image_reference/sounds/elephant.mp3");

        return


    def updateGameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                
                if event.key == pygame.K_b:
                    if self.check_ready == True:
                        self.check_ready = False
                    else:
                        return ("PICK_CHARACTERS", {"arena": self.arena, "lives": self.lives, "two_player": self.two_player})

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_w:
                    self.card_flip_sound.play()
                    self.flipped = not self.flipped

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.click_sound.play()
                    map_select.revolvingQueue_utils.shift_right(self.map_image_list)
                    print("shift right")
                    self.flipped = False
                    self.map_pointer_index = self.map_pointer_index + 1
                    self.mostRecentDirection = -1
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.click_sound.play()
                    map_select.revolvingQueue_utils.shift_left(self.map_image_list)
                    self.map_pointer_index = self.map_pointer_index - 1
                    print("shift left")
                    self.flipped = False
                    self.mostRecentDirection = 0
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN or event.key == pygame.K_e:
                    self.select_sound.play()
                    print("select")

                    if self.check_ready == False:
                        self.check_ready = True
                    else:
                        self.elephant_sound.play();
                        time.sleep(2);
                        return ("BOOTSTRAP", {})
                    
                    # gameplay stages currently broken, so removed this
                    #return ("GAMEPLAY", {
                    #    "player1_character": "fireball",
                    #    "player2_character": "throwing_knife",
                    #    "MAP": self.map_image_list[self.map_pointer_index]["name"],
                    #    "arena": self.arena,
                    #    "lives": self.lives
                    #})
                
        self.screen.fill(self.PINK)

        text_surface = self.my_font.render("Select a Map", True, (0, 0, 0))

        # added to center text
        text_width = text_surface.get_width()
        x_position = (self.WIDTH - text_width) // 2
        self.screen.blit(text_surface, (x_position + 5, 40))

        text_surface = self.instruction_font.render("B for back     -", True, (0, 0, 0))
        self.screen.blit(text_surface, (40, 470))
        text_surface = self.instruction_font.render("Left/Right arrows to switch map        -       Up/Down arrows to flip map      -", True, (0, 0, 0))
        self.screen.blit(text_surface, (140, 470))
        text_surface = self.instruction_font.render("Enter or E to begin match", True, (0, 0, 0))
        self.screen.blit(text_surface, (630, 470))
        
        # original
        # self.screen.blit(text_surface, (190, 100))
        
        map_select.revolvingQueue_utils.render_maps(self.screen, self.map_image_list, self.object_list, self.stage_font, self.mostRecentDirection, self.flipped)

        if self.flipped:
            stats = [
                f"Size: {self.map_image_list[self.map_pointer_index]['size']}",
                f"Elevation: {self.map_image_list[self.map_pointer_index]['elevation']}",
                f"Dynamic: {self.map_image_list[self.map_pointer_index]['dynamic']}"
            ]
        
            # Draw stage stats
            for i, line in enumerate(stats):
                stat_surf = self.stage_font.render(line, True, self.WHITE)
                self.screen.blit(stat_surf, (300, 150 + (i * 35)))

            back_text = self.instruction_font.render("B: Back", True, self.BLACK)
            self.screen.blit(back_text, (20, 470))

        if(self.check_ready) == True:
            text_surface = self.ready_font.render("Ready?", True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.center = (self.WIDTH // 2, self.HEIGHT // 2)

            padding = 10
            bg_rect = pygame.Rect(
                0,
                text_rect.top - padding,
                self.WIDTH,
                text_rect.height + padding*2
            )
            bg_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
            bg_surface.fill((0, 0, 0, 200))
            self.screen.blit(bg_surface, (bg_rect.left, bg_rect.top))
            self.screen.blit(text_surface, text_rect.topleft)

        pygame.display.flip()
    
        return None