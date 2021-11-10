# -*- coding: utf-8 -*-
"""
EX1 SCRIPT
"""
import timeit

start = timeit.default_timer()

#Your statements here

def annagrame(a,b):
    return sorted(a)==sorted(b)

with open('dico.txt.txt','r',encoding="UTF-8") as f:
    
    stocker = []
    for ligne in f:
        stocker.append(ligne[:-1])
    
    ligne = stocker[0]
    T = stocker.copy() #T est la liste stocker
    T.remove(ligne) #ligne est effacé de T
    dico = {}
    K=[]
    V=[]
    while True:
        newT = T.copy() #liste de la nouvelle liste prochaine
        temp=[]
        for t in T:
            if annagrame(ligne, t):
                temp.append(t)
                newT.remove(t)
        #temp les anagrames
        #newT liste mis à jour
        K.append(ligne)
        V.append(','.join(temp))
        
        
        print(round(timeit.default_timer() - start,2),' | ',round(100*(len(stocker)-len(T))/len(stocker),2),'%')
        T=newT.copy() #T est la liste newT (ancienne T effacé)
        if len(T)!=0:
            ligne = T[0]
            T.remove(ligne)
f.close()   

     
dico={'mot':K,'anagrame':V}
import pandas as pd
tab=pd.DataFrame(dico)
print(tab)     
 
newV = []
for t in V:
    newV.append(len(t.split(',')))
from collections import Counter
ens = list(Counter(newV).values())
ana = list(Counter(newV).keys())
newens = [Counter(newV)[key] for key in sorted(ana)]
tabv={'nombre densemble':newens,'nombre danagrame dans cette ensemble':sorted(ana)}      
tabv=pd.DataFrame(tabv)
print(tabv) 

