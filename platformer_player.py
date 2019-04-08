#holds Player class, which represents the user-controlled sprite on the screen
#76, 100
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

        #is player currently standing still?
        self.idle = True

        #List of sprites player could bump into
        self.level = None

        sprite_sheet = SpriteSheet("game_images/girlwalksprite.png")
        #Load all the right-facing images into a list
        image = sprite_sheet.get_image(0, 0, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(84, 0, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(167, 0, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(250, 0, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 92, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(84, 92, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(167, 92, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(250, 92, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 183, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(84, 183, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(167, 183, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(250, 183, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 274, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(84, 274, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(167, 274, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(250, 274, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 365, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(84, 365, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(167, 365, 83, 91)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(250, 365, 83, 91)
        self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(0, 455, 83, 91)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(84, 455, 83, 91)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(167, 455, 83, 91)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(250, 455, 83, 91)
        # self.walking_frames_r.append(image)


        #Load all the right-facing images, then flip them to make them face left
        # Load all the right-facing images into a list
        image = sprite_sheet.get_image(0, 0, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(84, 0, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(167, 0, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(250, 0, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 92, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(84, 92, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(167, 92, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(250, 92, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 183, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(84, 183, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(167, 183, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(250, 183, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 274, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(84, 274, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(167, 274, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(250, 274, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 365, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(84, 365, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(167, 365, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(250, 365, 83, 91)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(334, 365, 83, 91)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(0, 455, 83, 91)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(84, 455, 83, 91)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(167, 455, 83, 91)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(250, 455, 83, 91)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(334, 455, 83, 91)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)

        # image = sprite_sheet.get_image(0, 0, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(66, 0, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(132, 0, 67, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(0, 93, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(66, 93, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(132, 93, 72, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(0, 186, 70, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)

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
            if self.idle == False:
                frame = (pos // 20) % len(self.walking_frames_r)
            else:
                frame = 17
            self.image = self.walking_frames_r[frame]
        else:
            if self.idle == False:
                frame = (pos // 20) % len(self.walking_frames_l)
            else:
                frame = 17
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
        self.idle = False

    def go_right(self):
        #called when user hit right arrow
        self.change_x = 6
        self.direction = "R"
        self.idle = False

    def stop(self):
        #called when user lets off the keyboard
        self.change_x = 0
        self.idle = True