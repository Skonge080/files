import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Анимация")

x = 20
y = 20
width = 50
height = 70
speed = 15

Is_Jump = False
Jump_Count = 10

game = True
while game:
    pygame.time.delay(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 800 - width:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 600 - height:
        y += speed
    if not Is_Jump:
        if keys[pygame.K_SPACE]:
            Is_Jump = True
    else:
        if Jump_Count >= -10:
            if Jump_Count < 0:
                y += (Jump_Count ** 2)/2
                Jump_Count -= 1
            else:
                y -= (Jump_Count ** 2)/2
                Jump_Count -= 1
        else:
            Is_Jump = False
            Jump_Count = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))

    pygame.display.update()

pygame.quit()
