from winner import check_winner  # Import check_winner from winner.py

def minimax(grid, is_maximizing, alpha, beta):
    winner = check_winner(grid)
    if winner == "X":
        return -1  # X is the human player, so we minimize this score
    elif winner == "O":
        return 1   # O is the AI player, so we maximize this score
    elif winner == "Draw":
        return 0   # Draw has a neutral score

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] is None:
                    grid[row][col] = "O"
                    score = minimax(grid, False, alpha, beta)
                    grid[row][col] = None
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] is None:
                    grid[row][col] = "X"
                    score = minimax(grid, True, alpha, beta)
                    grid[row][col] = None
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def ai_move(grid):
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                grid[row][col] = "O"
                score = minimax(grid, False, -float('inf'), float('inf'))
                grid[row][col] = None
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        grid[best_move[0]][best_move[1]] = "O"
    