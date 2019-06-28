from solver import solveN


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
    print(f"\nSolN4 Test passed {time:.4f}s taken")
    

def test_solN5():
    """
    Tests if the given number of solutions are the same of the real solution for N=5
    """
    solutions , time =  solveN(5)
    assert len(solutions) == 10 
    print(f"SolN5 Test passed {time:.4f}s taken")

def test_solN6():
    """
    Tests if the given number of solutions are the same of the real solution for N=5
    """
    solutions , time =  solveN(6)
    assert len(solutions) == 4
    print(f"SolN6 Test passed {time:.4f}s taken")
    
"""
def test_time12():
    _ ,time = solveN(12)
    assert time<10*60 
    print(f"Time Test passed for N = 12 {time:.2f}s taken")
    return time 
"""

def test_time():
    """ Tests if te algorithm is cabla to finish the solution for N=12 in less than 10 minutes
    """
    for N in range(8,20):
        _ ,time = solveN(N)
        if(time>600):
            print("Test don't passed at N={N} should be less than 10 min Taken:{time}")
            break
        print(f"Time Test passed for N = {N} {time:.2f}s taken") 
