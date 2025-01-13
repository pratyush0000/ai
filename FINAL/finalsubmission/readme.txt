Tic Tac Toe Game

Description:
This is a Python-based Tic Tac Toe game with three difficulty levels for AI: Easy, Medium, and Hard. It uses the pygame library for graphical rendering and interactive buttons.

How to Run the Game:

1. Install Python:
   - Download and install Python (version 3.10 or higher) from https://www.python.org/downloads/.
   - During installation, check the box "Add Python to PATH" to ensure it can be used from the terminal/command prompt.

2. Install the Required Library:
   - Open a terminal or command prompt.
   - Navigate to the folder where this project is located.
   - Install the pygame library by running the command:
     pip install pygame

3. Project Structure:
   Make sure your project folder contains the following files and folders:

   TicTacToe/
   ├── Assets/                  # Contains images for buttons and background
   │   ├── bg3.png
   │   ├── titleimage.png
   │   ├── startbutton.png
   │   ├── quitbutton.png
   │   ├── copyrightt.png
   │   ├── easybutton.png
   │   ├── mediumbutton.png
   │   ├── hardbutton.png
   │   ├── menubutton.png
   ├── button.py                # Button class for interactive UI
   ├── check_winner.py          # Logic for checking the winner
   ├── easy_mode.py             # AI logic for Easy difficulty
   ├── medium_mode.py           # AI logic for Medium difficulty
   ├── hard_mode_alpha_beta.py  # AI logic for Hard difficulty (Minimax with Alpha-Beta pruning)
   ├── main.py                  # Main file to run the game
   └── README.txt               # This file

   Note: Ensure all image files are in the Assets folder and named exactly as shown above.

4. Run the Game:
   - Open a terminal or command prompt.
   - Navigate to the folder containing main.py.
   - Run the following command:
     python main.py

Gameplay Instructions:

1. Start the Game:
   - Launch the game, and click the Start button on the home screen.

2. Select Difficulty:
   - Choose between Easy, Medium, or Hard difficulty for the AI.

3. Gameplay:
   - The game alternates turns between the player (X) and AI (O).
   - Click on a cell to place your mark (X). The AI will automatically make its move (O).

4. Check Results:
   - The game announces the winner or a draw once the game ends.

5. Return to Menu:
   - Click the Menu button on the game screen to return to the home screen.

Troubleshooting:
- If the game doesn’t start:
  1. Ensure Python is installed correctly.
  2. Ensure the pygame library is installed using pip install pygame.
  3. Verify the project structure matches the layout provided above.

- If buttons or graphics don’t display:
  - Confirm that the images are in the correct Assets folder with the correct file names.

Credits:
- Best group of CSD311.
- Python and pygame.
