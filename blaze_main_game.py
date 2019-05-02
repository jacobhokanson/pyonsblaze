#Main class for the side scroller

#Credit to : http://programarcasegames.com/python_examples/sprite_sheets/ for the skeleton

#Game art from Kenney.nl: http://opengameart.org/content/platformer-art-deluxe
#<a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by vectorpocket - www.freepik.com</a>
#<a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by brgfx - www.freepik.com</a>
#<a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by vectorpocket - www.freepik.com</a>
#<a href="https://www.freepik.com/free-photos-vectors/business">Business vector created by katemangostar - www.freepik.com</a>
#<a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by brgfx - www.freepik.com</a>



#Sounds
#https://jalastram.itch.io/8-bit-jump-sound-effects/download/eyJleHBpcmVzIjoxNTU0Nzc2NDA3LCJpZCI6NTY1MjJ9.flChJi4ePYJyKySVgpLzZ7BL8yM%3d
#https://freesound.org/people/FoolBoyMedia/sounds/264295/
#https://freesound.org/people/plasterbrain/sounds/395443/
#https://freesound.org/people/Tuudurt/sounds/275104/


import pygame
import platformer_constants as constants
import platformer_levels as levels
import menu_screens

from platformer_player import Player
from platformer_interactables import Coin
from platformer_levels import level_definitions

def main():

    #Main program
    pygame.init()

    #set height/width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("ZcrollBois")

    #Create the player
    player = Player()
    winner = False

    # Create the coin
    end_coin = Coin()

    #Create Menu Screens
    menu_screen_list = []
    menu_screen_list.append(menu_screens.homeMenu())

    #start current menu at the first one
    current_menu_no = 0
    current_menu = menu_screen_list[current_menu_no]
    inMenu = True
    inGame = True

    active_sprite_list = pygame.sprite.Group()

    active_sprite_list.add(player)  # keep here

    #background music
    pygame.mixer.music.load('game_sounds/bg_music_loop.wav')
    pygame.mixer.music.play(-1, 0.0)

    falling_sound = pygame.mixer.Sound("game_sounds/falling.wav")

    #loop until the user clicks the close button
    done = False

    #used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #--------------Main Program Loop--------------
    while not done:
        if inMenu:
            current_menu.update()
            current_menu.draw(screen)
            for event in pygame.event.get():#User did something
                if event.type == pygame.QUIT: #if user clicked close
                    done = True # Flag that we are done so loop is exited
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        inMenu = False
                    current_level_no = 0
                    current_level = levels.NewLevel(player, level_definitions[current_level_no])
                    setupLevel(player, end_coin, current_level)


        elif inGame:
            for event in pygame.event.get():#User did something
                if event.type == pygame.QUIT: #if user clicked close
                    done = True # Flag that we are done so loop is exited

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()
                    if event.key == pygame.K_p:  # COORDINATES DEVKEY
                        print(str(player.rect.x + -current_level.shift_hori) + ",", player.rect.y)
                    if event.key == pygame.K_F5:  # RESET DEVKEY
                        player.die()
                    if event.key == pygame.K_EQUALS:
                            if current_level_no < len(level_definitions)-1:
                                current_level_no += 1
                                current_level = levels.NewLevel(player, level_definitions[current_level_no])
                                setupLevel(player, end_coin, current_level)
                            else:
                                winner = True
                                break

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
                current_level.world_shift_x(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if player.rect.left <= 120:
                diff = 120 - player.rect.left
                player.rect.left = 120
                current_level.world_shift_x(diff)

            # If the player gets near the top, shift the world down (-y)
            if player.rect.top <= 100:
                diff = 100 - player.rect.top
                player.rect.top = 100
                current_level.world_shift_y(diff)

            if player.rect.bottom >= 500 and current_level.shift_vert >= 0:
                diff = player.rect.bottom - 500
                player.rect.bottom = 500
                current_level.world_shift_y(-diff)
                

            # if player hits bottom of the screen, reset
            if player.rect.y >= (constants.SCREEN_HEIGHT + current_level.shift_vert) - player.rect.height: #and player.change_y >= 0:
                falling_sound.play()
                player.die()


            if player.coin_hit:
                if current_level_no < len(level_definitions)-1:
                    current_level_no += 1
                    current_level = levels.NewLevel(player, level_definitions[current_level_no])
                    setupLevel(player, end_coin, current_level)
                else:
                    winner = True
                    break

            #ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)
            active_sprite_list.draw(screen)
            #ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        #limit to 60 frames per second
        clock.tick(60)

        #go ahead and update the screen with what we've drawn
        pygame.display.flip()
    # done = False
    pygame.mixer.music.stop()

    win_music = pygame.mixer.music.load("game_sounds/winsound.mp3")

    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render("You Won!", True, constants.WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)

    if winner is True:
        pygame.mixer.music.play(1)
        while not done:
            for event in pygame.event.get():#User did something
                if event.type == pygame.QUIT: #if user clicked close
                    done = True # Flag that we are done so loop is exited
            screen.fill(constants.BLACK)
            screen.blit(textSurfaceObj, textRectObj)
            pygame.display.flip()


    pygame.quit()

def setupLevel(player, coin, level):
    level.interact_list.add(coin)
    player.level = level
    player.coin = coin
    player.rect.x, player.rect.y = current_level.player_start
    player.change_y = 0
    coin.rect.x, coin.rect.y = level.coin_xy

if __name__ == "__main__":
    main()
