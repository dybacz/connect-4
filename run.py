class Player:
    """
    Player class, Creates player, sets player name, counter colour, player type
    (Real or Computer)
    """

    def __init__(self, name, counter_color, type):
        self.name = name
        self.color = counter_color
        self.type = type
        print(self.name, self.color, self.type)


def new_game():
    """
    Starts a new game, collects player name.
    """
    #num_players = input("Enter 1 for Singleplayer or 2 for Multiplayer: \n")
    num_players = 2
    print("*" + ("-" * 36) + "*")
    print("*" + (" " * 4) + "Welcome to Python CONNECT-4!" + (" " * 4) + "*")
    print("*" + (" " * 4) + "Game type: Classic" + (" " * 14) + "*")
    print("*" + (" " * 4) + "Board size: Standard" + (" " * 12) + "*")
    print("*" + (" " * 4) + "Vs: Computer" + (" " * 20) + "*")
    print("*" + ("-" * 36) + "*")

    player_names = []
    if num_players == 1:
        player_name = input("Please enter your name: \n")
        player_names.append(player_name)
        player_name = "Computer"
        player_names.append(player_name)
    elif num_players == 2:
        player_name = input("Player One - Please enter your name: \n")
        player_names.append(player_name)
        player_name = input("Player Two - Please enter your name: \n")
        player_names.append(player_name)

    player_one = Player(player_names[0], "blue", "player")
    player_two = Player(player_names[1], "red", "player")

new_game()