import pygame

class PickCharactersStage:
    def __init__(self, arena, lives, two_player):
        pygame.init()

        self.arena = arena
        self.lives = lives
        self.two_player = two_player

        self.selectedIdx = 5
        self.selectedAltIdx = 0

        self.selectedIdxP2 = 6
        self.selectedAltIdxP2 = 0

        self.p1_selected = False
        self.p2_selected = False

        self.instruction_font = pygame.font.SysFont('Veranda', 20)
        self.ready_font = pygame.font.Font("pick_characters/DIMIS___.TTF", 32)

        self.WIDTH = 800
        self.HEIGHT = 500
        self.GRAY = (34, 34, 34)
        self.CREME = (255, 255, 220)
        self.BLACK = (0, 0, 0)
        self.PURPLE = (160, 32, 240)
        self.GREEN = (26, 224, 0)

        # character icons on select grid
        self.character_images = [
            pygame.image.load("image_reference/chars/tide.jpg"),
            pygame.image.load("image_reference/chars/kalen.png"),
            pygame.image.load("image_reference/chars/ref.jpg"),
            pygame.image.load("image_reference/chars/jc.png"),
            pygame.image.load("image_reference/chars/squirrel.png"),
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
            "Campus Squirrel", 
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
            pygame.image.load("image_reference/chars/squirrel_prev.png"),
            pygame.image.load("image_reference/chars/squirrel_prev1.png"),
            pygame.image.load("image_reference/chars/squirrel_prev2.png"),
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
            3, # squirrel
            1, # big al
            2, # nick saban
            4, # ride
            4, # veo
            1, # forrest
            2, # nacho
            5 # alex shunnarah
        ]

        # [HP, STR, SPD] 1-5
        self.character_stats = [
            [5, 3, 3], # tide
            [4, 4, 3], # kalen
            [3, 4, 4], # ref
            [3, 4, 3], # jeff carver
            [2, 2, 5], # squirrel
            [5, 5, 1], # big al
            [3, 5, 4], # nick saban
            [5, 5, 1], # ride
            [3, 3, 5], # veo
            [3, 4, 4], # forrest
            [5, 5, 1], # nacho
            [2, 3, 3]  # alex shunnarah
        ]
        self.filled_star = pygame.image.load("image_reference/chars/star.png").convert_alpha()
        self.hollow_star = pygame.image.load("image_reference/chars/hollow.png").convert_alpha()

        self.show_stats = False
        self.show_statsP2 = False

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

                if(self.p1_selected == False):
                    rows = 3
                    cols = 4
                    row = self.selectedIdx // cols
                    col = self.selectedIdx % cols
                    if event.key == pygame.K_d:
                        col = (col + 1) % cols
                        self.selectedAltIdx = 0
                        self.show_stats = False  # Assuming we want the stat screen to close itself when selecting another character
                    elif event.key == pygame.K_a:
                        col = (col - 1 + cols) % cols
                        self.selectedAltIdx = 0
                        self.show_stats = False
                    elif event.key == pygame.K_s:
                        row = (row + 1) % rows
                        self.selectedAltIdx = 0
                        self.show_stats = False
                    elif event.key == pygame.K_w:
                        row = (row - 1 + rows) % rows
                        self.selectedAltIdx = 0
                        self.show_stats = False
                    elif event.key == pygame.K_r:
                        self.selectedAltIdx = (self.selectedAltIdx + 1)% 3
                    elif event.key == pygame.K_t:
                        self.selectedAltIdx = (self.selectedAltIdx + 2)% 3
                    elif event.key == pygame.K_LSHIFT:
                        self.show_stats = not self.show_stats
                    elif event.key == pygame.K_RSHIFT and self.two_player == False:
                        self.show_stats = not self.show_stats
                    self.selectedIdx = row * cols + col

                if self.two_player == True and self.p2_selected == False:
                    rowsP2 = 3
                    colsP2 = 4
                    rowP2 = self.selectedIdxP2 // colsP2
                    colP2 = self.selectedIdxP2 % colsP2
                    if event.key == pygame.K_RIGHT:
                        colP2 = (colP2 + 1) % colsP2
                        self.selectedAltIdxP2 = 0
                        self.show_statsP2 = False
                    elif event.key == pygame.K_LEFT:
                        colP2 = (colP2 - 1 + colsP2) % colsP2
                        self.selectedAltIdxP2 = 0
                        self.show_statsP2 = False
                    elif event.key == pygame.K_DOWN:
                        rowP2 = (rowP2 + 1) % rowsP2
                        self.selectedAltIdxP2 = 0
                        self.show_statsP2 = False
                    elif event.key == pygame.K_UP:
                        rowP2 = (rowP2 - 1 + rowsP2) % rowsP2
                        self.selectedAltIdxP2 = 0
                        self.show_statsP2 = False
                    elif event.key == pygame.K_LEFTBRACKET:
                        self.selectedAltIdxP2 = (self.selectedAltIdxP2 + 1)% 3
                    elif event.key == pygame.K_RIGHTBRACKET:
                        self.selectedAltIdxP2 = (self.selectedAltIdxP2 + 2)% 3
                    elif event.key == pygame.K_RSHIFT:
                        self.show_statsP2 = not self.show_statsP2
                    self.selectedIdxP2 = rowP2 * colsP2 + colP2
                elif self.two_player == False and self.p1_selected == True:
                    rowsP2 = 3
                    colsP2 = 4
                    rowP2 = self.selectedIdxP2 // colsP2
                    colP2 = self.selectedIdxP2 % colsP2
                    if event.key == pygame.K_d:
                        colP2 = (colP2 + 1) % colsP2
                        self.selectedAltIdxP2 = 0
                    elif event.key == pygame.K_a:
                        colP2 = (colP2 - 1 + colsP2) % colsP2
                        self.selectedAltIdxP2 = 0
                    elif event.key == pygame.K_s:
                        rowP2 = (rowP2 + 1) % rowsP2
                        self.selectedAltIdxP2 = 0
                    elif event.key == pygame.K_w:
                        rowP2 = (rowP2 - 1 + rowsP2) % rowsP2
                        self.selectedAltIdxP2 = 0
                    elif event.key == pygame.K_r:
                        self.selectedAltIdxP2 = (self.selectedAltIdxP2 + 1)% 3
                    elif event.key == pygame.K_t:
                        self.selectedAltIdxP2 = (self.selectedAltIdxP2 + 2)% 3
                    elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                        self.show_statsP2 = not self.show_statsP2
                    self.selectedIdxP2 = rowP2 * colsP2 + colP2
                
                if (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN or event.key == pygame.K_e) and self.two_player == False:
                    self.select_sound.play()
                    if(self.p1_selected == False):
                        self.p1_selected = True
                    else:
                        return ("PICK_MAP", {"arena": self.arena, "lives": self.lives, "two_player": self.two_player})
                elif(self.two_player == True):
                    if(event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                        self.select_sound.play()
                        self.p2_selected = not self.p2_selected
                    if event.key == pygame.K_e:
                        self.select_sound.play()
                        self.p1_selected = not self.p1_selected
                    
                    if self.p1_selected == True and self.p2_selected == True:
                        pygame.time.set_timer(pygame.event.Event(pygame.USEREVENT+1), millis=500, loops=1)  # wait this long before going to next screen

                self.click_sound.play()
            elif event.type == pygame.USEREVENT+1:
                if self.p1_selected == True and self.p2_selected == True:   # allow players the chance to unselect before the above timer is up
                    return ("PICK_MAP", {"arena": self.arena, "lives": self.lives, "two_player": self.two_player})

        self.draw()

    def draw_difficulty(self, plr: int, rect):
        fill = self.filled_star
        hollow = self.hollow_star
        # draw difficulty rating - player 1
        if plr == 1:
            diff = self.character_diff[self.selectedIdx]
            if diff == 1:
                # render 1 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 2:
                # render 2 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 3:
                # render 3 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 4:
                # render 4 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 5:
                # render 5 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
        elif plr == 2:
            diff = self.character_diff[self.selectedIdxP2]
            right_side = 800
            if diff == 1:
                # render 1 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 2:
                # render 2 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 3:
                # render 3 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 4:
                # render 4 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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
            elif diff == 5:
                # render 5 star
                star1 = pygame.transform.smoothscale(fill, (25, 25))
                star2 = pygame.transform.smoothscale(hollow, (25, 25))
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

    def draw_stats(self, plr: int, x_offset: int, width: int, y_offset: int):   # takes a bunch of args so it'll align with the preview even if it is moved later
        hp_icon = pygame.transform.smoothscale(pygame.image.load("image_reference/chars/hp_icon.svg"), (20, 20))
        str_icon = pygame.transform.smoothscale(pygame.image.load("image_reference/chars/str_icon.svg"), (20, 20))
        spd_icon = pygame.transform.smoothscale(pygame.image.load("image_reference/chars/spd_icon.svg"), (20, 20))
        filled = pygame.transform.smoothscale(self.filled_star, (16, 16))
        hollow = pygame.transform.smoothscale(self.hollow_star, (16, 16))
        if plr == 1:
            panel_padding = 3
            pygame.draw.rect(self.screen, self.BLACK,
                (x_offset - panel_padding, y_offset - panel_padding,
                width + panel_padding*2, 64 + panel_padding*2), 2)
            
            self.screen.blit(hp_icon, (x_offset, y_offset))
            hp_stat = self.character_stats[self.selectedIdx][0]
            for i, star in enumerate(([True]*hp_stat)+([False]*(5-hp_stat))):
                if star:
                    self.screen.blit(filled, (x_offset+25+(i*23), y_offset))
                else:
                    self.screen.blit(hollow, (x_offset+25+(i*23), y_offset))

            self.screen.blit(str_icon, (x_offset, y_offset+22))
            str_stat = self.character_stats[self.selectedIdx][1]
            for i, star in enumerate(([True]*str_stat)+([False]*(5-str_stat))):
                if star:
                    self.screen.blit(filled, (x_offset+25+(i*23), y_offset+22))
                else:
                    self.screen.blit(hollow, (x_offset+25+(i*23), y_offset+22))

            self.screen.blit(spd_icon, (x_offset, y_offset+44))
            spd_stat = self.character_stats[self.selectedIdx][2]
            for i, star in enumerate(([True]*spd_stat)+([False]*(5-spd_stat))):
                if star:
                    self.screen.blit(filled, (x_offset+25+(i*23), y_offset+44))
                else:
                    self.screen.blit(hollow, (x_offset+25+(i*23), y_offset+44))

            
        elif plr == 2:
            panel_padding = 3
            pygame.draw.rect(self.screen, self.BLACK,
                (x_offset - panel_padding, y_offset - panel_padding,
                width + panel_padding*2, 64 + panel_padding*2), 2)
            
            self.screen.blit(hp_icon, (x_offset, y_offset))
            hp_stat = self.character_stats[self.selectedIdxP2][0]
            for i, star in enumerate(([True]*hp_stat)+([False]*(5-hp_stat))):
                if star:
                    self.screen.blit(filled, (x_offset+25+(i*23), y_offset))
                else:
                    self.screen.blit(hollow, (x_offset+25+(i*23), y_offset))
            
            self.screen.blit(str_icon, (x_offset, y_offset+22))
            str_stat = self.character_stats[self.selectedIdxP2][1]
            for i, star in enumerate(([True]*str_stat)+([False]*(5-str_stat))):
                if star:
                    self.screen.blit(filled, (x_offset+25+(i*23), y_offset+22))
                else:
                    self.screen.blit(hollow, (x_offset+25+(i*23), y_offset+22))

            self.screen.blit(spd_icon, (x_offset, y_offset+44))
            spd_stat = self.character_stats[self.selectedIdxP2][2]
            for i, star in enumerate(([True]*spd_stat)+([False]*(5-spd_stat))):
                if star:
                    self.screen.blit(filled, (x_offset+25+(i*23), y_offset+44))
                else:
                    self.screen.blit(hollow, (x_offset+25+(i*23), y_offset+44))
    
    def draw_ready(self, plr):
        if plr == 1:
            pygame.draw.rect(self.screen, self.BLACK,
            (40, 10, 100, 38), 2)
            text_surface = self.ready_font.render("Ready", True, self.GREEN)
            self.screen.blit(text_surface, (46, 10))
        elif plr == 2:
            pygame.draw.rect(self.screen, self.BLACK,
            (self.WIDTH-145, 10, 100, 38), 2)
            text_surface = self.ready_font.render("Ready", True, self.GREEN)
            self.screen.blit(text_surface, (self.WIDTH-138, 10))


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
            if i == self.selectedIdx and self.selectedIdx != self.selectedIdxP2:
                pygame.draw.rect(self.screen, self.BLUE, rect, 5)

            if i == self.selectedIdxP2 and self.selectedIdx != self.selectedIdxP2:
                pygame.draw.rect(self.screen, self.RED, rect, 5)

            if i == self.selectedIdx and self.selectedIdx == self.selectedIdxP2:
                pygame.draw.rect(self.screen, self.PURPLE, rect, 5)

        # character preview
        selected_char = self.character_preview[self.selectedIdx * 3 + self.selectedAltIdx]
        selected_charP2 = self.character_preview[self.selectedIdxP2 * 3 + self.selectedAltIdxP2]

        preview_width = 150
        preview_height = 300
        preview_pic = pygame.transform.scale(selected_char, (preview_width, preview_height))

        left_x = 15
        left_y = ((self.HEIGHT - preview_height) // 2) - 20
        self.screen.blit(preview_pic, (left_x, left_y))
        
        preview_pic = pygame.transform.scale(selected_charP2, (preview_width, preview_height))
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
        nameP2 = self.character_names[self.selectedIdxP2]
        name_surface = self.game_over_font.render(name, True, self.BLACK)
        name_surfaceP2 = self.game_over_font.render(nameP2, True, self.BLACK)
        name_rect_left = name_surface.get_rect(center=(
            left_x + (preview_width // 2),
            left_y + preview_height + 15
        ))
        name_rect_right = name_surfaceP2.get_rect(center=(
            right_x + (preview_width // 2),
            right_y + preview_height + 15
        ))
        self.screen.blit(name_surface, name_rect_left)
        pygame.draw.rect(self.screen, self.BLACK,
        (
            name_rect_left.x - panel_padding, name_rect_left.y - panel_padding-1,
            name_rect_left.width + (panel_padding*2), name_rect_left.height + (panel_padding*2)
        ), width=2)
        self.screen.blit(name_surfaceP2, name_rect_right)
        pygame.draw.rect(self.screen, self.BLACK,
        (
            name_rect_right.x - panel_padding, name_rect_right.y - panel_padding-1,
            name_rect_right.width + (panel_padding*2), name_rect_right.height + (panel_padding*2)
        ), width=2)

        # skip drawing difficulty if stats menu is open
        if self.show_stats:
            self.draw_stats(1, left_x, preview_width, left_y+preview_height+30)
        else:
            difficulty1_text = self.difficulty_font.render("Difficulty", True, self.BLACK)
            diff_rect_left = difficulty1_text.get_rect(center=(
                left_x + (preview_width // 2),
                left_y + preview_height + 45
            ))
            self.screen.blit(difficulty1_text, diff_rect_left)
            # moved draw difficulty to a function for better comprehension, and moved it out of the loop bc it was being drawn rows*cols times
            self.draw_difficulty(plr=1, rect=rect)

        if self.show_statsP2:   # since the show_stats are set to False when changing selection, the "Difficulty" text will already be drawn, no need to do it again
            self.draw_stats(2, right_x, preview_width, right_y+preview_height+30)
        else:
            difficulty2_text = self.difficulty_font.render("Difficulty", True, self.BLACK)
            diff_rect_right = difficulty2_text.get_rect(center=(
                right_x + (preview_width // 2),
                right_y + preview_height + 45
            ))
            self.screen.blit(difficulty2_text, diff_rect_right)
            self.draw_difficulty(plr=2, rect=rect)

        if self.p1_selected == True:
            self.draw_ready(1)
        if self.p2_selected == True:
            self.draw_ready(2)

        text_surface = self.instruction_font.render("B for back", True, (0, 0, 0))
        self.screen.blit(text_surface, (40, 480))
        if(self.two_player == True):
            text_surface = self.instruction_font.render("-    P1: WASD = Move, E = Select, R/T = Color      -      P2: Arrows = Move, Enter = Select, [ / ] = Color  ", True, (0, 0, 0))
            self.screen.blit(text_surface, (150, 480))
            text_surface = self.instruction_font.render("LShift to view stats", True, (0,0,0))
            self.screen.blit(text_surface, (175, 450))
            text_surface = self.instruction_font.render("RShift to view stats", True, (0,0,0))
            rect = text_surface.get_rect(topright=(self.WIDTH-175, 450))
            self.screen.blit(text_surface, rect)
        else:
            text_surface = self.instruction_font.render("-  WASD to switch character  -  R T to select color  -  Shift for Stats  -", True, (0, 0, 0))
            self.screen.blit(text_surface, (110, 480))
            text_surface = self.instruction_font.render("Enter or E to select character", True, (0, 0, 0))
            self.screen.blit(text_surface, (550, 480))

        pygame.display.flip()
    
        return None