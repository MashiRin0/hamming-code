from matrixclass import matrix
G = matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,1,1]])
def encode(x):
    global G
    y = G*x
    return y
def check_error(vector):
    H = matrix([[1,1,1,1,1]])
    if H*vector != matrix([[0]]):
        return 1
    else: return 0
