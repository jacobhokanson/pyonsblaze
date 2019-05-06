import pygame

import platformer_constants as constants
import platformer_platforms as platforms
from platformer_enemy import Enemy

class NewLevel():
    """ New Level class based on PAG Level class, redesigned by Jacob Hokanson """

    def __init__(self, player, datalist):

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        self.background = pygame.image.load(datalist[0]).convert()

        self.create_static_platforms(datalist[1])
        self.create_moving_platforms(datalist[2])
        self.create_enemies(datalist[3])

        self.coin_xy = datalist[4]

        self.shift_hori = 0
        self.shift_vert = 0

    def create_static_platforms(self, platlist):
        """ Dynamic Platform builder by Jacob Hokanson """
        for platform in platlist:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            self.platform_list.add(block)

    def create_moving_platforms(self, movlist):
        """ Dynamic MovingPlatform builder by Jacob Hokanson """
        for platform in movlist:
            block = platforms.MovingPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.boundary_top = platform[3]
            block.boundary_left = platform[4]
            block.boundary_right = platform[5]
            block.boundary_bottom = platform[6]
            block.change_x = platform[7]
            block.change_y = platform[8]
            block.player = self.player
            block.level = self
            self.platform_list.add(block)

            # bound1 = platforms.MovingMarker()
            # bound1.rect.x, bound1.rect.y = block.rect.x + 23, block.rect.y + 8
            # self.interact_list.add(bound1)
            # bound1 = platforms.MovingMarker()
            # bound1.rect.x, bound1.rect.y = block.boundary_right + 23, block.boundary_bottom + 8
            # self.interact_list.add(bound1)

    def create_enemies(self, enlist):
        """ Dynamic enemy builder by Jacob Hokanson """
        for en in enlist:
            enemy = Enemy()
            enemy.rect.x = en[0]
            enemy.rect.y = en[1]
            enemy.player = self.player
            enemy.level = self
            self.enemy_list.add(enemy)

    def update(self):
        # Update everything in this level. #
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        # Draw everything on this level. #

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.shift_hori // 3 - 200,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def world_shift_x(self, shift_x):

        # Keep track of the shift amount
        self.shift_hori += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    def world_shift_y(self, shift_y):
        """ Based on shift_world method from PAG, added by Jacob Hokanson """

        self.shift_vert += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

""" Level defenition tuple tree structure by Jacob Hokanson
    Level design for level 1, 2, and 3 from PAG, levels 4 and 5 by Caleb Magee"""
# Definition will follow this format: [background file path, static platform list, moving platform list, (coin_x, coin_y), (player_start_x, player_start_y)]
level_definitions = \
(
    (  # Level 1:
        "game_images/citydaytimebackground.jpg",  # Background image path 0
        (  # Static platform list 1
            (platforms.STONE_SINGLE, 130, 500),

            (platforms.GRASS_LEFT, 500, 500),
            (platforms.GRASS_MIDDLE, 570, 500),
            (platforms.GRASS_RIGHT, 640, 500),
            (platforms.GRASS_LEFT, 800, 400),
            (platforms.GRASS_MIDDLE, 870, 400),
            (platforms.GRASS_RIGHT, 940, 400),
            (platforms.STONE_PLATFORM_LEFT, 1120, 280),
            (platforms.STONE_PLATFORM_MIDDLE, 1190, 280),
            (platforms.STONE_PLATFORM_RIGHT, 1260, 280)
        ),
        (  # Moving platform list follows this structure: (sprite location, x, y, top, left, right, bottom, dx, dy) 2
            (platforms.STONE_SINGLE, 1350, 280, 0, 1350, 1600, 0, 1, 0),
        ),
        (  # Interactable list 3
            # put enemies here
        ),
        (1780, 91), # Coin_x and Coin_y 4
    ),  # End level 1

    (  # Level 2:
        "game_images/background_02.png",  # Background image path 0
        (  # static platform list 1
            (platforms.STONE_PLATFORM_LEFT, 100, 550),

            (platforms.STONE_PLATFORM_MIDDLE, 170, 550),
            (platforms.STONE_PLATFORM_RIGHT, 240, 550),
            (platforms.STONE_PLATFORM_LEFT, 500, 550),
            (platforms.STONE_PLATFORM_MIDDLE, 570, 550),
            (platforms.STONE_PLATFORM_RIGHT, 640, 550),
            (platforms.GRASS_LEFT, 800, 400),
            (platforms.GRASS_MIDDLE, 870, 400),
            (platforms.GRASS_RIGHT, 940, 400),
            (platforms.STONE_PLATFORM_LEFT, 1120, 280),
            (platforms.STONE_PLATFORM_MIDDLE, 1190, 280),
            (platforms.STONE_PLATFORM_RIGHT, 1260, 280),
        ),
        (  # Moving platform list 2
            (platforms.STONE_SINGLE, 1500, 300, 250, 0, 0, 550, 0, -1),
        ),
        (  # Interactables list 3
            # put enemies here
        ),
        (1750, 100), # Coin_x and Coin_y 4
    ),  # End level 2

    (  # Level 3:
        "game_images/mountain_bg.png",  # Background image path
        (
            (platforms.GRASS_LEFT, 0, constants.SCREEN_HEIGHT - 70),

            (platforms.GRASS_MIDDLE, 70, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 140, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 210, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 280, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 350, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_RIGHT, 420, constants.SCREEN_HEIGHT - 70),

            (platforms.GRASS_SINGLE, 750, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_LEFT, 900, constants.SCREEN_HEIGHT - 500),
            (platforms.GRASS_RIGHT, 970, constants.SCREEN_HEIGHT - 500),

            (platforms.GRASS_LEFT, 1200, constants.SCREEN_HEIGHT - 70),

            (platforms.DIRT, 1270, constants.SCREEN_HEIGHT - 70),
            (platforms.DIRT, 1270, constants.SCREEN_HEIGHT - 140),
            (platforms.DIRT, 1270, constants.SCREEN_HEIGHT - 210),
            (platforms.GRASS_MIDDLE, 1270, constants.SCREEN_HEIGHT - 280),

            (platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 70),
            (platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 140),
            (platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 210),
            (platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 280),
            (platforms.GRASS_MIDDLE, 1340, constants.SCREEN_HEIGHT - 350),

            (platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 70),
            (platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 140),
            (platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 210),
            (platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 280),
            (platforms.GRASS_MIDDLE, 1410, constants.SCREEN_HEIGHT - 350),

            (platforms.DIRT, 1480, constants.SCREEN_HEIGHT - 70),
            (platforms.DIRT, 1480, constants.SCREEN_HEIGHT - 140),
            (platforms.DIRT, 1480, constants.SCREEN_HEIGHT - 210),
            (platforms.GRASS_MIDDLE, 1480, constants.SCREEN_HEIGHT - 280),

            (platforms.GRASS_MIDDLE, 2940, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3010, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3080, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3150, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3220, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3290, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3360, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3430, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3500, constants.SCREEN_HEIGHT - 70),
            (platforms.GRASS_MIDDLE, 3570, constants.SCREEN_HEIGHT - 70),
        ),
        (  # Moving platform list
            #(sprite, x, y, top, left, right, bottom, dx, dy)
            (platforms.STONE_SINGLE, 600, 250, 200, 0, 0, 500, 0, -2),
            (platforms.STONE_SINGLE, 950, 525, 0, 920, 1100, 0, 1, 0),
            (platforms.STONE_SINGLE, 1750, 350, 100, 0, 0, 500, 0, -1),
            (platforms.STONE_SINGLE, 2075, 200, 100, 0, 0, 500, 0, -1),
            (platforms.STONE_SINGLE, 2400, 450, 100, 0, 0, 500, 0, -1),
        ),
        (  # Interactables list
            # put enemies here
        ),
        (3500, 400), # Coin_x and Coin_y
    ),  #End level 3

    (  # Level 4:
        "game_images/city_night_bg.jpg",  # Background image path 0
        (  # Static platform list 1
            (platforms.STONE_TOP, 138, constants.SCREEN_HEIGHT - 420),

            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 420),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 490),
            (platforms.STONE_TOP, -68, constants.SCREEN_HEIGHT - 560),

            (platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_TOP, 2, constants.SCREEN_HEIGHT - 420),

            (platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_TOP, 70, constants.SCREEN_HEIGHT - 420),

            (platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 350),

            (platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_TOP, 206, constants.SCREEN_HEIGHT - 420),

            (platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_TOP, 274, constants.SCREEN_HEIGHT - 420),

            (platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_TOP, 342, constants.SCREEN_HEIGHT - 350),

            (platforms.STONE_MIDDLE, 410, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 410, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 410, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_TOP, 410, constants.SCREEN_HEIGHT - 280),

            (platforms.STONE_MIDDLE, 800, 0),
            (platforms.STONE_MIDDLE, 800, 70),
            (platforms.STONE_MIDDLE, 800, 140),
            (platforms.STONE_MIDDLE, 800, 210),

            (platforms.STONE_MIDDLE, 870, 0),
            (platforms.STONE_MIDDLE, 870, 70),
            (platforms.STONE_MIDDLE, 870, 140),
            (platforms.STONE_MIDDLE, 870, 210),

            (platforms.STONE_MIDDLE, 940, 0),
            (platforms.STONE_MIDDLE, 940, 70),
            (platforms.STONE_MIDDLE, 940, 140),
            (platforms.STONE_MIDDLE, 940, 210),

            (platforms.STONE_MIDDLE, 1010, 0),
            (platforms.STONE_MIDDLE, 1010, 70),
            (platforms.STONE_MIDDLE, 1010, 140),
            (platforms.STONE_MIDDLE, 1010, 210),

            (platforms.STONE_MIDDLE, 1080, 0),
            (platforms.STONE_MIDDLE, 1080, 70),
            (platforms.STONE_MIDDLE, 1080, 140),
            (platforms.STONE_MIDDLE, 1080, 210),

            (platforms.STONE_MIDDLE, 1150, 0),
            (platforms.STONE_MIDDLE, 1150, 70),
            (platforms.STONE_MIDDLE, 1150, 140),
            (platforms.STONE_MIDDLE, 1150, 210),

            (platforms.STONE_MIDDLE, 1220, 0),
            (platforms.STONE_MIDDLE, 1220, 70),
            (platforms.STONE_MIDDLE, 1220, 140),
            (platforms.STONE_MIDDLE, 1220, 210),

            (platforms.PURPLE_MIDDLE, 1290, 210),
            (platforms.PURPLE_MIDDLE, 1358, 210),
            (platforms.PURPLE_MIDDLE, 1426, 210),


            (platforms.PURPLE_MIDDLE, 1010, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 1078, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 1146, constants.SCREEN_HEIGHT - 70),

            (platforms.STONE_TOP, 2150, constants.SCREEN_HEIGHT - 300),
            (platforms.STONE_TOP, 2220, constants.SCREEN_HEIGHT - 300),
            (platforms.STONE_TOP, 2290, constants.SCREEN_HEIGHT - 300),

            #End platform
            (platforms.PURPLE_LEFT, 2942, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3010, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3078, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3146, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3214, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3282, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3350, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3418, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3486, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3554, constants.SCREEN_HEIGHT - 70),
            (platforms.PURPLE_MIDDLE, 3622, constants.SCREEN_HEIGHT - 70),
        ),
        (  # Moving platform list follows this structure: (sprite location, x, y, top, left, right, bottom, dx, dy) 2
            (platforms.STONE_SINGLE, 700, 525, 0, 700, 850, 0, 2, 0),
            (platforms.STONE_SINGLE, 1360, 475, 0, 1360, 1600, 0, 2, 0),
            (platforms.STONE_SINGLE, 1750, 350, 300, 0, 0, 500, 0, -1),
            (platforms.STONE_SINGLE, 2100, 100, 0, 1730, 2100, 0, 2, 0),
            (platforms.STONE_SINGLE, 2600, 300, 200, 0, 0, 350, 0, -2),
        ),
        (  # Interactable list 3
            # put enemies here
        ),
        (3560, 400), # Coin_x and Coin_y 4
    ),  #End level 4

    (  # Level 5:
        "game_images/castle.jpg",  # Background image path 0
        (  # Static platform list 1
            (platforms.CARPET, 70, constants.SCREEN_HEIGHT - 70),

            (platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 420),
            (platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 490),
            (platforms.STONE_TOP, -136, constants.SCREEN_HEIGHT - 560),

            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 420),
            (platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 490),
            (platforms.STONE_TOP, -68, constants.SCREEN_HEIGHT - 560),

            (platforms.CARPET, 0, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 140, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 210, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 280, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 350, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 420, constants.SCREEN_HEIGHT - 70),

            (platforms.CARPET, 490, constants.SCREEN_HEIGHT - 70),

            (platforms.CARPET, 490, constants.SCREEN_HEIGHT - 140),
            (platforms.CARPET, 560, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 560, constants.SCREEN_HEIGHT - 70),

            (platforms.CARPET, 560, constants.SCREEN_HEIGHT - 210),
            (platforms.CARPET, 630, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 630, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 630, constants.SCREEN_HEIGHT - 140),

            (platforms.CARPET, 630, constants.SCREEN_HEIGHT - 280),
            (platforms.CARPET, 700, constants.SCREEN_HEIGHT - 280),
            (platforms.STONE_MIDDLE, 700, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 700, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 700, constants.SCREEN_HEIGHT - 210),

            (platforms.CARPET, 700, constants.SCREEN_HEIGHT - 350),
            (platforms.CARPET, 770, constants.SCREEN_HEIGHT - 350),
            (platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 280),

            (platforms.STONE_MIDDLE, 1035, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 1035, constants.SCREEN_HEIGHT - 140),
            (platforms.CARPET, 1000, constants.SCREEN_HEIGHT - 200),
            (platforms.CARPET, 1070, constants.SCREEN_HEIGHT - 200),

            (platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 280),
            (platforms.CARPET, 1300, constants.SCREEN_HEIGHT - 300),
            (platforms.CARPET, 1370, constants.SCREEN_HEIGHT - 300),

            (platforms.STONE_MIDDLE, 1635, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 1635, constants.SCREEN_HEIGHT - 140),
            (platforms.CARPET, 1600, constants.SCREEN_HEIGHT - 200),
            (platforms.CARPET, 1670, constants.SCREEN_HEIGHT - 200),

            (platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 140),
            (platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 210),
            (platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 280),
            (platforms.CARPET, 1900, constants.SCREEN_HEIGHT - 300),
            (platforms.CARPET, 1970, constants.SCREEN_HEIGHT - 300),

            (platforms.STONE_MIDDLE, 2942, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 3010, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 3078, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 3146, constants.SCREEN_HEIGHT - 70),
            (platforms.STONE_MIDDLE, 3214, constants.SCREEN_HEIGHT - 70),

            (platforms.CARPET, 4310, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4380, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4440, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4510, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4580, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4650, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4720, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4790, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4860, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 4930, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 5000, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 5070, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 5140, constants.SCREEN_HEIGHT - 70),
            (platforms.CARPET, 5210, constants.SCREEN_HEIGHT - 70),
        ),
        (  # Moving platform list follows this structure: (sprite location, x, y, top, left, right, bottom, dx, dy) 2
            (platforms.STONE_SINGLE, 2100, 200, 0, 2100, 2600, 0, 2, 0),
            (platforms.STONE_SINGLE, 2600, 400, 0, 2100, 2600, 0, 2, 0),
            (platforms.STONE_SINGLE, 3300, 475, 0, 3300, 4250, 0, 2, 0),
        ),
        (  # Interactable list 3
            # put enemies here
            (4770, 400),
        ),
        (5150, 350), # Coin_x and Coin_y 4
    ),  # End level 5
)
