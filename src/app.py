
import sys
from solver import solveN,print_solutions



def run(N,store=False):
    solutions ,time = solveN(N,store)
    print_solutions(solutions)
    print(f"{len(solutions)}  solutions for a board of size {N} x {N} \n{time:.4f}s taken")

if __name__ == '__main__':
    assert len(sys.argv[1:]) < 4
    run(int(sys.argv[1]),True) if len(sys.argv)==3  else run(int(sys.argv[1]))
