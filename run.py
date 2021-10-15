from termcolor import colored, cprint
from random import randint
import time


class Player:
    """
    Player class, Creates player, sets player name, counter colour, player type
    (Real or Computer)
    """

    def __init__(self, name, counter_color, player_type):
        self.name = name
        self.color = counter_color
        self.type = player_type


class Board:
    """
    Main Board Class, Sets the game type, board size ,vs?
    Has methods for printing the board, adding player turns.
    """

    def __init__(self, game_type, size, _vs):
        self.game_type = game_type
        self.size = size
        o_ctr = "\u25CB"
        self.board = [[o_ctr for x in range(size[0])] for y in range(size[1])]
        self.title = str
        self._vs = _vs
        self.turns = []

    def print_table(self):
        _title = (" " * 10) + "CONNECT-4" + (" " * 10)
        cprint(_title, 'green', 'on_white', attrs=['reverse'])

        print(self.title)

        print("-" * 29)
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("-" * 29)

        column_numbers = [(str(i+1)) for i in range(self.size[0])]
        print("| " + " | ".join(column_numbers) + " |")
        column_bar = (" " * 11) + "Columns" + (" " * 11)
        cprint(column_bar, 'green', 'on_white', attrs=['reverse'])


def play_game(game_board, player_one, player_two):

    title_vs = f"{player_one.name} VS {player_two.name}"
    title_len = (len(title_vs)-1)
    _gap = round((29-title_len)/2)
    game_board.title = (" " * (_gap)) + title_vs + (" " * _gap)

    first_turn(player_one, player_two)
    turn_switch(game_board, player_one, player_two)


def first_turn(player_one, player_two):
    print("\nTo see who plays first we flip a coin...\n")
    rand_int = randint(1, 2)
    print(f"Player One: {player_one.name}, choose:")
    print("1. Heads\n2. Tails")
    plr_input = input("")
    print("The coin is flipped...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    if rand_int == 1:
        print("The coin shows Heads")
    else:
        print("The coin shows Tails")

    if int(plr_input) == rand_int:
        print(f"{player_one.name} you will go first")
        player_one.turn_pos = 1
        player_two.turn_pos = 2
        time.sleep(2)
    else:
        print(f"{player_two.name} go first")
        player_one.turn_pos = 2
        player_two.turn_pos = 1
        if player_two.type == "player":
            time.sleep(2)


def turn_switch(game_board, player_one, player_two):
    for i in range(int(game_board.size[0]*game_board.size[1])):
        while player_one.turn_pos == 2:
            make_turn(game_board, player_two)
            player_one.turn_pos = 1
            player_two.turn_pos = 2
            i += 1
            break
        else:
            while player_two.turn_pos == 2:
                make_turn(game_board, player_one)
                player_one.turn_pos = 2
                player_two.turn_pos = 1
                i += 1
                break
    game_board.print_table()
    print("Draw")


def player_turn(game_board, player):
    _ctr = colored("\u25CF", player.color)
    print(f"{player.name}'s turn ({_ctr} counters)")
    print("Choose a column number to drop your counter")
    while True:
        try:
            player_input = int(input("(Input a value from 1 - 7):\n"))
            while game_board.board[0][player_input-1] != "\u25CB":
                print(f"Column {player_input} is full, try again:")
                player_input = int(input(""))
                continue
            for i in range(game_board.size[1]):
                while game_board.board[-1-i][player_input-1] != "\u25CB":
                    break
                else:
                    game_board.board[-1-i][player_input-1] = _ctr
                    break
            break
        except ValueError:
            print("This is not a number.")
            print("Choose a column number to drop your counter")
    check_win(game_board, -1-i, int(player_input)-1, _ctr, player)


def computer_turn(game_board, player):
    rand_time = randint(1, 2)
    _ctr = colored("\u25CF", player.color)
    print(f"{player.name}'s turn ({_ctr} counters)")
    print(".")
    time.sleep(rand_time)
    print("..")
    time.sleep(rand_time)
    print("...")
    time.sleep(rand_time)
    computer_input = randint(0, 6)

    while game_board.board[0][computer_input] != "\u25CB":
        computer_input = randint(0, 6)
        continue
    for i in range(game_board.size[1]):
        while game_board.board[-1-i][computer_input] != "\u25CB":
            break
        else:
            game_board.board[-1-i][computer_input] = _ctr
            break
    check_win(game_board, -1-i, computer_input, _ctr, player)


def make_turn(game_board, player):
    if player.type == "player":
        game_board.print_table()
        player_turn(game_board, player)
    elif player.type == "computer":
        game_board.print_table()
        computer_turn(game_board, player)
    # make_turn(game_board, player)


def check_win(game_board, _y, _x, _ctr, player):
    """
    y (-1 to -6) bottom of array to top, x 0 to 6)
    """
    # vertical check (down only)
    if _y < -3:
        count = 0
        for i in range(1, 4):
            if game_board.board[_y+i][_x] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)
    horizontal_check(game_board, _y, _x, _ctr, player)
    right_diagonal_check(game_board, _y, _x, _ctr, player)
    left_diagonal_check(game_board, _y, _x, _ctr, player)


def right_diagonal_check(game_board, _y, _x, _ctr, player):
    # diagonal check ---x<
    #                --o-<
    #                -o--<
    #                o---<
    if _x < 4 and _y < -3:
        count = 0
        for i in range(1, 4):
            if game_board.board[_y+i][_x-i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # diagonal check ---o<
    #                --x-<
    #                -o--<
    #                o---<
    if 1 < _x < 6 and -6 < _y < -2:
        count = 0
        if game_board.board[_y-1][_x+1] == _ctr:
            count = 1
        for i in range(1, 3):
            if game_board.board[_y+i][_x-i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # diagonal check ---o<
    #                --o-<
    #           ^^   -x--<
    #                o---<
    if 0 < _x < 5 and -5 < _y < -1:
        count = 0
        if game_board.board[_y+1][_x-1] == _ctr:
            count = 1
        for i in range(1, 3):
            if game_board.board[_y-i][_x+i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # diagonal check ---o<
    #                --o-<
    #           ^^   -o--<
    #                x---<
    if _x < 4 and _y > -4:
        count = 0
        for i in range(1, 4):
            if game_board.board[_y-i][_x+i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)


def left_diagonal_check(game_board, _y, _x, _ctr, player):
    # diagonal check x---<
    #                -o--<
    #                --o-<
    #                ---o<
    if _x < 4 and _y < -3:
        count = 0
        for i in range(1, 4):
            if game_board.board[_y+i][_x+i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # diagonal check o---<
    #                -x--<
    #                --o-<
    #                ---o<
    if 0 < _x < 5 and -6 < _y < -2:
        count = 0
        if game_board.board[_y-1][_x-1] == _ctr:
            count = 1
        for i in range(1, 3):
            if game_board.board[_y+i][_x+i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # diagonal check o---<
    #                -o--<
    #             ^^ --x-<
    #                ---o<
    if 1 < _x < 6 and -5 < _y < -1:
        count = 0
        if game_board.board[_y+1][_x+1] == _ctr:
            count = 1
        for i in range(1, 3):
            if game_board.board[_y-i][_x-i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # diagonal check o---<
    #                -o--<
    #             ^^ --o-<
    #                ---x<
    if _x > 2 and _y > -4:
        count = 0
        for i in range(1, 4):
            if game_board.board[_y-i][_x-i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)


def horizontal_check(game_board, _y, _x, _ctr, player):
    # horizontal check X--->
    if _x < 4:
        count = 0
        for i in range(1, 4):
            if game_board.board[_y][_x+i] == _ctr:
                count += 1

        if count == 3:
            _win(game_board, player)

    # horizontal check -X-->
    if 0 < _x < 5:
        count = 0
        if game_board.board[_y][_x-1] == _ctr:
            count = 1
        for i in range(1, 3):
            if game_board.board[_y][_x+i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # horizontal check <---X
    if _x > 2:
        count = 0
        for i in range(1, 4):
            if game_board.board[_y][_x-i] == _ctr:
                count += 1
        if count == 3:
            _win(game_board, player)

    # horizontal check <--x-
    if 1 < _x < 6:
        count = 0
        if game_board.board[_y][_x+1] == _ctr:
            count = 1
        for i in range(1, 3):
            if game_board.board[_y][_x-i] == _ctr:
                count += 1
                print(count)
        if count == 3:
            _win(game_board, player)


def _win(game_board, player):
    game_board.print_table()
    player_wins = f"{player.name} Wins!\n"
    player_wins_len = len(player_wins)
    _gap = round((29 - player_wins_len) / 2) + 1
    win_block = colored("!**CONNECT-4**!", "red", "on_yellow")
    print("")
    print((" "*7)+(win_block)+(" "*7))
    print("")
    print((" " * _gap) + player_wins + (" " * _gap))
    print("To play again press Enter")
    player_input = input("")
    while player_input != "":
        player_input = input("To play again press Enter\n")
    new_game()


def colour_pick(ctr_color_list, player_names):
    number_list = []
    for i in range(len(ctr_color_list)):
        i += 1
        number_list.append(str(i) + ".")
    print(f"\n{player_names[-1]} choose your counter color:")
    for number, color in zip(number_list, ctr_color_list):
        print(number, color.capitalize())
    while True:
        try:
            number_col = int(input(""))
            while True:
                if number_col > len(ctr_color_list) or number_col < 1:
                    print("\nThe number you entered is not in the list.")
                    print("Try again:\n")
                    for number, color in zip(number_list, ctr_color_list):
                        print(number, color.capitalize())
                    break
                else:
                    return ctr_color_list[number_col-1]
        except ValueError:
            print("This is not a number.\nChoose a number from the list:\n")
            for number, color in zip(number_list, ctr_color_list):
                print(number, color.capitalize())


def how_to():
    print("\nConnect 4 Rules\n")
    print("OBJECTIVE:")
    print("Be the first player to connect 4 of your colored counters in a row")
    print("(either vertically, horizontally, or diagonally)")
    print("\nHOW TO PLAY:")
    print("First, decide who goes first and what color each player will have.")
    print("Players alternate turns, only one counter can be dropped per turn.")
    print("On your turn, drop one counter into any of the seven columns.")
    print("The game ends when there is a 4-in-a-row or a stalemate/draw.")
    print("The starter of the previous game goes second on the next game.")
    while input("\nPress enter to go back.\n") != "":
        input("Press enter to go back.\n")
    new_game()


def title_screen():
    print("*" + ("-" * 54) + "*")
    print("*"+' _____ _____ _   _ _   _ _____ _____ _____        ___ '+"*")
    print("*"+'/  __ \  _  | \ | | \ | |  ___/  __ \_   _|      /   |'+"*")
    print("*"+'| /  \/ | | |  \| |  \| | |__ | /  \/ | |______ / /| |'+"*")
    print("*"+'| |   | | | | . ` | . ` |  __|| |     | |______/ /_| |'+"*")
    print("*"+'| \__/\ \_/ / |\  | |\  | |___| \__/\ | |      \___  |'+"*")
    print("*"+(' \____/\___/\_| \_|_| \_|____/ \____/ \_/          |_/')+"*")
    print("*" + ("-" * 54) + "*")
    print("*" + (" " * 13) + "Welcome to Python CONNECT-4!" + (" " * 13) + "*")
    _xtra = (" " * 5) + "*"
    print("*"+(" " * 5)+"Code Institute Project 3 - Python Essentials"+_xtra)
    print("*" + (" " * 15) + "Created by: James Dybacz" + (" " * 15) + "*")
    print("*" + (" " * 19) + "Copyright 2021 \u00A9" + (" " * 19) + "*")
    print("*" + ("-" * 54) + "*")


def new_game():
    """
    Starts a new game, collects player name.
    """
    title_screen()
    print("Game type:")
    print("1. 1P vs AI\n2. 1P vs 2P\n3. How to play")
    while True:
        try:
            select_players = int(input(""))
            while True:
                if select_players > 3 or select_players < 1:
                    print("That number is not available for selection\n")
                    print("Please select a Game type (1 - 3)\n")
                    print("1. 1P vs AI\n2. 1P vs 2P\n3. How to play")
                    select_players = int(input(""))
                else:
                    if select_players == 1:
                        num_players = 1
                    elif select_players == 2:
                        num_players = 2
                    elif select_players == 3:
                        how_to()
                    break
            break
        except (ValueError, TypeError):
            print("That is not a numer\n")
            print("Please select a Game type using its number (1 - 3)\n")
            print("1. 1P vs AI\n2. 1P vs 2P\n3. How to play")

    ctr_color_list = ["green", "yellow", "blue", "magenta", "cyan"]
    pl_names = []
    if num_players == 1:
        input_one = input("Player 1 - Please enter your name: \n")
        while len(input_one) > 10:
            print("Name too long - Please try a shorter name:")
            input_one = input("")
        pl_names.append(input_one)
        plr_clr = colour_pick(ctr_color_list, pl_names)
        print(f"{pl_names[0]} selected {plr_clr} "+colored("\u25CF", plr_clr))
        ctr_color_list.remove(plr_clr)
        player_one = Player(pl_names[0], plr_clr, "player")
        pl_names.append("Computer")
        player_two = Player(pl_names[1], "red", "computer")
    elif num_players == 2:
        input_one = input("Player 1 - Please enter your name: \n")
        while len(input_one) > 10:
            print("Name too long - Please try a shorter name:")
            input_one = input("")
        pl_names.append(input_one)
        plr_clr = colour_pick(ctr_color_list, pl_names)
        print(f"{pl_names[0]} selected {plr_clr} "+colored("\u25CF", plr_clr))
        ctr_color_list.remove(plr_clr)
        player_one = Player(pl_names[0], plr_clr, "player")
        input_two = input("\nPlayer 2 - Please enter your name: \n")
        while len(input_two) > 10:
            print("Name too long - Please try a shorter name:")
            input_two = input("")
        pl_names.append(input_two)
        plr_clr = colour_pick(ctr_color_list, pl_names)
        print(f"{pl_names[1]} selected {plr_clr} "+colored("\u25CF", plr_clr))
        ctr_color_list.remove(plr_clr)
        player_two = Player(pl_names[1], plr_clr, "player")

    game_board = Board("Classic", [7, 6], "Player")
    play_game(game_board, player_one, player_two)


new_game()
