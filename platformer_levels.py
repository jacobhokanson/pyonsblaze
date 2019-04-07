import pygame

import platformer_constants as constants
import platformer_platforms as platforms

class Level():
    #generic super class for levels. A specific child class needs to be defined for each level.

    def __init__(self, player):
        #constructor

        #list of sprites used in all levels.
        self.platform_list = None
        self.enemy_list = None

        #background image
        self.background = None

        #World shift: how far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    #update everything on this level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    #draw everything on this level
    def draw(self, screen):

        #draw background
        screen.fill(constants.BLUE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        #draw all the sprite lists
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        #when user moves left/right, scroll the level

        #keep track of the shift amount
        self.world_shift += shift_x

        #go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

class Level_01(Level):
    #definition for level 1

    def __init__(self, player):

        #Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("game_images/background_01.png").convert()
        self.background.set_colorkey(constants.LIME_GREEN)
        self.level_limit = -2500

        #Array with type of platform, and x, y location of the platform.
        level = [[platforms.GRASS_LEFT, 500, 500],
                 [platforms.GRASS_MIDDLE, 570, 500],
                 [platforms.GRASS_RIGHT, 640, 500],
                 [platforms.GRASS_LEFT, 800, 400],
                 [platforms.GRASS_MIDDLE, 870, 400],
                 [platforms.GRASS_RIGHT, 940, 400],
                 [platforms.GRASS_LEFT, 1000, 500],
                 [platforms.GRASS_MIDDLE, 1070, 500],
                 [platforms.GRASS_RIGHT, 1140, 500],
                 [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                 [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [platforms.STONE_PLATFORM_RIGHT, 1260, 280]
                 ]

        #add all from above array to the platform list
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        #add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("game_images/background_02.png").convert()
        self.background.set_colorkey(constants.LIME_GREEN)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.STONE_PLATFORM_LEFT, 500, 550],
                 [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                 [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                 [platforms.GRASS_LEFT, 800, 400],
                 [platforms.GRASS_MIDDLE, 870, 400],
                 [platforms.GRASS_RIGHT, 940, 400],
                 [platforms.GRASS_LEFT, 1000, 500],
                 [platforms.GRASS_MIDDLE, 1070, 500],
                 [platforms.GRASS_RIGHT, 1140, 500],
                 [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                 [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)