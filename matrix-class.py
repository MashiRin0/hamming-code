import numpy as np

class matrix:
    def __init__(self,matrix) -> None:
        
        self.matrix = matrix
        self.shape = matrix.shape

    def __str__(self):
        out = "[\n"
        str_mat = np.char.mod("%d",self.matrix)
        for i in range(self.shape[0]):
            out+="["
            for j in range(self.shape[1]):
                out+=str_mat[i][j]+"    "
            out = out[:-4]
            out+="]\n"
        out+="]"
        return out

    def __add__(self,other):
        if self.shape!=other.shape:
            raise ValueError("matrices hebben niet dezelfde vorm")
            pass
        solmat = matrix(np.zeros(self.shape))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                solmat.matrix[i][j]= self.matrix[i][j]+other.matrix[i][j]
        return solmat
    def __radd__(self,other):
        if self.shape!=other.shape:
            raise ValueError("matrices hebben niet dezelfde vorm")
            pass
        solmat = matrix(np.zeros(self.shape))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                solmat.matrix[i][j]= self.matrix[i][j]+other.matrix[i][j]
        return solmat
    def __mul__(self,other):
        if self.shape[1]!=other.shape[0]:
            raise ValueError("matrices kunnen niet vermenigvuldigd worden!")
            pass
        solmat = matrix(np.zeros((self.shape[0],other.shape[1])))
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(other.shape[0]):
                    solmat.matrix[i][j]+=self.matrix[i][k]*other.matrix[k][j]
        return solmat

