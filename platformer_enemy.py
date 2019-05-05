from platformer_spritesheet_functions import SpriteSheet
from platformer_entities import Entity
import pygame, random

sprite_sheet = None

class Enemy(pygame.sprite.Sprite, Entity):
    # """ Superclass for all enemies.
    #     Maybe subclass into different kinds of enemies based on behavior
    #     e.g. walk, fly, how they are killed"""

    """Enemy class for objects"""

    def __init__(self):
        # Call parent constructors
        pygame.sprite.Sprite.__init__(self)
        Entity.__init__(self)

        sprite_sheet = SpriteSheet("game_images/enemy_spritesheet.png")
        self.jumpsound = pygame.mixer.Sound("game_sounds/jump.wav")

        image = sprite_sheet.get_image(0, 0, 128, 56)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 56, 128, 56)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

    def update(self):

        self.act()

        Entity.update(self)

    def act(self):
        cond = random.randint(0, 100)

        if cond > 95:
            self.go_left()
        elif cond < 5:
            self.go_right()
        elif cond == 10:
            self.jump()
        else:
            self.stop()

    def die(self):
        self.change_x = 0
        self.change_y = 0
        self.idle = True

        self.rect.bottom = 0
