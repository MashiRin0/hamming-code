from matrixclass import matrix
#This code will take a 4-bit message and add 3 parity bits, with which it can detect 1 and 2 bit errors
#and correct 1-bit errors, however it cannot distinguish between 1 and 2 bit errors, so it won't work if there
#is a 2-bit error. 
G = matrix([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) #code-generator matrix
H = matrix([[1,0,1,0,1,0,1],[0,1,1,0,0,1,1],[0,0,0,1,1,1,1]]) #parity-check matrix
R = matrix([[0,0,1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]) #decoding matrix

def encode(x):
    y = G*x
    return y

def check_error(y):
    #returns 4 for no error, and else the position in data bit of the error
    nul = matrix.nul_mat(3,1) 
    if H*y == nul:
        return 4 
    else:
        data_bits = [2,4,5,6]
        for i in data_bits:
            nul7 = matrix.nul_mat(7,1)
            nul7.matrix[i]=[1]
            if H*(nul7+y)==nul:
                return data_bits.index(i)
    #we don't have to check for errors in the parity bits, since that doesn't affect the data
    
def decode(y):
    x = R*y
    if check_error(y)!=4:
        for i in range(4):
            nul = matrix.nul_mat(4,1)
            nul.matrix[i]=1
            x += nul
    return x
