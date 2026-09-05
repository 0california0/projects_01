import pygame

# pygame setup
pygame.init()
# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((1280/4, 720/4))
clock = pygame.time.Clock()
running = True
dt = 0

# global player speed
player_speed = 400
r = 20

# player 1
play_one_pos = pygame.math.Vector2(screen.get_width() / 3, screen.get_height() / 2)
player_one_x = screen.get_width() / 3
player_one_y = screen.get_height() / 2
velocity_x_player_1 = 0 
velocity_y_player_1 = 0
# player_one_line_x = [x for x in range(int(player_two_x) - r, int(player_two_x) + r + 1)]
# player_one_line_y = [y for y in range(int(player_two_y) - r, int(player_two_y) + r + 1)]
player_one_cross_hitbox = [x for x in range(int(player_one_x) - r, int(player_one_x) + r + 1) for y in range(int(player_one_y) - r, int(player_one_y) + r + 1)]
player_one_sphere = [(x, y) for x in range(int(player_one_x) - r, int(player_one_x) + r + 1) for y in range(int(player_one_y) - r, int(player_one_y) + r + 1) if (x - int(player_one_x))**2 + (y - int(player_one_y))**2 <= r**2]

# player 2
play_two_pos = pygame.math.Vector2(screen.get_width() / 3 * 2, screen.get_height() / 2)
player_two_x = screen.get_width() / 3 * 2
player_two_y = screen.get_height() / 2
velocity_x_player_2 = 0 
velocity_y_player_2 = 0
# player_two_line_x = [x for x in range(int(player_two_x) - r, int(player_two_x) + r + 1)]
# player_two_line_y = [y for y in range(int(player_two_y) - r, int(player_two_y) + r + 1)]
player_two_cross_hitbox = [x for x in range(int(player_two_x) - r, int(player_two_x) + r + 1) for y in range(int(player_two_y) - r, int(player_two_y) + r + 1)]
player_two_sphere = [(x, y) for x in range(int(player_two_x) - r, int(player_two_x) + r + 1) for y in range(int(player_two_y) - r, int(player_two_y) + r + 1) if (x - int(player_two_x))**2 + (y - int(player_two_y))**2 <= r**2]

differenz_x = player_one_x - player_two_x
differenz_y = player_one_y - player_two_y

distance = (differenz_x ** 2) + (differenz_y ** 2)
r_sum = (r + r) ** 2

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

    player_one_x += velocity_x_player_1 * dt
    player_one_y += velocity_y_player_1 * dt
    # diffrent base speed (faster turn/press speed)

    # collions detection player 1 NEW
    # width
    if player_one_x >= screen.get_width():
        player_one_x = screen.get_width()
        velocity_x_player_1 = velocity_x_player_1 * -1
    if player_one_x <= screen.get_width() - screen.get_width():
        player_one_x = screen.get_width() - screen.get_width()
        velocity_x_player_1 = velocity_x_player_1 * -1
    # height
    if player_one_y >= screen.get_height():
        player_one_y = screen.get_height()
        velocity_y_player_1 = velocity_y_player_1 * -1
    if player_one_y <= screen.get_height() - screen.get_height():
        player_one_y = screen.get_height() - screen.get_height()
        velocity_y_player_1 = velocity_y_player_1 * -1


    # test: collissions between spheres
    """if distance == r_sum:
        velocity_x_player_1 = velocity_x_player_1 * -1
        # velocity_y_player_1 = velocity_y_player_1 * -1"""

    abstand = play_one_pos.distance_to(play_two_pos)

    # 2. Prüfe, ob der Abstand kleiner als die Summe der Radien ist
    if abstand <= (r + r):
        velocity_x_player_1 = velocity_x_player_1 * -1


    

    # PLAYER 2
    pygame.draw.circle(screen, "blue", (int(player_two_x), int(player_two_y)), 20)    

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
    if player_two_x >= screen.get_width():
        player_two_x = screen.get_width()
        velocity_x_player_2 = velocity_x_player_2 * -1
    if player_two_x <= screen.get_width() - screen.get_width():
        player_two_x = screen.get_width() - screen.get_width()
        velocity_x_player_2 = velocity_x_player_2 * -1
    # height
    if player_two_y >= screen.get_height():
        player_two_y = screen.get_height()
        velocity_y_player_2 = velocity_y_player_2 * -1
    if player_two_y <= screen.get_height() - screen.get_height():
        player_two_y = screen.get_height() - screen.get_height()
        velocity_y_player_2 = velocity_y_player_2 * -1



    """# player_2_pos.y -= player_speed * dt
    player_2_pos.y += player_speed / 2 * dt
    # player_2_pos.x -= player_speed * dt
    player_2_pos.x += player_speed / 2 * dt"""


    # player_speed = player_speed * -1
    """pygame.QUIT
        running = False"""

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










"""
player_2_pos = pygame.Vector2(screen.get_width() / 3 * 2, screen.get_height() / 2)

pygame.draw.circle(screen, "blue", player_2_pos, 20)    

    keys_player_2 = pygame.key.get_pressed()
    if keys_player_2[pygame.K_UP]:
        player_2_pos.y -= player_speed * dt
    if keys_player_2[pygame.K_DOWN]:
        player_2_pos.y += player_speed * dt
    if keys_player_2[pygame.K_LEFT]:
        player_2_pos.x -= player_speed * dt
    if keys_player_2[pygame.K_RIGHT]:
        player_2_pos.x += player_speed * dt

    # collions detection player 2
    # width
    if player_2_pos.x >= screen.get_width():
        player_2_pos.x = screen.get_width()
    if player_2_pos.x <= screen.get_width() - screen.get_width():
        player_2_pos.x = screen.get_width() - screen.get_width()
    # height
    if player_2_pos.y >= screen.get_height():
        player_2_pos.y = screen.get_height()
    if player_2_pos.y <= screen.get_height() - screen.get_height():
        player_2_pos.y = screen.get_height() - screen.get_height()"""