"""Coin to end level class designed by Jacob Hokanson & Caleb Magee based on pygame sprite"""

from platformer_spritesheet_functions import SpriteSheet
import random, pygame

class Coin(pygame.sprite.Sprite):
    # A pickup that ends the current level when collected. #
    # Could do other things, effect is implemented by Player #

    def __init__(self):

        super().__init__()

        coin_sprite_sheet = SpriteSheet("game_images/level_end.png")
        self.coin_frames = []

        image = coin_sprite_sheet.get_image(0, 0, 16, 16)
        self.coin_frames.append(image)
        image = coin_sprite_sheet.get_image(17, 0, 16, 16)
        self.coin_frames.append(image)
        image = coin_sprite_sheet.get_image(0, 17, 16, 16)
        self.coin_frames.append(image)
        image = coin_sprite_sheet.get_image(17, 17, 16, 16)
        self.coin_frames.append(image)

        self.image = self.coin_frames[0]

        self.rect = self.image.get_rect()

    def update(self):

        if random.randint(60, 100) == 99:
            self.image = self.coin_frames[(self.coin_frames.index(self.image) + 1) % len(self.coin_frames)]

        if self.coin_frames.index(self.image) > 0:
            self.image = self.coin_frames[(self.coin_frames.index(self.image) + 1) % len(self.coin_frames)]
