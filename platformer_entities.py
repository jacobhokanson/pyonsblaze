"""Entity abstract class designed and implemented by Jacob Hokanson"""

import pygame
from platformer_platforms import MovingPlatform
import platformer_constants as constants

class Entity():

    def __init__(self):
        self.change_x = 0
        self.change_y = 0

        self.walking_frames_l = []
        self.walking_frames_r = []

        self.direction = "R"

        #is player currently standing still?
        self.idle = True

        #List of sprites player could bump into
        self.level = None

    def calc_grav(ent):
        #calculate effect of gravity
        if ent.change_y == 0:
            ent.change_y = 1
        else:
            ent.change_y += .35

    def jump(self):
        #move down 2 pixels to see if there is a platform below us. 2 px helps with platforms moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        #if it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0:
            self.change_y = -10
            self.jumpsound.play()

    def go_left(self):
        self.change_x = -6
        self.direction = "L"
        self.idle = False

    def go_right(self):
        self.change_x = 6
        self.direction = "R"
        self.idle = False

    def stop(self):
        self.change_x = 0
        self.idle = True

    def setImage(self):
        pos = self.rect.x + self.level.shift_hori
        imgs = len(self.walking_frames_l)
        if self.direction == "R":
            if self.idle == False:
                frame = (pos // imgs) % imgs
            else:
                frame = 0
            self.image = self.walking_frames_r[frame]
        else:
            if self.idle == False:
                frame = (pos // imgs) % imgs
            else:
                frame = 0
            self.image = self.walking_frames_l[frame]

    def update(self):
        self.calc_grav()

        self.rect.x += self.change_x

        if self.rect.y >= (constants.SCREEN_HEIGHT + self.level.shift_vert) - self.rect.height: #and player.change_y >= 0:
            # falling_sound.play()
            self.die()

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            #if moving right, set right side to the left side of the item hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                #vice-versa if moving left
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # reset position based on top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

        self.setImage()
