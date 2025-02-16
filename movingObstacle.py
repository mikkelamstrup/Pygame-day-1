import pygame 
import random

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
obstacleSpeedX = 4
obstacleSpeedY = 3
font = pygame.font.SysFont("Arial", 50)

running = True
gameOver = False

while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not gameOver:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: x -= speed
        if keys[pygame.K_RIGHT]: x += speed
        if keys[pygame.K_UP]: y -= speed
        if keys[pygame.K_DOWN]: y += speed

        obstacleX += obstacleSpeedX
        obstacleSpeedY += obstacleSpeedY

        if obstacleX <= 0 or obstacleX >= WIDTH - 50:
            obstacleSpeedX *= -1
        if obstacleY <= 0 or obstacleY >= WIDTH - 50:
            obstacleSpeedY *= -1
        
    
        playerRect = pygame.Rect(x, y, 50, 50)
        obstacleRect = pygame.Rect(obstacleX, obstacleY, 50, 50)

        if playerRect.colliderect(obstacleRect):
            gameOver = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 20))
    pygame.draw.rect(screen, RED, (obstacleX, obstacleY, 50, 50))

    if gameOver:
        gameOverText = font.render("GAME OVER", True, BLACK)
        screen.blit(gameOverText, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
        pygame.display.update()

        pygame.time.delay(5000)
        running = False
    
    pygame.display.update()

pygame.quit()