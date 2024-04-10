from random import randint

import pygame

pygame.init()

# Размер экрана
SC = pygame.display.set_mode((400, 200))

# Задний фон
background = pygame.Surface((400, 200))
background.fill((0, 255, 0))

# Координаты начального положения героя
xb = 0
yb = 100

# Параметры героя
hero = pygame.Surface((100, 100))
hero.fill((255, 0, 0))
x = 0
y = 50

# Отрисовка элементов в порядке прорисовки
background.blit(hero, (x, y))
SC.blit(background, (xb, yb))
pygame.display.update()

while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            yb = randint(0, 200)

    # Движение героя
    if x < 400:
        x += 2
    else:
        x = 0

    # Очистка экрана и отрисовка элементов
    SC.fill((0, 0, 0))
    background.fill((0, 255, 0))
    background.blit(hero, (x, y))
    SC.blit(background, (xb, yb))
    pygame.display.update()
    pygame.time.delay(30)
  
