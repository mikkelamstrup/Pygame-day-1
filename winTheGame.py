import pygame 
import random
import time

pygame.init()

WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

x, y = 225, 225 
speed = 5

obstacleX = random.randint(0, WIDTH - 50)
obstacleY = random.randint(0, HEIGHT - 50)
obstacleSpeedY = 4

font = pygame.font.SysFont("Arial", 50)

timeStart = time.time()

running = True
gameOver = False
win = False

while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not gameOver and not win:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: x -= speed
        if keys[pygame.K_RIGHT]: x += speed
        if keys[pygame.K_UP]: y -= speed
        if keys[pygame.K_DOWN]: y += speed

        obstacleY += obstacleSpeedY

        if obstacleY <= 0 or obstacleY >= HEIGHT - 50:
            obstacleSpeedY *= -1
    
        playerRect = pygame.Rect(x, y, 50, 50)
        obstacleRect = pygame.Rect(obstacleX, obstacleY, 50, 50)

        if playerRect.colliderect(obstacleRect):
            gameOver = True

        if x >= WIDTH - 50:
            win = True
            elapseTime = round(time.time() - timeStart, 2)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 20))
    pygame.draw.rect(screen, RED, (obstacleX, obstacleY, 50, 50))

    if gameOver:
        gameOverText = font.render("GAME OVER", True, BLACK)
        screen.blit(gameOverText, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False
        
    if win:
        winText = font.render(f"YOU WIN IN {elapseTime} SECONDS!", True, BLACK)
        screen.blit(winText, (WIDTH // 2 - 200, HEIGHT // 2 - 25))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False
    
    pygame.display.update()

pygame.quit()