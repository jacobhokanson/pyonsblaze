import pygame

import platformer_constants as constants
import platformer_platforms as platforms

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000
    player_start_y = constants.SCREEN_HEIGHT - 100
    player_start_x = 100

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("game_images/citydaytimebackground.jpg").convert()
        self.background.set_colorkey(constants.LIME_GREEN)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500],
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
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("game_images/background_02.png").convert()
        self.background.set_colorkey(constants.LIME_GREEN)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
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

        player_start_y = 200
        player_start_x = 500

class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("game_images/mountain_bg.png").convert()
        self.background.set_colorkey(constants.LIME_GREEN)
        self.level_limit = -3000

        # Array with type of platform, and x, y location of the platform.
        level = [
                  [platforms.GRASS_MIDDLE, 0, constants.SCREEN_HEIGHT - 70],
                  [platforms.GRASS_MIDDLE, 70, constants.SCREEN_HEIGHT - 70],
                  [platforms.GRASS_MIDDLE, 140, constants.SCREEN_HEIGHT - 70],
                  [platforms.GRASS_MIDDLE, 210, constants.SCREEN_HEIGHT - 70],
                  [platforms.GRASS_MIDDLE, 280, constants.SCREEN_HEIGHT - 70],
                  [platforms.GRASS_MIDDLE, 350, constants.SCREEN_HEIGHT - 70],
                  [platforms.GRASS_MIDDLE, 420, constants.SCREEN_HEIGHT - 70],

            [platforms.GRASS_SINGLE, 750, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_LEFT, 900, constants.SCREEN_HEIGHT - 500],
            [platforms.GRASS_RIGHT, 970, constants.SCREEN_HEIGHT - 500],


            [platforms.GRASS_LEFT, 1200, constants.SCREEN_HEIGHT - 70],

            [platforms.DIRT, 1270, constants.SCREEN_HEIGHT - 70],
            [platforms.DIRT, 1270, constants.SCREEN_HEIGHT - 140],
            [platforms.DIRT, 1270, constants.SCREEN_HEIGHT - 210],
            [platforms.GRASS_MIDDLE, 1270, constants.SCREEN_HEIGHT - 280],

            [platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 70],
            [platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 140],
            [platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 210],
            [platforms.DIRT, 1340, constants.SCREEN_HEIGHT - 280],
            [platforms.GRASS_MIDDLE, 1340, constants.SCREEN_HEIGHT - 350],

            [platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 70],
            [platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 140],
            [platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 210],
            [platforms.DIRT, 1410, constants.SCREEN_HEIGHT - 280],
            [platforms.GRASS_MIDDLE, 1410, constants.SCREEN_HEIGHT - 350],

            [platforms.DIRT, 1480, constants.SCREEN_HEIGHT - 70],
            [platforms.DIRT, 1480, constants.SCREEN_HEIGHT - 140],
            [platforms.DIRT, 1480, constants.SCREEN_HEIGHT - 210],
            [platforms.GRASS_MIDDLE, 1480, constants.SCREEN_HEIGHT - 280],

            [platforms.GRASS_MIDDLE, (self.level_limit * -1) - 420 , constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, (self.level_limit * -1) - 350, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, (self.level_limit * -1) - 280, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, (self.level_limit * -1) - 210, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, (self.level_limit * -1) - 140, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, (self.level_limit * -1) - 70, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, (self.level_limit * -1) - 0, constants.SCREEN_HEIGHT - 70],

                  # [platforms.STONE_PLATFORM_LEFT, 650, 550],
                  # [platforms.STONE_PLATFORM_MIDDLE, 720, 550],
                  # [platforms.STONE_PLATFORM_RIGHT, 790, 550],
                  # [platforms.GRASS_LEFT, 800, 400],
                  # [platforms.GRASS_MIDDLE, 870, 400],
                  # [platforms.GRASS_RIGHT, 940, 400],
                  # [platforms.GRASS_LEFT, 1000, 500],
                  # [platforms.GRASS_MIDDLE, 1070, 500],
                  # [platforms.GRASS_RIGHT, 1140, 500],
                  # [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  # [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  # [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
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
        block.rect.x = 600
        block.rect.y = 250
        block.boundary_top = 200
        block.boundary_bottom = 500
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 950
        block.rect.y = constants.SCREEN_HEIGHT - 75
        block.boundary_left = 850
        block.boundary_right = 1100
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1750
        block.rect.y = 350
        block.boundary_top = 100
        block.boundary_bottom = constants.SCREEN_HEIGHT - 100
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2075
        block.rect.y = 200
        block.boundary_top = 100
        block.boundary_bottom = constants.SCREEN_HEIGHT - 100
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2400
        block.rect.y = 450
        block.boundary_top = 100
        block.boundary_bottom = constants.SCREEN_HEIGHT - 100
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)





        player_start_y = constants.SCREEN_HEIGHT - 75
