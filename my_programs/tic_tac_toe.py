import random

def display_board(board):
    print("""
        |     |   
     {6}  |  {7}  |  {8}  
        |     |   
    ---------------
        |     |   
     {3}  |  {4}  |  {5}  
        |     |   
    ---------------
        |     |   
     {0}  |  {1}  |  {2}  
        |     |   
    """.format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]))

def assign_markers():
    user_input = ''
    while user_input not in ('x','o'):
        user_input = input("Player 1, please choose your marker (X or O): ").lower()
    return ('x','o') if user_input == 'x' else ('o','x')               # return Class: tuple

def turn_func():
    return_var = random.randint(1,2)
    print('Player {0} has the first turn.'.format(int(return_var)))
    return return_var                                   # return Class: int

def game_on_func():
    user_input = ''
    while user_input not in ('y','n'):
        user_input = input('Are you ready to play the game? (Y/N): ').lower()
    return True if user_input == 'y' else False         # return Class: boolean

def assign_position(turn_arg, marker_arg, board_arg):
    user_input = ''
    while True:
        if user_input not in ('1','2','3','4','5','6','7','8','9'):
            user_input = input('Player {}, please choose a position (1-9): '.format(str(turn_arg)))
        elif board_arg[int(user_input)] != ' ':
            user_input = input('Player {}, please choose a position (1-9): '.format(str(turn_arg)))
        else:
            board_arg[int(user_input)] = marker_arg.upper()
            break

def win_check(marker_arg, board_arg):
    if (board_arg[1] == board_arg[2] == board_arg[3] == marker_arg.upper() or
        board_arg[4] == board_arg[5] == board_arg[6] == marker_arg.upper() or
        board_arg[7] == board_arg[8] == board_arg[9] == marker_arg.upper() or
        board_arg[1] == board_arg[4] == board_arg[7] == marker_arg.upper() or
        board_arg[2] == board_arg[5] == board_arg[8] == marker_arg.upper() or
        board_arg[3] == board_arg[6] == board_arg[9] == marker_arg.upper() or
        board_arg[1] == board_arg[5] == board_arg[9] == marker_arg.upper() or
        board_arg[3] == board_arg[5] == board_arg[7] == marker_arg.upper()):
        return True             # return Class: boolean
    else:
        return False            # return Class: boolean

def board_full_check(board_arg):
    return not ' ' in board_arg[1:]         # return Class: boolean

def game_replay():
    user_input = ''
    while user_input not in ('y','n'):
        user_input = input('Do you want to play again? (Y/N): ').lower()
    return True if user_input == 'y' else False         # return Class: boolean

# WHILE TRUE - GAME LOOP
while True:

    # Welcome message
    print('Welcome to TIC TAC TOE!')

    # INITIALIZE AND DISPLAY_BOARD

    board_list = ['','1','2','3','4','5','6','7','8','9']
    display_board(board_list)
    board_list = [' '] * 10

    # Ask player 1 to choose marker and assign marker
    p1_marker, p2_marker = assign_markers()

    # Choose which player will go first
    turn = turn_func()

    # Ask if ready to start game
    game_on = game_on_func()

    while game_on:
        # if Player 1 turn:
        if turn == 1:
            # ASSIGN POSITION
            assign_position(turn, p1_marker, board_list)
            display_board(board_list)
            # WIN_CHECK
            if win_check(p1_marker, board_list):
                # TRUE: Display win.
                print('Player {0} WON the game! Congratulations!'.format(turn))
                # BREAK
                break
            # BOARD_FULL_CHECK
            elif board_full_check(board_list):
                #Game is draw and Break
                print('The game is a DRAW!')
                break
            #ELSE
            else:
                # Next player turn
                turn = 2

        if turn == 2:
            # ASSIGN POSITION
            assign_position(turn, p2_marker, board_list)
            display_board(board_list)
            # WIN_CHECK
            if win_check(p2_marker, board_list):
                # TRUE: Display win.
                print('Player {0} WON the game! Congratulations!'.format(turn))
                # BREAK
                break
            # BOARD_FULL_CHECK
            elif board_full_check(board_list):
                #Game is draw and Break
                print('The game is a DRAW!')
                break
            #ELSE
            else:
                # Next player turn
                turn = 1


    # CHECK_REPLAY:
    if game_replay():
        # YES: PASS
        continue
    else:
        # NO: BREAK
        break