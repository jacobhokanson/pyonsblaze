

import pygame
from platformer_spritesheet_functions import SpriteSheet
from platformer_entities import Entity

class Player(pygame.sprite.Sprite, Entity):

    def __init__(self):
        # Call parent constructors
        pygame.sprite.Sprite.__init__(self)
        Entity.__init__(self)

        # Player keeps track of coin  **** SPECIFIC TO THE PLAYER ****
        self.coin = None

        sprite_sheet = SpriteSheet("game_images/girlwalksprite.png")
        self.jumpsound = pygame.mixer.Sound("game_sounds/jump.wav")

        #Load all the right-facing images into a list
        image = sprite_sheet.get_image(84, 365, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(167, 365, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(250, 365, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 0, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(84, 0, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(167, 0, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(250, 0, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 92, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(84, 92, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(167, 92, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(250, 92, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 183, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(84, 183, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(167, 183, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(250, 183, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 274, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(84, 274, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(167, 274, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(250, 274, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 365, 83, 90)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #Set the image the player starts with
        self.image = self.walking_frames_r[0]

        #Set a reference to the image rect
        self.rect = self.image.get_rect()

    def update(self):
        Entity.update(self)

        # Next level coin:
        self.coin_hit = pygame.sprite.collide_rect(self, self.coin)

        enemy_hit = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for atk in enemy_hit:
            if not self.rect.bottom > atk.rect.top + 10:
                atk.die()
            else:
                self.die()

    def die(self):
        """Player die method designed and implemented by Jacob Hokanson"""
        self.change_x = 0
        self.change_y = 0
        self.idle = True

        self.level.world_shift_x(-(self.rect.x + self.level.shift_hori) + self.rect.x)
        self.level.world_shift_y(-(self.rect.y + self.level.shift_vert) + self.rect.y)

        self.rect.left, self.rect.bottom = self.level.platform_list.sprites()[0].rect.x, self.level.platform_list.sprites()[0].rect.y
