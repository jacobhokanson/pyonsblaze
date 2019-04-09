#Main class for the side scroller

#Credit to : http://programarcasegames.com/python_examples/sprite_sheets/

#Game art from Kenney.nl: http://opengameart.org/content/platformer-art-deluxe
#<a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by vectorpocket - www.freepik.com</a>
#<a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by brgfx - www.freepik.com</a>

#Sounds
#https://jalastram.itch.io/8-bit-jump-sound-effects/download/eyJleHBpcmVzIjoxNTU0Nzc2NDA3LCJpZCI6NTY1MjJ9.flChJi4ePYJyKySVgpLzZ7BL8yM%3d
#https://freesound.org/people/FoolBoyMedia/sounds/264295/

import pygame
import platformer_constants as constants
import platformer_levels as levels

from platformer_player import Player

def main():
    #Main program
    pygame.init()

    #set height/width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    #Create the player
    player = Player()

    #Create all the levels
    level_list = []
    level_list.append(levels.Level_03(player))
    #level_list.append(levels.Level_02(player))
    #level_list.append(levels.Level_01(player))

    #set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = current_level.player_start_y
    active_sprite_list.add(player)

    #background music
    pygame.mixer.music.load('game_sounds/bg_music_loop.wav')
    pygame.mixer.music.play(-1, 0.0)

    #loop until the user clicks the close button
    done = False

    #used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #--------------Main Program Loop--------------
    while not done:
        for event in pygame.event.get():#User did something
            if event.type == pygame.QUIT: #if user clicked close
                done = True # Flag that we are done so loop is exited

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        #update the player
        active_sprite_list.update()
        #update items in the level
        current_level.update()

        #If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        #if player gets to end of the level, fo to the next level
        current_position  = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                player.rect.y = current_level.player_start_y
                player.rect.x = current_level.player_start_x
            else: break

        #ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        #ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        #limite to 60 frames per second
        clock.tick(60)

        #go ahead and update the screen with what we've drawn
        pygame.display.flip()

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()