class matrix:
    def __init__(self,matrix) -> None:
        self.matrix = matrix #this will give the matrix in list form
        self.shape = [len(self.matrix),len(self.matrix[0])] #[rows,columns]

    def __str__(self):
        out = "[\n" #this will be the string pasted, we have chosen for a format here, but this could be anything
        for i in range(self.shape[0]): #goes through the rows
            out+="["
            for j in range(self.shape[1]): #goes through the collumns
                self.matrix[i][j]=self.matrix[i][j]%2 #mod 2
                out+=str(self.matrix[i][j])+"    " #adds every element to the string
            out = out[:-4]
            out+="]\n"
        out+="]"
        return out
    
    def __add__(self,other):
        if self.shape!=other.shape: #addition is only possible with matrices of the same shape
            raise ValueError("matrices hebben niet dezelfde vorm")
        solmat = self
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                solmat.matrix[i][j] = (other.matrix[i][j] + self.matrix[i][j])%2 #adds elements in same positions together
        return solmat
    
    def __radd__(self,other): #does the same as __add__
        if self.shape!=other.shape:
            raise ValueError("matrices hebben niet dezelfde vorm")
        solmat = self
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                solmat.matrix[i][j] = (other.matrix[i][j] + self.matrix[i][j])%2
        return solmat

    def __mul__(self,other):
        if self.shape[1]!=other.shape[0]: #rules for matrix multiplication
            raise ValueError("matrices kunnen niet vermenigvuldigd worden!")
        solmat = matrix.nul_mat(self.shape[0],other.shape[1])
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(other.shape[0]):
                    solmat.matrix[i][j]+=self.matrix[i][k]*other.matrix[k][j] #rules for matrix multiplication
        for i in range(solmat.shape[0]):
            for j in range(solmat.shape[1]):
                solmat.matrix[i][j] = solmat.matrix[i][j]%2 #we have to use a seperate loop for the mod 2 since we add

        return solmat

    def nul_mat(row,col):
        nul = [] #generates a matrix with only zeroes
        for i in range(row):
            nul.append([])
            for j in range(col):
                nul[i].append(0)
        return matrix(nul)
    
    def __eq__(self,other): #checks if matrices are equal
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.matrix[i][j]!=other.matrix[i][j]: #they are equal if they are not not equal
                    return False
        return True
    
    def __neq__(self,other):
        if self==other: #they are neq if they are not equal ...
            return False
        else: return True

    def transpose(self): #this swaps the rows and columns 
        solmat = matrix.nul_mat(self.shape[1],self.shape[0]) #generate a matrix in which we will place the values
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                solmat.matrix[j][i]=self.matrix[i][j]
        return solmat