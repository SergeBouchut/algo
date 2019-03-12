import math
import sys

import pygame


BACK_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)


#        ----
#       /    \
# y     \    /
# |_ x   ----
#
RADIUS = 50
WIDTH = 2 * RADIUS
HEIGHT = math.sqrt(3) * RADIUS
X_LEN = 16
Y_LEN = 8


def get_center(position):
    x, y = position
    x_offset = WIDTH / 2
    y_offset = HEIGHT / 2 if x % 2 else HEIGHT
    x = x_offset + 3 * WIDTH / 4 * x
    y = y_offset + HEIGHT * y
    return x, y


def draw_hex(surface, position):
    x, y = get_center(position)
    points = [(
        x + math.cos(2 * i * math.pi / 6) * RADIUS,
        y + math.sin(2 * i * math.pi / 6) * RADIUS,
    ) for i in range(6)]
    pygame.draw.lines(surface, LINE_COLOR, True, points)


pygame.init()
surface = pygame.display.set_mode((
    math.ceil((X_LEN + 1) * WIDTH * 3 / 4),
    math.ceil((Y_LEN + 1) * HEIGHT),
))
surface.fill(BACK_COLOR)
for x in range(X_LEN):
    for y in range(Y_LEN):
        draw_hex(surface, (x, y))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
