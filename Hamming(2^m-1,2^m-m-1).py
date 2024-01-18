from matrixclass import matrix
import math
#would be great to create general hamming code
m = 4 #number of parity bits
def generate_code_gen_mat(m):
    a = 0
    bits = [] #this list will tell us where the parity bits are
    while a<2**m-1:
        if math.log(a+1,2)%1==0:
            bits.append("p")
        else: bits.append("d")
        a += 1
    code_gen = [] #we will append the rows which will tell us what to put in the generator matrix
    while len(code_gen)<len(bits):
        counter_d = 0
        for i in range(len(bits)):
            if bits[i]=="d":
                row = []
                for j in range(len(bits)):
                    if j == i:
                        row.append(1)
                    else: row.append(0)
                code_gen.append(row)
                counter_d += 1
            else:
                row = []
                for j in range(i):
                    row.append(0)
                counter = 0
                while len(bits)>len(row):
                    if counter == 0:
                        for j in range(i+1):
                            row.append(1)
                            if len(bits)<len(row):
                                row.pop(-1)
                        counter += 1
                    else:
                        for j in range(i+1):
                            row.append(0)
                            if len(bits)<len(row):
                                row.pop(-1)
                        counter -= 1
                code_gen.append(row)
    G = [] #this is the generator matrix
    for j in range(len(code_gen)):
        G.append([])
        for i in range(len(code_gen[j])):
            if bits[i]=="d":
                G[j].append(code_gen[j][i])
    return matrix(G)

print(generate_code_gen_mat(3))