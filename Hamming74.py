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
    if H*y == nul:#the parity check matrix is designed so that it should always return nul if there is no error
        return 4 #this number is a choice we made since it is one higher than the last data bit
    else:
        data_bits = [2,4,5,6] #the data bits will be on these indeces
        for i in data_bits:
            nul7 = matrix.nul_mat(7,1)
            nul7.matrix[i]=[1] #we change 1 data bit and see if this does give the right parity
            if H*(nul7+y)==nul: #note that it doesn't matter if we add or subtract y and nul7, since it is base 2
                return data_bits.index(i) 
    #we don't have to check for errors in the parity bits, since that doesn't affect the data
    
def decode(y):
    x = R*y
    e = check_error(y)
    if check_error(y)!=4: #if it IS 4, there are no errors
        nul = matrix.nul_mat(4,1)
        nul.matrix[e]=[1] 
        x += nul #changes the bit that the error check says is wrong
    return x