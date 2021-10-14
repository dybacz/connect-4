from termcolor import colored, cprint
from random import randint


class Player:
    """
    Player class, Creates player, sets player name, counter colour, player type
    (Real or Computer)
    """

    def __init__(self, name, counter_color, type):
        self.name = name
        self.color = counter_color
        self.type = type


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

    # make_turn(game_board, player_one)
    first_turn(game_board, player_one, player_two)


def first_turn(game_board, player_one, player_two):
    print("To see who plays first we must flip a coin")
    rand_int = randint(1, 2)
    player_turn_input = input("Player 1, Input 1 for head and 2 for tails: \n")
    if rand_int == 1:
        print("The coin is heads")
    else:
        print("The coin is tails")

    if int(player_turn_input) == rand_int:
        print("Player 1 you will go first")
        make_turn(game_board, player_one)
    else:
        print("Player 2 you will go first")
        make_turn(game_board, player_two)


def player_turn(game_board, player):
    player_input = input("Input a column to drop your counter:")

    _ctr = colored("\u25CF", player.color)

    while game_board.board[0][int(player_input)-1] == _ctr:
        player_input = input(f"Column {player_input} is full, try again: \n")
    else:
        for i in range(game_board.size[1]):
            if game_board.board[-1-i][int(player_input)-1] == "\u25CB":
                game_board.board[-1-i][int(player_input)-1] = _ctr
                break
            elif game_board.board[-1-i][int(player_input)-1] == _ctr:
                continue
            

def computer_turn(game_board, player):
    computer_input = randint(1, 7)

    _ctr = colored("\u25CF", player.color)

    while game_board.board[0][int(computer_input)-1] == _ctr:
        player_input = input(f"Column {computer_input} is full, try again: \n")
    else:
        for i in range(game_board.size[1]):
            if game_board.board[-1-i][int(computer_input)-1] == "\u25CB":
                game_board.board[-1-i][int(computer_input)-1] = _ctr
                break
            elif game_board.board[-1-i][int(computer_input)-1] == _ctr:
                continue


def make_turn(game_board, player):
    game_board.print_table()
    
    if player.type == "player":
        player_turn(game_board, player)
    elif player.type == "computer":
        computer_turn(game_board, player)

    make_turn(game_board, player)


def new_game():
    """
    Starts a new game, collects player name.
    """
    # num_players = input("Enter 1 for Singleplayer or 2 for Multiplayer: \n")
    num_players = 1
    print("*" + ("-" * 36) + "*")
    print("*" + (" " * 4) + "Welcome to Python CONNECT-4!" + (" " * 4) + "*")
    print("*" + (" " * 4) + "Game type: Classic" + (" " * 14) + "*")
    print("*" + (" " * 4) + "Board size: Standard" + (" " * 12) + "*")
    print("*" + (" " * 4) + "Vs: Computer" + (" " * 20) + "*")
    print("*" + ("-" * 36) + "*")

    player_names = []
    if num_players == 1:
        player_names.append(input("Please enter your name: \n"))
        player_names.append("Computer")
    elif num_players == 2:
        player_names.append(input("Player One - Please enter your name: \n"))
        player_names.append(input("Player Two - Please enter your name: \n"))

    player_one = Player(player_names[0], "red", "computer")
    player_two = Player(player_names[1], "blue", "player")

    game_board = Board("Classic", [7, 6], "Player")
    play_game(game_board, player_one, player_two)


new_game()
