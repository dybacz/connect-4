def new_game():

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
        player_names = input("Please enter your name: \n")
    elif num_players == 2:
        player_name = input("Player One - Please enter your name: \n")
        player_names.append(player_name)
        player_name = input("Player Two - Please enter your name: \n")
        player_names.append(player_name)

    print(player_names)


new_game()