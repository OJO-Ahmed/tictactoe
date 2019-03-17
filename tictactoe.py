theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
    }
def printBoard(board):
    print('     ' + board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('     '+ '-+-+-')
    print('     ' + board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('     ' + '-+-+-')
    print('     ' + board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# printBoard(theBoard)

"""
def winner(turn):
    if theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn:
        print(turn + 'is the winner')
        #break
        return
    if theBoard['mid-L'] == turn and theBoard['mid-M'] == turn and theBoard['mid-R'] == turn:
        print(turn + 'is the winner')
        #break
        return
    if theBoard['low-L'] == turn and theBoard['low-M'] == turn and theBoard['low-R'] == turn:
        print(turn + 'is the winner')
        #break
        return
"""

turn = 'X'
for i in range(9):
    #winner(turn)
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    while move not in ('top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R'):
        print('please, pass in the right parameter\n')
        print('Turn for ' + turn + '. Move on which space?')
        move = input()

    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    #Winning conditions

    if theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn:
        print(turn + ' is the winner')
        break;
    if theBoard['mid-L'] == turn and theBoard['mid-M'] == turn and theBoard['mid-R'] == turn:
        print(turn + ' is the winner')
        break;
    if theBoard['low-L'] == turn and theBoard['low-M'] == turn and theBoard['low-R'] == turn:
        print(turn + ' is the winner')
        break;
    
    if theBoard['top-L'] == turn and theBoard['mid-L'] == turn and theBoard['low-L'] == turn:
        print(turn + ' is the winner')
        break;
    if theBoard['top-M'] == turn and theBoard['mid-M'] == turn and theBoard['low-M'] == turn:
        print(turn + ' is the winner')
        break;
    if theBoard['top-R'] == turn and theBoard['mid-R'] == turn and theBoard['low-R'] == turn:
        print(turn + ' is the winner')
        break;
    
    if theBoard['top-R'] == turn and theBoard['mid-M'] == turn and theBoard['low-L'] == turn:
        print(turn + ' is the winner')
        break;
    
    if theBoard['top-L'] == turn and theBoard['mid-R'] == turn and theBoard['low-R'] == turn:
        print(turn + ' is the winner')
        break;
    
printBoard(theBoard)
