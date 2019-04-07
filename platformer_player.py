#holds Player class, which represents the user-controlled sprite on the screen

import pygame
import platformer_constants as constants
from platformer_platforms import MovingPlatform
from platformer_spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    #this class represents the bar at the bottom that the player controls

    # -- Methods
    def __init__(self):
        #constructor

        #call parent's constructor
        super().__init__()

        #-- Attributes
        #set speed vector of the player
        self.change_x = 0
        self.change_y = 0

        #this holds the images for the animated walk left/right
        self.walking_frames_l = []
        self.walking_frames_r = []

        #what direction is player facing?
        self.direction = "R"

        #List of sprites player could bump into
        self.level = None

        sprite_sheet = SpriteSheet("game_images/p1_walk.png")
        #Load all the right-facing images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)

        #Load all the right-facing images, then flip them to make them face left
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #Set the image the player starts with
        self.image = self.walking_frames_r[0]

        #Set a reference to the image rect
        self.rect = self.image.get_rect()

    def update(self):
        #move the player

        #gravity
        self.calc_grav()

        #move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        #see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            #if moving right, set right side to the left side of the item hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                #vice-versa if moving left
                self.rect.left = block.rect.right

        #move up/down
        self.rect.y += self.change_y

        #check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # reset position based on top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                # vice-versa if moving left
                self.rect.top = block.rect.bottom

            #stop vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        #calculate effect of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        #Check if on ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        #called when user hits jump button

        #move down 2 pixels to see if there is a platform below us. 2 px helps with platforms moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        #if it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):
        #called when user hits left arrow
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        #called when user hit right arrow
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        #called when user lets off the keyboard
        self.change_x = 0