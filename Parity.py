from matrixclass import matrix
#This code will take a 4-bit message and add one parity bit, meaning it can detect a single bit error
#but it is not able to correct anything
G = matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,1,1]]) #parity-generator matrix
H = matrix([[1,1,1,1,1]]) #parity-check matrix
R = matrix([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]]) #decoding matrix
def encode(x):
    y = G*x
    return y

def check_error(vector):
    if H*vector != matrix([[0]]):
        return 1
    else: return 0

def decode(y):
    if check_error(y)==1:
        return "Error"
    else:
        x = R*y
        return x
