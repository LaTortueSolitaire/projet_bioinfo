import numpy as np
from pylab import *
import time

start_time = time.clock()

fichier = open("s_3_sequence_1M.txt")
adapter = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"
s_match = []

for line in fichier:
    compteur = 50
    lane = line[0:len(line)-1]
    # print(compteur)
    while ( compteur!=0 and lane[len(lane)-compteur:50]!=adapter[0:compteur] ):
        compteur= compteur-1
    # print(compteur)
    if compteur!=0:
        s_match.append(lane[0:len(lane)-compteur])
    else:
        s_match.append(lane)

# print(s_match)
print("sequences trouvees "+str(len(s_match)))
print time.clock() - start_time, "seconds"

x = range(51)
y = [0]*51

for seq in s_match:
    y[len(seq)]= y[len(seq)]+1

plot(x,y,"+")

show()
