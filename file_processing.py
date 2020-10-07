import numpy as np
# LINK
# 
#
#
#
#
#
#
GRASS = 10 
DESERT = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180
"""LINK 6
SWORD 7
RED 8
EMERALD 9
BLUE 0
"""
hyrule = np.loadtxt("hyrule.txt", dtype='int', skiprows=1)
hyrule2 = [['+' for j in range(42)] for i in range(42)]
i =j = 0
for row in hyrule:
    for col in row:
        if col==1:
            hyrule2[i][j]='G'
        elif col==2:
            hyrule2[i][j] = 'D'
        elif col==3:
            hyrule2[i][j] = 'F'
        elif col==4:
            hyrule2[i][j] = 'M'
        elif col==5:
            hyrule2[i][j] = 'W'
        elif col==6:
            hyrule2[i][j] = 'L'
        elif col==7:
            hyrule2[i][j] = 'S'
        elif col==8:
            hyrule2[i][j] = 'R'
        elif col==9:
            hyrule2[i][j] = 'E'
        else:
            hyrule2[i][j] = 'B'
        j++1
    i=+1

np.savetxt("hyrule2.txt",hyrule2, fmt='%-0.1s', delimiter=' ', header='Grama=G,Areia=D,Floresta=F,Montanha=M,Agua=A,Link=L,Espada=S,Três pingentes=REB')
print(input)
