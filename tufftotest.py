import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
DISPLAY.fill((255, 255, 255))
pygame.display.set_caption("Pyon's Blaze")


while True:
    
    for event in pygame.event.get():  # Begin main event loop (listen, update, draw)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.time.Clock().tick(30)
