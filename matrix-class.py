import numpy as np
<<<<<<< HEAD
<<<<<<< HEAD

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
=======
=======

matrix1,matrix2 = input().split()
def mat_not(mat):
    inp_list = mat.split('],[')
    print(inp_list)
    for i in range(len(inp_list)):
        inp_list[i]=inp_list[i].split(",")
    inp_list[0][0]=inp_list[0][0].replace('[[','')
    inp_list[-1][-1] = inp_list[-1][-1].replace(']]','')
    return inp_list
    for i in range(len(inp_list)):
        for j in range(len(inp_list[i])):
            inp_list[i][j] = int(inp_list[i][j])
    
print(mat_not(matrix1))
>>>>>>> 685294b2029e756e8437e03bf13ad7d425c7d3ca
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
y= np.array([[1,9,8],[2,9,8],[3,9,8]])
y= np.array(matrix1)
A = matrix(y)
x = np.array([[4,5,6],[7,8,9],[1,2,3]])
x = np.array(matrix2)
B = matrix(x)
<<<<<<< HEAD
print(A*B)
>>>>>>> b8c1fbe6851b05cbaeb4e8be63c59c0c6beb0ca8
=======
print()
>>>>>>> 685294b2029e756e8437e03bf13ad7d425c7d3ca
