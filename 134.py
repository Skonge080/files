import pygame

pygame.init()

screen = pygame.display.set_mode((400, 416))

screen.fill((100, 150, 200))

img_surf = pygame.image.load('bater.bmp')
img_rect = img_surf.get_rect(bottomright=(400, 416))

screen.blit(img_surf, img_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.time.delay(20)
  
