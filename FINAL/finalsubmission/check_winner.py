def check_winner(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] is not None:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] is not None:
            return grid[0][i]
    
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None:
        return grid[0][2]
    
    for row in grid:
        if None in row:
            return None  # Continue game if there are empty cells
    
    return "Draw"  # Board is full and no winner
