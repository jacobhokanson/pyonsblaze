""" Directly from PAG """

import pygame

class SpriteSheet(object):
    #class used to pull individual images out of spritesheet

    def __init__(self, filename):
        #constructor. Pass in the filename of the spritesheet
        #load the spritesheet
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height): #pass in origin x, y of sprite, as well as width and height
        #create new blank image
        image = pygame.Surface([width, height], pygame.SRCALPHA).convert_alpha()

        #copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        return image
