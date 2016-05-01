from random import *
import math
def generate_random_hex(n):
    randBinList = lambda n: [randint(0,15) for b in range(1,n+1)]
    key=randBinList(n)
    Map={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}    
    for i in range(len(key)):
        key[i]=Map[key[i]]
    return key
def addRoundKey(k,b):
    #takes 64 bit plain text as argument,gives modified 64 bit plain text 
    #assume 80 bit key given as [79] [78] [77].........[1][0]
    #assume 64 bit key given as [63][62]................[1][0]
    Map={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    reMap={'A': 10, 'C': 12, 'B': 11, 'E': 14, 'D': 13, 'F': 15, '1': 1, '0': 0, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6, '9': 9, '8': 8}
    shortKey=k[:16]
    for j in range(0,len(b)):
        shortKey[j]=Map[(reMap[shortKey[j]]^reMap[b[j]])]
    return shortKey
def sBoxLayer(b):
    #takes 64 bit plain text as argument,gives modified 64 bit plain text 
    sBox={"0":"C","1":"5","2":"6","3":"B","4":"9","5":"0","6":"A","7":"D","8":"3","9":"E","A":"F","B":"8","C":"4","D":"7","E":"1","F":"2"}
    for i in range(len(b)):
        b[i]=sBox[b[i]]
    return b
def pBoxLayer(plaintext):
    #takes 64 bit plain text as argument,gives modified 64 bit plain text 
    pBox={0:0,1:16,2:32,3:48,4:1,5:17,6:33,7:49,8:2,9:18,10:34,11:50,12:3,13:19,14:35,15:51,16:4,17:20,18:36,19:52,20:5,21:21,22:37,23:53,24:6,25:22,26:38,27:54,28:7,29:23,30:39,31:55,32:8,33:24,34:40,35:56,36:9,37:25,38:41,39:57,40:10,41:26,42:42,43:58,44:11,45:27,46:43,47:59,48:12,49:28,50:44,51:60,52:13,53:29,54:45,55:61,56:14,57:30,58:46,59:62,60:15,61:31,62:47,63:63}
    reMap={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    binary_pt=[]
    afterPbinary=[""]*64
    for word in plaintext:
        tmp=reMap[word]
        binary_pt.append(tmp[0])
        binary_pt.append(tmp[1])
        binary_pt.append(tmp[2])
        binary_pt.append(tmp[3])
    #print "binary pt ",binary_pt
    #reverse binary_pt
    reverse_binary_pt=[]
    afterPbin=[]
    for j in range(63,-1,-1):
        reverse_binary_pt.append(binary_pt[j])
    #print "reverse_binary_pt ",reverse_binary_pt
    for i in range(len(afterPbinary)):
        afterPbinary[i]=reverse_binary_pt[pBox[i]]
    #print "afterPbinary ",afterPbinary
    for j in range(63,-1,-1):
        afterPbin.append(afterPbinary[j])
    #print "afterPbin ",afterPbin
    ret=[]
    Map={0:"0",1:"1",10:"2",11:"3",100:"4",101:"5",110:"6",111:"7",1000:"8",1001:"9",1010:"A",1011:"B",1100:"C",1101:"D",1110:"E",1111:"F"}
    for i in range(16):
        tmp=((int)(afterPbin[(4*i)])*(10**3))+((int)(afterPbin[(4*i)+1])*(10**2))+((int)(afterPbin[(4*i)+2])*(10**1))+((int)(afterPbin[(4*i)+3])*(10**0))
        ret.append(Map[tmp])
    #print ret
    return ret
def prin(arr):
    st=""
    for k in arr:
        st=st+str(k)
    return st
def key_update(key,counter):
    #takes 80 bit key as input argument ,returns modified key as output
    #print "initial key is ",key
    KeyUpdateMap={}
    editKey=[]
    for j in range(80):
        temp=j
        temp=temp-61
        if temp<0:
            temp=temp+80
        KeyUpdateMap[j]=temp
    #print KeyUpdateMap
    reMap={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    binaryKey=[]
    for t in key:
        binaryKey.append(reMap[t][0])
        binaryKey.append(reMap[t][1])
        binaryKey.append(reMap[t][2])
        binaryKey.append(reMap[t][3])
    #print "Binary key ",binaryKey
    for i in range(79,-1,-1):
        editKey.append(binaryKey[KeyUpdateMap[i]])
    tmp=((int)(editKey[0])*1000) +((int)(editKey[1])*100)+((int)(editKey[2])*10)+(int)(editKey[3])
    sBox={"0":"C","1":"5","2":"6","3":"B","4":"9","5":"0","6":"A","7":"D","8":"3","9":"E","A":"F","B":"8","C":"4","D":"7","E":"1","F":"2"}
    reMap={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    Map={0:"0",1:"1",10:"2",11:"3",100:"4",101:"5",110:"6",111:"7",1000:"8",1001:"9",1010:"A",1011:"B",1100:"C",1101:"D",1110:"E",1111:"F"}
    temp=reMap[sBox[Map[tmp]]]
    tmp2=(str)(temp[0])+(str)(temp[1])+(str)(temp[2])+(str)(temp[3])
    editKey[0]=Map[(int)(tmp2[0])]
    editKey[1]=Map[(int)(tmp2[1])]
    editKey[2]=Map[(int)(tmp2[2])]
    editKey[3]=Map[(int)(tmp2[3])]
    binary=bin(counter)[2:]
    if len(binary)==1:
        editKey[60]=str((int)(editKey[60])^0)
        editKey[61]=str((int)(editKey[61])^0)
        editKey[62]=str((int)(editKey[62])^0)
        editKey[63]=str((int)(editKey[63])^0)
        editKey[64]=str((int)(editKey[64])^(int)(binary[0]))
    if len(binary)==2:
        editKey[60]=str((int)(editKey[60])^0)
        editKey[61]=str((int)(editKey[61])^0)
        editKey[62]=str((int)(editKey[62])^0)
        editKey[63]=str((int)(editKey[63])^(int)(binary[0]))
        editKey[64]=str((int)(editKey[64])^(int)(binary[1]))
    if len(binary)==3:
        editKey[60]=str((int)(editKey[60])^0)
        editKey[61]=str((int)(editKey[61])^0)
        editKey[62]=str((int)(editKey[62])^(int)(binary[0]))
        editKey[63]=str((int)(editKey[63])^(int)(binary[1]))
        editKey[63]=str((int)(editKey[64])^(int)(binary[2]))
    if len(binary)==4:
        editKey[60]=str((int)(editKey[60])^0)
        editKey[61]=str((int)(editKey[61])^(int)(binary[0]))
        editKey[62]=str((int)(editKey[62])^(int)(binary[1]))
        editKey[63]=str((int)(editKey[63])^(int)(binary[2]))
        editKey[64]=str((int)(editKey[64])^(int)(binary[3]))
    if len(binary)==5:
        editKey[60]=str((int)(editKey[60])^(int)(binary[0]))
        editKey[61]=str((int)(editKey[61])^(int)(binary[1]))
        editKey[62]=str((int)(editKey[62])^(int)(binary[2]))
        editKey[63]=str((int)(editKey[63])^(int)(binary[3]))
        editKey[64]=str((int)(editKey[64])^(int)(binary[4]))
    ret=[]
    Map={0:"0",1:"1",10:"2",11:"3",100:"4",101:"5",110:"6",111:"7",1000:"8",1001:"9",1010:"A",1011:"B",1100:"C",1101:"D",1110:"E",1111:"F"}
    for i in range(20):
        tmp=((int)(editKey[(4*i)])*(10**3))+((int)(editKey[(4*i)+1])*(10**2))+((int)(editKey[(4*i)+2])*(10**1))+((int)(editKey[(4*i)+3])*(10**0))
        ret.append(Map[tmp])
    return ret
            
            
        
        
            
        

#main Algo PRESENT-80
#key=['3', '8', 'B', 'E', '2', 'D', 'D', 'A', 'B', '7', 'E', '0', '4', '1', '7', 'C', 'A', '5', '6', 'A']
key=[]
cipher=[]
pt=[]
msg=[]#never change
init_key=[]#never change
nochangeCipher=[]#never change
def generate_key_pt():
    global key,pt,cipher,msg,init_key
    key=generate_random_hex(20)
    pt=generate_random_hex(16)
    msg=[]
    for k in pt:
        msg.append(k)
    init_key=[]
    for k in key:
        init_key.append(k)
def enc():
    global key,pt,cipher
    print "initial key is ",prin(key)
    print "initial plain text is ",prin(pt)
    for i in range(1,32):
        pt= addRoundKey(key,pt)
        #print "addround key ",pt
        pt=sBoxLayer(pt)
        #print "sBox  ",pt
        pt=pBoxLayer(pt)
        #print "pBox ",pt
        key=key_update(key,i)
        print "update key ",prin(key)," cipher ",prin(pt)
    pt= addRoundKey(key,pt)
    print "cipher is ",prin(pt)
    cipher=[]
    for k in pt:
        cipher.append(k)


def reversePbox(cipher):
    revpBox={0: 0, 1: 4, 2: 8, 3: 12, 4: 16, 5: 20, 6: 24, 7: 28, 8: 32, 9: 36, 10: 40, 11: 44, 12: 48, 13: 52, 14: 56, 15: 60, 16: 1, 17: 5, 18: 9, 19: 13, 20: 17, 21: 21, 22: 25, 23: 29, 24: 33, 25: 37, 26: 41, 27: 45, 28: 49, 29: 53, 30: 57, 31: 61, 32: 2, 33: 6, 34: 10, 35: 14, 36: 18, 37: 22, 38: 26, 39: 30, 40: 34, 41: 38, 42: 42, 43: 46, 44: 50, 45: 54, 46: 58, 47: 62, 48: 3, 49: 7, 50: 11, 51: 15, 52: 19, 53: 23, 54: 27, 55: 31, 56: 35, 57: 39, 58: 43, 59: 47, 60: 51, 61: 55, 62: 59, 63: 63}
    reMap={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    binary_cipher=[]
    afterrevPbinary=[""]*64
    for word in cipher:
        tmp=reMap[word]
        binary_cipher.append(tmp[0])
        binary_cipher.append(tmp[1])
        binary_cipher.append(tmp[2])
        binary_cipher.append(tmp[3])
    #print "binary_cipher ",binary_cipher
    reverse_binary_cipher=[]
    afterPbin=[]
    for j in range(63,-1,-1):
        reverse_binary_cipher.append(binary_cipher[j])
    #print "reverse_binary_cipher ",reverse_binary_cipher
    for i in range(len(afterrevPbinary)):
        afterrevPbinary[i]=reverse_binary_cipher[revpBox[i]]
    #print "afterrevPbinary ",afterrevPbinary
    #print "revpBox ",revpBox
    afterrevPbin=[]
    for j in range(63,-1,-1):
        afterrevPbin.append(afterrevPbinary[j])
    #print afterrevPbin
    ret=[]
    Map={0:"0",1:"1",10:"2",11:"3",100:"4",101:"5",110:"6",111:"7",1000:"8",1001:"9",1010:"A",1011:"B",1100:"C",1101:"D",1110:"E",1111:"F"}
    for i in range(16):
        tmp=((int)(afterrevPbin[(4*i)])*(10**3))+((int)(afterrevPbin[(4*i)+1])*(10**2))+((int)(afterrevPbin[(4*i)+2])*(10**1))+((int)(afterrevPbin[(4*i)+3])*(10**0))
        ret.append(Map[tmp])
    #print ret
    return ret
def revSbox(cipher):
    revsbox={'A': '6', 'C': '0', 'B': '3', 'E': '9', 'D': '7', 'F': 'A', '1': 'E', '0': '5', '3': '8', '2': 'F', '5': '1', '4': 'C', '7': 'D', '6': '2', '9': '4', '8': 'B'}
    for i in range(len(cipher)):
        cipher[i]=revsbox[cipher[i]]
    return cipher
def revKeyUpdate(key,counter):
    ret=[]
    reMap={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    binaryKey=[]
    afterrevPbinary=[""]*64
    for word in key:
        tmp=reMap[word]
        binaryKey.append(tmp[0])
        binaryKey.append(tmp[1])
        binaryKey.append(tmp[2])
        binaryKey.append(tmp[3])
    #print "binary_key ",binaryKey
    POO=bin(counter)
    binary=POO[2:]
    if len(binary)==1:
        binaryKey[60]=str((int)(binaryKey[60])^0)
        binaryKey[61]=str((int)(binaryKey[61])^0)
        binaryKey[62]=str((int)(binaryKey[62])^0)
        binaryKey[63]=str((int)(binaryKey[63])^0)
        binaryKey[64]=str((int)(binaryKey[64])^(int)(binary[0]))
    if len(binary)==2:
        binaryKey[60]=str((int)(binaryKey[60])^0)
        binaryKey[61]=str((int)(binaryKey[61])^0)
        binaryKey[62]=str((int)(binaryKey[62])^0)
        binaryKey[63]=str((int)(binaryKey[63])^(int)(binary[0]))
        binaryKey[64]=str((int)(binaryKey[64])^(int)(binary[1]))
    if len(binary)==3:
        binaryKey[60]=str((int)(binaryKey[60])^0)
        binaryKey[61]=str((int)(binaryKey[61])^0)
        binaryKey[62]=str((int)(binaryKey[62])^(int)(binary[0]))
        binaryKey[63]=str((int)(binaryKey[63])^(int)(binary[1]))
        binaryKey[63]=str((int)(binaryKey[64])^(int)(binary[2]))
    if len(binary)==4:
        binaryKey[60]=str((int)(binaryKey[60])^0)
        binaryKey[61]=str((int)(binaryKey[61])^(int)(binary[0]))
        binaryKey[62]=str((int)(binaryKey[62])^(int)(binary[1]))
        binaryKey[63]=str((int)(binaryKey[63])^(int)(binary[2]))
        binaryKey[64]=str((int)(binaryKey[64])^(int)(binary[3]))
    if len(binary)==5:
        binaryKey[60]=str((int)(binaryKey[60])^(int)(binary[0]))
        binaryKey[61]=str((int)(binaryKey[61])^(int)(binary[1]))
        binaryKey[62]=str((int)(binaryKey[62])^(int)(binary[2]))
        binaryKey[63]=str((int)(binaryKey[63])^(int)(binary[3]))
        binaryKey[64]=str((int)(binaryKey[64])^(int)(binary[4]))
    #print "binary_key ",binaryKey
    revsbox={'A': '6', 'C': '0', 'B': '3', 'E': '9', 'D': '7', 'F': 'A', '1': 'E', '0': '5', '3': '8', '2': 'F', '5': '1', '4': 'C', '7': 'D', '6': '2', '9': '4', '8': 'B'}
    Map={0:"0",1:"1",10:"2",11:"3",100:"4",101:"5",110:"6",111:"7",1000:"8",1001:"9",1010:"A",1011:"B",1100:"C",1101:"D",1110:"E",1111:"F"}
    reMap={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    tmp=((int)(binaryKey[0])*1000) +((int)(binaryKey[1])*100)+((int)(binaryKey[2])*10)+(int)(binaryKey[3])
    temp=reMap[revsbox[Map[tmp]]]
    tmp2=(str)(temp[0])+(str)(temp[1])+(str)(temp[2])+(str)(temp[3])
    binaryKey[0]=Map[(int)(tmp2[0])]
    binaryKey[1]=Map[(int)(tmp2[1])]
    binaryKey[2]=Map[(int)(tmp2[2])]
    binaryKey[3]=Map[(int)(tmp2[3])]
    #revKeyUpdate={0: 61, 1: 62, 2: 63, 3: 64, 4: 65, 5: 66, 6: 67, 7: 68, 8: 69, 9: 70, 10: 71, 11: 72, 12: 73, 13: 74, 14: 75, 15: 76, 16: 77, 17: 78, 18: 79, 19: 0, 20: 1, 21: 2, 22: 3, 23: 4, 24: 5, 25: 6, 26: 7, 27: 8, 28: 9, 29: 10, 30: 11, 31: 12, 32: 13, 33: 14, 34: 15, 35: 16, 36: 17, 37: 18, 38: 19, 39: 20, 40: 21, 41: 22, 42: 23, 43: 24, 44: 25, 45: 26, 46: 27, 47: 28, 48: 29, 49: 30, 50: 31, 51: 32, 52: 33, 53: 34, 54: 35, 55: 36, 56: 37, 57: 38, 58: 39, 59: 40, 60: 41, 61: 42, 62: 43, 63: 44, 64: 45, 65: 46, 66: 47, 67: 48, 68: 49, 69: 50, 70: 51, 71: 52, 72: 53, 73: 54, 74: 55, 75: 56, 76: 57, 77: 58, 78: 59, 79: 60}
    KeyUpdate={0: 19, 1: 20, 2: 21, 3: 22, 4: 23, 5: 24, 6: 25, 7: 26, 8: 27, 9: 28, 10: 29, 11: 30, 12: 31, 13: 32, 14: 33, 15: 34, 16: 35, 17: 36, 18: 37, 19: 38, 20: 39, 21: 40, 22: 41, 23: 42, 24: 43, 25: 44, 26: 45, 27: 46, 28: 47, 29: 48, 30: 49, 31: 50, 32: 51, 33: 52, 34: 53, 35: 54, 36: 55, 37: 56, 38: 57, 39: 58, 40: 59, 41: 60, 42: 61, 43: 62, 44: 63, 45: 64, 46: 65, 47: 66, 48: 67, 49: 68, 50: 69, 51: 70, 52: 71, 53: 72, 54: 73, 55: 74, 56: 75, 57: 76, 58: 77, 59: 78, 60: 79, 61: 0, 62: 1, 63: 2, 64: 3, 65: 4, 66: 5, 67: 6, 68: 7, 69: 8, 70: 9, 71: 10, 72: 11, 73: 12, 74: 13, 75: 14, 76: 15, 77: 16, 78: 17, 79: 18}
    editKey=[]
    for i in range(79,-1,-1):
        editKey.append(binaryKey[KeyUpdate[i]])
    ret=[]
    Map={0:"0",1:"1",10:"2",11:"3",100:"4",101:"5",110:"6",111:"7",1000:"8",1001:"9",1010:"A",1011:"B",1100:"C",1101:"D",1110:"E",1111:"F"}
    for i in range(20):
        tmp=((int)(editKey[(4*i)])*(10**3))+((int)(editKey[(4*i)+1])*(10**2))+((int)(editKey[(4*i)+2])*(10**1))+((int)(editKey[(4*i)+3])*(10**0))
        ret.append(Map[tmp])
    #print ret
    return ret
    
    
print "-----------------------------------------------------------------------------------------------------------------------"  
    
#decryption

def dec():
    global key,pt
    cipher=pt
    print "initial cipher ",cipher
    print "initial key ",key
    cipher=addRoundKey(key,cipher)
    print "key ",key," cipher ",cipher

    for i in range(31,0,-1):
        #print "add round key ",cipher
        cipher=reversePbox(cipher)
        #print "reversePbox ",cipher
        cipher=revSbox(cipher)
        #print "revSbox ",cipher
        key=revKeyUpdate(key,i)
        cipher=addRoundKey(key,cipher)
        print "key ",prin(key)," cipher ",prin(cipher)
    pt=cipher
    print pt
final=[]
A=[]
#4
for i in range(8):
        A.append(0)
def Binary(n):
    if n<1:
        #final.append(A)
        tmp=[]
        for k in A:
            tmp.append(k)
        final.append(tmp)
        tmp=[]
    else:
        A[n-1]=0
        Binary(n-1)
        A[n-1]=1
        Binary(n-1)
check_cipher=[]
def simple_exhaustive():
    global key,pt,init_key,msg,check_cipher
    counter=0
    generate_key_pt()
    enc()
    #1
    newkey=init_key[2:]
    for j in range(len(cipher)):
        check_cipher.append(cipher[j])
    #2
    Binary(8)    
    #print final
    for k in final:
        counter=counter+1
        test_key=newkey
        ret=[]
        Map={0:"0",1:"1",10:"2",11:"3",100:"4",101:"5",110:"6",111:"7",1000:"8",1001:"9",1010:"A",1011:"B",1100:"C",1101:"D",1110:"E",1111:"F"}
        #3
        for i in range(2):
            tmp=((int)(k[(4*i)])*(10**3))+((int)(k[(4*i)+1])*(10**2))+((int)(k[(4*i)+2])*(10**1))+((int)(k[(4*i)+3])*(10**0))
            ret.append(Map[tmp])
        test_key=ret+test_key
        print "ret ",prin(ret)
        print "test_key ",prin(test_key)
        for j in range(len(test_key)):
            key[j]=test_key[j]
        for j in range(len(msg)):
            pt[j]=msg[j]
        enc()
        if check_cipher==cipher:
            print "Got IT"
            print "key number ",counter," out of 256"
            break
simple_exhaustive()

        

        
        
        
    
    
    


    






    






    


    
