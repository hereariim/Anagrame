import timeit

start = timeit.default_timer()

with open('dico.txt.txt','r',encoding="UTF-8") as f:
    
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
from collections import Counter
ens = list(Counter(newV).values())
ana = list(Counter(newV).keys())
newens = [Counter(newV)[key] for key in sorted(ana)]
tabv={'nombre densemble':newens,'nombre danagrame dans cette ensemble':sorted(ana)}      
tabv=pd.DataFrame(tabv)
print(tabv) 

print(round(timeit.default_timer()-start,2),'s')
