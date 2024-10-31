import pygame
import button
pygame.font.init()
from hard import ai_move  # Import ai_move from hard.py
from winner import check_winner  # Import check_winner from winner.py

WIDTH, HEIGHT = 700, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THE TIC TAC TOE")


REAL_BG = pygame.image.load("Assets/bg3.png")


#home page
TITLE_IMG = pygame.transform.scale(pygame.image.load("Assets/titleimage.png").convert_alpha(),(1500,250))
START_IMG = pygame.transform.scale(pygame.image.load("Assets/startbutton.png").convert_alpha(),(200,75))
START_BUTTON = button.Button(WIDTH//2-START_IMG.get_width()//2,HEIGHT//2-START_IMG.get_height()//4,START_IMG,1)
QUIT_IMG = pygame.transform.scale(pygame.image.load("Assets/quitbutton.png").convert_alpha(),(200,75))
QUIT_BUTTON = button.Button(WIDTH//2 - QUIT_IMG.get_width()//2 , HEIGHT//2 + QUIT_IMG.get_height() + 30 ,QUIT_IMG,1)
COPYRIGHT = pygame.transform.scale(pygame.image.load("Assets/copyrightt.png").convert_alpha(),(200,20))

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
BOARD_X = (WIDTH - BOARD_SIZE)  // 2  # X offset to center the board horizontally
BOARD_Y = (HEIGHT - BOARD_SIZE) // 2 - 50  # Y offset to center the board vertically

# Grid state and counters
grid = [[None, None, None], [None, None, None], [None, None, None]]
current_turn = "X"  # Start with "X"
x_wins = 0
o_wins = 0



def start():
    START = False  # Initialize START as False
    run = True


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(REAL_BG,(0,0))
        WIN.blit(TITLE_IMG,(WIDTH//2 - TITLE_IMG.get_width()//2 -10 , HEIGHT//4 - TITLE_IMG.get_height()//2))
        WIN.blit(COPYRIGHT,(WIDTH//2 - COPYRIGHT.get_width()//2 -10 , HEIGHT - COPYRIGHT.get_height() -10 ))

        # Check if the start button is clicked
        if START_BUTTON.draw(WIN):
            START = True  # Set START to True if the button is clicked
            break  # Exit the loop to start the game

        if QUIT_BUTTON.draw(WIN):
            pygame.time.delay(550)
            run = False
        
        pygame.display.update()

    if START:
        main()




def drawwindow():
    #WIN.fill(RED)
    WIN.blit(REAL_BG,(0,0))

    # Draw the Tic Tac Toe grid lines
    for i in range(1, 3):
        pygame.draw.rect(WIN, WHITE, (BOARD_X + i * CELL_SIZE - 5, BOARD_Y, 10, BOARD_SIZE))  # Vertical lines
        pygame.draw.rect(WIN, WHITE, (BOARD_X, BOARD_Y + i * CELL_SIZE - 5, BOARD_SIZE, 10))  # Horizontal lines

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
    WIN.blit(x_counter_text, (50, HEIGHT - 80))
    WIN.blit(o_counter_text, (WIDTH - o_counter_text.get_width() - 50, HEIGHT - 80))

    pygame.display.update()

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
                    winner = check_winner(grid)  # Pass grid as argument
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
                ai_move(grid)  # Pass grid as argument to ai_move
                winner = check_winner(grid)  # Check for a winner after AI's move
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
    start()
