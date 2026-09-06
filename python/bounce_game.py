import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
# screen = pygame.display.set_mode((1280/4, 720/4))
clock = pygame.time.Clock()
running = True
dt = 0

# global player vaiables
player_speed = 400
r = 40
turn_rate = 5
target_velocity_x = 60
target_velocity_y = 60

# player 1
umfang_player_one = 2 * r * math.pi
player_one_pos = pygame.math.Vector2(screen.get_width() / 3, screen.get_height() / 2)
player_one_x = screen.get_width() / 3
player_one_y = screen.get_height() / 2
velocity_x_player_1 = 0 
velocity_y_player_1 = 0

# player 2
umfang_player_two = 2 * r * math.pi
player_two_pos = pygame.math.Vector2(screen.get_width() / 3 * 2, screen.get_height() / 2)
player_two_x = screen.get_width() / 3 * 2
player_two_y = screen.get_height() / 2
velocity_x_player_2 = 0 
velocity_y_player_2 = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # PLAYER 1
    pygame.draw.circle(screen, "red", (int(player_one_x), int(player_one_y)), r)


    
    keys_player_1 = pygame.key.get_pressed()
    if keys_player_1[pygame.K_w]:
        velocity_y_player_1 = -player_speed
        # velocity_x_player_1 = 0
    if keys_player_1[pygame.K_s]:
        velocity_y_player_1 = player_speed
        # velocity_x_player_1 = 0
    if keys_player_1[pygame.K_a]:
        velocity_x_player_1 = -player_speed
        # velocity_y_player_1 = 0
    if keys_player_1[pygame.K_d]:
        velocity_x_player_1 = player_speed
        # velocity_y_player_1 = 0

    """t = 1 - math.exp(-turn_rate * dt)
    velocity_x_player_1 += (target_velocity_x - velocity_x_player_1) * t
    velocity_y_player_1 += (target_velocity_y - velocity_y_player_1) * t"""

    player_one_x += velocity_x_player_1 * dt
    player_one_y += velocity_y_player_1 * dt
    # diffrent base speed (faster turn/press speed)

    # collision between players 
    distance_between_players = math.sqrt((player_two_x - player_one_x)**2 + (player_two_y - player_one_y)**2)
    collision = abs(r - r) <= distance_between_players <= (r + r)
    if collision:
        velocity_x_player_1 = velocity_x_player_1 * -1
        velocity_y_player_1 = velocity_y_player_1 * -1
        velocity_x_player_2 = velocity_x_player_2 * -1
        velocity_y_player_2 = velocity_y_player_2 * -1

    # collions detection player 1 NEW
    # width
    if player_one_x >= screen.get_width() - r:
        player_one_x = screen.get_width() - r
        velocity_x_player_1 = velocity_x_player_1 * -1
    if player_one_x <= screen.get_width() + r - screen.get_width():
        player_one_x = screen.get_width() + r - screen.get_width()
        velocity_x_player_1 = velocity_x_player_1 * -1
    # height
    if player_one_y >= screen.get_height() - r:
        player_one_y = screen.get_height() - r
        velocity_y_player_1 = velocity_y_player_1 * -1
    if player_one_y <= screen.get_height() + r - screen.get_height():
        player_one_y = screen.get_height() + r - screen.get_height()
        velocity_y_player_1 = velocity_y_player_1 * -1

    # PLAYER 2
    pygame.draw.circle(screen, "blue", (int(player_two_x), int(player_two_y)), r)    

    keys_player_2 = pygame.key.get_pressed()
    if keys_player_2[pygame.K_UP]:
        velocity_y_player_2 = -player_speed
        # velocity_x_player_2 = 0
    if keys_player_2[pygame.K_DOWN]:
        velocity_y_player_2 = player_speed
        # velocity_x_player_2 = 0
    if keys_player_2[pygame.K_LEFT]:
        velocity_x_player_2 = -player_speed
        # velocity_y_player_2 = 0
    if keys_player_2[pygame.K_RIGHT]:
        velocity_x_player_2 = player_speed
        # velocity_y_player_2 = 0

    player_two_x += velocity_x_player_2 * dt
    player_two_y += velocity_y_player_2 * dt

    # collions detection player 2 NEW
    # width
    if player_two_x >= screen.get_width() - r:
        player_two_x = screen.get_width() - r
        velocity_x_player_2 = velocity_x_player_2 * -1
    if player_two_x <= screen.get_width() + r - screen.get_width():
        player_two_x = screen.get_width() + r - screen.get_width()
        velocity_x_player_2 = velocity_x_player_2 * -1
    # height
    if player_two_y >= screen.get_height() - r:
        player_two_y = screen.get_height() - r
        velocity_y_player_2 = velocity_y_player_2 * -1
    if player_two_y <= screen.get_height() + r - screen.get_height():
        player_two_y = screen.get_height() + r - screen.get_height()
        velocity_y_player_2 = velocity_y_player_2 * -1




    print(player_speed)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 120
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000

pygame.quit()



# diffrent base speed (faster turn/press speed)
# cooldown nach dem man eine wand gehittet hat (in dem man den key in die richtung der wand nicht mehr drücken kann)