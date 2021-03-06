# Two player Tic-Tac-Toe game

''' Form the Tic-Tac-Toe board using a dictionary. Each key is a number
    corresponding to its location. Each value is initially an empty space
    that will be filled with X or O as the game is played. '''

gameBoard = {"7": " ", "8": " ", "9": " ",
             "4": " ", "5": " ", "6": " ",
             "1": " ", "2": " ", "3": " "}

board_keys = []

for key in gameBoard:
    board_keys.append(key)


# The printBoard function prints the updated board after every turn in the game.
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# The game function contains the Tic-Tac-Toe gameplay rules.
def game():
    player = 'X'
    count = 0  # number of valid moves

    # Print the board and prompt the user for an input.
    for i in range(10):
        printBoard(gameBoard)
        mark = input("Player " + player + " pick a spot: ")

        # The player marks the chosen spot on the board, if that spot is empty.
        if gameBoard[mark] == ' ':
            gameBoard[mark] = player
            count += 1
        else:
            print("Spot is already filled.")
            continue

        # Check the board for 3 in a row from player X or O.
        if count >= 3:
            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':  # top horizontal
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':  # middle horizontal
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break
            elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':  # bottom horizontal
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break
            elif gameBoard['7'] == gameBoard['4'] == gameBoard['1'] != ' ':  # left vertical
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break
            elif gameBoard['8'] == gameBoard['5'] == gameBoard['2'] != ' ':  # middle vertical
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break
            elif gameBoard['9'] == gameBoard['6'] == gameBoard['3'] != ' ':  # right vertical
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break
            elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ':  # diagonal
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break
            elif gameBoard['9'] == gameBoard['5'] == gameBoard['1'] != ' ':  # diagonal
                printBoard(gameBoard)
                print("\nGame Over\n" + player + " WON!")
                break

        # If the board has been filled up and there are no 3 in a row. The game ends with a tie.
        if count == 9:
            printBoard(gameBoard)
            print("\nGame Over\nGAME IS TIED!")
            break

        # Alternate between players after every turn.
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    # Prompt user to restart game.
    restart = input("Play Again?(y/n): ")
    if restart.lower() == "y":
        # reset the board with empty spaces
        for key in board_keys:
            gameBoard[key] = " "
        game()

# Defines special variables for running program.
if __name__ == "__main__":
    game()