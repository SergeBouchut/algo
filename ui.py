import random
import sys
import time

import pygame

from graph import a_star


MOUSE_LEFT_CLICK = 1
MOUSE_MIDDLE_CLICK = 2
MOUSE_RIGHT_CLICK = 3

CELL_SIZE = 120
BACKGROUND_COLOR = (245, 222, 179)  # SAND


def get_cell(x, y):
    return pygame.Rect((x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def get_coord(x, y):
    return int(x / CELL_SIZE), int(y / CELL_SIZE)


def render_map(map_, trees, bot):
    map_.fill(BACKGROUND_COLOR)
    for tree in trees:
        map_.blit(pygame.image.load("tree.png"), get_cell(*tree))
    map_.blit(pygame.image.load("bot.png"), get_cell(*bot))
    pygame.display.update()


def render_cells(coords, map_, trees, bot):
    cells = []
    for coord in coords:
        cell = get_cell(*coord)
        map_.fill(BACKGROUND_COLOR, cell)
        if coord in trees:
            map_.blit(pygame.image.load("tree.png"), cell)
        if coord == bot:
            map_.blit(pygame.image.load("bot.png"), cell)
        cells.append(cell)
    pygame.display.update(cells)


def move_bot(map_, trees, bot, map_x, map_y):
    target = get_coord(*pygame.mouse.get_pos())
    path = a_star(bot, target, trees, (map_x, map_y)) or ()
    for step in path:
        render_cells([bot, step], map_, trees, step)
        bot = step
        time.sleep(0.1)
    return bot


def edit_tree(map_, trees, bot):
    target = get_coord(*pygame.mouse.get_pos())
    if target == bot:
        return
    if target in trees:
        trees.remove(target)
    else:
        trees.add(target)
    render_cells([target], map_, trees, bot)


def spawn_trees(map_, tree_count, map_x, map_y):
    trees = set()
    while len(trees) < tree_count + 1:
        trees.add((random.randint(0, map_x - 1),
                   random.randint(0, map_y - 1)))
    return trees


if __name__ == "__main__":
    map_x, map_y, tree_count = [int(arg) for arg in sys.argv[1:]]
    pygame.init()
    map_ = pygame.display.set_mode((map_x * CELL_SIZE, map_y * CELL_SIZE))
    trees = spawn_trees(map_, tree_count, map_x, map_y)
    bot = trees.pop()
    render_map(map_, trees, bot)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == MOUSE_LEFT_CLICK:
                    bot = move_bot(map_, trees, bot, map_x, map_y)
                elif event.button == MOUSE_RIGHT_CLICK:
                    edit_tree(map_, trees, bot)
            if event.type == pygame.QUIT:
                sys.exit()
