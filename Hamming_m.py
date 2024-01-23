from matrixclass import matrix
import math
#Hamming(2**m-1,2**m-m-1)
#general hamming code with m parity bits and 2**m-m-1 data bits
m = 4 #number of parity bits
def generate_code_gen_mat(m):
    a = 0
    bits = [] #this list will tell us where the parity bits are
    while a<2**m-1:
        if math.log(a+1,2)%1==0: #every bit that is a power of 2 will be a parity bit
            bits.append("p")
        else: bits.append("d")
        a += 1
    
    #here we make the encoding matrix
    code_gen = [] #we will append the rows which will tell us what to put in the generator matrix
    while len(code_gen)<len(bits): 
        counter_d = 0
        for i in range(len(bits)):
            if bits[i]=="d": #all data bits will point only to itself
                row = []
                for j in range(len(bits)):
                    if j == i:
                        row.append(1)
                    else: row.append(0)
                code_gen.append(row)
                counter_d += 1
            else: #the parity bits will point to the bits according to this algorithm
                row = []
                for j in range(i):
                    row.append(0)
                counter = 0
                while len(bits)>len(row):
                    if counter == 0:
                        for j in range(i+1):
                            row.append(1)
                            if len(bits)<len(row): #fixes a problem with adding too many bits to this row
                                row.pop(-1)
                        counter += 1
                    else:
                        for j in range(i+1):
                            row.append(0)
                            if len(bits)<len(row): #fixes the same problem as before
                                row.pop(-1)
                        counter -= 1
                code_gen.append(row)
    G = [] #this is the generator matrix
    for j in range(len(code_gen)):
        G.append([])
        for i in range(len(code_gen[j])):
            if bits[i]=="d": #the matrix G will take the data bits as input and output the message
                G[j].append(code_gen[j][i])
    #now  the decoding matrix
    R = [] #we want a 1 for every data bit and a 0 for the parity bits, leaving us with only the data bits
    bits_R = bits.copy() #we will use a copy of bits since we will be modifying it and might need it later
    for j in range(2**m-m-1): #the amount of data bits we have
        data_bit_counter = 0 #every row should only have one 1
        R.append([])
        for i in range(len(bits_R)): #every row should have the length of the input vector
            if bits_R[i]=="d":
                if data_bit_counter==0:
                    R[j].append(1)
                    data_bit_counter+=1
                    bits_R[i]="del_d"
                else:
                    R[j].append(0)
            else:
                R[j].append(0)
    #parity check matrix
    return matrix(G),matrix(R)
G,R = generate_code_gen_mat(2)
