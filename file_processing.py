import numpy as np

GRASS = 10 
DESERT = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180

def color_map(fname):
    hyrule = np.loadtxt(fname, dtype= str,skiprows = 1)
    return hyrule


#    hyrulenew = np.empty_like(hyrule,dtype=int)
#    hyrulenew[hyrule == 'G'] = GRASS
#    hyrulenew[hyrule == 'D'] = DESERT
#    hyrulenew[hyrule == 'F'] = FLOREST
#    hyrulenew[hyrule == 'M'] = MOUNTAIN
#    hyrulenew[hyrule == 'W'] = WATER
#    hyrulenew[hyrule == 'L'] = 'L'# link posintion
#    hyrulenew[hyrule == 'S'] = 'S' # sword position
#    hyrulenew[hyrule == 'R'] = 'R'
#    hyrulenew[hyrule == 'E'] = 'E'
#    hyrulenew[hyrule == 'B'] = 'B'