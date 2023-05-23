import pygame

pygame.init()

SW = 600
SH = 400

screen = pygame.display.set_mode((SW , SH))
pygame.display.set_caption("Making Shapes")

run = True
while run:

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (200, 100, 150, 150), width = 2, border_radius = 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    
pygame.quit()
