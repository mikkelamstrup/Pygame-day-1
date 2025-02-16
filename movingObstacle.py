import pygame
import random

pygame.init()

# Skærm opsætning
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")

# Farver
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Spilleren
player_width, player_height = 50, 20
x, y = 225, 225
speed = 5

# Forhindringen (den røde firkant)
obstacle_size = 50

# Sørg for, at forhindringen IKKE starter på spilleren
while True:
    obstacleX = float(random.randint(0, WIDTH - obstacle_size))
    obstacleY = float(random.randint(0, HEIGHT - obstacle_size))
    playerRect_initial = pygame.Rect(x, y, player_width, player_height)
    obstacleRect_initial = pygame.Rect(round(obstacleX), round(obstacleY), obstacle_size, obstacle_size)
    if not playerRect_initial.colliderect(obstacleRect_initial):
        break

obstacleSpeedX = 4
obstacleSpeedY = 3

# Font til GAME OVER
font = pygame.font.SysFont("Arial", 50)

running = True
gameOver = False

while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spilleren kan bevæge sig, hvis spillet ikke er ovre
    if not gameOver:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

    # Opdater forhindringens position – denne kode kører uanset gameOver
    obstacleX += obstacleSpeedX
    obstacleY += obstacleSpeedY

    # Skift retning, når den rammer skærmens kanter
    if obstacleX <= 0 or obstacleX >= WIDTH - obstacle_size:
        obstacleSpeedX *= -1
    if obstacleY <= 0 or obstacleY >= HEIGHT - obstacle_size:
        obstacleSpeedY *= -1

    # Opret rektangler til kollisionstjek
    playerRect = pygame.Rect(x, y, player_width, player_height)
    obstacleRect = pygame.Rect(round(obstacleX), round(obstacleY), obstacle_size, obstacle_size)

    # Tjek for kollision hvis spillet ikke er ovre
    if not gameOver:
        if playerRect.colliderect(obstacleRect):
            gameOver = True

    # Tegn alt
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, playerRect)      # Spilleren
    pygame.draw.rect(screen, RED, obstacleRect)       # Forhindringen

    if gameOver:
        gameOverText = font.render("GAME OVER", True, BLACK)
        screen.blit(gameOverText, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    pygame.display.update()

pygame.quit()
