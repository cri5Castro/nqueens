import copy
import sys
import time
import pytest
from models import Solution
from database import opendb

def create_board(size):
    """ Returns an board of size n^2
    
    Arguments:
        size {[int]} -- [size of the board]
    Returns:
        board{array[int]} -- [ matrix  of size nxn]
    """
    board = [0]*size
    for ix in range(size):
        board[ix] = [0]*size
    return board


def print_solutions(solutions):
    """ Print the solution matrices
    
    Arguments:
        solutions{array[array[int]]} -- [a list of solution matrices]
    """
    for board in solutions:
        for row in board:
            print(row)
        print()


def check_tile(board, row, col, size):
    """ Check if a queen could be placed at board[x][y]
    
    Arguments:
        board{array[int]} -- [ matrix  of size nxn]
        row {[int]} -- [row position of tile]
        col {[int]} -- [col position of tile]
        size {[int]} -- [size of the board nxn]
    
    Returns:
        [type] -- [description]
    """
    #check on the left side
    for y in range(col):
        if board[row][y] == 1:
            return False

    #check left upper diagonal 
    x, y = row, col
    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1
    
    #check lower diagonal on left side
    x, y = row, col
    while x < size and y >= 0:
        if board[x][y] == 1:
            return False
        x += 1
        y -= 1

    return True


def solve(board, col, size, solutions,store=False,dbsession=None):
    """
    Implements backtrack to search all the possible solutions
    - we put a queen first corner 
    - then we start to place queen in 
    the follow rows in such a way they don't attack each other 
    - if N queens have been placed stores the solution
    then we remove the queen from the previous step and try to increment the row of the queen in the column before
    - if the queen can't be placed increment the row of the queen in the previous column
    - continue until we are in row N
    
    
    
    Arguments:
        board {[type]} -- [description]
        col {[type]} -- [description]
        size {[type]} -- [description]
        solutions {[type]} -- [description]
    """
    # we finished
    if col >= size:
        return
    
    for i in range(size):
        if check_tile(board, i, col, size):
            #a queen could be placed
            board[i][col] = 1 
            if col == size-1:
                #we found a solution
                if (store):
                    dbsession.add(Solution(n=size, result=board))
                solutions.append(copy.deepcopy(board))
                board[i][col] = 0
                return
            #backtrack step
            solve(board, col+1, size, solutions)
            board[i][col] = 0
    if(store):
        dbsession.commit()

def solveN(N,store=False):
    s = time.time()
    N = N
    assert N >= 4
    board = create_board(N)
    solutions = []
    dbsession=opendb() if store else None
    solve(board, 0, N, solutions,store,dbsession)
    return solutions,(time.time()-s)
