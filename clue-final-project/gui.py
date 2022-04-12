from game import *
import pygame
from screen import *
from button import *
import threading

BACKGROUND = (128, 86, 61)
FONT_COLOR = (235, 166, 38)
PLAY_COLOR = (94, 181, 106)
PLAY_HOVER = (42, 82, 48)
HELP_COLOR = (186, 58, 184)
HELP_HOVER = (74, 23, 73)
TITLE_COLOR = (255, 255, 255)
TITLE_BORDER_COLOR = (194, 23, 23)
TITLE_BACK_COLOR = (28, 99, 12)


pygame.init()
pygame.font.init()

start_screen = Screen("Clue Start Screen", BACKGROUND, 1000, 880)
play_screen = Screen("Clue Board", BACKGROUND, 1000, 880)
help_screen = Screen("Clue Help", BACKGROUND, 1000, 880)

start_screen.make_current()

# toggle = False

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/board.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(355,375)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Help(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/rsz_help_screens.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (500,375)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


BOARD1 = Board()
HELP = Help()
game_title_font = pygame.font.SysFont('malgungothic', 40, True, False)

done = False

first_loop = True

play_button = Button(350, 400, 300, 100, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "Play")
help_button = Button(350, 600, 300, 100, HELP_COLOR, HELP_HOVER, "ariel", 40, FONT_COLOR, "Help")

COLUMN1X = 860
COLUMN2X = 880
COLUMN3X = 900

YCORDSTART = 440
SIDELENGTH = 10

#Column labels
notes_title_btn = Button(880, 0, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Notes")
notes_p1_btn = Button(860, 20, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 15, FONT_COLOR, "You")
notes_p2_btn = Button(880, 20, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 15, FONT_COLOR, "P2")
notes_p3_btn = Button(900, 20, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 15, FONT_COLOR, "P3")

#Row labels
row_1_label = Button(820, 40, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Colonel Mustard")
row_2_label = Button(820, 60, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Miss Scarlet")
row_3_label = Button(820, 80, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Mr. Green")
row_4_label = Button(820, 100, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Mrs. Peacock")
row_5_label = Button(820, 120, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Mrs. White")
row_6_label = Button(820, 140, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Professor Plum")
row_7_label = Button(820, 160, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Candlestick")
row_8_label = Button(820, 180, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Knife")
row_9_label = Button(820, 200, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Lead Pipe")
row_10_label = Button(820, 220, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Revolver")
row_11_label = Button(820, 240, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Rope")
row_12_label = Button(820, 260, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Wrench")
row_13_label = Button(820, 280, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Ballroom")
row_14_label = Button(820, 300, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Billiard Room")
row_15_label = Button(820, 320, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Conservatory")
row_16_label = Button(820, 340, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Dining Room")
row_17_label = Button(820, 360, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Hall")
row_18_label = Button(820, 380, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Kitchen")
row_19_label = Button(820, 400, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Lounge")
row_20_label = Button(820, 420, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Library")
row_21_label = Button(820, 440, 0, 0, BACKGROUND, PLAY_HOVER, "ariel", 20, FONT_COLOR, "Study")

pA1 = Button(COLUMN1X, YCORDSTART, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA2 = Button(COLUMN1X, YCORDSTART-20, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA3 = Button(COLUMN1X, YCORDSTART-40, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA4 = Button(COLUMN1X, YCORDSTART-60, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA5 = Button(COLUMN1X, YCORDSTART-80, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA6 = Button(COLUMN1X, YCORDSTART-100, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA7 = Button(COLUMN1X, YCORDSTART-120, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA8 = Button(COLUMN1X, YCORDSTART-140, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA9 = Button(COLUMN1X, YCORDSTART-160, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA10 = Button(COLUMN1X, YCORDSTART-180, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA11 = Button(COLUMN1X, YCORDSTART-200, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA12 = Button(COLUMN1X, YCORDSTART-220, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA13 = Button(COLUMN1X, YCORDSTART-240, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA14 = Button(COLUMN1X, YCORDSTART-260, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA15 = Button(COLUMN1X, YCORDSTART-280, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA16 = Button(COLUMN1X, YCORDSTART-300, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA17 = Button(COLUMN1X, YCORDSTART-320, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA18 = Button(COLUMN1X, YCORDSTART-340, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA19 = Button(COLUMN1X, YCORDSTART-360, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA20 = Button(COLUMN1X, YCORDSTART-380, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pA21 = Button(COLUMN1X, YCORDSTART-400, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")

pB1 = Button(COLUMN2X, YCORDSTART, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB2 = Button(COLUMN2X, YCORDSTART-20, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB3 = Button(COLUMN2X, YCORDSTART-40, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB4 = Button(COLUMN2X, YCORDSTART-60, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB5 = Button(COLUMN2X, YCORDSTART-80, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB6 = Button(COLUMN2X, YCORDSTART-100, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB7 = Button(COLUMN2X, YCORDSTART-120, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB8 = Button(COLUMN2X, YCORDSTART-140, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB9 = Button(COLUMN2X, YCORDSTART-160, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB10 = Button(COLUMN2X, YCORDSTART-180, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB11 = Button(COLUMN2X, YCORDSTART-200, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB12 = Button(COLUMN2X, YCORDSTART-220, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB13 = Button(COLUMN2X, YCORDSTART-240, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB14 = Button(COLUMN2X, YCORDSTART-260, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB15 = Button(COLUMN2X, YCORDSTART-280, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB16 = Button(COLUMN2X, YCORDSTART-300, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB17 = Button(COLUMN2X, YCORDSTART-320, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB18 = Button(COLUMN2X, YCORDSTART-340, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB19 = Button(COLUMN2X, YCORDSTART-360, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB20 = Button(COLUMN2X, YCORDSTART-380, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pB21 = Button(COLUMN2X, YCORDSTART-400, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")

pC1 = Button(COLUMN3X, YCORDSTART, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC2 = Button(COLUMN3X, YCORDSTART-20, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC3 = Button(COLUMN3X, YCORDSTART-40, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC4 = Button(COLUMN3X, YCORDSTART-60, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC5 = Button(COLUMN3X, YCORDSTART-80, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC6 = Button(COLUMN3X, YCORDSTART-100, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC7 = Button(COLUMN3X, YCORDSTART-120, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC8 = Button(COLUMN3X, YCORDSTART-140, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC9 = Button(COLUMN3X, YCORDSTART-160, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC10 = Button(COLUMN3X, YCORDSTART-180, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC11 = Button(COLUMN3X, YCORDSTART-200, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC12 = Button(COLUMN3X, YCORDSTART-220, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC13 = Button(COLUMN3X, YCORDSTART-240, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC14 = Button(COLUMN3X, YCORDSTART-260, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC15 = Button(COLUMN3X, YCORDSTART-280, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC16 = Button(COLUMN3X, YCORDSTART-300, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC17 = Button(COLUMN3X, YCORDSTART-320, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC18 = Button(COLUMN3X, YCORDSTART-340, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC19 = Button(COLUMN3X, YCORDSTART-360, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC20 = Button(COLUMN3X, YCORDSTART-380, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")
pC21 = Button(COLUMN3X, YCORDSTART-400, SIDELENGTH, SIDELENGTH, PLAY_COLOR, PLAY_HOVER, "ariel", 40, FONT_COLOR, "")


def take_notes():
    print("take_notes thread")
    notes_title_btn.show_button(play_screen.return_screen())
    notes_p1_btn.show_button(play_screen.return_screen())
    notes_p2_btn.show_button(play_screen.return_screen())
    notes_p3_btn.show_button(play_screen.return_screen())

    row_1_label.show_button(play_screen.return_screen())
    row_2_label.show_button(play_screen.return_screen())
    row_3_label.show_button(play_screen.return_screen())
    row_4_label.show_button(play_screen.return_screen())
    row_5_label.show_button(play_screen.return_screen())
    row_6_label.show_button(play_screen.return_screen())
    row_7_label.show_button(play_screen.return_screen())
    row_8_label.show_button(play_screen.return_screen())
    row_9_label.show_button(play_screen.return_screen())
    row_10_label.show_button(play_screen.return_screen())
    row_11_label.show_button(play_screen.return_screen())
    row_12_label.show_button(play_screen.return_screen())
    row_13_label.show_button(play_screen.return_screen())
    row_14_label.show_button(play_screen.return_screen())
    row_15_label.show_button(play_screen.return_screen())
    row_16_label.show_button(play_screen.return_screen())
    row_17_label.show_button(play_screen.return_screen())
    row_18_label.show_button(play_screen.return_screen())
    row_19_label.show_button(play_screen.return_screen())
    row_20_label.show_button(play_screen.return_screen())
    row_21_label.show_button(play_screen.return_screen())

    pA1.show_button(play_screen.return_screen())
    pA2.show_button(play_screen.return_screen())
    pA3.show_button(play_screen.return_screen())
    pA4.show_button(play_screen.return_screen())
    pA5.show_button(play_screen.return_screen())
    pA6.show_button(play_screen.return_screen())
    pA7.show_button(play_screen.return_screen())
    pA8.show_button(play_screen.return_screen())
    pA9.show_button(play_screen.return_screen())
    pA10.show_button(play_screen.return_screen())
    pA11.show_button(play_screen.return_screen())
    pA12.show_button(play_screen.return_screen())
    pA13.show_button(play_screen.return_screen())
    pA14.show_button(play_screen.return_screen())
    pA15.show_button(play_screen.return_screen())
    pA16.show_button(play_screen.return_screen())
    pA17.show_button(play_screen.return_screen())
    pA18.show_button(play_screen.return_screen())
    pA19.show_button(play_screen.return_screen())
    pA20.show_button(play_screen.return_screen())
    pA21.show_button(play_screen.return_screen())

    pB1.show_button(play_screen.return_screen())
    pB2.show_button(play_screen.return_screen())
    pB3.show_button(play_screen.return_screen())
    pB4.show_button(play_screen.return_screen())
    pB5.show_button(play_screen.return_screen())
    pB6.show_button(play_screen.return_screen())
    pB7.show_button(play_screen.return_screen())
    pB8.show_button(play_screen.return_screen())
    pB9.show_button(play_screen.return_screen())
    pB10.show_button(play_screen.return_screen())
    pB11.show_button(play_screen.return_screen())
    pB12.show_button(play_screen.return_screen())
    pB13.show_button(play_screen.return_screen())
    pB14.show_button(play_screen.return_screen())
    pB15.show_button(play_screen.return_screen())
    pB16.show_button(play_screen.return_screen())
    pB17.show_button(play_screen.return_screen())
    pB18.show_button(play_screen.return_screen())
    pB19.show_button(play_screen.return_screen())
    pB20.show_button(play_screen.return_screen())
    pB21.show_button(play_screen.return_screen())

    pC1.show_button(play_screen.return_screen())
    pC2.show_button(play_screen.return_screen())
    pC3.show_button(play_screen.return_screen())
    pC4.show_button(play_screen.return_screen())
    pC5.show_button(play_screen.return_screen())
    pC6.show_button(play_screen.return_screen())
    pC7.show_button(play_screen.return_screen())
    pC8.show_button(play_screen.return_screen())
    pC9.show_button(play_screen.return_screen())
    pC10.show_button(play_screen.return_screen())
    pC11.show_button(play_screen.return_screen())
    pC12.show_button(play_screen.return_screen())
    pC13.show_button(play_screen.return_screen())
    pC14.show_button(play_screen.return_screen())
    pC15.show_button(play_screen.return_screen())
    pC16.show_button(play_screen.return_screen())
    pC17.show_button(play_screen.return_screen())
    pC18.show_button(play_screen.return_screen())
    pC19.show_button(play_screen.return_screen())
    pC20.show_button(play_screen.return_screen())
    pC21.show_button(play_screen.return_screen())

    button_list = [pA1,pA2,pA3,pA4,pA5,pA6,pA7,pA8,pA9,pA10,pA11,pA12,pA13,pA14,pA15,pA16,pA17,pA18,pA19,pA20,pA21,
                   pB1,pB2,pB3,pB4,pB5,pB6,pB7,pB8,pB9,pB10,pB11,pB12,pB13,pB14,pB15,pB16,pB17,pB18,pB19,pB20,pB21,
                   pC1,pC2,pC3,pC4,pC5,pC6,pC7,pC8,pC9,pC10,pC11,pC12,pC13,pC14,pC15,pC16,pC17,pC18,pC19,pC20,pC21
                   ]

    for button in button_list:
        click_test = button.mouse_check(mouse_coord, mouse_press)
        if click_test:
            if button.get_color() == TITLE_COLOR:
                button.set_color(PLAY_COLOR)
                print("clicked")
            else:
                button.set_color(TITLE_COLOR)


game = Game()

show = True
while not done:
    start_screen.screen_update()
    play_screen.screen_update()
    help_screen.screen_update()
    mouse_coord = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    # keys = pygame.key.get_pressed()

    if start_screen.check_current():
        game.set_surface(start_screen.return_screen())
        title_text = "Welcome to the game of Clue"
        pygame.draw.rect(start_screen.return_screen(), TITLE_BORDER_COLOR, [180, 160, 640, 150])
        pygame.draw.rect(start_screen.return_screen(), TITLE_BACK_COLOR, [190, 170, 620, 130])
        title = game_title_font.render(title_text, True, TITLE_COLOR)
        start_screen.return_screen().blit(title, [210, 200])
        play = play_button.mouse_check(mouse_coord, mouse_press)
        play_button.show_button(start_screen.return_screen())
        help = help_button.mouse_check(mouse_coord, mouse_press)
        help_button.show_button(start_screen.return_screen())

        if play:
            win = play_screen.make_current()
            start_screen.end_current()

        elif help:
            win = help_screen.make_current()
            start_screen.end_current()

    if play_screen.check_current():
        # display board and user cards
        BOARD1.draw(play_screen.return_screen())
        # can put next two lines into a for loop to iterate through a deck of cards
        game.draw_user_cards()

        # can add a help button here

        # testing display_message and display_image functions of the game class
        # card = Card("a_card", "suspect", "images/mrs. peacock.jpg")


        game.set_surface(play_screen.return_screen())
        # player = game.get_players()[0]

        # if first_loop:
            # take_notes()
            # notes_thread = threading.Thread(target=take_notes(), daemon=True)
            # notes_thread.start()
        if not game.game_over and not first_loop:
            # take_notes()
            # turn_thread = threading.Thread(target=game.take_turn())
            # turn_thread.start()
            # turn_thread.join()
            game.take_turn()
        first_loop = False

    # Sean - help screen displays help_screen image (image may need updating)
    if help_screen.check_current():
        HELP.draw(help_screen.return_screen())

        game.set_surface(help_screen.return_screen())

        # add play button
        play_button.change_xy(350, 700)
        play = play_button.mouse_check(mouse_coord, mouse_press)
        play_button.show_button(start_screen.return_screen())
        if play:
            win = play_screen.make_current()
            help_screen.end_current()

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True

    pygame.display.update()

pygame.quit()
