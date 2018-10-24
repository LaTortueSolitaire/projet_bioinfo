import numpy as np
from pylab import *
import time
import pickle

start_time = time.clock()

fichier = open("MultiplexedSamples")
diction4 = dict()
diction5 = dict()
diction6 = dict()
diction7 = dict()
diction8 = dict()

print("Dictionnaire cree :\n")
compt = 1
for line in fichier:
    print("Ligne fichier : "+str(compt)+"\n")
    compteur = 51
    lane = line[0:len(line)-1]

    # while(compteur >= 1):
    #     lone = lane[len(lane)-compteur:76]
    #     if lone in diction:
    #         diction[lone] = diction[lone] + 1
    #     else:
    #         diction[lone] = 1
    #     compteur = compteur - 1
    compt = compt +1

    lone = lane[47:51]
    if lone in diction4:
        diction4[lone] = diction4[lone] + 1
    else:
        diction4[lone] = 1

    lone = lane[46:51]
    if lone in diction5:
        diction5[lone] = diction5[lone] + 1
    else:
        diction5[lone] = 1

    lone = lane[45:51]
    if lone in diction6:
        diction6[lone] = diction6[lone] + 1
    else:
        diction6[lone] = 1

    lone = lane[44:51]
    if lone in diction7:
        diction7[lone] = diction7[lone] + 1
    else:
        diction7[lone] = 1

    lone = lane[43:51]
    if lone in diction8:
        diction8[lone] = diction8[lone] + 1
    else:
        diction8[lone] = 1

# print("J'ecris le dico\n")
# file = open("dictio.txt", "wb")
# pickle.dump(diction, file)
# print("dico ecris\n")

max = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0

adapter = ""
adapter2 = ""
adapter3 = ""
adapter4 = ""
adapter5 = ""

for x, y in diction4.items():
    if y > max:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = max
        adapter2 =adapter
        max = y
        adapter = x
    elif y > max2:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = y
        adapter2 = x
    elif y > max3:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = y
        adapter3 = x
    elif y > max4:
        max5 = max4
        adapter5 = adapter4
        max4 = y
        adapter4 = x
    elif y > max5:
        max5 = y
        adapter5 = x

print("pour 4 :\n")
print(adapter+"\n")
print(max)

print("\n"+adapter2+"\n")
print(max2)

print("\n"+adapter3+"\n")
print(max3)

print("\n"+adapter4+"\n")
print(max4)

print("\n"+adapter5+"\n")
print(max5)

x4 = [1,2,3,4,5]
y4 = [max,max2,max3,max4,max5]

plot(x4,y4,"g+-", label="len 4")

max = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0

adapter = ""
adapter2 = ""
adapter3 = ""
adapter4 = ""
adapter5 = ""

for x, y in diction5.items():
    if y > max:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = max
        adapter2 =adapter
        max = y
        adapter = x
    elif y > max2:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = y
        adapter2 = x
    elif y > max3:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = y
        adapter3 = x
    elif y > max4:
        max5 = max4
        adapter5 = adapter4
        max4 = y
        adapter4 = x
    elif y > max5:
        max5 = y
        adapter5 = x

print("pour 5 :\n")
print(adapter+"\n")
print(max)

print("\n"+adapter2+"\n")
print(max2)

print("\n"+adapter3+"\n")
print(max3)

print("\n"+adapter4+"\n")
print(max4)

print("\n"+adapter5+"\n")
print(max5)

x5 = [1,2,3,4,5]
y5 = [max,max2,max3,max4,max5]

plot(x5,y5,"m+-", label="len 5")

max = 0
adapter = ""
max2 = 0
adapter2 = ""
max3 = 0
adapter3 = ""
max4 = 0
adapter4 = ""
max5 = 0
adapter5 = ""

for x, y in diction6.items():
    if y > max:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = max
        adapter2 =adapter
        max = y
        adapter = x
    elif y > max2:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = y
        adapter2 = x
    elif y > max3:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = y
        adapter3 = x
    elif y > max4:
        max5 = max4
        adapter5 = adapter4
        max4 = y
        adapter4 = x
    elif y > max5:
        max5 = y
        adapter5 = x

print("pour 6 :\n")
print(adapter+"\n")
print(max)

print("\n"+adapter2+"\n")
print(max2)

print("\n"+adapter3+"\n")
print(max3)

print("\n"+adapter4+"\n")
print(max4)

print("\n"+adapter5+"\n")
print(max5)

x6 = [1,2,3,4,5]
y6 = [max,max2,max3,max4,max5]

plot(x6,y6,"y+-", label="len 6")

max = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0

adapter = ""
adapter2 = ""
adapter3 = ""
adapter4 = ""
adapter5 = ""

for x, y in diction7.items():
    if y > max:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = max
        adapter2 =adapter
        max = y
        adapter = x
    elif y > max2:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = y
        adapter2 = x
    elif y > max3:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = y
        adapter3 = x
    elif y > max4:
        max5 = max4
        adapter5 = adapter4
        max4 = y
        adapter4 = x
    elif y > max5:
        max5 = y
        adapter5 = x

print("pour 7 :\n")
print(adapter+"\n")
print(max)

print("\n"+adapter2+"\n")
print(max2)

print("\n"+adapter3+"\n")
print(max3)

print("\n"+adapter4+"\n")
print(max4)

print("\n"+adapter5+"\n")
print(max5)

x7 = [1,2,3,4,5]
y7 = [max,max2,max3,max4,max5]

plot(x7 ,y7 ,"b+-", label="len 7")

max = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0

adapter = ""
adapter2 = ""
adapter3 = ""
adapter4 = ""
adapter5 = ""

for x, y in diction8.items():
    if y > max:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = max
        adapter2 =adapter
        max = y
        adapter = x
    elif y > max2:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = max2
        adapter3 = adapter2
        max2 = y
        adapter2 = x
    elif y > max3:
        max5 = max4
        adapter5 = adapter4
        max4 = max3
        adapter4 = adapter3
        max3 = y
        adapter3 = x
    elif y > max4:
        max5 = max4
        adapter5 = adapter4
        max4 = y
        adapter4 = x
    elif y > max5:
        max5 = y
        adapter5 = x

print("pour 8 :\n")
print(adapter+"\n")
print(max)

print("\n"+adapter2+"\n")
print(max2)

print("\n"+adapter3+"\n")
print(max3)

print("\n"+adapter4+"\n")
print(max4)

print("\n"+adapter5+"\n")
print(max5)

x8 = [1,2,3,4,5]
y8 = [max,max2,max3,max4,max5]

plot(x8,y8,"k+-", label="len 8")

print time.clock() - start_time, "seconds"


legend()
show()
