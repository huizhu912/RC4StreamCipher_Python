from math import *

def KSA(l):
    global L1, L2, S, K
    L1 = 256
    L2 = 5
    S = K = []
    i = j = temp = 0
    S = [i for i in range(256)]
    if l == L1:
        K = [0 for i in range(L1)]
    elif l == L2:
        K = [15, 202, 33, 6, 8]
    for i in range(len(S)):
        j = (j + S[i] + K[(i % l)]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp

def SGA(l):
    KSA(l)
    global subkeys
    subkeys	= []
    i = j = u = temp = 0
    while u < 20:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp		
        subkeys.append(S[(S[i] + S[j]) % 256])
        u = u + 1
    print("When l = ", l, ", the first 20 bytes of the generated key stream in decimal notation are:") 
    print(subkeys)

SGA(256)
#SGA(5)
	




    
        