import pygame

pygame.init()

clk = pygame.time.Clock()

pygame.display.set_caption('testeo con control xbox')

size = width, height = 256, 256
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('templates/snesctrl.png').convert()
frameReact = pygame.Rect((0, 0), (width, height))

pressed_btn = pygame.surface.Surface((10, 10))
pygame.draw.circle(pressed_btn, pygame.Color("white"), (5, 5), 10, 0)

pressed_crosspad = pygame.surface.Surface((10, 10))
pygame.draw.circle(pressed_crosspad, pygame.Color("red"), (5, 5), 5, 0)

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

while True:

    pygame.event.pump()

    screen.blit(background_image, (0, 0))

    # marafalla para el teclado
    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(pressed_btn, (200, 100))
    if Keys[pygame.K_c]: screen.blit(pressed_btn, (180, 120))
    if Keys[pygame.K_v]: screen.blit(pressed_btn, (230, 120))
    if Keys[pygame.K_z]: screen.blit(pressed_btn, (200, 140))

    if Keys[pygame.K_k]: screen.blit(pressed_btn, (220, 60))
    if Keys[pygame.K_l]: screen.blit(pressed_btn, (70, 60))
    if Keys[pygame.K_j]: screen.blit(pressed_btn, (95, 130))
    if Keys[pygame.K_i]: screen.blit(pressed_btn, (120, 130))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0

    # marafalla para el control
    for event in pygame.event.get():
        # pygame.joybuttondown sirve para cuando se levanta un boton
        if event.type == pygame.JOYBUTTONDOWN:

            print(event.button)
            print("Joystick button pressed.")
            if event.button == 0: screen.blit(pressed_btn, (200, 140))  # a
            if event.button == 1: screen.blit(pressed_btn, (230, 120))  # b
            if event.button == 2: screen.blit(pressed_btn, (170, 120))  # x
            if event.button == 3: screen.blit(pressed_btn, (200, 100))  # y
            if event.button == 6:  # menu
                screen.blit(pressed_btn, (130, 130))
                joystick = joysticks[event.instance_id]
                if joystick.rumble(0, 0.7, 1000):
                    print(f"Rumble effect played on joystick {event.instance_id}")
            if event.button == 4:  # share
                screen.blit(pressed_btn, (95, 130))
                joystick = joysticks[event.instance_id]
                if joystick.rumble(0, 0.7, 1000):
                    print(f"Rumble effect played on joystick {event.instance_id}")

            # crosspad
            x = -1 if event.button == 13 else 1 if event.button == 14 else 0

            y = -1 if event.button == 11 else 1 if event.button == 12 else 0
            # bumpers
            if event.button == 9: screen.blit(pressed_btn, (70, 60))  # lb
            if event.button == 10: screen.blit(pressed_btn, (200, 60)) # rb
        if event.type == pygame.QUIT:
            pygame.joystick.quit()
            pygame.quit()
            exit()

    screen.blit(pressed_crosspad, ((x * 20) + 55 - 5, (y * 20) + 125 - 5))

    pygame.display.flip()

    clk.tick(40)
