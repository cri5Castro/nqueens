
from nqueens.solver import *
def run(N):
    solutions ,time = solveN(N)
    print_solutions(solutions)
    print(f"{len(solutions)}  solutions for a board of size {N} x {N} \n{time:.4f}s taken")
