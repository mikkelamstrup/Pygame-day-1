import pygame 

pygame.init()

WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x, y = 225, 225 
speed = 5

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    if keys[pygame.K_UP]: y -= speed
    if keys[pygame.K_DOWN]: y += speed
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 20))
    pygame.display.update()

pygame.quit()

