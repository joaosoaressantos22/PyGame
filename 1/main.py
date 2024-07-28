#!/usr/bin/env python3

import pygame
import random 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Canibal Atack")
wid = 10 
hei = 10
player = pygame.Rect((300, 250, wid, hei))
object = pygame.Rect((random.randint(0,300), random.randint(0,250), 30, 30))

run = True

while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), object)
    key = pygame.key.get_pressed()
    
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(+1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, +1)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)

    if player.colliderect(object):
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()