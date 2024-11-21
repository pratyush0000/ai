#minimax algorithm without alpha beta pruning (not being used in code)
from check_winner import check_winner  # Import check_winner from winner.py

def minimax(grid, is_maximizing):
    winner = check_winner(grid)
    if winner == "X":
        return -10  # X is the human player, so we minimize this score
    elif winner == "O":
        return 10   # O is the AI player, so we maximize this score
    elif winner == "Draw":
        return 0   # Draw has a neutral score

    if is_maximizing:
        best_score = -float('inf')  # Initialize to the lowest possible score
        for row in range(3):
            for col in range(3):
                if grid[row][col] is None:  # Check for empty cells
                    grid[row][col] = "O"  # Simulate AI's move
                    score = minimax(grid, False)  # Recursive call for minimizing player
                    grid[row][col] = None  # Undo the move
                    best_score = max(best_score, score)  # Update the best score
        return best_score
    else:
        best_score = float('inf')  # Initialize to the highest possible score
        for row in range(3):
            for col in range(3):
                if grid[row][col] is None:  # Check for empty cells
                    grid[row][col] = "X"  # Simulate human's move
                    score = minimax(grid, True)  # Recursive call for maximizing player
                    grid[row][col] = None  # Undo the move
                    best_score = min(best_score, score)  # Update the best score
        return best_score

def hard_move(grid):
    best_score = -float('inf')  # Initialize to the lowest possible score
    best_move = None
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:  # Check for empty cells
                grid[row][col] = "O"  # Simulate AI's move
                score = minimax(grid, False)  # Call minimax without alpha-beta pruning
                grid[row][col] = None  # Undo the move
                if score > best_score:  # Update the best score and best move
                    best_score = score
                    best_move = (row, col)
    if best_move:
        grid[best_move[0]][best_move[1]] = "O"  # Make the best move for AI
