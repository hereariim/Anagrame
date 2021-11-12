#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EX2 SCRIPT
"""
import timeit
import csv

start = timeit.default_timer()

with open('/usr/share/dict/words','r',encoding="UTF-8") as f:
    stocker = []
    for ligne in f:
        stocker.append(ligne[:-1])
f.close()

#Ranger les mots dans l'ordre alphabetique
A = [''.join(sorted(word)) for word in stocker]

dico ={}

#Affectation des mots en tant que clé
for t in A:
    dico[t]=[]

#Range les index à leur correspondant
for index,t in enumerate(A):
    dico[t].append(stocker[index])
    
import pandas as pd
newV = []
for t in dico.values():
    newV.append(len(t))
from collections import Counter,OrderedDict

dico = dict(Counter(newV))
dico_sort = dict(OrderedDict(sorted(dico.items())))

from tabulate import tabulate
M=[[k,dico_sort[k]] for k in dico_sort.keys()]
print(tabulate(M,headers=["Nombre d'Anagrame","Nombre d'ensemble"]))

with open(f'Anagrame_ensemble_ex2.csv','w',newline='') as f:
    write = csv.DictWriter(f, fieldnames=["Nombre d'Anagrame","Nombre d'ensemble"])
    write.writeheader()
    for k in dico_sort.keys():
        write.writerow({"Nombre d'Anagrame":k,"Nombre d'ensemble":dico_sort[k]})
f.close()

print("Temps total d'exécution",round(timeit.default_timer()-start,2),'s')
