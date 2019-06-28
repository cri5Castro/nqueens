import sys
from nqueens import app
    
if __name__ == '__main__':
    assert len(sys.argv[1:]) < 3
    app.run(int(sys.argv[1]))