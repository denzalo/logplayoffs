# Import libraries
import random
import numpy as np
import math

top2 = 0
#ax = 0.90
#ay = 0.70
#az = 0.40
# print([a])
#a = np.array([[1/(math.log10(1-ax)),-1/(math.log10(1-ay)),0],[1/(math.log10(1-ax)),0,-1/(math.log10(1-az))],[0,1/(math.log10(1-ay)),-1/(math.log10(1-az))],[1,1,1]])
#b = np.array([[0,0,0,1]])
#x = np.linalg.lstsq(a,b.T,rcond=None)[0]
#print([a])
#print([b])
#print(x)

BG = ["BG",0.99,top2,9900]
CHA = ["CHA",0.97,top2,9700]
BT = ["BT",0.95,top2,9500]
KCT = ["KCT",0.82,top2,8200]
BSC = ["BSC",0.68,top2,6800]
TDP = ["TDP",0.57,top2,5700]
EJ = ["EJ",0.48,top2,4800]
AA = ["AA",0.33,top2,3300]
DDB = ["DDB",0.11,top2,1100]
THR = ["THR",0.09,top2,900]
MTA = ["MTA",0.01,top2,100]
NSR = ["NSR",0.00,top2,0]

a = np.zeros((67,12))
for i in range(11):
    a[i,0]=BG[1]

for i in range(11):
    if i == 0:
        a[0,1]=CHA[1]
    else:
        a[i+10,1]=CHA[1]

for i in range(11):
    if i == 0:
        a[1,2]=BT[1]
    elif i == 1:
        a[11,2]=BT[1]
    else:
        a[i+19,2]=BT[1]

for i in range(11):
    if i == 0:
        a[2,3]=KCT[1]
    elif i == 1:
        a[12,3]=KCT[1]
    elif i == 2:
        a[21,3]=KCT[1]
    else:
        a[i+27,3]=KCT[1]

for i in range(11):
    if i == 0:
        a[3,4]=BSC[1]
    elif i == 1:
        a[13,4]=BSC[1]
    elif i == 2:
        a[22,4]=BSC[1]
    elif i == 3:
        a[30,4]=BSC[1]
    else:
        a[i+34,4]=BSC[1]

for i in range(11):
    if i == 0:
        a[4,5]=TDP[1]
    elif i == 1:
        a[14,5]=TDP[1]
    elif i == 2:
        a[23,5]=TDP[1]
    elif i == 3:
        a[31,5]=TDP[1]
    elif i == 4:
        a[38,5]=TDP[1]
    else:
        a[i+40,5]=TDP[1]

for i in range(11):
    if i == 0:
        a[5,6]=EJ[1]
    elif i == 1:
        a[15,6]=EJ[1]
    elif i == 2:
        a[24,6]=EJ[1]
    elif i == 3:
        a[32,6]=EJ[1]
    elif i == 4:
        a[39,6]=EJ[1]
    elif i == 5:
        a[45,6]=EJ[1]
    else:
        a[i+45,6]=EJ[1]

for i in range(11):
    if i == 0:
        a[6,7]=AA[1]
    elif i == 1:
        a[16,7]=AA[1]
    elif i == 2:
        a[25,7]=AA[1]
    elif i == 3:
        a[33,7]=AA[1]
    elif i == 4:
        a[40,7]=AA[1]
    elif i == 5:
        a[46,7]=AA[1]
    elif i == 6:
        a[51,7]=AA[1]
    else:
        a[i+49,7]=AA[1]

for i in range(11):
    if i == 0:
        a[7,8]=DDB[1]
    elif i == 1:
        a[17,8]=DDB[1]
    elif i == 2:
        a[26,8]=DDB[1]
    elif i == 3:
        a[34,8]=DDB[1]
    elif i == 4:
        a[41,8]=DDB[1]
    elif i == 5:
        a[47,8]=DDB[1]
    elif i == 6:
        a[52,8]=DDB[1]
    elif i == 7:
        a[56,8]=DDB[1]
    else:
        a[i+52,8]=DDB[1]

for i in range(11):
    if i == 0:
        a[8,9]=THR[1]
    elif i == 1:
        a[18,9]=THR[1]
    elif i == 2:
        a[27,9]=THR[1]
    elif i == 3:
        a[35,9]=THR[1]
    elif i == 4:
        a[42,9]=THR[1]
    elif i == 5:
        a[48,9]=THR[1]
    elif i == 6:
        a[53,9]=THR[1]
    elif i == 7:
        a[57,9]=THR[1]
    elif i == 8:
        a[60,9]=THR[1]
    else:
        a[i+54,9]=THR[1]

for i in range(11):
    if i == 0:
        a[9,10]=MTA[1]
    elif i == 1:
        a[19,10]=MTA[1]
    elif i == 2:
        a[28,10]=MTA[1]
    elif i == 3:
        a[36,10]=MTA[1]
    elif i == 4:
        a[43,10]=MTA[1]
    elif i == 5:
        a[49,10]=MTA[1]
    elif i == 6:
        a[54,10]=MTA[1]
    elif i == 7:
        a[58,10]=MTA[1]
    elif i == 8:
        a[61,10]=MTA[1]
    elif i == 9:
        a[63,10]=MTA[1]
    else:
        a[i+55,10]=MTA[1]

for i in range(12):
    a[66,i] = 1

#print(a)
#print("and now a test")
#a[1,5]=1
print(a)
#for i in range(12):
#    a[]
