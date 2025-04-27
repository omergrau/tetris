import copy
import random

import pygame

from classes import *


def check_win(bord, stay_items, hight):
    for line in range(len(bord)):
        if len(bord[line]) == 23:
            win(bord, line, stay_items, hight)


def win(bord, line, stay_items, hight):
    bord.pop(line)
    for item in stay_items:
        for block in item.blocks:
            if block.color != "grey" and int((hight - block.y) / 21) > line:
                block.move("down", 3)
    bord.append([])


def creat_level(hight, widht):
    border = []
    for y in range(20):
        border.append(line("grey", 0, int(widht * 0.5) - 12 * 21, hight - y * 21, 1))
        border.append(line("grey", 0, int(widht * 0.5) + 12 * 21, hight - y * 21, 1))
    for x in range(25):
        border.append(line("grey", 0, int(widht * 0.5) - (12 - x) * 21, hight - 21, 1))
    return border


def put_in_bord(item, bord, hight, stay_items):
    for block in item.blocks:
        try:
            bord[int((hight - block.y) / 21)].append(block)
        except IndexError:
            pass

    check_win(bord, stay_items, hight)


def try_move(shape, direction, stay_items, borders, bord, hight):
    shape1 = copy.deepcopy(shape)
    if direction in ["left", "right"]:
        shape1.move(direction)
        for item in borders + stay_items:
            for block in item.blocks:
                if block in shape1.blocks:
                    return False
        return True
    elif direction in ["down", "up"]:
        shape1.transpose(direction)
        for item in borders + stay_items:
            for block in item.blocks:
                if block in shape1.blocks:
                    return False
        return True


def move_to_stay(item, stays_items, bord, hight, real=True):
    stays_items_new = copy.deepcopy(stays_items)
    if item is square:
        for line in bord:
            for blocks in line:
                for block in blocks.blocks:
                    if block in item.blocks:
                        if real:
                            put_in_bord(item, bord, hight, stays_items_new)
                        item.blocks = []
        return item, stays_items_new
    for block in range(len(item.blocks)):
        b = item.blocks[block]  ##הבלוק של האייתם הנופל
        for i in stays_items:
            for bl in i.blocks:  # הבלוק של האייתם הנייח
                for x in range(i.blocks[0].width):
                    if b.x == bl.x and b.y + b.hight + 1 == bl.y:
                        if real:
                            stays_items_new.append(copy.deepcopy(item))
                            #put_in_bord(item, bord, hight, stays_items_new)
                        item.blocks = []
                        return item, stays_items_new
    for line in bord:
        for block in line.blocks:
            if block in item.blocks:
                if real:
                    put_in_bord(item, bord, hight, stays_items_new)
                item.blocks = []
    return item, stays_items_new


def play_game():
    bord = [[] for i in range(18)]
    count = 0
    pygame.init()
    pygame.key.set_repeat(0, 8000000)
    hight = 500
    width = 800
    bg = (0, 0, 0)
    screen = pygame.display.set_mode((width, hight))
    clock = pygame.time.Clock()
    movement_speed = 3
    stays_items, borders = [], creat_level(hight, width)
    stays_items=stays_items +borders
    #bord[1] = borders
    falling = False
    flif = False
    move = False
    while True:
        screen.fill(bg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if not falling:
            kind = random.choice([line, pluse, cube])
            size = random.choice(range(1, 9))
            if size in [1, 4, 9]:
                kind = cube
            color = random.choice(["red", "green", "blue", "yellow"])

            shape1 = kind(color, 3, width * 0.5, 17, size)
            falling = True

        if keys[pygame.K_LEFT] and try_move(shape1, "left", stays_items, borders, bord, hight) and not move:
            shape1.move("left")
            move = True
        elif keys[pygame.K_RIGHT] and try_move(shape1, "right", stays_items, borders, bord, hight) and not move:
            shape1.move("right")
            move = True
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            move = False

        if keys[pygame.K_UP] and try_move(shape1, "up", stays_items, borders, bord, hight) and not flif:
            shape1.transpose("up")
            flif = True
        elif keys[pygame.K_DOWN] and try_move(shape1, "down", stays_items, borders, bord, hight) and not flif:
            shape1.transpose("down")
            flif = True
        elif not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            flif = False

        for item in stays_items + borders:
            for block in item.blocks:
                pygame.draw.rect(screen, block.color, (block.x, block.y, block.hight, block.width))

        shape1, stays_items = move_to_stay(shape1, stays_items, borders, hight)

        if len(shape1.blocks) == 0:
            falling = False

        if falling:
            for block in shape1.blocks:
                pygame.draw.rect(screen, shape1.color,
                                 (block.x, block.y, block.hight, block.width))
        if count == 30:
            shape1.move("down")
            count = 0
        count += 1
        pygame.display.update()
        pygame.time.Clock()
        clock.tick(80)

pygame.init()
play_game()
