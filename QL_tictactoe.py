# QLearning Tic Tac Toe

import random
from math import *
from sys import *
from collections import defaultdict

#QL parametros


epsilon = 0.1
alpha = 0.2
gamma = 0.9
actions = 10 #acao 1,2,3,4,5,6,7,8,9
reward = -1

State=defaultdict(int)
QL = defaultdict(int)


############################################

#### QL funcoes ############################

def qlstate(board,state):
    for i in range (0,9):
        #print board
        if board[i]=='X':
            state[i]=1
        elif board[i]=='O':
            state[i]=2
        else:
            state[i]=0

    return state

    
def resetQ():
    for l1 in range(2):
        for l2 in range(2):
            for l3 in range(2):
                for l4 in range(2):
                    for l5 in range(2):
                        for l6 in range(2):
                            for l7 in range(2):
                                for l8 in range(2):
                                    for l9 in range(2):
                                        for l10 in range(1,10):
                                            QL[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10] = random.uniform(0,2)
    print "Tabela Resetada"
        
        
def getQ(state, action):
	value=QL[state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8],action]
	return	value


def chooseaction(state):	
	temp=-1000
        if (random.random() < epsilon):
            ac=int(random.uniform(1,9))
        else:
            for a in range(actions):
                vQ = QL[state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8],a]
                if vQ > temp:
                    temp=vQ
                    ac=a
    
        return ac

def chooseargmax(state):
	temp = -100
	
	for a in range(1,9):
	    vQ=QL[state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8],a]
            if vQ > temp:
                ac=a
                vQ=temp
        
        return ac


def QL_update(estado,estadoN,reward,action):
	
	best_a=chooseargmax(estadoN)
	QLNew=getQ(estadoN, best_a)
	QLold=getQ(estado, action)
	
	
	#calcula delta
	delta= ((reward) + ((gamma*QLNew) - QLold))
	
	QL[State[0],State[1],State[2],State[3],State[4],State[5],State[6],State[7],State[8],action]=QLold+(alpha*delta)



def applyaction (bd,action):
    letterX='X'
    if isSpaceFree(bd, action):
        makeMove(bd, letterX, action)
    
    
########### Gravacao de Dados ################################################

def gravaQ(Qbo):
    print "Gravando Tabela Q"
    teste = 0
    adicionar = open("Qtabela.txt","a")
    for l1 in range(2):
        for l2 in range(2):
            for l3 in range(2):
                for l4 in range(2):
                    for l5 in range(2):
                        for l6 in range(2):
                            for l7 in range(2):
                                for l8 in range(2):
                                    for l9 in range(2):
                                            s1=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,1])
                                            s2=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,2])
                                            s3=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,3])
                                            s4=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,4])
                                            s5=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,5])
                                            s6=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,6])
                                            s7=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,7])
                                            s8=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,8])
                                            s9=str(Qbo[l1,l2,l3,l4,l5,l6,l7,l8,l9,9])
                                            adicionar.write(s1)
                                            adicionar.write(s2)
                                            adicionar.write(s3)
                                            adicionar.write(s4)
                                            adicionar.write(s5)
                                            adicionar.write(s6)
                                            adicionar.write(s7)
                                            adicionar.write(s8)
                                            adicionar.write(s9)
                                            adicionar.write('\n')
    
    

        
    adicionar.close()
    
def Resultado(trial,jogada):
    arquivo = open("Resultado.txt","a")
    s1=str(trial)
    s2=str(jogada)
    arquivo.write(s1)
    arquivo.write(' ')
    arquivo.write(s2)
    arquivo.write('\n')
    arquivo.close()
    
    
################################################################################
	
	
def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
	#letter = input().upper()
	letter = 'X'
		 
    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    
    volta='y'
    #return input().lower().startswith('y')
    return volta

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        #move = input()
        move =random.randint(1, 9)
	print (move)
    #return int(move)
	return (move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True




print('Welcome to Tic Tac Toe!')

trials=0
jogadas=0
ganhou=0

resetQ()

while trials<100:  

    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        print ('Your Letter ' + playerLetter + '')
        gameIsPlaying = True
    
        while gameIsPlaying:
            if turn == 'player':
                # Player's turn.
                #drawBoard(theBoard)
                #move = getPlayerMove(theBoard)
                #makeMove(theBoard, playerLetter, move)
                                                    
                #gravaQ(QL)
    			######## QL ###########
    			# 1-Determinar o estado
    			# 2 - escolher acao
    			# 3 - aplicar acao
    			# 4 - receber retorno
    			# Calcular QL
                
                vstateinicial=qlstate(theBoard,State)
                #print EstadoInicial
                
                while True:                                 #so deixa escolher acao que possa realizar
                    acao=chooseaction(vstateinicial)
                    if isSpaceFree(theBoard, acao):
                        break
                
                applyaction(theBoard,acao)
                    
                vstatefinal=qlstate(theBoard,State)
                #print    vstateinicial
                #print    vstatefinal
    
                if isWinner(theBoard, playerLetter):
                    ganhou=ganhou+1
                    reward=100 #ganhou ganha 100
                    QL_update(vstateinicial,vstatefinal,reward,acao)
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        reward=0 #so conta se ganhar
                        QL_update(vstateinicial,vstatefinal,reward,acao)
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        gameIsPlaying = False
                        #break
                    else:
                        turn = 'computer'
    
            else:
                # Computer's turn.
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
    
                if isWinner(theBoard, computerLetter):
                    #drawBoard(theBoard)
                    reward=-100 #perdeu perde 100
                    QL_update(vstateinicial,vstatefinal,reward,acao)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        reward=0 #empatar nao conta
                        QL_update(vstateinicial,vstatefinal,reward,acao)
                        #drawBoard(theBoard)
                        print('The game is a tie!')
                        gameIsPlaying = False
                    else:
                        turn = 'player'

        s = 'Jogo atual ' + str(jogadas)
        print s
        
        if not playAgain():
            break
        if jogadas>1000:                       # vai jogar o jogo 10000 vezes (pode mudar)
            
            Resultado(trials,ganhou)            #salva tabela jogos/vezes ganhou
            ganhou=0                            #zera a soma dos ganhos
            jogadas=0                           # zera o numero de jogadas
            trials=trials+1                     #proximo jogo
            break
        else:
            jogadas=jogadas+1
            