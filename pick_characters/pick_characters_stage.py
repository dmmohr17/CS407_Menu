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

        self.character_images = [
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/al.png"),
            pygame.image.load("image_reference/chars/nick.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
            pygame.image.load("image_reference/chars/stock.jpg"),
        ]

        self.game_over_font = pygame.font.SysFont('Veranda', 30)
        self.arena_message_font = pygame.font.SysFont('Veranda', 50)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Welcome, Players!")


    def updateGameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                
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


        pygame.display.flip()
    
        return None