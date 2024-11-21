import pygame
import button
pygame.font.init()
from hard_mode_alpha_beta import hard_move  
from easy_mode import easy_move
from medium_mode import medium_move
from check_winner import check_winner 

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

#levelselect
EASY_IMG = pygame.transform.scale(pygame.image.load("Assets/easybutton.png").convert_alpha(),(300,112))
EASY_BUTTON = button.Button(WIDTH//2-EASY_IMG.get_width()//2, 150-EASY_IMG.get_height()//4,EASY_IMG,1)
MEDIUM_IMG = pygame.transform.scale(pygame.image.load("Assets/mediumbutton.png").convert_alpha(),(300,112))
MEDIUM_BUTTON = button.Button(WIDTH//2-MEDIUM_IMG.get_width()//2, 350-MEDIUM_IMG.get_height()//4,MEDIUM_IMG,1)
HARD_IMG = pygame.transform.scale(pygame.image.load("Assets/hardbutton.png").convert_alpha(),(300,112))
HARD_BUTTON = button.Button(WIDTH//2-HARD_IMG.get_width()//2, 550-HARD_IMG.get_height()//4,HARD_IMG,1)

#gamepage
MENU_IMG = pygame.transform.scale(pygame.image.load("Assets/menubutton.png").convert_alpha(),(150,56))
MENU_BUTTON = button.Button(WIDTH//2-MENU_IMG.get_width()//2, HEIGHT - MENU_IMG.get_height() - 35 ,MENU_IMG,1)


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
    START = False
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit gracefully if the user exits the window
                return  # Ensure it exits the loop immediately

        WIN.blit(REAL_BG, (0, 0))
        WIN.blit(TITLE_IMG, (WIDTH // 2 - TITLE_IMG.get_width() // 2 - 10, HEIGHT // 4 - TITLE_IMG.get_height() // 2))
        WIN.blit(COPYRIGHT, (WIDTH // 2 - COPYRIGHT.get_width() // 2 - 10, HEIGHT - COPYRIGHT.get_height() - 10))

        if START_BUTTON.draw(WIN):
            pygame.time.delay(300)
            START = True
            break  # Proceed to level select

        if QUIT_BUTTON.draw(WIN):
            pygame.time.delay(550)
            pygame.quit()  # Quit Pygame
            return  # Exit function immediately to avoid further screen updates

        pygame.display.update()

    if START:
        levelselect()

def levelselect():
    run = True
    difficulty_selected = None

    while run and not difficulty_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the function

        WIN.blit(REAL_BG, (0, 0))

        if EASY_BUTTON.draw(WIN):
            difficulty_selected = "easy"
        elif MEDIUM_BUTTON.draw(WIN):
            difficulty_selected = "medium"
        elif HARD_BUTTON.draw(WIN):
            difficulty_selected = "hard"

        pygame.display.update()

    if difficulty_selected:
        main(difficulty_selected)

def drawwindow():
    WIN.blit(REAL_BG, (0, 0))

    # Draw the Tic Tac Toe grid lines
    for i in range(1, 3):
        pygame.draw.rect(WIN, WHITE, (BOARD_X + i * CELL_SIZE - 5, BOARD_Y, 10, BOARD_SIZE))
        pygame.draw.rect(WIN, WHITE, (BOARD_X, BOARD_Y + i * CELL_SIZE - 5, BOARD_SIZE, 10))

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

    if MENU_BUTTON.draw(WIN):
        pygame.time.delay(550)
        reset_board()
        start()  # Re-enter the start screen after resetting the board

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

def main(difficulty):
    global current_turn, x_wins, o_wins
    print(f"Game started with difficulty: {difficulty}")

    # Map difficulty to the respective AI move function
    ai_move_function = {
        "easy": easy_move,
        "medium": medium_move,
        "hard": hard_move
    }[difficulty]
    
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
                    winner = check_winner(grid)
                    drawwindow()
                    pygame.time.delay(1000)

                    if winner:
                        if winner == "X":
                            x_wins += 1
                        elif winner == "O":
                            o_wins += 1
                        drawwindow()
                        pygame.time.delay(3000)
                        reset_board()
                    else:
                        current_turn = "O"  

            if current_turn == "O":
                ai_move_function(grid)  # Calls the correct AI move function
                winner = check_winner(grid)
                drawwindow()
                
                if winner:
                    if winner == "X":
                        x_wins += 1
                    elif winner == "O":
                        o_wins += 1
                    drawwindow()
                    pygame.time.delay(3000)
                    reset_board()
                else:
                    current_turn = "X"
    pygame.quit()

if __name__ == "__main__":
    start()
