import random

def easy_move(grid):
    # Collect all empty cells
    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] is None]
    # Choose a random cell from the empty cells
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = "O"
