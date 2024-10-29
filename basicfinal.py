import pygame
pygame.font.init()

WIDTH, HEIGHT = 700, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THE TIC TAC TOE")

# fps
FPS = 60
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# board dimensions
BOARD_SIZE = 600  # 600x600 board, with 200x200 cells
CELL_SIZE = BOARD_SIZE // 3

# Fonts
FONT = pygame.font.Font(None, 100)
COUNTER_FONT = pygame.font.Font(None, 50)
BOARD_X = (WIDTH - BOARD_SIZE) // 2  # X offset to center the board horizontally
BOARD_Y = (HEIGHT - BOARD_SIZE) // 2 - 50  # Y offset to center the board vertically

# Grid state and counters
grid = [[None, None, None], [None, None, None], [None, None, None]]
current_turn = "X"  # Start with "X"
x_wins = 0
o_wins = 0

def drawwindow():
    WIN.fill(RED)
    
    # Draw the Tic Tac Toe grid lines
    for i in range(1, 3):
        pygame.draw.rect(WIN, BLACK, (BOARD_X + i * CELL_SIZE, BOARD_Y, 5, BOARD_SIZE))  # Vertical lines
        pygame.draw.rect(WIN, BLACK, (BOARD_X, BOARD_Y + i * CELL_SIZE, BOARD_SIZE, 5))  # Horizontal lines

    # Draw X and O based on the grid state
    for row in range(3):
        for col in range(3):
            if grid[row][col] is not None:
                text = FONT.render(grid[row][col], True, WHITE)
                x_pos = BOARD_X + col * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2
                y_pos = BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2
                WIN.blit(text, (x_pos, y_pos))
    
    x_counter_text = COUNTER_FONT.render(f"X Wins: {x_wins}", True, WHITE)
    o_counter_text = COUNTER_FONT.render(f"O Wins: {o_wins}", True, WHITE)
    WIN.blit(x_counter_text, (10, HEIGHT - 80))
    WIN.blit(o_counter_text, (WIDTH - o_counter_text.get_width() - 10, HEIGHT - 80))

    pygame.display.update()

def check_winner():
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

def minimax(is_maximizing, alpha, beta):
    winner = check_winner()
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
                    score = minimax(False, alpha, beta)
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
                    score = minimax(True, alpha, beta)
                    grid[row][col] = None
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def ai_move():
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                grid[row][col] = "O"
                score = minimax(False, -float('inf'), float('inf'))
                grid[row][col] = None
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        grid[best_move[0]][best_move[1]] = "O"

def handle_click(pos):
    global current_turn, x_wins, o_wins

    x, y = pos
    # Adjust the click position to the centered board
    row = (y - BOARD_Y) // CELL_SIZE
    col = (x - BOARD_X) // CELL_SIZE

    if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] is None:
        grid[row][col] = current_turn
        return True  # Return true if the move is successful
    return False


def reset_board():
    global grid, current_turn
    grid = [[None, None, None], [None, None, None], [None, None, None]]
    current_turn = "X"

def main():
    global current_turn, x_wins, o_wins  # Declare x_wins and o_wins as global
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        drawwindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and current_turn == "X":
                if handle_click(pygame.mouse.get_pos()):
                    winner = check_winner()
                    drawwindow()
                    pygame.time.delay(1000)  # Delay for 1 second before AI move
                    
                    if winner:  # Check if there's a winner after the player's move
                        if winner == "X":
                            x_wins += 1
                        elif winner == "O":
                            o_wins += 1
                        drawwindow()
                        pygame.time.delay(3000)  # Show the winning board
                        reset_board()
                    else:
                        current_turn = "O"  # Switch to AI's turn

            if current_turn == "O":
                ai_move()  # AI makes its move
                winner = check_winner()  # Check for a winner after AI's move
                drawwindow()  # Show the updated board after AI's move
                
                if winner:
                    if winner == "X":
                        x_wins += 1
                    elif winner == "O":
                        o_wins += 1
                    drawwindow()
                    pygame.time.delay(3000)  # Show the winning board
                    reset_board()
                else:
                    current_turn = "X"  # Switch back to player turn after AI move
    pygame.quit()

if __name__ == "__main__":
    main()
