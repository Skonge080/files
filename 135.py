import pygame

# Инициализация Pygame
pygame.init()

# Создание окна игры
screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))

# Название окна
pygame.display.set_caption('My Game')

# Загрузка изображения
car_image = pygame.image.load('auto.bmp').convert()

# Удаление фона изображения
car_image.set_colorkey((255, 255, 255))

# Определение позиции изображения
car_rect = car_image.get_rect(center=(150, 150))

# Отображение изображения на экране
screen.blit(car_image, car_rect)

# Обновление экрана
pygame.display.update()

# Обработка событий
running = True
while running:
    for event in pygame.event.get():
        # Закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # Отражение изображения по нажатию клавиши F
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            flipped_image = pygame.transform.flip(car_image, True, False)
            screen.fill((100, 150, 200))
            screen.blit(flipped_image, car_rect)
            pygame.display.update(car_rect)

    # Задержка обновления экрана
    pygame.time.delay(20)

# Завершение Pygame
pygame.quit()
