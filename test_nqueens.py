from nqueens.solver import *

    
def test_solN4():
    """
    Tests if the fiven solution for N = 4 is the corect solution
    """
    sol_real= [[[0, 0, 1, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0]],
               [[0, 1, 0, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0],
                [0, 0, 1, 0]]]
    solutions , time =  solveN(4)
    assert solutions==sol_real
    print(f"Test passed {time:.4f}s taken")
    

def test_solN5():
    """
    Tests if the given number of solutions are the same of the real solution for N=5
    """
    solutions , time =  solveN(5)
    assert len(solutions) == 10 
    print(f"Test passed {time:.4f}s taken")

def test_solN6():
    """
    Tests if the given number of solutions are the same of the real solution for N=5
    """
    solutions , time =  solveN(6)
    assert len(solutions) == 4
    print(f"Test passed {time:.4f}s taken")
    
def test_time():
    """ Tests if te algorithm is cabla to finish the solution for N=12 in less than 10 minutes
    """
    for N in range(8,20):
        time= testN(N)
        if  time > 10*60:
            break
    print(f"Test passed {time:.2f}s taken")

def testN(N):
    _ ,time = solveN(12)
    assert time<10*60 
    print(f"Test passed for N = {N} {time:.2f}s taken")
    return time 
    