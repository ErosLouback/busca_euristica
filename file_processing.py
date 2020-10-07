import numpy as np

GRASS = 10 
DESERT = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180

def color_map(fname):
    hyrule = np.loadtxt(fname, dtype= str,skiprows = 1)
    return hyrule

#    hyrulenew = np.empty_like(hyrule)
#    hyrulenew[hyrule == 'G'] = 'D'
#    hyrulenew[hyrule == 'D'] = 'D'
#    hyrulenew[hyrule == 'F'] = 'F'
#    hyrulenew[hyrule == 'M'] = 'M'
#    hyrulenew[hyrule == 'W'] = 'W'
#    hyrulenew[hyrule == 'L'] = 'L'
#    hyrulenew[hyrule == 'S'] = 'S'
#    hyrulenew[hyrule == 'R'] = 'R'
#    hyrulenew[hyrule == 'E'] = 'E'
#    hyrulenew[hyrule == 'B'] = 'B'