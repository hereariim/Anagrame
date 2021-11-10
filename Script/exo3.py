# -*- coding: utf-8 -*-
"""
EX3 SCRIPT
"""
import timeit
import multiprocessing
import csv

class MyProcess(multiprocessing.Process):

    dico ={}

    def __init__(self,liste,num_task,q):
        multiprocessing.Process.__init__(self)
        self.L = liste
        self.n = num_task
        self.q = q

    def run(self):
        #Ranger les mots dans l'ordre alphabetique
        A = [''.join(sorted(word)) for word in self.L]

        #Affectation des mots en tant que clé
        for t in A:
            MyProcess.dico[t]=[]

        #Range les index à leur correspondant
        for index,t in enumerate(A):
            MyProcess.dico[t].append(self.L[index])

        with open(f'anagrame_{self.n}_lettre.csv','w') as f:
            write=csv.writer(f)
            write.writerows(MyProcess.dico.values())
        f.close()
        
        newV=[len(t) for t in MyProcess.dico.values()]

        from collections import Counter

        ens = list(Counter(newV).values())
        ana = list(Counter(newV).keys())
        #newens = [Counter(newV)[key] for key in sorted(ana)]
        self.q.put([ana,ens])
      


if __name__ == '__main__':
    with open('dico.txt.txt','r',encoding="UTF-8") as f:    
        stocker1 = []
        stocker2 = []
        stocker3 = []
        stocker4 = []
        stocker5 = []
        stocker6 = []
        stocker7 = []
        stocker8 = []
        stocker9 = []
        stocker10 = []
        stocker11 = []
        stocker12 = []
        stocker13 = []
        stocker14 = []
        stocker = []
        
        for ligne in f:
            mot = ligne[:-1]
            if len(mot)==1:
                stocker1.append(mot)
            elif len(mot)==2:
                stocker2.append(mot)
            elif len(mot)==3:
                stocker3.append(mot)
            elif len(mot)==4:
                stocker4.append(mot)
            elif len(mot)==5:
                stocker5.append(mot)
            elif len(mot)==6:
                stocker6.append(mot)
            elif len(mot)==7:
                stocker7.append(mot)
            elif len(mot)==8:
                stocker8.append(mot)
            elif len(mot)==9:
                stocker9.append(mot)
            elif len(mot)==10:
                stocker10.append(mot)
            elif len(mot)==11:
                stocker11.append(mot)
            elif len(mot)==12:
                stocker12.append(mot)
            elif len(mot)==13:
                stocker13.append(mot)
            elif len(mot)==14:
                stocker14.append(mot)
            else:
                stocker.append(mot)
    f.close()
    
    #print('Dico Téléchargé',end='\n')
    #print(
    #      [len(stocker1),len(stocker2),len(stocker3),len(stocker4),len(stocker5),len(stocker6),len(stocker7),len(stocker8),len(stocker9),len(stocker10),len(stocker)])

    D = [stocker1,stocker2,stocker3,stocker4,stocker5,stocker6,stocker7,stocker8,stocker9,stocker10,stocker11,stocker12,stocker13,stocker14,stocker]
    q=multiprocessing.Queue()
    tasks=[ MyProcess(L,D.index(L)+1,q) for L in D]
    start = timeit.default_timer()
    for i in tasks:
        i.start()

    for i in tasks:
        i.join()
    print('Terminé')
    print(round(timeit.default_timer()-start,2),'s')

    X = []
    while not q.empty():
        X.append(q.get(block=True))

    dico_anagram={}
    for I in X:
        for J in I[0]:
            if J not in dico_anagram.keys():
                dico_anagram[J]=0
    
    for I in X:
        for J in I[1]:
            dico_anagram[I[0][I[1].index(J)]]=dico_anagram[I[0][I[1].index(J)]]+J

    import pandas as pd
    tabv=pd.DataFrame(dico_anagram)
    print(tabv)

    print(round(timeit.default_timer()-start,2),'s')
