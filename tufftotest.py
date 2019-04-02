import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pyon's Blaze")
image = pygame.image.load("stripe.png")
move = 'right'
movex = 0
movey = 0

while True:
    DISPLAY.fill((255, 255, 255))
    if move == 'right':
        movex += 20
        if movex >= 688:
            move = 'down'
    elif move == 'down':
        movey += 20
        if movey >= 488:
            move = 'left'
    elif move == 'left':
        movex -= 20
        if movex <= 100:
            move = 'up'
    elif move == 'up':
        movey -= 20
        if movey <= 100:
            move = 'right'

    DISPLAY.blit(image, (movex, movey))

    for event in pygame.event.get():  # Begin main event loop (listen, update, draw)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.time.Clock().tick(60)
