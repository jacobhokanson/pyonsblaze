""" Menu Screen class design and use by Caleb Magee """

import pygame
import platformer_constants as constants
from platformer_spritesheet_functions import SpriteSheet


class menuScreen():
    #generic menuScreen
    screen_center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - constants.SCREEN_HEIGHT / 5)
    pygame.font.init()
    fontObj = pygame.font.Font("freesansbold.ttf", 32)
    title = fontObj.render("Pyon's Blaze", True, constants.WHITE)
    title_rect_obj = title.get_rect()
    title_rect_obj.center = (screen_center)
    background = None
    buttonlist = None

    def __init__(self):
        self.buttonlist = pygame.sprite.Group() #initialize button list

    def update(self):
        self.buttonlist.update()

    def draw(self, screen):
        #draw the stuff on the screen
        screen.fill(constants.BLACK)
        screen.blit(self.background, (0, 0))
        screen.blit(self.title, self.title_rect_obj)

        # Draw all the sprite lists that we have
        self.buttonlist.draw(screen)


class homeMenu(menuScreen):

    def __init__(self):
        super().__init__()
        self.title = self.fontObj.render("Pyon's Blaze", True, constants.WHITE)
        self.background = pygame.image.load("game_images/mountain_bg.png").convert_alpha()


# class menuButtons(pygame.sprite.Sprite):
#
#     def __init__(self, sprite_sheet_data):
#         pygame.sprite.Sprite.__init__(self)
#
#         button_sheet = SpriteSheet("game_images/tiles_spritesheet.png")
#         # Grab the image for this platform
#         self.image = button_sheet.get_image(sprite_sheet_data[0],
#                                             sprite_sheet_data[1],
#                                             sprite_sheet_data[2],
#                                             sprite_sheet_data[3])
#         self.rect = self.image.get_rect()
