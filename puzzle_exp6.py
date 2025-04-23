from collections import deque

N = 3  # 3x3 Puzzle

# Puzzle state class
class PuzzleState:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth

# Goal check
def is_goal(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal

# Check valid move
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

# Print the board
def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print("----------")

# BFS to solve puzzle
def solve_bfs(start, x, y):
    q = deque()
    visited = set()

    q.append(PuzzleState(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while q:
        curr = q.popleft()

        print(f"Depth: {curr.depth}")
        print_board(curr.board)

        if is_goal(curr.board):
            print(f"Goal found at depth {curr.depth}")
            return

        for dx, dy in moves:
            new_x, new_y = curr.x + dx, curr.y + dy
            if is_valid(new_x, new_y):
                # Copy board and swap values
                new_board = [row[:] for row in curr.board]
                new_board[curr.x][curr.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[curr.x][curr.y]

                if tuple(map(tuple, new_board)) not in visited:
                    visited.add(tuple(map(tuple, new_board)))
                    q.append(PuzzleState(new_board, new_x, new_y, curr.depth + 1))

    print("No solution found.")

# Main function
if __name__ == "__main__":
    start = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
    x, y = 2, 1  # Position of 0
    print("Initial State:")
    print_board(start)
    solve_bfs(start, x, y)
