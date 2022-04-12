import random
from Player import *
from Card import *
from room import *
from tkinter import *
from tkinter.ttk import *
from block import *
from PIL import Image, ImageTk
import pygame


class Game:
    # initializer -zach
    def __init__(self):
        self.player_notes = {
            "Colonel Mustard": [0, 0, 0],
            "Professor Plum": [0, 0, 0],
            "Mr. Green": [0, 0, 0],
            "Mrs. Peacock": [0, 0, 0],
            "Miss Scarlet": [0, 0, 0],
            "Mrs. White": [0, 0, 0],
            "Knife": [0, 0, 0],
            "Candlestick": [0, 0, 0],
            "Revolver": [0, 0, 0],
            "Rope": [0, 0, 0],
            "Lead Pipe": [0, 0, 0],
            "Wrench": [0, 0, 0],
            "Hall": [0, 0, 0],
            "Lounge": [0, 0, 0],
            "Dining Room": [0, 0, 0],
            "Kitchen": [0, 0, 0],
            "Ballroom": [0, 0, 0],
            "Conservatory": [0, 0, 0],
            "Billiard Room": [0, 0, 0],
            "Library": [0, 0, 0],
            "Study": [0, 0, 0]
        }
        self.surface = NONE
        self.game_over = False
        self.turn = 0
        self.first_turn = True
        self.rooms = [Room((), "Ballroom", 369, 562),
                      Room((), "Billiard Room", 130, 429),
                      Room((), "Conservatory Room", 130, 615),
                      Room((), "Dining Room", 555, 376),
                      Room((), "Hall", 369, 137),
                      Room((), "Kitchen", 581, 588),
                      Room((), "Lounge", 555, 137),
                      Room((), "Study", 130, 110),
                      Room((), "Library", 130, 270)
                      ]
        # link secret passages
        self.rooms[2].add_passage(self.rooms[6])  # Conservatory -> Lounge
        self.rooms[6].add_passage(self.rooms[2])  # Lounge -> Conservatory
        self.rooms[5].add_passage(self.rooms[7])  # Kitchen -> Study
        self.rooms[7].add_passage(self.rooms[5])  # Study -> Kitchen
        # create instance of block class to use load_blocks method
        dummy_block = Block(None, None, None)
        self.blocks = dummy_block.load_blocks()
        # create starting blocks for each player/suspect
        scarlet_start = Block(475, 58, None)
        green_start = Block(289, 695, None)
        peacock_start = Block(51, 535, None)
        white_start = Block(422, 695, None)
        mustard_start = Block(661, 243, None)
        plum_start = Block(51, 190, None)
        # blocks that are entrances to rooms
        self.blocks[5][3].set_room(self.rooms[7])    # F4, Study
        self.blocks[7][3].set_room(self.rooms[4])    # H4, Hall
        self.blocks[10][6].set_room(self.rooms[4])   # K7, Hall
        self.blocks[11][6].set_room(self.rooms[4])   # L7, Hall
        self.blocks[16][5].set_room(self.rooms[6])   # Q6, Lounge
        self.blocks[16][7].set_room(self.rooms[3])   # Q8, Dining Room
        self.blocks[6][7].set_room(self.rooms[8])    # G8, Library
        self.blocks[0][10].set_room(self.rooms[1])   # A11, Billiard Room
        self.blocks[2][10].set_room(self.rooms[8])   # C11, Library
        self.blocks[14][11].set_room(self.rooms[3])  # O12, Dining Room
        self.blocks[5][14].set_room(self.rooms[1])   # F15, Billiard Room
        self.blocks[4][18].set_room(self.rooms[2])   # E19, Conservatory
        self.blocks[6][18].set_room(self.rooms[0])   # G19, Ballroom
        self.blocks[8][15].set_room(self.rooms[0])   # I16, Ballroom
        self.blocks[13][15].set_room(self.rooms[0])  # N16, Ballroom
        self.blocks[15][18].set_room(self.rooms[0])  # P19, Ballroom
        self.blocks[18][16].set_room(self.rooms[5])  # S17, Kitchen
        # add the entrance blocks to the rooms list of entrances
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                r = self.blocks[i][j].get_room()
                if r is not None:
                    r.add_entrance((i, j))

        # 3 players
        # poss_players = []
        # makes all the players
        # put them in a list
        self.players = []
        self.COMPUTER_1_NAME = "player 2"
        self.COMPUTER_2_NAME = "player 3"
        self.players.append(Player("You", False, 15, 0, (202, 1, 1)))
        self.players.append(Player(self.COMPUTER_1_NAME, True, 8, 22, (2, 187, 0)))
        self.players.append(Player(self.COMPUTER_2_NAME, True, 0, 17, (10, 192, 209)))
        # makes room deck
        self.room_cards = [Card("Ballroom", "room", "images/ballroom.jpg"),
                           Card("Billiard Room", "room", "images/billiard room.jpg"),
                           Card("Conservatory Room", "room", "images/conservatory.jpg"),
                           Card("Dining Room", "room", "images/dining room.jpg"),
                           Card("Hall", "room", "images/hall.jpg"),
                           Card("Kitchen", "room", "images/kitchen.jpg"),
                           Card("Lounge", "room", "images/lounge.jpg"),
                           Card("Library", "room", "images/library.jpg"),
                           Card("Study", "room", "images/study.jpg")
                           ]
        # makes suspect deck
        self.suspect_cards = [Card("Colonel Mustard", "suspect", "images/colonel mustard.jpg"),
                              Card("Miss Scarlet", "suspect", "images/miss scarlet.jpg"),
                              Card("Mr. Green", "suspect", "images/mr. green.jpg"),
                              Card("Mrs. Peacock", "suspect", "images/mrs. peacock.jpg"),
                              Card("Mrs. White", "suspect", "images/mrs. white.jpg"),
                              Card("Professor Plum", "suspect", "images/professor plum.jpg")
                              ]
        # makes weapon deck
        self.weapon_cards = [Card("Candlestick", "weapon", "images/candlestick.jpg"),
                             Card("Knife", "weapon", "images/knife.jpg"),
                             Card("Lead Pipe", "weapon", "images/lead pipe.jpg"),
                             Card("Revolver", "weapon", "images/revolver.jpg"),
                             Card("Rope", "weapon", "images/rope.jpg"),
                             Card("Wrench", "weapon", "images/wrench.jpg")
                             ]
        # deck copies
        # to be used in the computer turn 'AI' and in user input
        self.room_cards_copy = self.room_cards.copy()
        self.suspect_cards_copy = self.suspect_cards.copy()
        self.weapon_cards_copy = self.weapon_cards.copy()
        # Shuffle decks
        random.shuffle(self.room_cards)
        random.shuffle(self.suspect_cards)
        random.shuffle(self.weapon_cards)
        # makes the casefile
        self.casefile_cards = [self.room_cards.pop(0), self.suspect_cards.pop(0), self.weapon_cards.pop(0)]
        # adding all cards together and shuffle them
        self.all_cards = self.room_cards + self.suspect_cards + self.weapon_cards
        random.shuffle(self.all_cards)
        # deal cards to the players
        while len(self.all_cards) > 0:
            for player in self.players:
                player.add_card(self.all_cards.pop())

    # set surface
    def set_surface(self, surface):
        self.surface = surface

    # user_turn function - kevin
    def user_turn(self):
        moves_left = self.roll_dice()
        # moves_left = 10000  # for testing: should be commented out during normal use

        user = self.players[0]

        # give option to solve the case after the first turn
        if not self.first_turn:
            if self.get_user_input("Would you like to solve the case?")[0]:
                if self.solve_case(self.get_card_selection("room")[0], self.get_card_selection("suspect")[0],
                                   self.get_card_selection("weapon")[0]):
                    self.end_game(user.get_name)
                else:
                    # user was wrong (Lost game and just end it)
                    self.end_game(None)
                self.game_over = True
                return

        # get current position on board
        room = None
        for r in self.rooms:
            if r.has_player(user):
                room = r
        self.draw_player(user)
        self.draw_player(self.players[1])
        self.draw_player(self.players[2])
        pygame.display.update()
        # if in a room
        if room is not None:
            recently_exited = False
            if room.has_passage():
                if self.get_user_input("Use Secret Passage?")[0]:
                    room.use_passage(user)
                    room = room.get_passage()
                    self.draw_player(user)
                    self.draw_player(self.players[1])
                    self.draw_player(self.players[2])
                    pygame.display.update()
            if self.get_user_input("Exit Room?")[0]:
                exits = room.get_entrances()
                self.reload_player_blocks()
                for e in exits:
                    if not self.blocks[e[0]][e[1]].has_player():
                        if self.get_user_input("Exit at " + str(e) + "?")[0]:
                            recently_exited = True
                            user.set_x(e[0])
                            user.set_y(e[1])
                            moves_left -= 1
                            if not room.remove_player(user):
                                print("ERROR: user should be in " + room.get_name() + " but isn't")
                                sys.exit(1)
                            room = None
                            if not self.blocks[e[0]][e[1]].set_player(user):
                                # this line shouldn't be reached but is a just in case
                                print("ERROR: user tried to exit in bad exit " + str(e))
                                sys.exit(1)
                            break
                    else:
                        show = True
                        while show:
                            self.display_message("Exit at " + str(e) + " is blocked!")
                            show = False
        else:
            recently_exited = False

        self.draw_player(user)
        self.draw_player(self.players[1])
        self.draw_player(self.players[2])
        pygame.display.update()
        # if user is now outside a room (or never was in one)
        if room is None:
            self.display_message("You rolled: " + str(moves_left))
            declined_entrance = False
            while moves_left > 0:
                self.reload_player_blocks()
                user_coords = user.get_coordinates()
                # print(user_coords)
                # let the user enter the room if they want
                curr_block = self.blocks[user_coords["x"]][user_coords["y"]]
                room = curr_block.get_room()
                if room is not None:
                    if not declined_entrance and not recently_exited and \
                            self.get_user_input("Enter the " + room.get_name() + "?")[0]:
                        curr_block.enter_room()
                        user.set_x(None)
                        user.set_y(None)
                        room.add_player(user)
                        moves_left = 0
                    else:
                        declined_entrance = True
                # let the user move on the board
                valid_move = False
                move = self.arrow_key_input()
                # noinspection DuplicatedCode
                if move == 0:  # up
                    valid_move = self.verify_space(user_coords["x"], user_coords["y"] - 1)
                    if valid_move:
                        user.set_y(user_coords["y"] - 1)
                        curr_block.move_player(self.blocks[user_coords["x"]][user_coords["y"] - 1])
                elif move == 1:  # left
                    valid_move = self.verify_space(user_coords["x"] - 1, user_coords["y"])
                    if valid_move:
                        user.set_x(user_coords["x"] - 1)
                        curr_block.move_player(self.blocks[user_coords["x"] - 1][user_coords["y"]])
                elif move == 2:  # down
                    valid_move = self.verify_space(user_coords["x"], user_coords["y"] + 1)
                    if valid_move:
                        # print(user_coords['y'])
                        user.set_y(user_coords["y"] + 1)
                        # print(user_coords['y'])
                        curr_block.move_player(self.blocks[user_coords["x"]][user_coords["y"]])
                elif move == 3:  # right
                    valid_move = self.verify_space(user_coords["x"] + 1, user_coords["y"])
                    if valid_move:
                        user.set_x(user_coords["x"] + 1)
                        curr_block.move_player(self.blocks[user_coords["x"]][user_coords["y"]])
                if valid_move:
                    moves_left -= 1
                    # reset these after the user moves so they can enter rooms again
                    recently_exited = False
                    declined_entrance = False
                self.draw_player(user)
                self.draw_player(self.players[1])
                self.draw_player(self.players[2])
                pygame.display.update()

        # check if in room again
        if room is not None:
            # let the user make an accusation (what cards they want to ask about)
            accusation_suspect = self.get_card_selection("suspect")[0]
            accusation_weapon = self.get_card_selection("weapon")[0]
            accusation_room = room
            # have some pop up in the gui to click on what cards they are asking about
            # check accusation against next players' cards
            shown_card = False
            computer_number = 1
            while not shown_card and computer_number <= 2:
                cards = self.players[computer_number].get_cards()
                for c in cards:
                    if (accusation_suspect == c or accusation_weapon == c or accusation_room == c) and not shown_card:
                        shown_card = True
                        while True:  # not sure why but this only works in a while loop
                            self.display_image(c.get_image())
                            pygame.display.update()
                            break
                computer_number += 1
        self.first_turn = False

    # computer_turn function - kevin
    def computer_turn(self):
        moves_left = self.roll_dice()

        computer_user = self.players[self.turn]
        # 'solve' the case once the computer has seen or has all the cards (21 total - 3 = 18)
        if len(computer_user.get_cards()) + len(computer_user.get_seen_cards()) == 18:
            self.end_game(computer_user.get_name())
            self.game_over = True
        # get current position on board
        room = None
        old_room = None
        for r in self.rooms:
            if r.has_player(computer_user):
                room = r
        # if in a room
        if room is not None:
            old_room = room
            if room.has_passage():
                # Randomly decide to use passage 50/50 chance
                if random.randrange(0, 2) == 0:
                    room.use_passage(computer_user)
            # Randomly decide to exit room 50/50 chance
            if random.randrange(0, 2) == 0:
                exits = room.get_entrances()
                # exit at first available exit
                for e in exits:
                    if not self.blocks[e[0]][e[1]].has_player():
                        computer_user.set_x(e[0])
                        computer_user.set_y(e[1])
                        moves_left -= 1
                        room = None
                        if not self.blocks[e[0]][e[1]].set_player(computer_user):
                            # this line shouldn't be reached but is a just in case
                            print("ERROR: computer tried to exit in bad exit")
                            sys.exit(1)

        # if user is now outside a room (or never was in one)
        if room is None:
            while moves_left > 0:
                user_coords = computer_user.get_coordinates()
                # let the user enter the room if they want
                curr_block = self.blocks[user_coords["x"]][user_coords["y"]]
                room = curr_block.get_room()
                if room is not None:
                    # enter the room unless it was the one that the computer just came out of
                    # (probably gonna get stuck in a loop of going in the same room repeatedly turn after turn but idc)
                    if room != old_room:
                        curr_block.enter_room()
                        computer_user.set_x(None)
                        computer_user.set_y(None)
                        room.add_player(computer_user)
                        moves_left = 0
                        break
                # let the user move on the board
                valid_move = False
                # this is the computer movement (it is probably bad. Might improve it later)
                move = 0
                # try moves until one works
                while move <= 3:
                    # noinspection DuplicatedCode
                    if move == 0:  # up
                        valid_move = self.verify_space(user_coords["x"], user_coords["y"] - 1)
                        if valid_move:
                            computer_user.set_y(user_coords["y"] - 1)
                            curr_block.move_player(self.blocks[user_coords["x"]][user_coords["y"] - 1])
                    elif move == 1:  # left
                        valid_move = self.verify_space(user_coords["x"] - 1, user_coords["y"])
                        if valid_move:
                            computer_user.set_x(user_coords["x"] - 1)
                            curr_block.move_player(self.blocks[user_coords["x"] - 1][user_coords["y"]])
                    elif move == 2:  # down
                        valid_move = self.verify_space(user_coords["x"], user_coords["y"] + 1)
                        if valid_move:
                            computer_user.set_y(user_coords["y"] + 1)
                            curr_block.move_player(self.blocks[user_coords["x"]][user_coords["y"]])
                    elif move == 3:  # right
                        valid_move = self.verify_space(user_coords["x"] + 1, user_coords["y"])
                        if valid_move:
                            computer_user.set_x(user_coords["x"] + 1)
                            curr_block.move_player(self.blocks[user_coords["x"]][user_coords["y"]])
                    if valid_move:
                        moves_left -= 1
                        move = 4  # exit the move loop
                        # print(computer_user.get_name() + " " + str(computer_user.get_x()) + ", " + str(computer_user.get_y()))
                    move += 1
        # check if in room again
        if room is not None:
            # make the computer guess random stuff
            accusation_suspect = self.suspect_cards_copy[random.randrange(0, 6)]
            accusation_weapon = self.weapon_cards_copy[random.randrange(0, 6)]
            accusation_room = room
            # check accusation against next players' cards
            shown_card = False
            # index of the player who is being asked to show the cards
            asking_player = (self.turn + 1) % 3
            while not shown_card and asking_player != self.turn:
                cards = self.players[asking_player].get_cards()
                for c in cards:
                    if (accusation_suspect == c or accusation_weapon == c or accusation_room == c) and not shown_card:
                        shown_card = True
                        computer_user.add_seen_card(c)
                asking_player = (asking_player + 1) % 3

    # take_turn -kevin
    def take_turn(self):
        # print("take_turn called")
        # pygame.display.update()
        # print out all blocks with players: FOR TESTING
        # print("")
        # for i in range(len(self.blocks)):
        #     for j in range(len(self.blocks[i])):
        #         if self.blocks[i][j].has_player():
        #             print(self.blocks[i][j].get_player().get_name() + " on block " + str(i) + ", " + str(j))
                    # self.blocks[i][j].remove_player()

        # END TESTING SECTION
        if not self.game_over:
            if self.turn == 0:
                pygame.display.update()
                self.user_turn()
            else:
                self.computer_turn()
            self.turn = (self.turn + 1) % 3

    # solve case function - zach
    # returns True if solved correctly False otherwise
    def solve_case(self, room_card, suspect_card, weapon_card):
        if (self.casefile_cards[0] == room_card and self.casefile_cards[1] == suspect_card and
                self.casefile_cards == weapon_card):
            return True
        return False

    # roll dice function - zach
    @staticmethod
    def roll_dice():
        return random.randrange(1, 7) + random.randrange(1, 7)

    # end_game function
    def end_game(self, winner):
        if winner is None:
            show = True
            while show:
                self.display_message("Game Over. Guess was wrong")
                show = False
        else:
            self.display_message(winner.get_name + " wins!")
        self.display_message("It was " + self.casefile_cards[1].get_name() + " with the " +
                             self.casefile_cards[2].get_name() + " in the " + self.casefile_cards[0].get_name())

    def verify_space(self, x, y):
        # returns True if the space exists and has no player, False otherwise
        if x < 0 or x >= len(self.blocks):  # space is outside the board
            return False
        if y < 0 or y >= len(self.blocks[x]):
            return False
        b = self.blocks[x][y]
        if b.has_player() or b.get_coordinates()[0] is None:
            return False
        return True

    # get_user_input function
    # @staticmethod
    def get_user_input(self, prompt):
        self.draw_all_players()
        # gui function to display the prompt
        # ask only yes/no questions
        # yes returns true, no returns false
        # win = Tk()
        # win.withdraw()
        # win.overrideredirect(1)
        # win.update()

        # Temporary class to get the boolean from the callback function on the yes/no buttons
        class TempTrueFalse:
            def __init__(self):
                self.yes_no = None

        # display a gui with all the cards of the given type
        # return the selected card
        win = Tk()
        win.title("Select Yes or No")
        temp_tf = TempTrueFalse()

        def set_return_val(tf):
            temp_tf.yes_no = tf
            win.quit()

        string_label = StringVar()
        string_label.set(prompt)

        # w = win.winfo_width()
        # h = win.winfo_height()
        # x = int((win.winfo_screenwidth() - w) / 2)
        # y = int((win.winfo_screenheight() - h) / 2)
        # win.geometry("+%d+%d" % ( x, y))
        win.overrideredirect(1)

        label = Label(win, textvariable=string_label, font=("Courier", "18"))
        label.pack(pady=10, padx= 10)

        yes_button = Button(win, text="Yes", command=lambda: set_return_val(True))
        no_button = Button(win, text="No", command=lambda: set_return_val(False))
        yes_button.pack(pady=10)
        no_button.pack(pady=10)

        w = 20 + 14 * len(prompt)
        h = 100
        x = int((win.winfo_screenwidth() - w) / 2)
        y = int((win.winfo_screenheight() - h) / 2)
        win.geometry("+%d+%d" % (x, y))

        win.mainloop()

        # please don't look at this line of code (I know it's super hacky)
        # uses win.destroy here so the mainloop ending doesn't stop execution
        return temp_tf.yes_no, win.destroy()
        # return messagebox.askyesno("Input Needed!", prompt)

    def get_card_selection(self, card_type):
        self.draw_all_players()
        # Temporary class to get the selected card from the callback function on each button
        class TempCard:
            def __init__(self):
                self.selected_card = None

        # display a gui with all the cards of the given type
        # return the selected card
        win = Tk()
        win.title("Choose a Card")
        temp_card = TempCard()

        def set_return_val(card):
            temp_card.selected_card = card
            win.quit()

        string_label = StringVar()
        if card_type == "room":
            card_list = self.room_cards_copy
            string_label.set("Guess a Room")
        elif card_type == "suspect":
            string_label.set("Guess a Suspect")
            card_list = self.suspect_cards_copy
        elif card_type == "weapon":
            string_label.set("Guess a Weapon")
            card_list = self.weapon_cards_copy
        else:
            raise Exception("INVALID CARD TYPE")

        x = int((win.winfo_screenwidth() - 100 * len(card_list))/2)
        y = int((win.winfo_screenheight() - 200)/2)
        win.geometry("+%d+%d" % (x, y))
        win.overrideredirect(1)

        label = Label(win, textvariable=string_label, font=("Courier", "18"))
        label.pack(pady=10)

        images = []
        buttons = []

        for i in range(len(card_list)):
            images.append(ImageTk.PhotoImage(Image.open(card_list[i].get_image())))

        # can't be in a loop because messes with lambda functions
        buttons.append(Button(win, image=images[0], command=lambda: set_return_val(card_list[0])))
        buttons.append(Button(win, image=images[1], command=lambda: set_return_val(card_list[1])))
        buttons.append(Button(win, image=images[2], command=lambda: set_return_val(card_list[2])))
        buttons.append(Button(win, image=images[3], command=lambda: set_return_val(card_list[3])))
        buttons.append(Button(win, image=images[4], command=lambda: set_return_val(card_list[4])))
        buttons.append(Button(win, image=images[5], command=lambda: set_return_val(card_list[5])))
        if card_type == "room":
            buttons.append(Button(win, image=images[6], command=lambda: set_return_val(card_list[6])))
            buttons.append(Button(win, image=images[7], command=lambda: set_return_val(card_list[7])))
            buttons.append(Button(win, image=images[8], command=lambda: set_return_val(card_list[8])))
        for button in buttons:
            button.pack(side=LEFT)

        win.mainloop()

        # please don't look at this line of code (I know it's super hacky)
        # uses win.destroy here so the mainloop ending doesn't stop execution
        return temp_card.selected_card, win.destroy()

    def display_message(self, message):
        self.draw_all_players()
        # gui function to display a message to the user
        # user can click on it to dismiss
        window = Tk()
        window.title("A Message")
        x = int(window.winfo_screenwidth()/2 - 15*len(message)/2)
        y = int((window.winfo_screenheight() - 200) / 2)
        window.geometry("+%d+%d" % (x, y))
        window.overrideredirect(1)
        message_str = StringVar()
        message_str.set(message)
        label = Label(window, textvariable=message_str, font=("Courier", "18"))
        label.pack(pady=10)
        ok_button = Button(window, text="Dismiss", command=lambda: window.quit())
        ok_button.pack(side=BOTTOM)
        window.mainloop()
        return window.destroy()

    def display_image(self, image):
        # rewritten to display with tkinter
        self.draw_all_players()
        # gui function to display a message to the user
        # user can click on it to dismiss
        window = Tk()

        image_to_display = ImageTk.PhotoImage(Image.open(image))
        Label(
            window,
            image=image_to_display
        ).pack()
        message = "Card Revealed!"
        window.title("An Image")
        x = int(window.winfo_screenwidth()/2 - 15*len(message)/2)
        y = int((window.winfo_screenheight() - 200) / 2)
        window.geometry("+%d+%d" % (x, y))
        window.overrideredirect(1)
        message_str = StringVar()
        message_str.set(message)
        label = Label(window, textvariable=message_str, font=("Courier", "18"))
        label.pack(pady=10)
        ok_button = Button(window, text="Dismiss", command=lambda: window.quit())
        ok_button.pack(side=BOTTOM)
        window.mainloop()
        return window.destroy()

    def arrow_key_input(self):
        self.draw_all_players()
        events = pygame.event.get()
        move = -1
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move = 0
                if event.key == pygame.K_LEFT:
                    move = 1
                if event.key == pygame.K_DOWN:
                    move = 2
                if event.key == pygame.K_RIGHT:
                    move = 3
                if event.key == pygame.K_n:
                    self.open_notebook()
        return move

    def get_user_cards(self):
        return self.players[0].get_cards()

    def draw_user_cards(self):
        cards = self.get_user_cards()
        x = 70
        y = 800
        for c in cards:
            card_image = pygame.image.load(c.get_image())
            rect = card_image.get_rect()
            rect.center = (x, y)
            self.surface.blit(card_image, rect)
            x += 80
        return

    def draw_player(self, player):
        color = player.get_color()
        if player.get_x() is None or player.get_y() is None:
            room = None
            for r in self.rooms:
                if r.has_player(player):
                    room = r
            if room is None:
                print("ERROR: Player is not in a room or on the board")
                return
            else:
                # don't draw players in rooms on top of each other
                offset = 0
                # print(player.get_name())
                if player.get_name() == self.COMPUTER_1_NAME:
                    # print("CP1")
                    offset = 27
                elif player.get_name() == self.COMPUTER_2_NAME:
                    # print("CP2")
                    offset = -27
                pygame.draw.rect(self.surface, color, (room.get_x() - offset, room.get_y(), 20, 20))
        else:
            pixel_coords = self.blocks[player.get_x()][player.get_y()].get_coordinates()
            x_coord = pixel_coords[0]
            y_coord = pixel_coords[1]
            pygame.draw.rect(self.surface, color, (x_coord - 10, y_coord - 10, 20, 20))
        return

    def get_players(self):
        return self.players

    def draw_all_players(self):
        self.draw_player(self.players[0])
        self.draw_player(self.players[1])
        self.draw_player(self.players[2])
        pygame.display.update()
        return

    def reload_player_blocks(self):
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                self.blocks[i][j].remove_player()

        for p in self.players:
            x = p.get_x()
            y = p.get_y()
            if x is not None and y is not None:
                self.blocks[x][y].set_player(p)

    def open_notebook(self):
        self.draw_all_players()
        # gui function to hold a players notes
        window = Tk()
        player_notes = self.load_note_dict()
        window.title("Notebook")
        x = int(window.winfo_screenwidth() / 2 + 275)
        y = int(window.winfo_screenheight() / 2 - 300)
        window.geometry("+%d+%d" % (x, y))
        window.overrideredirect(1)

        string_vars = [StringVar(value="Colonel Mustard"), StringVar(value="Professor Plum"),
                       StringVar(value="Mr. Green"), StringVar(value="Mrs. Peacock"), StringVar(value="Miss Scarlet"),
                       StringVar(value="Mrs. White"), StringVar(value="Knife"), StringVar(value="Candlestick"),
                       StringVar(value="Revolver"), StringVar(value="Rope"), StringVar(value="Lead Pipe"),
                       StringVar(value="Wrench"), StringVar(value="Hall"), StringVar(value="Lounge"),
                       StringVar(value="Dining Room"), StringVar(value="Kitchen"), StringVar(value="Ballroom"),
                       StringVar(value="Conservatory"), StringVar(value="Billiard Room"), StringVar(value="Library"),
                       StringVar(value="Study")]

        for i in range(len(string_vars)):
            Label(window, textvariable=string_vars[i]).grid(row=i)
            Checkbutton(window, variable=player_notes[string_vars[i].get()][0], onvalue=1, offvalue=0).grid(row=i,
                                                                                                            column=1)
            Checkbutton(window, variable=player_notes[string_vars[i].get()][1], onvalue=1, offvalue=0).grid(row=i,
                                                                                                            column=2)
            Checkbutton(window, variable=player_notes[string_vars[i].get()][2], onvalue=1, offvalue=0).grid(row=i,
                                                                                                            column=3)

        save_button = Button(window, text="Save and Close", command=lambda: self.save_notes(player_notes, window))
        save_button.grid(row=22, column=0)

        window.mainloop()
        return window.destroy()

    def load_note_dict(self):
        player_notes = {}
        for key in self.player_notes:
            player_notes[key] = [IntVar(value=self.player_notes[key][0]), IntVar(value=self.player_notes[key][1]),
                                 IntVar(value=self.player_notes[key][2])]
        return player_notes

    def save_notes(self, notes_dict, window):
        for key in notes_dict:
            self.player_notes[key][0] = notes_dict[key][0].get()
            self.player_notes[key][1] = notes_dict[key][1].get()
            self.player_notes[key][2] = notes_dict[key][2].get()
        return window.quit()

