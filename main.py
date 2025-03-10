import pygame

pygame.init()

running = True
screen = pygame.display.set_mode((900,680))
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()