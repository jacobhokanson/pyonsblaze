""" Menu Screen class design and use by Caleb Magee """

import pygame
import platformer_constants as constants
import platformer_platforms as platforms
from platformer_spritesheet_functions import SpriteSheet

sprite_sheet = None


class menu():
    pygame.font.init()
    fontObj = pygame.font.Font("freesansbold.ttf", 32)

    def __init__(self, dataList):

        self.button_list = pygame.sprite.Group()

        self.title = dataList[0]
        self.titletext = self.fontObj.render(self.title, True, constants.WHITE)
        self.title_rect_obj = self.titletext.get_rect()
        self.title_rect_obj.center = (constants.SCREEN_WIDTH * .5, constants.SCREEN_HEIGHT * .2)
        self.background = pygame.image.load(dataList[1]).convert()
        self.create_buttons(dataList[2])

    def create_buttons(self, buttonList):
        for button in buttonList:
            button_sprite_data = button[0]
            title = button[3]
            myFunction = button[4]
            mybutton = menuButton(button_sprite_data, title, myFunction)
            mybutton.rect.x = button[1]
            mybutton.rect.y = button[2]
            self.button_list.add(mybutton)

    def update(self, state, level_selected):
        for button in self.button_list:
            mytuple = pygame.mouse.get_pos()
            xrange = range(button.rect[0], button.rect[0] + button.rect[2])
            yrange = range(button.rect[1], button.rect[1] + button.rect[3])
            if mytuple[0] in xrange and mytuple[1] in yrange:
                #button.image = sprite_sheet.get_image(100, 100, 70, 70)
                press = pygame.mouse.get_pressed()

                if press[0] == 1:
                    state = button.myFunction
                    if state >= 10:
                        level_selected = state - 10
                        print(level_selected)
                        state = 3


            else:
                #button.image = sprite_sheet.get_image(100, 200, 70, 70)
                button.mouseChecker = 0
        self.button_list.update()
        return state, level_selected
        # for button in self.button_list:
        #     mytuple = pygame.mouse.get_pos()
        #     xrange = range(button.rect[0], button.rect[0] + button.rect[2])
        #     yrange = range(button.rect[1], button.rect[1] + button.rect[3])
        #     if mytuple[0] in xrange and mytuple[1] in yrange:
        #         button.image = sprite_sheet.get_image(100, 100, 70, 70)
        #         #print(pygame.mouse.get_pressed())
        #         print("Here")
        #         mousePress = pygame.mouse.get_pressed(0)
        #         print(mousePress)
        #         if mousePress[0] == 0 and button.mouseChecker == 1:
        #             import blaze_main_game as main_game  # allows for using main game functions
        #             print(button.myFunction)
        #             return button.myFunction
        #         button.mouseChecker = mousePress[0]
        #         # for event in pygame.event.get():
        #         #     print(pygame.mouse.get_pressed(1))
        #         #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         #         import blaze_main_game as main_game #allows for using main game functions
        #         #         exec(button.myFunction)
        #
        #     else:
        #         button.image = sprite_sheet.get_image(100, 200, 70, 70)
        #         button.mouseChecker = 0
        # self.button_list.update()
        # return state

    def draw(self, screen):
        screen.fill(constants.BLACK)
        screen.blit(self.background, (0, 0))
        screen.blit(self.titletext, self.title_rect_obj)
        self.button_list.draw(screen)

class menuButton(pygame.sprite.Sprite):
    pygame.font.init()
    fontObj = pygame.font.Font("freesansbold.ttf", 12)

    def __init__(self, image_data, title, myFunction):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.get_image(image_data[0], image_data[1], image_data[2], image_data[3])
        self.rect = self.image.get_rect()
        self.title = title
        self.mouseChecker = 0
        self.myFunction = myFunction
        self.textSurf = self.fontObj.render(self.title, True, constants.BLACK)

def updateMenu(number):
    import blaze_main_game as main_game  # allows for using main game functions
    main_game.current_menu = menu(menu_definitions[number])




"""Menu definitions are as follows: [title, background file path, button list]"""
menu_definitions = \
[
    [
        "Pyon's Blaze",
        "game_images/mountain_bg.png",
        [
            [platforms.BOX, 150, 250, 'Level Select', 1],
            [platforms.BOXX, 550, 250, 'Quit', -1],
        ],
    ],
    [
        "Level Select",
        "game_images/mountain_bg.png",
        [
            [platforms.BOX, 150, 420, "Home Screen", 0],
            [platforms.BOXX, 550, 420, 'Quit', -1],
            [platforms.DIRT, 70, 200, 'Level 1,', 10],
            [platforms.STONE_MIDDLE, 200, 200, 'Level 2', 11],
            [platforms.GRASS_MIDDLE, 330, 200, 'Level 3', 12],
            [platforms.PURPLE_MIDDLE, 460, 200, 'Level 4', 13],
            [platforms.CARPET, 590, 200, 'Level 5', 14],

        ],
    ],
]







def startMenuScreen(screen):
    print("Hello")

    quit_button = thorpy.make_button("Quit", thorpy.functions.quit_func())
    box = thorpy.Box(elements=[quit_button,])

    #background = thorpy.Background(elements=[quit_button])
    #thorpy.store(background)
    menu = thorpy.Menu(box)
    for element in  menu.get_population():
        element.surface = screen
    return menu



class menuScreen():
    #generic menuScreen
    screen_center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - constants.SCREEN_HEIGHT / 5)
    pygame.font.init()
    fontObj = pygame.font.Font("freesansbold.ttf", 32)
    # titletext = fontObj.render(title, True, constants.WHITE)
    # title_rect_obj = titletext.get_rect()
    # title_rect_obj.center = (screen_center)
    background = None
    buttonlist = None

    def __init__(self, title):
        self.buttonlist = pygame.sprite.Group() #initialize button list
        self.title = title
        self.titletext = self.fontObj.render(title, True, constants.WHITE)
        self.title_rect_obj = self.titletext.get_rect()
        self.title_rect_obj.center = (self.screen_center)

    def update(self):
        self.buttonlist.update()

    def draw(self, screen):
        #draw the stuff on the screen
        screen.fill(constants.BLACK)
        screen.blit(self.background, (0, 0))
        screen.blit(self.titletext, self.title_rect_obj)

        # Draw all the sprite lists that we have
        self.buttonlist.draw(screen)
