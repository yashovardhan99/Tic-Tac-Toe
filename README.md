# Tic-Tac-Toe
A simple native Python based tic tac toe game with a very basic AI.
Completely written in Python with only tkinter used for GUI.
Also helps test different AI's of tic tac toe via an in-built simulator.
## Play the game
### Play in GUI
The GUI is very limited right now. It makes you go first and gives you only a 'X' right now. To play using GUI, make sure python is installed. Download the files [ticTacToe.py](ticTacToe.py) and [ticTacToeGUI.py](ticTacToeGUI.py). Then run [ticTacToeGUI.py](ticTacToeGUI.py) using any command line tool such as command prompt (Windows).
Specifically, in Windows, open cmd in the directory where these files are located and run the command ``Python ticTacToeGUI.py``
### Play in command line
To play the game in any command line tool such as cmd or terminal, make sure python is installed. Download the files [ticTacToe.py](ticTacToe.py) and [ticTacToeStart](ticTacToeStart.py). Then run [ticTacToeStart.py](ticTacToeStart.py) using any command line tool.
## Simulation
Multiple alternative AIs have been created in [ticTacToeCenterFirstAI](ticTacToeCenterFirstAI.py) and other similar files. To test it, download [the original file](ticTacToe.py), [the alternative AI file](ticTacToeCenterFirstAI.py) and [the simulator script](ticTacToeSimulator.py) and then run ticTacToeSimulator.py. You can also make necessary changes in the simulator such as changing which AI goes first or the number of games to be played. Comments have been added at relevant sections to guide you.
## Writing your own AI
To use your own AI with this simulator, you can write your own AI which makes a move based on the given parameters as in [the sample AI function](ticTacToeCenterFirstAI.py) or even the necessary function in [the original game](ticTacToe.py). Then make necessary changes in [the simulator script](ticTacToeSimulator.py) to run it against the defined AI or against your very own AI.
