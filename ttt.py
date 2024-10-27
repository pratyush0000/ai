import pygame
import os
pygame.font.init()
pygame.mixer.init()

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

# Grid state
grid = [[None, None, None], [None, None, None], [None, None, None]]
current_turn = "X"  # Start with "X"

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

    pygame.display.update()

def handle_click(pos):
    global current_turn
    x, y = pos
    row, col = y // CELL_SIZE, x // CELL_SIZE
    
    # Check if the cell is empty before placing X or O
    if row < 3 and col < 3 and grid[row][col] is None:
        grid[row][col] = current_turn
        # Toggle between X and O
        current_turn = "O" if current_turn == "X" else "X"

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())
                
        drawwindow()

    pygame.quit()

if __name__ == "__main__":
    main()
