import sys
import time

import pygame

from graph import a_star


CELL_SIZE = 120
BACKGROUND_COLOR = (245, 222, 179)  # SAND

BORDERS = (10, 6)
TREES = [(1, 3), (2, 4), (5, 3), (6, 3), (6, 2),
         (6, 1), (4, 0), (4, 1), (3, 1), (3, 3)]
START = (2, 2)


def get_cell(x, y):
    return pygame.Rect((x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def init():
    pygame.init()
    x, y = BORDERS
    map_ = pygame.display.set_mode((x * CELL_SIZE, y * CELL_SIZE))
    map_.fill(BACKGROUND_COLOR)
    for tree in TREES:
        map_.blit(pygame.image.load("tree.png"), get_cell(*tree))
    bot = START
    bot_cell = get_cell(*bot)
    map_.blit(pygame.image.load("bot.png"), bot_cell)
    pygame.display.update()
    return map_, bot_cell, bot

def render(map_, bot_cell, bot):
    map_.fill(BACKGROUND_COLOR, bot_cell)
    new_bot_cell = get_cell(*bot)
    map_.blit(pygame.image.load("bot.png"), new_bot_cell)
    pygame.display.update([bot_cell, new_bot_cell])
    return new_bot_cell

def move(map_, bot_cell, bot):
    x, y = pygame.mouse.get_pos()
    dest = (int(x / CELL_SIZE), int(y / CELL_SIZE))
    path = a_star(bot, dest, TREES, BORDERS) or ()
    for step in path:
        bot = step
        bot_cell = render(map_, bot_cell, bot)
        time.sleep(0.1)
    return bot_cell, bot


map_, bot_cell, bot = init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            bot_cell, bot = move(map_, bot_cell, bot)
        if event.type == pygame.QUIT:
            sys.exit()
