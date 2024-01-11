import numpy as np

class matrix:
    
    def __init__(self, matrix) -> None:
        
        self.matrix = matrix
        self.shape = matrix.shape()
        

    def RREF(self):

        pass

A = np.array([[3,1,2],[0,4,3],[1,7,2]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])

# A = np.zeros(shape=(3,2), dtype=int)

# Poep = matrix(A)

print(A)
print(B)