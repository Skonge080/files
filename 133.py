import pygame
pygame.init()

width = 300
height = 200

screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')

red = (255, 0, 0)
screen.fill(red)

pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
