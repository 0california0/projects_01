import pygame
import math
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# global player vaiables
player_speed = 300*1.5
turn_speed = 275*1.5 # 100
brake_speed = 150 # 150
accel_speed = 400 # 450 maybe better, but really not
turn_rate = 180
r = 5

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
        self.lines = []

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
 
            max_step = turn_rate * dt
            self.direction = self.direction.rotate(max(-max_step, min(max_step, angle)))

            self.speed = move_towards(self.speed, turn_speed, brake_speed * dt)

        else:
            self.speed = move_towards(self.speed, player_speed, accel_speed * dt)
 
        self.pos += self.direction * self.speed * dt
        # self.collision_wall()
        collision = self.collision_wall()
        self.strings(collision)

    def collision_wall(self):
        collision = False
        if self.pos.x < r:
                self.pos.x = r
                self.direction.x *= -1
                collision = True
        elif self.pos.x > screen.get_width() - r:
            self.pos.x = screen.get_width() - r
            self.direction.x *= -1
            collision = True

        if self.pos.y < r:
            self.pos.y = r
            self.direction.y *= -1
            collision = True
        elif self.pos.y > screen.get_height() - r:
            self.pos.y = screen.get_height() - r
            self.direction.y *= -1
            collision = True
        return collision

    def strings(self, collision):
        if collision == True:
            pygame.draw.circle(screen, '#f50000', self.pos, r*0.05) # Aufprall Effekt
            self.lines.append(pygame.math.Vector2(self.pos))
            print('test')

    def draw(self, surface):
        for line in self.lines:
            # x,y = self.pos
            pygame.draw.line(screen, self.color, line, self.pos, 2)
        pygame.draw.circle(surface, self.color, self.pos, r)
#############################
def line_distance(point, a, b):
    ab = b - a
    if ab.length_squared() == 0:
        return point.distance_to(a)
    t = (point - a).dot(ab) / ab.length_squared()
    t = max(0, min(1, t))
    return point.distance_to(a + ab * t)

def cut_lines(player, other):
    for line in other.lines[:]:
        if line_distance(player.pos, line, other.pos) <= r:
            other.lines.remove(line)
#############################
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
 
players = [player_one, player_two]

colors = ["red", "blue", "white", "yellow", "green", "purple", "orange", "cyan", "magenta", "gray"]

for i in range(100):
    x = random.uniform(0, screen.get_width())
    y = random.uniform(0, screen.get_height())
    # color = random.choice(colors)
    color = 'black'
    new_player = Player(
        (x, y),
        color,
        (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),  # keine Tastatursteuerung für Extra-Spieler
    )
    players.append(new_player)

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

    for a in players:
        for b in players:
            if a is not b:
                cut_lines(a, b)
 
    for player in players:
        player.draw(screen)
 
    pygame.display.flip()
 
    # dt ist die Zeit in Sekunden seit dem letzten Frame
    dt = clock.tick(120) / 1000
 
pygame.quit()