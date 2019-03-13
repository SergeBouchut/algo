import math
import random
import sys

import pygame


BACK_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)


#        ----
#       /    \
# y     \    /
# |_ x   ----
#
RADIUS = 60
WIDTH = 2 * RADIUS

Q_RANGE = range(-3, -3)
R_RANGE = range(-3, -3)
X_LEN = 1000
Y_LEN = 600


def get_center(position):
    q, r = position
    x = WIDTH * 3 * q / 2.
    y = WIDTH * math.sqrt(3) * (q / 2. + r)
    return x + X_LEN / 2, y + Y_LEN / 2


def get_position(coord):
    x = coord[0] - X_LEN / 2
    y = coord[1] - Y_LEN / 2
    q = 2 * x / 3. / WIDTH
    r = (-x + math.sqrt(3) * y) / 3. / WIDTH
    return round_hex(q, r)


def round_hex(x, z):
    y = -x-z
    rx, ry, rz = (round(i) for i in (x, y, z))
    dx, dy, dz = (abs(round(i) - i) for i in (x, y, z))
    if dx > dy and dx > dz:
        rx = -ry-rz
    elif dz > dy:
        rz = -rx-ry
    return rx, rz


def draw_hex(surface, position):
    print(position)
    x, y = get_center(position)
    print(x, y)
    points = [(
        x + math.cos(2 * i * math.pi / 6) * RADIUS,
        y + math.sin(2 * i * math.pi / 6) * RADIUS,
    ) for i in range(6)]
    random_color = tuple([random.randint(128, 255) for _ in range(3)])
    return pygame.draw.polygon(surface, random_color, points)


pygame.init()
surface = pygame.display.set_mode((X_LEN, Y_LEN))
surface.fill(BACK_COLOR)
for q in Q_RANGE:
    for r in R_RANGE:
        print(q, r)
        draw_hex(surface, (q, r))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            cell = draw_hex(surface, get_position(pygame.mouse.get_pos()))
            pygame.display.update([cell])
        if event.type == pygame.QUIT:
            sys.exit()
