import os
import sys
from sys import exit
import pygame
pygame.mixer.init()

class BootStrapStage:
    def __init__(self):
        pygame.init()

        self.arena = False
        self.lives = 3
        self.two_player = False

        self.current_menu = "main"
        self.main_options = ["Arcade", "Versus", "Options"]
        self.credits_option = "Credits"
        self.main_selected_idx = 0
        self.options_selected_idx = 0
        self.status_message = ""

        self.WIDTH = 800
        self.HEIGHT = 500
        self.GRAY = (34, 34, 34)
        self.CREME = (255, 255, 220)
        self.PINK = (220, 180, 160)
        self.BLACK = (0, 0, 0)
        self.CRIMSON = (154, 23, 37)

        if getattr(sys, 'frozen', False):
            font_path = os.path.join(sys._MEIPASS, 'pick_characters', 'DIMIS___.TTF')
            bgm_path = os.path.join(sys._MEIPASS, 'image_reference', 'sounds', 'YeaBama.mp3')
        else:
            font_path = 'pick_characters/DIMIS___.TTF'
            bgm_path = 'image_reference/sounds/YeaBama.mp3'

        self.title_font = pygame.font.Font(font_path, 56)
        self.option_font = pygame.font.Font(font_path, 38)
        self.small_option_font = pygame.font.Font(font_path, 20)
        self.help_font = pygame.font.Font(font_path, 20)
        self.credits_font = pygame.font.Font(font_path, 28)

        self.credits_lines = [
            "CS407 Fighting Game",
            "",
            "Created by",
            "Derek Mohr (The Idea Guy)",
            "Dylan Melnick (The Pygame Expert)",
            "Brock Kitterman (The Music Guy)",
            "Josh Keane (The Artist)",
            "Jackson Burke (The Bum)",
            "",
            "Press B or ESC to return"
        ]
        self.credits_scroll_y = self.HEIGHT - 70
        self.credits_line_spacing = 44
        self.credits_scroll_speed = .04  # Increase this for faster scrolling
        self.credits_top_limit = 145
        self.credits_bottom_limit = self.HEIGHT - 60

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("FIGHTING GAME")

        pygame.mixer.init()
        pygame.mixer.music.load(bgm_path)
        pygame.mixer.music.play(start=1.0, loops=-1)

    def updateGameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

                if self.current_menu == "main":
                    total_main_items = len(self.main_options) + 1

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.main_selected_idx = (self.main_selected_idx - 1) % total_main_items
                        self.status_message = ""

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.main_selected_idx = (self.main_selected_idx + 1) % total_main_items
                        self.status_message = ""

                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if self.main_selected_idx == len(self.main_options):
                            self.current_menu = "credits"
                            self.credits_scroll_y = self.credits_bottom_limit
                            self.status_message = ""
                            continue

                        selected_mode = self.main_options[self.main_selected_idx]
                        if selected_mode == "Arcade":
                            self.two_player = False
                            return ("PICK_CHARACTERS", {"arena": self.arena, "lives": self.lives, "two_player": self.two_player})
                        if selected_mode == "Versus":
                            self.two_player = True
                            return ("PICK_CHARACTERS", {"arena": self.arena, "lives": self.lives, "two_player": self.two_player})
                        self.current_menu = "options"
                        self.options_selected_idx = 0
                        self.status_message = ""

                elif self.current_menu == "options":
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_b:
                        self.current_menu = "main"
                        self.status_message = ""

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.options_selected_idx = (self.options_selected_idx - 1) % 3

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.options_selected_idx = (self.options_selected_idx + 1) % 3

                    if event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                        if self.options_selected_idx == 0:
                            self.arena = not self.arena
                        elif self.options_selected_idx == 1:
                            if event.key in (pygame.K_LEFT, pygame.K_a):
                                self.lives = max(1, self.lives - 1)
                            else:
                                self.lives = min(10, self.lives + 1)

                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if self.options_selected_idx == 0:
                            self.arena = not self.arena
                        elif self.options_selected_idx == 2:
                            self.current_menu = "main"
                            self.status_message = ""

                elif self.current_menu == "credits":
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_b:
                        self.current_menu = "main"
                        self.status_message = ""

        self.draw()

    def draw(self):
        self.screen.fill(self.PINK)

        if self.current_menu == "main":
            self.draw_main_menu()
        elif self.current_menu == "options":
            self.draw_options_menu()
        else:
            self.draw_credits_menu()

        if self.status_message != "":
            status_surface = self.help_font.render(self.status_message, True, self.BLACK)
            status_rect = status_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT - 70))
            self.screen.blit(status_surface, status_rect)

        pygame.display.flip()

        return None

    def draw_main_menu(self):
        title_surface = self.title_font.render("BAMA BASH", True, self.CRIMSON)
        title_rect = title_surface.get_rect(center=(self.WIDTH // 2, 110))
        self.screen.blit(title_surface, title_rect)

        start_y = 220
        spacing = 70
        for idx, option in enumerate(self.main_options):
            color = self.CRIMSON if idx == self.main_selected_idx else self.GRAY
            option_surface = self.option_font.render(option, True, color)
            option_rect = option_surface.get_rect(center=(self.WIDTH // 2, start_y + idx * spacing))
            self.screen.blit(option_surface, option_rect)

        credits_color = self.CRIMSON if self.main_selected_idx == len(self.main_options) else self.GRAY
        credits_surface = self.small_option_font.render(self.credits_option, True, credits_color)
        credits_rect = credits_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT - 84))
        self.screen.blit(credits_surface, credits_rect)

        help_surface = self.help_font.render("Use W/S or UP/DOWN to move, ENTER to select, Q to quit.", True, self.GRAY)
        help_rect = help_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT - 40))
        self.screen.blit(help_surface, help_rect)

    def draw_options_menu(self):
        title_surface = self.title_font.render("Options", True, self.BLACK)
        title_rect = title_surface.get_rect(center=(self.WIDTH // 2, 110))
        self.screen.blit(title_surface, title_rect)

        option_labels = [
            f"Arena: {'On' if self.arena else 'Off'}",
            f"Lives: {self.lives}",
            "Back"
        ]

        start_y = 220
        spacing = 70
        for idx, option in enumerate(option_labels):
            color = self.CRIMSON if idx == self.options_selected_idx else self.GRAY
            option_surface = self.option_font.render(option, True, color)
            option_rect = option_surface.get_rect(center=(self.WIDTH // 2, start_y + idx * spacing))
            self.screen.blit(option_surface, option_rect)

        help_surface = self.help_font.render(
            "UP/DOWN selects. LEFT/RIGHT changes values. ENTER confirms. B/ESC returns.", True, self.GRAY)
        help_rect = help_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT - 40))
        self.screen.blit(help_surface, help_rect)

    def draw_credits_menu(self):
        title_surface = self.title_font.render("Credits", True, self.BLACK)
        title_rect = title_surface.get_rect(center=(self.WIDTH // 2, 70))
        self.screen.blit(title_surface, title_rect)

        y = self.credits_scroll_y
        for line in self.credits_lines:
            line_surface = self.credits_font.render(line, True, self.GRAY)
            line_rect = line_surface.get_rect(center=(self.WIDTH // 2, y))
            if line_rect.bottom > self.credits_top_limit and line_rect.top < self.credits_bottom_limit:
                self.screen.blit(line_surface, line_rect)
            y += self.credits_line_spacing

        self.credits_scroll_y -= self.credits_scroll_speed
        total_height = len(self.credits_lines) * self.credits_line_spacing
        if self.credits_scroll_y + total_height < self.credits_top_limit:
            self.credits_scroll_y = self.credits_bottom_limit

        help_surface = self.help_font.render("Press B or ESC to return.", True, self.GRAY)
        help_rect = help_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT - 30))
        self.screen.blit(help_surface, help_rect)
