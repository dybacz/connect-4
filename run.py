from termcolor import colored, cprint
from random import randint
import time


class Player:
    """
    Player class, Creates player, sets player name, counter color, player type
    (Real or Computer)
    """

    def __init__(self, name, counter_color, player_type):
        self.name = name
        self.color = counter_color
        self.type = player_type


class Board:
    """
    Main Board Class, Sets the game type, board size.
    Has methods for printing the board, adding player turns.
    """

    def __init__(self, game_type, size):
        self.game_type = game_type
        self.size = size
        o_ctr = "\u25CB"
        self.board = [[o_ctr for x in range(size[0])] for y in range(size[1])]
        self.title = str

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
    """
    Generates title from player names, stores it to gameboard variable .title
    initiates first turn(includes coin toss)
    initiates turn switching algorithm.
    """

    title_vs = f"{player_one.name} VS {player_two.name}"
    title_len = (len(title_vs)-1)
    _gap = round((29-title_len)/2)
    game_board.title = (" " * (_gap)) + title_vs + (" " * _gap)

    first_turn(player_one, player_two)
    turn_switch(game_board, player_one, player_two)


def first_turn(player_one, player_two):
    """
    Coin toss to decide who goes first, coin face decided from
    random integer 0 or 1.
    Input from user is validated within a range of 2 [1, 2] and passed
    through exception handeling for ValueError check
    Initial player turn position generated and stored in each players
    class object as player.turn_pos
    """
    print("\nTo see who plays first we flip a coin...\n")
    rand_int = randint(1, 2)
    print(f"Player One: {player_one.name}, choose:")
    while True:
        print("1. Heads\n2. Tails")
        try:
            plr_input = int(input("\n"))
            while True:
                if plr_input > 2 or plr_input < 1:
                    print("The number you entered is not in the list.")
                    print("Try again:\n")
                    break
                else:
                    print("The coin is flipped...")
                    time.sleep(2)
                    print("...")
                    time.sleep(2)
                    if rand_int == 1:
                        print("The coin shows Heads")
                    else:
                        print("The coin shows Tails")

                    if plr_input == rand_int:
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
                    return
        except ValueError:
            print("\nThis is not a number.")
            print("Choose a number from the list:")
            print("\n1. Heads\n2. Tails")


def turn_switch(game_board, player_one, player_two):
    """
    calculates amount of turns left from gameboard size, starts game.
    loops through turns, changing turn_pos of each player after every turn.
    Draw condition met if all turns are completed and no win condition met.
    """
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
    print("To play again press Enter")
    player_input = input("\n")
    while player_input != "":
        player_input = input("To play again press Enter\n")
    new_game()


def player_turn(game_brd, player):
    """
    Initiates player turn, sets color of counter from color variable in
    each players class.
    Takes player input for column. This input is validated in the range 1-7
    -1 is subtracted from this value to give true array index values.
    Exception handleing is done on input to make sure no ValueErrors occur.
    Once data is validated, loop though column is used until next empty place
    players colored counter is added to that empty place.
    Full columns are also handled in this function.
    """
    _ctr = colored("\u25CF", player.color)
    print(f"{player.name}'s turn ({_ctr} counters)")
    print("Choose a column number to drop your counter")
    while True:
        try:
            player_inpt = int(input("(Input a value from 1 - 7):\n"))
            while True:
                if player_inpt > 7 or player_inpt < 1:
                    print(f"Column {player_inpt} does not exist.")
                    print("Choose a different column to drop your counter in")
                    player_inpt = int(input("(Input a value from 1 - 7):\n"))
                else:
                    while game_brd.board[0][player_inpt-1] != "\u25CB":
                        print(f"Column {player_inpt} is full, try again:")
                        player_inpt = int(input("\n"))
                        continue
                    for i in range(game_brd.size[1]):
                        while game_brd.board[-1-i][player_inpt-1] != "\u25CB":
                            break
                        else:
                            game_brd.board[-1-i][player_inpt-1] = _ctr
                            break
                    check_win(game_brd, -1-i, int(player_inpt)-1, _ctr, player)
                    break
            break
        except ValueError:
            print("This is not a number.")
            print("Choose a column number to drop your counter")
        except IndexError:
            print("This is not a column.")
            print("Choose a column number to drop your counter")


def computer_turn(game_board, player):
    """
    Similar to player_turn but no need for validating or exception handleing
    Column is selected from random integer generated between 0 - 6
    (true array index values)
    time.sleep used to give the effect of artificial thinking.
    Full columns are also handled in this function.
    """
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
    """
    function used to determine which turn function should be used.
    Also prints game board before each turn.
    """
    if player.type == "player":
        game_board.print_table()
        player_turn(game_board, player)
    elif player.type == "computer":
        game_board.print_table()
        computer_turn(game_board, player)


def check_win(game_board, _y, _x, _ctr, player):
    """
    Holds all functions used for checking win conditions are met
    vertical has a single downwards.
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
    """
    Function for checking right pointing diagonal win conditions (4 in total)
    each check has diagram with X being the the counter last placed
    and o being the counters that are checked relative to x.
    """
    # diagonal check ---x<
    #                --o-<
    #                -o--<
    #                o---<
    if _x > 2 and _y < -3:
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
    """
    Function for checking left pointing diagonal win conditions (4 in total)
    each check has diagram with X being the the counter last placed
    and o being the counters that are checked relative to x.
    """
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
    """
    Function for horizontal win conditions (4 in total)
    each check has diagram with X being the the counter last placed
    and o being the counters that are checked relative to x.
    """
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
        if count == 3:
            _win(game_board, player)


def _win(game_board, player):
    """
    Win function. Called when a win condition is met.
    Generates UI to show user who has won.
    User must then press enter to continue to new game.
    """
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
    player_input = input("\n")
    while player_input != "":
        player_input = input("To play again press Enter\n")
    new_game()


def color_pick(ctr_color_list, player_names):
    """
    Funtion allowing players to select the color of their counter.
    Number list generated and zip with colors.
    Player selects a color, index of color is returned and
    added to player class upon class initiation.
    input is put through exception handeling fot Value error
    and validated against length of colors list.
    Once a color has been selected it is removed from the list
    so color clashes cannot occur.
    """
    number_list = []
    for i in range(len(ctr_color_list)):
        i += 1
        number_list.append(str(i) + ".")
    print(f"\n{player_names[-1]} choose your counter color:")
    for number, color in zip(number_list, ctr_color_list):
        print(number, color.capitalize())
    while True:
        try:
            number_col = int(input("\n"))
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
    """
    Prints a page of game instructions.
    player must only press enter to return to game menu.
    """
    print("\nConnect 4 Rules\n")
    print("OBJECTIVE:")
    print("Be the first player to connect 4 of your colored counters in a row")
    print("(either vertically, horizontally, or diagonally)")
    print("\nHOW TO PLAY:")
    print("First, decide who goes first and what color each player will have.")
    print("Players alternate turns, only one counter can be dropped per turn.")
    print("On your turn, drop one counter into any of the seven columns.")
    print("The game ends when there is a 4-in-a-row or a stalemate/draw.")
    while input("\nPress enter to go back.\n") != "":
        input("Press enter to go back.\n")
    new_game()


def title_screen():
    """
    Prints Game ASCII Title
    """
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
    print("*" + (" " * 14) + "Created by: James Dybacz" + (" " * 16) + "*")
    print("*" + (" " * 14) + "https://github.com/dybacz" + (" " * 15) + "*")
    print("*" + (" " * 19) + "Copyright\u00A9 2021" + (" " * 20) + "*")
    print("*" + ("-" * 54) + "*")


def new_game():
    """
    Starts a new game, requests game type. input is validated and put through
    exception handeling so a ValueError does not occur.
    Board class initialised with game type and size.
    Player class initialised with name, counter color and player type(player
    or computer).
    Once initialised game is started with play_game function.
    """
    title_screen()
    print("Game type:")
    print("1. 1P vs CPU\n2. 1P vs 2P\n3. How to play")
    while True:
        try:
            select_players = int(input("\n"))
            while True:
                if select_players > 3 or select_players < 1:
                    print("That number is not available for selection\n")
                    print("Please select a Game type (1 - 3)\n")
                    print("1. 1P vs AI\n2. 1P vs 2P\n3. How to play")
                    select_players = int(input("\n"))
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
            print("That is not a number\n")
            print("Please select a Game type using its number (1 - 3)\n")
            print("1. 1P vs AI\n2. 1P vs 2P\n3. How to play")

    ctr_color_list = ["green", "yellow", "blue", "magenta", "cyan"]
    pl_names = []
    if num_players == 1:
        input_one = input("Player 1 - Please enter your name: \n")
        while len(input_one) > 10:
            print("Name too long - Please try a shorter name:")
            input_one = input("\n")
        pl_names.append(input_one.capitalize())
        plr_clr = color_pick(ctr_color_list, pl_names)
        print(f"{pl_names[0]} selected {plr_clr} "+colored("\u25CF", plr_clr))
        ctr_color_list.remove(plr_clr)
        player_one = Player(pl_names[0], plr_clr, "player")
        pl_names.append("Computer")
        player_two = Player(pl_names[1], "red", "computer")
    elif num_players == 2:
        input_one = input("Player 1 - Please enter your name: \n")
        while len(input_one) > 10:
            print("Name too long - Please try a shorter name:")
            input_one = input("\n")
        pl_names.append(input_one.capitalize())
        plr_clr = color_pick(ctr_color_list, pl_names)
        print(f"{pl_names[0]} selected {plr_clr} "+colored("\u25CF", plr_clr))
        ctr_color_list.remove(plr_clr)
        player_one = Player(pl_names[0], plr_clr, "player")
        input_two = input("\nPlayer 2 - Please enter your name: \n")
        while len(input_two) > 10:
            print("Name too long - Please try a shorter name:")
            input_two = input("\n")
        pl_names.append(input_two.capitalize())
        plr_clr = color_pick(ctr_color_list, pl_names)
        print(f"{pl_names[1]} selected {plr_clr} "+colored("\u25CF", plr_clr))
        ctr_color_list.remove(plr_clr)
        player_two = Player(pl_names[1], plr_clr, "player")

    game_board = Board("Classic", [7, 6])
    play_game(game_board, player_one, player_two)


new_game()
