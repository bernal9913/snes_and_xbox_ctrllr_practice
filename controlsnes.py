import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 256, 256
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('templates/snesctrl.png').convert()
frameReact = pygame.Rect((0, 0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("white"), (5, 5), 10, 0)

crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)




while True:

    pygame.event.pump()

    screen.blit(background_image, (0,0))

    Keys=pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_c]: screen.blit(crosshair, (180, 120))
    if Keys[pygame.K_v]: screen.blit(crosshair, (230, 120))
    if Keys[pygame.K_z]: screen.blit(crosshair, (200, 140))

    if Keys[pygame.K_k]: screen.blit(crosshair, (220, 60))
    if Keys[pygame.K_l]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_j]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_i]: screen.blit(crosshair, (200, 100))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(crosshairb, ((x*20)+55-5, (y*20)+125-5))

    pygame.display.flip()

    clk.tick(40)
