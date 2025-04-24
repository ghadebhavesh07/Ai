import math

# Constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if there's a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

# Function to check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax function for decision making
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return -1
    elif winner == PLAYER_O:
        return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Find the best move for AI
def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main game loop
if __name__ == "__main__":
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    print("Initial Board:")
    print_board(board)

    while True:
        # Player X's turn
        x_row, x_col = map(int, input("Player X, enter your move (row and column): ").split())
        if board[x_row][x_col] == EMPTY:
            board[x_row][x_col] = PLAYER_X
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)
        if check_winner(board):
            print("Player X wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # Player O's turn (AI)
        print("Player O is making a move...")
        o_move = find_best_move(board)
        if o_move != (-1, -1):
            board[o_move[0]][o_move[1]] = PLAYER_O

        print_board(board)
        if check_winner(board):
            print("Player O wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
