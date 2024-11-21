import random
from check_winner import check_winner

def medium_move(grid):
    # Check if there's a move that can block the player ("X") from winning
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                # Place "X" temporarily to see if it results in a win
                grid[row][col] = "X"
                if check_winner(grid) == "X":  # If X would win, block it
                    grid[row][col] = "O"  # Block by placing "O"
                    return
                grid[row][col] = None  # Undo the move

    # If no blocking move, make a random move
    empty_cells = [(r, c) for r in range(3) for c in range(3) if grid[r][c] is None]
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = "O"