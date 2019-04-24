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
<<<<<<< HEAD
    shift_hori = 0
=======
    world_shift = 0
>>>>>>> master
    shift_vert = constants.SCREEN_HEIGHT
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
        screen.fill(constants.BLACK)
<<<<<<< HEAD
        screen.blit(self.background,(self.shift_hori // 3 - 200,0))
=======
        screen.blit(self.background, (self.world_shift // 3 - 200, 0))
>>>>>>> master

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def world_shift_x(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.shift_hori += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

<<<<<<< HEAD
    def world_shift_y(self, shift_y):

        self.shift_vert += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y
=======
    # def shift_vert(self, shift_y):
    #     """When the user moves up/down and we need to scroll everything: """
    #
    #     self.shift_vert += shift_y
>>>>>>> master

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("game_images/citydaytimebackground.jpg").convert_alpha()
        # self.background.set_colorkey(constants.PINK_KEY)
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

        self.background = pygame.image.load("game_images/background_02.png").convert_alpha()
        # self.background.set_colorkey(constants.PINK_KEY)
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

        self.background = pygame.image.load("game_images/mountain_bg.png").convert_alpha()
        # self.background.set_colorkey(constants.PINK_KEY)
        self.level_limit = -2500

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

            [platforms.GRASS_MIDDLE, 2940, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3010, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3080, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3150, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3220, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3290, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3360, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3430, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3500, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3570, constants.SCREEN_HEIGHT - 70],
            [platforms.GRASS_MIDDLE, 3640, constants.SCREEN_HEIGHT - 70],
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
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 950
        block.rect.y = constants.SCREEN_HEIGHT - 75
        block.boundary_left = 920
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
        player_start_x = 200


class Level_04(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("game_images/city_night_bg.jpg").convert_alpha()
        # self.background.set_colorkey(constants.PINK_KEY)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 420],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 490],
            [platforms.STONE_TOP, -68, constants.SCREEN_HEIGHT - 560],


            [platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, 2, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_TOP, 2, constants.SCREEN_HEIGHT - 420],


            [platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, 70, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_TOP, 70, constants.SCREEN_HEIGHT - 420],

            [platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, 138, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_TOP, 138, constants.SCREEN_HEIGHT - 420],

            [platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, 206, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_TOP, 206, constants.SCREEN_HEIGHT - 420],

            [platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, 274, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_TOP, 274, constants.SCREEN_HEIGHT - 420],

            [platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 342, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_TOP, 342, constants.SCREEN_HEIGHT - 350],


            [platforms.STONE_MIDDLE, 410, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 410, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 410, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_TOP, 410, constants.SCREEN_HEIGHT - 280],

            [platforms.STONE_MIDDLE, 800, 0],
            [platforms.STONE_MIDDLE, 800, 70],
            [platforms.STONE_MIDDLE, 800, 140],
            [platforms.STONE_MIDDLE, 800, 210],

            [platforms.STONE_MIDDLE, 870, 0],
            [platforms.STONE_MIDDLE, 870, 70],
            [platforms.STONE_MIDDLE, 870, 140],
            [platforms.STONE_MIDDLE, 870, 210],

            [platforms.STONE_MIDDLE, 940, 0],
            [platforms.STONE_MIDDLE, 940, 70],
            [platforms.STONE_MIDDLE, 940, 140],
            [platforms.STONE_MIDDLE, 940, 210],

            [platforms.STONE_MIDDLE, 1010, 0],
            [platforms.STONE_MIDDLE, 1010, 70],
            [platforms.STONE_MIDDLE, 1010, 140],
            [platforms.STONE_MIDDLE, 1010, 210],

            [platforms.STONE_MIDDLE, 1080, 0],
            [platforms.STONE_MIDDLE, 1080, 70],
            [platforms.STONE_MIDDLE, 1080, 140],
            [platforms.STONE_MIDDLE, 1080, 210],

            [platforms.STONE_MIDDLE, 1150, 0],
            [platforms.STONE_MIDDLE, 1150, 70],
            [platforms.STONE_MIDDLE, 1150, 140],
            [platforms.STONE_MIDDLE, 1150, 210],

            [platforms.STONE_MIDDLE, 1220, 0],
            [platforms.STONE_MIDDLE, 1220, 70],
            [platforms.STONE_MIDDLE, 1220, 140],
            [platforms.STONE_MIDDLE, 1220, 210],

            [platforms.PURPLE_MIDDLE, 1290, 210],
            [platforms.PURPLE_MIDDLE, 1358, 210],
            [platforms.PURPLE_MIDDLE, 1426, 210],


            [platforms.PURPLE_MIDDLE, 1010, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 1078, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 1146, constants.SCREEN_HEIGHT - 70],

            [platforms.STONE_TOP, 2150, constants.SCREEN_HEIGHT - 300],
            [platforms.STONE_TOP, 2220, constants.SCREEN_HEIGHT - 300],
            [platforms.STONE_TOP, 2290, constants.SCREEN_HEIGHT - 300],





#End platform
            [platforms.PURPLE_LEFT, 2942, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3010, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3078, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3146, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3214, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3282, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3350, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3418, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3486, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3554, constants.SCREEN_HEIGHT - 70],
            [platforms.PURPLE_MIDDLE, 3622, constants.SCREEN_HEIGHT - 70],
                    ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 700
        block.rect.y = constants.SCREEN_HEIGHT - 75
        block.boundary_left = 700
        block.boundary_right = 850
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1360
        block.rect.y = constants.SCREEN_HEIGHT - 125
        block.boundary_left = 1360
        block.boundary_right = 1600
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1750
        block.rect.y = 350
        block.boundary_top = 300
        block.boundary_bottom = constants.SCREEN_HEIGHT - 100
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2099
        block.rect.y = 100
        block.boundary_left = 1730
        block.boundary_right = 2100
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2600
        block.rect.y = 300
        block.boundary_top = 200
        block.boundary_bottom = constants.SCREEN_HEIGHT - 250
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        self.player_start_y = constants.SCREEN_HEIGHT - 483
        self.player_start_x = 100



class Level_05(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)


        self.background = pygame.image.load("game_images/castle.jpg").convert()
        self.background.set_colorkey(constants.PINK_KEY)

        self.level_limit = -4300

        # Array with type of platform, and x, y location of the platform.
        level = [
            [platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 420],
            [platforms.STONE_MIDDLE, -136, constants.SCREEN_HEIGHT - 490],
            [platforms.STONE_TOP, -136, constants.SCREEN_HEIGHT - 560],

            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 420],
            [platforms.STONE_MIDDLE, -68, constants.SCREEN_HEIGHT - 490],
            [platforms.STONE_TOP, -68, constants.SCREEN_HEIGHT - 560],

            [platforms.CARPET, 0, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 70, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 140, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 210, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 280, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 350, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 420, constants.SCREEN_HEIGHT - 70],

            [platforms.CARPET, 490, constants.SCREEN_HEIGHT - 70],

            [platforms.CARPET, 490, constants.SCREEN_HEIGHT - 140],
            [platforms.CARPET, 560, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 560, constants.SCREEN_HEIGHT - 70],

            [platforms.CARPET, 560, constants.SCREEN_HEIGHT - 210],
            [platforms.CARPET, 630, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 630, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 630, constants.SCREEN_HEIGHT - 140],

            [platforms.CARPET, 630, constants.SCREEN_HEIGHT - 280],
            [platforms.CARPET, 700, constants.SCREEN_HEIGHT - 280],
            [platforms.STONE_MIDDLE, 700, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 700, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 700, constants.SCREEN_HEIGHT - 210],

            [platforms.CARPET, 700, constants.SCREEN_HEIGHT - 350],
            [platforms.CARPET, 770, constants.SCREEN_HEIGHT - 350],
            [platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 770, constants.SCREEN_HEIGHT - 280],

            [platforms.STONE_MIDDLE, 1035, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 1035, constants.SCREEN_HEIGHT - 140],
            [platforms.CARPET, 1000, constants.SCREEN_HEIGHT - 200],
            [platforms.CARPET, 1070, constants.SCREEN_HEIGHT - 200],

            [platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 1335, constants.SCREEN_HEIGHT - 280],
            [platforms.CARPET, 1300, constants.SCREEN_HEIGHT - 300],
            [platforms.CARPET, 1370, constants.SCREEN_HEIGHT - 300],

            [platforms.STONE_MIDDLE, 1635, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 1635, constants.SCREEN_HEIGHT - 140],
            [platforms.CARPET, 1600, constants.SCREEN_HEIGHT - 200],
            [platforms.CARPET, 1670, constants.SCREEN_HEIGHT - 200],

            [platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 140],
            [platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 210],
            [platforms.STONE_MIDDLE, 1935, constants.SCREEN_HEIGHT - 280],
            [platforms.CARPET, 1900, constants.SCREEN_HEIGHT - 300],
            [platforms.CARPET, 1970, constants.SCREEN_HEIGHT - 300],



            [platforms.STONE_MIDDLE, 2942, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 3010, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 3078, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 3146, constants.SCREEN_HEIGHT - 70],
            [platforms.STONE_MIDDLE, 3214, constants.SCREEN_HEIGHT - 70],


            [platforms.CARPET, 4310, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4380, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4440, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4510, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4580, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4650, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4720, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4790, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4860, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 4930, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 5000, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 5070, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 5140, constants.SCREEN_HEIGHT - 70],
            [platforms.CARPET, 5210, constants.SCREEN_HEIGHT - 70],

                    ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2100
        block.rect.y = constants.SCREEN_HEIGHT - 400
        block.boundary_left = 2100
        block.boundary_right = 2600
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2600
        block.rect.y = constants.SCREEN_HEIGHT - 200
        block.boundary_left = 2100
        block.boundary_right = 2600
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3300
        block.rect.y = constants.SCREEN_HEIGHT - 125
        block.boundary_left = 3300
        block.boundary_right = 4250
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        self.player_start_y = constants.SCREEN_HEIGHT - 100
        self.player_start_x = 100
