import pygame
pygame.font.init()

WIDTH, HEIGHT = 600, 800
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

# Grid state and counters
grid = [[None, None, None], [None, None, None], [None, None, None]]
current_turn = "X"  # Start with "X"
x_wins = 0
o_wins = 0

def drawwindow():
    WIN.fill(RED)
    
    # Draw the Tic Tac Toe grid lines
    for i in range(1, 3):
        pygame.draw.rect(WIN, BLACK, (i * CELL_SIZE, 0, 5, BOARD_SIZE))  # Vertical lines
        pygame.draw.rect(WIN, BLACK, (0, i * CELL_SIZE, BOARD_SIZE, 5))  # Horizontal lines

    # Draw X and O based on the grid state
    for row in range(3):
        for col in range(3):
            if grid[row][col] is not None:
                text = FONT.render(grid[row][col], True, WHITE)
                x_pos = col * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2
                y_pos = row * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2
                WIN.blit(text, (x_pos, y_pos))
    
    # Draw the win counter at the bottom
    x_counter_text = COUNTER_FONT.render(f"X Wins: {x_wins}", True, WHITE)
    o_counter_text = COUNTER_FONT.render(f"O Wins: {o_wins}", True, WHITE)
    WIN.blit(x_counter_text, (10, BOARD_SIZE + 20))
    WIN.blit(o_counter_text, (WIDTH - o_counter_text.get_width() - 10, BOARD_SIZE + 20))

    pygame.display.update()

def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows and columns
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] is not None:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] is not None:
            return grid[0][i]
    
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None:
        return grid[0][2]
    
    # Check if the board is full (draw)
    for row in grid:
        if None in row:
            return None  # Continue game if there are empty cells
    
    return "Draw"  # Board is full and no winner

def handle_click(pos):
    global current_turn, x_wins, o_wins, grid

    x, y = pos
    row, col = y // CELL_SIZE, x // CELL_SIZE
    
    # Check if the cell is empty before placing X or O
    if row < 3 and col < 3 and grid[row][col] is None:
        grid[row][col] = current_turn
        winner = check_winner()
        
        if winner:
            if winner == "X":
                x_wins += 1
            elif winner == "O":
                o_wins += 1
            return True  # Indicate a win happened
        else:
            # Toggle between X and O if there’s no winner yet
            current_turn = "O" if current_turn == "X" else "X"
    
    return False  # No win

def reset_board():
    global grid, current_turn
    grid = [[None, None, None], [None, None, None], [None, None, None]]
    current_turn = "X"  # Reset to X as the starting turn

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        drawwindow()  # Always update the display each frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if handle_click(pygame.mouse.get_pos()):
                    drawwindow()  # Update display to show the win before delay
                    pygame.time.delay(3000)  # Delay for 3 seconds after a win
                    reset_board()  # Reset the board after displaying the win

    pygame.quit()

if __name__ == "__main__":
    main()
