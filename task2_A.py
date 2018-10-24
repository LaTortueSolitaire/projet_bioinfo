import numpy as np
import matplotlib.pyplot as plt
import time
import pickle

start_time = time.clock()

fichier = open("MultiplexedSamples")
diction = dict()

print("Dictionnaire cree :\n")
compt = 1
for line in fichier:
    print("Ligne fichier : "+str(compt)+"\n")
    compteur = 51
    lane = line[0:len(line)-1]

    while(compteur >= 1):
        lone = lane[len(lane)-compteur:51]
        if lone in diction:
            diction[lone] = diction[lone] + 1
        else:
            diction[lone] = 1
        compteur = compteur - 1
    compt = compt +1

    # lone = lane[13:76]
    # if lone in diction:
    #     diction[lone] = diction[lone] + 1
    # else:
    #     diction[lone] = 1

# print("J'ecris le dico\n")
# file = open("dictio.txt", "wb")
# pickle.dump(diction, file)
# print("dico ecris\n")
fo = 0
tab_x = []
tab_max = []
tab_len = []
file = open("result_task4_adapter.txt", "w")

while(fo<100):
    max = 0
    adapter =""
    fo= fo +1
    tab_x.append(fo)
    for x, y in diction.items():
        if y >= max:
            max = y
            adapter = x
    tab_max.append(max)
    tab_len.append(len(adapter))
    strin = "\n"+str(fo)+" : "+adapter+"  - "+str(max)
    file.write(strin)
    print("\n"+str(fo))
    print("\n"+adapter+"\n"+str(max)+"\n")
    diction.pop(adapter)

fig, ax1 = plt.subplots()

ax1.plot(tab_x,tab_max,"r+-", label="occurancies")
ax1.legend(loc=0)
ax2 = ax1.twinx()
ax2.plot(tab_x,tab_len,"m+-", label="length")

print time.clock() - start_time, "seconds"
fichier.close()
file.close()
ax2.legend(loc=1)
plt.show()
