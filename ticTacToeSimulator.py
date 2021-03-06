'''Used to simulate matches in ticTacToe, change parameters in caps below as per comments and make sure you import the correct alternative AI'''
from ticTacToe import getAIMove,makeAIMove,isWinner,drawBoard
import ticTacToeAlternativeAI as altAI
import ticTacToeCenterFirstAI as alt2AI
import ticTacToeMinimaxAI as alt3AI
import time
START_TIME = time.time() #Calculate start time
NO_OF_GAMES = 10 #Change as per requirement
ORIGINAL_AI,ALT_AI,DRAW=0,0,0 #DO NOT MODIFY THIS LINE
START = 1  #Use 0 for original AI and 1 for altAI. This defines which makes the first move. Currently, can't set it to random
LETTERS = ['X','O'] #X for original and O for altAI. It doesn't matter though because the board is rarely displayed in this game. I recommend not changing this line
#DO NOT MODIFY ANYTHING BELOW unless you know what you are doing
for i in range(NO_OF_GAMES):
    gameBoard = [' ']*10
    for i in range(1,10):
        gameBoard[i]=str(i)
    gameInProgress = True
    moves=0
    current = START
    while True:
        #drawBoard(gameBoard) #comment out when testing with large nos.
        if moves>=9:
            DRAW = DRAW+1
            break
        if current==0:
            #print('Move by original AI') # comment out when testing with large nos.
            move = getAIMove(gameBoard,LETTERS[0])
            gameBoard[move]=LETTERS[0]
            moves = moves+1
            current=1
            if moves>=5 and isWinner(gameBoard,LETTERS[0]):
                ORIGINAL_AI=ORIGINAL_AI+1
                break
        else:
            AImove = alt3AI.getAIMove(gameBoard,LETTERS[1])# change altAI to alternative AI as imported
            gameBoard[AImove]=LETTERS[1]
            moves = moves+1
            current=0
            if moves>=5 and isWinner(gameBoard,LETTERS[1]):
                ALT_AI=ALT_AI+1
                break
END_TIME = time.time() #End time
#DO NOT MODIFY ANYTHING ABOVE. You can modify the below code to format the output according to your needs
print('ORIGINAL AI = '+str(ORIGINAL_AI))
print('ALTERNATIVE AI = '+str(ALT_AI))
print('DRAWS = '+str(DRAW))
print('TOTAL TIME TAKEN = '+str(END_TIME-START_TIME)+' SECONDS')