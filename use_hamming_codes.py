from Hamming74 import encode as encode3
from Hamming74 import decode as decode3
from Hamming_m import gen_encode 
from Hamming_m import gen_decode
from Hamming_m import encode
from Hamming_m import decode
from matrixclass import matrix

def make_list(not_list):
    list = []
    for i in range(len(not_list)):
        list.append([])
        for j in range(len(not_list[i])):
            list[i].append(int(not_list[i][j]))
    return list
m=int(input("How many parity bits will you use, this will be Hamming(2**m-1,2**m-m-1) code where m is the number of parity bits\n Note that this value should be greater than 1, and for the smallest complexity choose m=3:"))
func = input("Do you want to decode or encode? d for decode and e for encode:")
if func=="e":
    message = input("input your message as groups of "+str((2**m)-m-1)+" bits seperated by spaces:").split()
    msg_lst = make_list(message)
    out = ""
    if m != 3:
        gen_encode(m)
    for i in range(len(msg_lst)):
        x = matrix.transpose(matrix([msg_lst[i]]))
        if m == 3: #the general function is slower, so that is why we use a seperate function for m = 3
            out += str(matrix.transpose(encode3(x)))
        else:
            out += str(matrix.transpose(encode(x)))
    out = out.replace("\n]["," ")
elif func=="d":
    message = input("input the encoded message as groups of "+str((2**m)-1)+" bits seperated by spaces:").split()
    msg_lst = make_list(message)
    out = ""
    if m != 3:
        gen_decode(m)
    for i in range(len(msg_lst)):
        y = matrix.transpose(matrix([msg_lst[i]]))
        if m == 3: #the general function is slower, so that is why we use a seperate function for m = 3
            out+= str(matrix.transpose(decode3(y)))
        else:
            out+= str(matrix.transpose(decode(y)))
    out = out.replace("\n][","")
else: raise ValueError("input incorrect")
print(out)