import pygame

class PickCharactersStage:
    def __init__(self, arena, lives):
        pygame.init()

        self.arena = arena
        self.lives = lives

        self.selectedIdx = 5
        self.selectedAltIdx = 0

        self.instruction_font = pygame.font.SysFont('Veranda', 20)

        self.WIDTH = 800
        self.HEIGHT = 500
        self.GRAY = (34, 34, 34)
        self.CREME = (255, 255, 220)
        self.BLACK = (0, 0, 0)

        # character icons on select grid
        self.character_images = [
            pygame.image.load("image_reference/chars/tide.jpg"),
            pygame.image.load("image_reference/chars/kalen.png"),
            pygame.image.load("image_reference/chars/ref.jpg"),
            pygame.image.load("image_reference/chars/jc.png"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/al.png"),
            pygame.image.load("image_reference/chars/nick.jpg"),
            pygame.image.load("image_reference/chars/ride.jpg"),
            pygame.image.load("image_reference/chars/veo.png"),
            pygame.image.load("image_reference/chars/forrest.png"),
            pygame.image.load("image_reference/chars/nacho.jpg"),
            pygame.image.load("image_reference/chars/alex.jpg")
        ]

        self.character_names = [
            "Crimson Tide", 
            "Kalen DeBoer", 
            "Corrupt Ref", 
            "Jeff Carver", 
            "Stock", 
            "Big Al", 
            "Nick Saban", 
            "Crimson Ride", 
            "VEO Rider", 
            "Forrest Gump", 
            "Nacho Alabamo", 
            "Alex Shunnarah"
        ]

        # pictures for characters when hovered over
        self.character_preview = [
            pygame.image.load("image_reference/chars/tide_prev.jpg"),
            pygame.image.load("image_reference/chars/tide_prev1.png"),
            pygame.image.load("image_reference/chars/tide_prev2.png"),
            pygame.image.load("image_reference/chars/deboer_prev.png"),
            pygame.image.load("image_reference/chars/deboer_prev1.png"),
            pygame.image.load("image_reference/chars/deboer_prev2.png"),
            pygame.image.load("image_reference/chars/ref_prev.jpg"),
            pygame.image.load("image_reference/chars/ref_prev1.png"),
            pygame.image.load("image_reference/chars/ref_prev2.png"),
            pygame.image.load("image_reference/chars/jc_prev.jpg"),
            pygame.image.load("image_reference/chars/jc_prev1.png"),
            pygame.image.load("image_reference/chars/jc_prev2.png"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/al_prev.jpg"),
            pygame.image.load("image_reference/chars/al_prev1.png"),
            pygame.image.load("image_reference/chars/al_prev2.png"),
            pygame.image.load("image_reference/chars/nick_prev.png"),
            pygame.image.load("image_reference/chars/nick_prev1.png"),
            pygame.image.load("image_reference/chars/nick_prev2.png"),
            pygame.image.load("image_reference/chars/ride_prev.jpg"),
            pygame.image.load("image_reference/chars/ride_prev1.png"),
            pygame.image.load("image_reference/chars/ride_prev2.png"),
            pygame.image.load("image_reference/chars/veo_prev.jpg"), 
            pygame.image.load("image_reference/chars/veo_prev1.png"),
            pygame.image.load("image_reference/chars/veo_prev2.png"),
            pygame.image.load("image_reference/chars/forrest_prev.jpg"),
            pygame.image.load("image_reference/chars/forrest_prev1.png"),
            pygame.image.load("image_reference/chars/forrest_prev2.png"),
            pygame.image.load("image_reference/chars/nacho_prev.jpg"),
            pygame.image.load("image_reference/chars/nacho_prev1.png"),
            pygame.image.load("image_reference/chars/nacho_prev2.png"),
            pygame.image.load("image_reference/chars/alex_prev.png"),
            pygame.image.load("image_reference/chars/alex_prev1.png"),
            pygame.image.load("image_reference/chars/alex_prev2.png")
        ]

        # difficulty rating for each character
        self.character_diff = [
            5, # tide
            3, # kalen
            4, # ref
            3, # jeff carver
            3, # stock
            1, # big al
            2, # nick saban
            4, # ride
            4, # veo
            1, # forrest
            2, # nacho
            5 # alex shunnarah
        ]
        self.filled_star = pygame.image.load("image_reference/chars/star.png").convert_alpha()
        self.hollow_star = pygame.image.load("image_reference/chars/hollow.png").convert_alpha()

        self.game_over_font = pygame.font.SysFont('Veranda', 30)
        self.arena_message_font = pygame.font.SysFont('Veranda', 50)
        self.difficulty_font = pygame.font.SysFont('Veranda', 25)

        self.player1_font = pygame.font.SysFont('Veranda', 30)
        self.player2_font = pygame.font.SysFont('Veranda', 30)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Welcome, Players!")

        pygame.mixer.init()

        self.click_sound = pygame.mixer.Sound("image_reference/sounds/click.mp3")
        self.select_sound = pygame.mixer.Sound("image_reference/sounds/select.mp3")



    def updateGameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

                if event.key == pygame.K_b:
                    return ("BOOTSTRAP", {})

                rows = 3
                cols = 4
                row = self.selectedIdx // cols
                col = self.selectedIdx % cols
                if event.key == pygame.K_RIGHT:
                    col = (col + 1) % cols
                    self.selectedAltIdx = 0
                elif event.key == pygame.K_LEFT:
                    col = (col - 1 + cols) % cols
                    self.selectedAltIdx = 0
                elif event.key == pygame.K_DOWN:
                    row = (row + 1) % rows
                    self.selectedAltIdx = 0
                elif event.key == pygame.K_UP:
                    row = (row - 1 + rows) % rows
                    self.selectedAltIdx = 0
                elif event.key == pygame.K_LEFTBRACKET:
                    self.selectedAltIdx = (self.selectedAltIdx + 1)% 3
                elif event.key == pygame.K_RIGHTBRACKET:
                    self.selectedAltIdx = (self.selectedAltIdx + 2)% 3
                self.selectedIdx = row * cols + col
                
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    self.select_sound.play()
                    return ("PICK_MAP", {"arena": self.arena, "lives": self.lives})
                self.click_sound.play()

        self.draw()

    def draw(self):
        self.screen.fill(self.CREME)

        text_surface = self.arena_message_font.render("Select Your Fighter", True, self.GRAY)

        # added to center text
        text_width = text_surface.get_width()
        x_position = (self.WIDTH - text_width) // 2
        self.screen.blit(text_surface, (x_position, 40))

        # text for players 1 & 2
        player1_text = self.player1_font.render("Player 1", True, self.BLUE)
        player2_text = self.player2_font.render("Player 2", True, self.RED)
        self.screen.blit(player1_text, (50, 50))
        self.screen.blit(player2_text, (self.WIDTH - 135, 50))

        # self.screen.blit(text_surface, (190, 450))

        # to draw character select grid
        cols = 4
        rows = 3
        padding = 0
        bottom_margin = 70
        side_margin = 100
        top_margin = 100

        grid_width = self.WIDTH - (side_margin * 2) - (padding * (cols + 1))
        grid_height = self.HEIGHT - top_margin - bottom_margin - (padding * (rows + 1))
        box_width = grid_width // cols
        box_height = grid_height // rows
        box_size = min(box_width, box_height)
        total_grid_width = cols * box_size + (cols + 1) * padding
        start_x = (self.WIDTH - total_grid_width) // 2

        # animate grid
        for i in range(rows * cols):
            row = i // cols
            col = i % cols

            x = start_x + padding + col * (box_size + padding)
            y = top_margin + padding + row * (box_size + padding)

            rect = pygame.Rect(x, y, box_size, box_size)

            img = self.character_images[i]
            scaled_img = pygame.transform.scale(img, (box_size, box_size))

            self.screen.blit(scaled_img, (x, y))
            pygame.draw.rect(self.screen, self.BLACK, rect, 1)

            # highlight if selected box - have player 2 box be red later
            if i == self.selectedIdx:
                pygame.draw.rect(self.screen, self.BLUE, rect, 3)

            # draw difficulty rating - player 1
            fill = self.filled_star
            hollow = self.hollow_star
            if self.character_diff[self.selectedIdx] == 1:
                # render 1 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (25, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 2:
                # render 2 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (25, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 3:
                # render 3 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (25, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 4:
                # render 4 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (25, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 5:
                # render 5 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (25, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)

            # draw difficulty rating - player 2
            fill = self.filled_star
            hollow = self.hollow_star
            right_side = 800
            if self.character_diff[self.selectedIdx] == 1:
                # render 1 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (right_side - 150, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 2:
                # render 2 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (right_side - 150, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 3:
                # render 3 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (right_side - 150, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 4:
                # render 4 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (right_side - 150, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star2, (right_side - 50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
            elif self.character_diff[self.selectedIdx] == 5:
                # render 5 star
                star1 = pygame.transform.scale(fill, (25, 25))
                star2 = pygame.transform.scale(hollow, (25, 25))
                self.screen.blit(star1, (right_side - 150, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 125, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 100, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 75, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                self.screen.blit(star1, (right_side - 50, 435))
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)

        # character preview
        selected_char = self.character_preview[self.selectedIdx * 3 + self.selectedAltIdx]

        preview_width = 150
        preview_height = 300
        preview_pic = pygame.transform.scale(selected_char, (preview_width, preview_height))

        left_x = 15
        left_y = ((self.HEIGHT - preview_height) // 2) - 20
        self.screen.blit(preview_pic, (left_x, left_y))
        
        # need to add code for right preview later, for now just mirror player 1
        right_x = self.WIDTH - preview_width - 15
        right_y = ((self.HEIGHT - preview_height) // 2) - 20
        flip = pygame.transform.flip(preview_pic, True, False)
        self.screen.blit(flip, (right_x, right_y))

        panel_padding = 3
        pygame.draw.rect(self.screen, self.BLACK,
            (left_x - panel_padding, left_y - panel_padding,
            preview_width + panel_padding*2, preview_height + panel_padding*2), 2)

        pygame.draw.rect(self.screen, self.BLACK,
            (right_x - panel_padding, right_y - panel_padding,
            preview_width + panel_padding*2, preview_height + panel_padding*2), 2)
        
        name = self.character_names[self.selectedIdx]
        name_surface = self.game_over_font.render(name, True, self.BLACK)
        name_rect_left = name_surface.get_rect(center=(
            left_x + (preview_width // 2),
            left_y + preview_height + 20
        ))
        name_rect_right = name_surface.get_rect(center=(
            right_x + (preview_width // 2),
            right_y + preview_height + 20
        ))
        self.screen.blit(name_surface, name_rect_left)
        self.screen.blit(name_surface, name_rect_right)

        # difficulty text
        difficulty1_text = self.difficulty_font.render("Difficulty", True, self.BLACK)
        difficulty2_text = self.difficulty_font.render("Difficulty", True, self.BLACK)
        diff_rect_left = difficulty1_text.get_rect(center=(
            left_x + (preview_width // 2),
            left_y + preview_height + 45
        ))
        diff_rect_right = difficulty2_text.get_rect(center=(
            right_x + (preview_width // 2),
            right_y + preview_height + 45
        ))
        self.screen.blit(difficulty1_text, diff_rect_left)
        self.screen.blit(difficulty2_text, diff_rect_right)

        text_surface = self.instruction_font.render("B for back", True, (0, 0, 0))
        self.screen.blit(text_surface, (50, 470))
        text_surface = self.instruction_font.render("-      WASD to switch player1      -    Arrows to switch player2      -", True, (0, 0, 0))
        self.screen.blit(text_surface, (200, 470))
        text_surface = self.instruction_font.render("Enter to begin match", True, (0, 0, 0))
        self.screen.blit(text_surface, (640, 470))

        pygame.display.flip()
    
        return None