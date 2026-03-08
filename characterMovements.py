import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
GRAY = (34, 34, 34)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Mechanics")

clock = pygame.time.Clock()
sprite_sheet_image = pygame.image.load('CharacterMovements/character.png').convert_alpha()

GRAVITY = 1500
ACCELERATION = 1500
DASH_ACCELERATION = 3000
FRICTION = 1200
MAX_SPEED = 400
MAX_DASH_SPEED = 700
JUMP_STRENGTH = -450
GROUND_Y = 450
BLACK = (0, 0, 0)

def getImage(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (frame*width, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

frame0 = getImage(sprite_sheet_image, 8, 24, 24, 2, BLACK)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = 245
        self.rect.y = GROUND_Y

        self.velocity_x = 0
        self.velocity_y = 0
        self.isOnGround = True
        self.dash = False
        self.canDash = True
        self.mostRecentXDirection = 'Right'
        self.dashTime = 0
        self.dashDuration = 0.15
        self.dashSpeed = 800


player = Player()
running = True

while running:
    dt = clock.tick(60) / 1000  # seconds per frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

            if event.key == pygame.K_UP and player.isOnGround:
                player.velocity_y = JUMP_STRENGTH
                player.isOnGround = False
                player.canDash = True
            
            if event.key == pygame.K_d and not player.isOnGround and player.canDash:
                player.dash = True
                player.dashTime = player.dashDuration
                player.canDash = False
                if player.mostRecentXDirection == 'Right':
                    player.velocity_x = player.dashSpeed
                if player.mostRecentXDirection == 'Left':
                    player.velocity_x = -player.dashSpeed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.velocity_x -= ACCELERATION * dt
        player.mostRecentXDirection = 'Left'

    if keys[pygame.K_RIGHT] and player.isOnGround:
        player.velocity_x += ACCELERATION * dt
        player.mostRecentXDirection = 'Right'

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]: # friction
        if player.velocity_x > 0:
            player.velocity_x -= FRICTION * dt
            if player.velocity_x < 0:
                player.velocity_x = 0
        elif player.velocity_x < 0:
            player.velocity_x += FRICTION * dt
            if player.velocity_x > 0:
                player.velocity_x = 0
    if player.dash:
        player.dashTime -= dt
        player.velocity_y = 0

        if player.dashTime <= 0:
            player.dash = False
    # clamp horizontal speed
    if not player.dash:
        player.velocity_x = max(-MAX_SPEED, min(MAX_SPEED, player.velocity_x))
    if player.dash:
        player.velocity_x = max(-MAX_DASH_SPEED, min(MAX_DASH_SPEED, player.velocity_x))

    # apply gravity
    player.velocity_y += GRAVITY * dt

    # apply movement
    player.rect.x += player.velocity_x * dt
    player.rect.y += player.velocity_y * dt

    # ground collision
    if player.rect.y >= GROUND_Y:
        player.rect.y = GROUND_Y
        player.velocity_y = 0
        player.isOnGround = True
        player.dash = False
        player.canDash = False

    screen.fill(WHITE)
    screen.blit(frame0, (0, 0))
    screen.blit(player.image, player.rect)
    pygame.display.flip()

pygame.quit()