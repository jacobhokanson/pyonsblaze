#manages the platforms themselves for the platformer game

import pygame
from platformer_spritesheet_functions import SpriteSheet

#These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

GRASS_LEFT              = (576, 70, 70, 70)
GRASS_RIGHT             = (576, 576, 70, 70)
GRASS_MIDDLE            = (504, 576, 70, 70)
STONE_PLATFORM_LEFT     = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE   = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT    = (792, 648, 70, 40)

class Platform(pygame.sprite.Sprite):
    #creates a platform the player can jump on

    def __init__(self, sprite_sheet_data):
        #platform constructor
        super().__init__()

        sprite_sheet = SpriteSheet("game_images/tiles_spritesheet.png")
        #grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    #creates a platform that can move as a subclass of the Platform class

    def __init__(self, sprite_sheet_data):
        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        #moves the platform
        #if the player is in the way, it will shove the player out of the way
        #Does NOT currently have a way to handle if the player is shoved into an object (smashed)

        #Move left/right
        self.rect.x += self.change_x

        # check if platform has hit player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:  # if player has been hit
            # if we are moving right, set player right to the left side of the platform
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                #if player is moving left, set player left to the right side fo the platform
                self.player.rect.left = self.right

        #check if platform has hit player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit: #if player has been hit
            #reset our position based on the top/bottom of the object
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        #check the boundaries to see if we need to reverse platform direction
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1

