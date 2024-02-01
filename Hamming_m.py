from matrixclass import matrix
import math
#Hamming(2**m-1,2**m-m-1)
#general hamming code with m parity bits and 2**m-m-1 data bits

def gen_bits():
    a = 0
    bits = [] #this list will tell us where the parity bits are
    while a<2**m-1:
        if math.log(a+1,2)%1==0: #every bit that is a power of 2 will be a parity bit
            bits.append("p")
        else: bits.append("d")
        a += 1
    return bits

def code_gen():#this list will tell us which bits the parity bits encompass
    code_gen = [] #we will append the rows to this list
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
    return code_gen

def encode_mat(): 
    G = [] #this is the generator matrix
    for j in range(len(C)):
        G.append([])
        for i in range(len(C[j])):
            if bits[i]=="d": #the matrix G will take the data bits as input and output the message
                G[j].append(C[j][i])
    return matrix(G)

def decode_mat(): #now  the decoding matrix
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
                    bits_R[i]=""
                else:
                    R[j].append(0)
            else:
                R[j].append(0)
    return matrix(R)

def parity_check_mat(): 
    H = [] 
    for i in range(len(bits)): #we will go through all bits and for every parity bit we will add the corresponding row to H
        if bits[i] == "p":
            H.append(C[i])
    return matrix(H)

def error_correct(y): #will return nothing for no error, and for an error the index of the error excluding parity bits
    nul = matrix.nul_mat(m,1)
    dat = [i for i,n in enumerate(bits) if n == "d"] #we again only care about the data bits
    if H*y == nul:
        pass
    else:
        nulvec = matrix.nul_mat(2**m-1,1)
        for i in dat:
            nulvec.matrix[i]=[1] #we change one of the data bits with this vecor
            if H*(nulvec+y)== nul:#check if changing this data bit solves our error
                return dat.index(i)#if it does, return the place of the error
            nulvec.matrix[i]=[0] #we save complexity by not looping the nulvec creation

def gen_encode(n):
    global C #this will generate all we need for encode
    global bits #so that when we encode more nibbles repeatedly
    global G #we don't have to regenerate the matrices etc. greatly decreasing complexity
    global m
    m = n
    bits = gen_bits()
    C = code_gen()
    G = encode_mat()

def gen_decode(n):
    global C #see comments under gen_encode
    global bits
    global H 
    global R
    global m
    m = n
    bits = gen_bits()
    C = code_gen()
    H = parity_check_mat()
    R = decode_mat()

def encode(x):
    return G*x

def decode(y):
    x = R*y
    e = error_correct(y)
    if e != None:
        nul = matrix.nul_mat(2**m-m-1,1)
        nul.matrix[e] = [1]
        x = nul+x
    return x
