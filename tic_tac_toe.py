#creating a tic tac toe program that two users 
#can play on one computer by inputting numbers in
#a grid-like system that will print everytime an input is given

#to clear the screen between moves:
#from IPython.display import clear_output
#clear_output() **jupyter notebook only
#other IDEs: print('\n'*100)

from IPython.display import clear_output
from random import randint
#making the board as separated by '|' and displaying
#the O's or X's from a list 
def display_board(board):
    print('    |  |  ')
    print(board[7]+'   |'+board[8]+' |'+board[9])
    print('    |  |  ')
    print('-------------')
    print('    |  |  ')
    print(board[4]+'   |'+board[5]+' |'+board[6])
    print('    |  |  ')
    print('-------------')
    print('    |  |  ')
    print(board[1]+'   |'+board[2]+' |'+board[3])
    print('    |  |  ')

test_board = [' ']*10
display_board(test_board)
# def player_mark():
#     marker = ''
#     while not (marker == 'X' or marker == 'O'):
#         marker = input('Player 1: Do you want to be X or O? ').upper()
    
#     if marker == 'X':
#         return ('X', 'O')

#     else:
#         return ('O', 'X')

# def place_marker(board, marker, position):
#     board[position] = marker 

# def win_check(board, mark):
#     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
#     (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
#     (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
#     (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left
#     (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
#     (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
#     (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
#     (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal



# def who_goes_first():
#     if randint(0, 1) == 0:
#         return 'Player 1'
#     else:
#         return 'Player 2'

# def space_check(board, position):
#     return board[position] == ' '

# def full_board_check(board):
#     for i in range (1,10):
#         if space_check(board, i):
#             return False
#     return True 

# def player_choice(board):
#     position = 0 

#     while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
#         position = int(input('Choose your next position: (1-9) '))

#     return position 

# def replay():
#     return input('Do you want to play again? Enter Yes or No ').lower().startswith('y')

# print('Welcome to Tic Tac Toe!')

# while True:
#     theBoard = [' ']*10
#     player1_marker, player2_marker = player_mark()
#     turn = who_goes_first()
#     print(turn + ' will go first.')

#     play_game = input('Are you ready to play? Enter Yes or No. ')

#     if play_game.lower()[0]== 'y':
#         game_on = True
#     else:
#         game_on = False
    
#     while game_on:
#         if turn == 'Player 1':

#             display_board(theBoard)
#             position = player_choice(theBoard)
#             place_marker(theBoard, player1_marker, position)

#             if win_check(theBoard, player1_marker):
#                 display_board(theBoard)
#                 print('Congratulations! You have won the game!')
#                 game_on = False
#             else: 
#                 if full_board_check(theBoard):
#                     display_board(theBoard)
#                     print('This game is a draw!')
#                     break 
#                 else: 
#                     turn = 'Player 2'

#         else:
#             display_board(theBoard)
#             position = player_choice(theBoard)
#             place_marker(theBoard, player2_marker, position)

#             if win_check(theBoard, player2_marker):
#                 display_board(theBoard)
#                 print('Congratulations! Player 2 has won the game!')
#                 game_on = False
#             else: 
#                 if full_board_check(theBoard):
#                     display_board(theBoard)
#                     print('This game is a draw!')
#                     break 
                
#                 else:
#                     turn = 'Player 1'
#     if not replay():
#         break