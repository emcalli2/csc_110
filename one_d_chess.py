
'''
Elizabeth McAllister
CSC110
Project -4
This program creates a one - d chess game
'''
# creates initial board
def create_board():
    '''
    This functions returns a list  
    Args:
        None
    Returns: 
        a list that creates the initial board
    '''
    return ["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]
# sets board varable equal to the initial board

def printable_board(board):
    '''
    This functions returns a graphical representation of the board 
    Args:
        board: the initial board (list from create_board)
    Returns: 
        graphical representation of board
    
    '''
    board_top = "+-----------------------------------------------------+"
    board_line = ""
    for item in board:
        if item != "EMPTY":
            board_line += "| " + item + " "
        else:
            board_line += "| " + "   " + " "
    board_bottom = "+-----------------------------------------------------+"
    return board_top + "\n" + board_line + "|" + "\n" + board_bottom

# varifies of the move is valid
def is_valid_move(board, position, player):
    '''
    This functions returns True or False 
    Args:
        board: the list of pieces
        position: index 
        player: Black or White
    Returns: 
        Boolian if move is valid
    '''
    if 0 <= position and position <= 8:
        # checks if the player is Black and its position is on the board
        if player[0] == "B" and "B" in board[position]:
            return True
        #checks if the player is White and its position is on the board
        if player[0] == "W" and "W" in board[position]:
            return True
        else:
            return False
    else:
        return False

def move_king(board, position,direction):
    '''
    This functions returns the board with moved king
    Args:
        board: list of pieces
        position: index
        direction: left or right
    Returns: 
        the updates board with the new position of the king
    '''
    i = position 
    #iterates through board and moves king according to direction
    if direction == "LEFT":
        while i > 0 and board[i-1]=="EMPTY":
        # moves the king left if the position next to it is empty 
            board[i-1] = board[i]
            # makes the position the king was in empty
            board[i] = "EMPTY"
            # runs if the position to the left of the king is not empty
            i -= 1
        if i > 0 and board[i-1] != "EMPTY":
            board[i-1] = board[i]
            # makes the position the king was in empty
            board[i] = "EMPTY"
            
    if direction == "RIGHT":
        while i < 8 and board[i+1]=="EMPTY":
            # moves the king right if the position next to it is empty 
            board[i+1] = board[i]
            # makes the position the king was in empty
            board[i] = "EMPTY"
            # runs if the position to the right of the king is not empty
            i += 1
        if i < 8 and board[i+1] != "EMPTY":
                board[i+1] = board[i]
                # makes the position the king was in empty
                board[i] = "EMPTY"
    return board



def move_knight(board, position, direction):
    '''
    This functions returns board with moved knight
    Args:
        board: list of pieces
        position: index
        direction: left or right
    Returns: 
        the board with the new position of the knight
    '''
    if direction == "RIGHT":
        if position < 7:
            # moves the knight right two spaces
            board[position + 2] = board[position]
            # makes the position the knight was in empty
            board[position] = "EMPTY"
    elif direction == "LEFT":
        if position > 1:
            # moves the knight left two spaces
            board[position - 2] = board[position]
            # makes the position the knight was in empty
            board[position] = "EMPTY"
    # runs if the ending position of the move is out of bounds
    else:
        board[position] = board[position]
    return board[position]


def move(board, position, direction):
    '''
    This functions calls a function based on type of piece
    Args:
        board: list of pieces
        position: index
        direction: left or right
    Returns: 
        calls necessary function based on type of piece
    '''
    # if the piece is a knight, calls the move_night function
    if "Kn" in board[position]:
        move_knight(board, position, direction)
    # if the piece is a king, calls the move_king function
    if "Ki" in board[position]:
        move_king(board, position, direction)



def is_game_over(board):
    '''
    This functions returns a boolean indicating if the game is over
    Args:
        board: list of pieces
    Returns: 
        True if the game or over
        False if the game is not over
    '''
    # if there are not any kings on the board, the game is over
    if "WKi" not in board or "BKi" not in board:
        return True # game over
    # if there are still kings on the board
    else:
        return False #game not over


def whos_the_winner(board):
    '''
    This functions returns who won the game
    Args:
        board: list of pieces
    Returns: 
        BLACK: if there are no white kings
        WHITE: if there are no black kings
        NONE: if there are no kings
    '''
    # if there is a BKi on the board but not a WKi
    if "WKi" not in board and "BKi" in board:
        return "Black" #Black wins
    # if there is a WKi on the board but not a BKi
    elif "BKi" not in board and "WKi" in board:
        return "White" #White wins
    # if there are no kings left, no one wins
    else:
        return None

