#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 09:33:11 2018

@author: rem
"""
from math import *
import time


#mismatch= 0
start_time = time.clock()

fichier = open("s_3_sequence_1M.txt")
adapter = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"
s_match = []



nb_line = 0

for line in fichier:
    nb_line +=1
    print(nb_line)

    compteur = 50
    lane = line[0:len(line)-1]

    while(compteur!=0):

        nb_mismatch = floor(0.1 * compteur)
        flag = 0
        for i in range(0,compteur):
            
            if (lane[len(lane)-compteur:50][i] !=adapter[0:compteur][i]) :
                nb_mismatch -= 1


        if(nb_mismatch >= 0 and flag == 0 ):
            flag = 1
            s_match.append(lane[len(lane)-compteur:50])
            
        compteur -= 1



#print(s_match)
print time.clock() - start_time, "seconds"
