import pygame

class PickCharactersStage:
    def __init__(self, arena, lives):
        pygame.init()

        self.arena = arena
        self.lives = lives

        self.selectedIdx = 0

        self.WIDTH = 800
        self.HEIGHT = 500
        self.GRAY = (34, 34, 34)
        self.CREME = (255, 255, 220)
        self.BLACK = (0, 0, 0)

        # character icons on select grid
        self.character_images = [
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/kalen.png"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/jc.png"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/al.png"),
            pygame.image.load("image_reference/chars/nick.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/forrest.png"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/nacho.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg")
        ]

        self.character_names = [
            "Stock", 
            "Kalen DeBoer", 
            "Stock", 
            "Jeff Carver", 
            "Stock", 
            "Big Al", 
            "Nick Saban", 
            "Stock", 
            "Forrest Gump", 
            "Stock", 
            "Nacho Alabamo", 
            "Stock"
        ]

        # pictures for characters when hovered over
        self.character_preview = [
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/al_prev.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
        ]

        self.game_over_font = pygame.font.SysFont('Veranda', 30)
        self.arena_message_font = pygame.font.SysFont('Veranda', 50)

        self.player1_font = pygame.font.SysFont('Veranda', 30)
        self.player2_font = pygame.font.SysFont('Veranda', 30)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Welcome, Players!")


    def updateGameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

                rows = 3
                cols = 4
                row = self.selectedIdx // cols
                col = self.selectedIdx % cols
                if event.key == pygame.K_RIGHT:
                    col = (col + 1) % cols
                elif event.key == pygame.K_LEFT:
                    col = (col - 1 + cols) % cols
                elif event.key == pygame.K_DOWN:
                    row = (row + 1) % rows
                elif event.key == pygame.K_UP:
                    row = (row - 1 + rows) % rows
                self.selectedIdx = row * cols + col
                
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    return ("PICK_MAP", {"arena": self.arena, "lives": self.lives})

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

            # highlight if selected box
            if i == self.selectedIdx:
                pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)

        # character preview
        selected_char = self.character_preview[self.selectedIdx]

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

        self.screen.blit(name_surface, (left_x, left_y + 310))
        self.screen.blit(name_surface, (right_x, right_y + 310))

        pygame.display.flip()
    
        return None