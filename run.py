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
        self.board = [["." for i in range(size[0])] for j in range(size[1])]
        self._vs = _vs
        self.turns = []

    def print_table(self):
        for row in self.board:
            print(" ".join(row))


def new_game():
    """
    Starts a new game, collects player name.
    """
    # num_players = input("Enter 1 for Singleplayer or 2 for Multiplayer: \n")
    num_players = 2
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


    player_one = Player(player_names[0], "blue", "player")
    player_two = Player(player_names[1], "red", "player")

    game_board = Board("Classic", [7, 6], "Player")
    game_board.print_table()


new_game()