"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    The player function should take a board state as input, and return which player’s turn it is (either X or O).
    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    player_x = 0
    player_0 = 0

    for axis_x in board:
        for axis_y in board:
            if axis_x == X:
                player_x += 1
            elif axis_x == O:
                player_0 += 1
    if player_x <= player_0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    The actions function should return a set of all of the possible actions that can be taken on a given board.
    Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    Possible moves are any cells on the board that do not already have an X or an O in them.
    Any return value is acceptable if a terminal board is provided as input.
    """
    raise NotImplementedError


def result(board, action):
    """
    The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
If action is not a valid action for the board, your program should raise an exception.
The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell
in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    """
    raise NotImplementedError


def winner(board):
    """
    The winner function should accept a board as input, and return the winner of the board if there is one.
If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    """
    for index in range(3):
        if (board[0][index] == board[1][index] == board[2][index] and board[0][index] != EMPTY):
            return board[0][index]
        if (board[index][0] == board[index][1] == board[index][2] and board[index][0] != EMPTY):
            return board[0][index]
    if(board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) :
        return board[1][1]
    return None


def terminal(board):
    """
    The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
    If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    Otherwise, the function should return False if the game is still in progress.
    """
    winner_result = winner(board)
    if winner_result == X or winner_result == O:
        return True
    elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
