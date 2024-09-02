#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    # Check if all spots are filled
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get valid input
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == " ":
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        # Update the board with the player's move
        board[row][col] = player

        # Check if the current player has won
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check if the game is a draw
        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

tic_tac_toe()
