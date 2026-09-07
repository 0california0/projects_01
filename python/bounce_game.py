import pygame
import math

# pygame setup
pygame.init()
# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()
running = True
dt = 0

# global player vaiables
player_speed = 300
turn_speed = 100
brake_speed = 150
accel_speed = 400 # 450 maybe better, but really not
turn_rate = 180
r = 20

def move_towards(value, target, max_step):
    if value < target:
        return min(value + max_step, target)
    return max(value - max_step, target)

class Player:
    def __init__(self, pos, color, keys):
        self.pos = pygame.math.Vector2(pos)
        self.color = color
        self.keys = keys
        self.direction = pygame.math.Vector2(0,0)
        self.speed = player_speed

    def direction_input(self, pressed):
        up, down, left, right = self.keys
        dir = pygame.math.Vector2(0,0)
        if pressed[up]:
            dir.y -= 1
        if pressed[down]:
            dir.y += 1
        if pressed[left]:
            dir.x -= 1
        if pressed[right]:
            dir.x += 1
        return dir

    def update(self, pressed, dt):
        target = self.direction_input(pressed)
        if self.direction.length_squared() == 0:
            self.direction = pygame.math.Vector2(1, 1)
 
        if target.length_squared() > 0:
            target = target.normalize()
 
            angle = self.direction.angle_to(target)
            angle = (angle + 180) % 360 - 180
 
            max_step = turn_speed * dt
            self.direction = self.direction.rotate(max(-max_step, min(max_step, angle)))

            self.speed = move_towards(self.speed, turn_speed, brake_speed * dt)

        else:
            self.speed = move_towards(self.speed, player_speed, accel_speed * dt)
 
        self.pos += self.direction * self.speed * dt
        self.collision_wall()

    def collision_wall(self):
        if self.pos.x < r:
                self.pos.x = r
                self.direction.x *= -1
        elif self.pos.x > screen.get_width() - r:
            self.pos.x = screen.get_width() - r
            self.direction.x *= -1

        if self.pos.y < r:
            self.pos.y = r
            self.direction.y *= -1
        elif self.pos.y > screen.get_height() - r:
            self.pos.y = screen.get_height() - r
            self.direction.y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, r)

def collision_player(a, b):
        delta = b.pos - a.pos
        distance = delta.length()

        if distance >= 2 * r or distance == 0:
            return
        
        normal = delta / distance
 
        a.pos -= normal * (2 * r - distance) / 2
        b.pos += normal * (2 * r - distance) / 2
    
        a.direction = a.direction.reflect(normal)
        b.direction = b.direction.reflect(normal)


player_one = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
player_two = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
player_three = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
player_four = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
player_five = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
player_six = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)
a = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
b = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
c = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
d = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
e = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
f = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)
gee = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
hee = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
iee = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
jee = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
kee = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
lee = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)
mee = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
nee = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
oee = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
pee = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
qee = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
ree = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)

players1 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
players2 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
players3 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
players4 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
players5 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
players6 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)
players7 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
players8 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
players9 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
players10 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
players11 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
players12 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)
players13 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
players14 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
players15 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
players16 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
players17 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
players18 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)
players19 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "red",
    (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
)
players20 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "blue",
    (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT),
)
players21 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "white",
    (pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a),
)
players22 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "yellow",
    (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
)
players23 = Player(
    (screen.get_width() / 3, screen.get_height() / 2),
    "pink",
    (pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a),
)
players24 = Player(
    (screen.get_width() / 3 * 2, screen.get_height() / 2),
    "green",
    (pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w),
)
 
players = [player_one, player_two,player_three,player_four,player_five,player_six,a,b,c,d,e,f,gee,hee,iee,jee,kee,lee,mee,nee,oee,pee,qee,ree,players12,players13,players14,players15,players16,players17,players18,players19,players20,players21,players22,players23,players24]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill("purple")
 
    pressed = pygame.key.get_pressed()
    for player in players:
        player.update(pressed, dt)

    for i, a in enumerate(players):
        for b in players[i + 1:]:
            collision_player(a, b)
 
    for player in players:
        player.draw(screen)
 
    pygame.display.flip()
 
    # dt ist die Zeit in Sekunden seit dem letzten Frame
    dt = clock.tick(120) / 1000
 
pygame.quit()


"""

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


    speedmulti = [(x+x)*0.01 for x in range(50)]
    keys_player_1 = pygame.key.get_pressed()
    if keys_player_1[pygame.K_w]:
        for multiplier in speedmulti:
            velocity_y_player_1 = -player_speed*multiplier
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




    # print(player_speed)

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