import pygame

window = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Hello!")

screen = pygame.Surface((40, 40))

done = True

while done:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:

            done = False

    screen.fill((0, 0, 255))

    window.blit(screen, (10, 70))

    pygame.display.flip()
