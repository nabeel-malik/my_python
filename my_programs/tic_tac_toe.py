from IPython.display import clear_output

def display_board(board):
    print("""
        |    |   
     {6}  | {7}  | {8}  
        |    |   
    -----------
        |    |   
     {3}  | {4}  | {5}  
        |    |   
    -----------
        |    |   
     {0}  | {1}  | {2}  
        |    |   
    """.format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]))


def player_input():
    player_marker = input("Do you want to be X or O?")
    while not player_marker in ('X', 'O'):
        player_marker = input("Invalid entry. Do you want to be X or O?")


def place_marker(board, marker, position):
    board[position] = marker

