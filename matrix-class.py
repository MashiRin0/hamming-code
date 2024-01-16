class matrix:
    def __init__(self,matrix) -> None:
        self.matrix = matrix
        self.shape = [len(self.matrix),len(self.matrix[0])] #[rows,columns]

    def __str__(self):
        out = "[\n"
        for i in range(self.shape[0]):
            out+="["
            for j in range(self.shape[1]):
                out+=str(self.matrix[i][j])+"    "
            out = out[:-4]
            out+="]\n"
        out+="]"
        return out
    
    def __add__(self,other):
        if self.shape!=other.shape:
            raise ValueError("matrices hebben niet dezelfde vorm")
        solmat = self
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                solmat.matrix[i][j] = (other.matrix[i][j] + self.matrix[i][j])%2
        return solmat
    
    def __radd__(self,other):
        if self.shape!=other.shape:
            raise ValueError("matrices hebben niet dezelfde vorm")
        solmat = self
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                solmat.matrix[i][j] = (other.matrix[i][j] + self.matrix[i][j])%2
        return solmat
    
    def __mul__(self,other):
        if self.shape[1]!=other.shape[0]:
            raise ValueError("matrices kunnen niet vermenigvuldigd worden!")
        solmat = matrix.nul_mat(self.shape[0],other.shape[1])
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(other.shape[0]):
                    solmat.matrix[i][j]+=self.matrix[i][k]*other.matrix[k][j]  
        for i in range(solmat.shape[0]):
            for j in range(solmat.shape[1]):
                solmat.matrix[i][j] = solmat.matrix[i][j]%2

        return solmat

    def nul_mat(row,col):
        nul = []
        for i in range(row):
            nul.append([])
            for j in range(col):
                nul[i].append(0)
        return matrix(nul)

y = [[1,1,0],[1,1,1],[0,0,1]]
A = matrix(y)
x = [[0,1,0],[1,1,1],[0,0,0]]
B = matrix(x)

print(A*B)