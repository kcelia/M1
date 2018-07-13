# -*- coding: utf-8 -*-

from matplotlib.pyplot import show, imshow
import numpy as np
from gurobipy import *

FILENAME = "instances/0.txt"



BLACK = 1  # case noire
WHITE = -1  # case blanche
IND = 0  # case indéterminée


def memoize(f):
    memo = {}
    def helper(*args):
        ind = tuple(args)
        if not ind in memo.keys():
            memo[ind] = f(*args)
        return memo[ind]
    return helper



def lecture_sequences(filename):
    # lecture du fichier
    with open(filename, "r") as f:
        file = f.read()
        lines = file.split("\n")
    sep = lines.index("#")
    # creation des listes de sequences
    seq_r, seq_c = [], []
    for sr in lines[:sep]:
        seq_r.append([int(i) for i in sr.split(" ") if i])
    for sc in lines[sep + 1:-1]:
        seq_c.append([int(j) for j in sc.split(" ") if j])
    return seq_r, seq_c

#@memoize
def T(l_i, seq):
    @memoize
    def mini_T(j, l):
        # Cas : l >= 0 (fréquent)
        if l:
            sl = seq[l-1]
            # Cas : j > sl - 1
            if j > sl - 1:
                # On vérifie la presence d'une case blanche dans les sl dernieres cases
                ind = j - sl + 1
                try:
                    b = l_i[ind:j+1].index(-1) + ind
                    # S'il y en a une, on vérifie la presence d'une case noire apres
                    # la case blanche -> faux
                    # Sinon on enlève à j toutes les cases apres la case blanche (incluse)
                    # et on rappelle avec la meme sequence
                    return not (BLACK in l_i[b+1:j+1]) and mini_T(b-1, l)
                except Exception:
                    # Est-ce que la case avant les sl cases n'est pas noire ? Oui : On passe a la suite
                    # Sinon est-ce que la derniere case de j est noire ? Oui : Faux
                    # Sinon on reteste en enlevant la derniere case de j
                    return ((l_i[ind-1] != BLACK) and mini_T(ind-2, l-1))\
                        or ((l_i[j] != BLACK) and mini_T(j-1, l))
            # Cas : j < sl - 1
            elif j < sl - 1:
                    return False
            # Cas : j = sl - 1
            else:
                # Est-ce le dernier bloc ET est-ce qu'il n'y a pas de case blanche ?
                return (l == 1) and not(WHITE in l_i[:j+1])
        # Cas : l = 0
        else:
            return not (BLACK in l_i[:j+1])
            
    return mini_T(len(l_i)-1, len(seq))



def coloration(A, seq_r, seq_c):
    grille = np.array(A)
    len_r, len_c = len(A), len(A[0])
    rows, cols = set(range(len_r)), set(range(len_c))
    k = 0 # Condition d'arrêt en cas de grille impossible
    while (rows or cols) and k < 35:
        k += 1
        for i in rows:
            tmp = list(grille[i])
            for j in range(len_c):
                if tmp[j] == IND:
                    tmp[j] = WHITE
                    blanc = T(tuple(tmp), tuple(seq_r[i]))
                    tmp[j] = BLACK
                    noir = T(tuple(tmp), tuple(seq_r[i]))
                    if blanc and noir:
                        tmp[j] = IND
                    else:
                        if blanc:
                            tmp[j] = WHITE
                        elif noir:
                            tmp[j] = BLACK
                        else:
                            return grille
                    cols.add(j)
                    grille[i][j] = tmp[j]
        rows = set()
        for j in cols:
            tmp = [grille[i][j] for i in range(len_r)]
            for i in range(len_r):
                if tmp[i] == IND:
                    tmp[i] = WHITE
                    blanc = T(tuple(tmp), tuple(seq_c[j]))
                    tmp[i] = BLACK
                    noir = T(tuple(tmp), tuple(seq_c[j]))
                    if blanc and noir:
                        tmp[i] = IND
                    else:
                        if blanc:
                            tmp[i] = WHITE
                        elif noir:
                            tmp[i] = BLACK
                        else:
                            return grille
                    rows.add(i)
                    grille[i][j] = tmp[i]
        cols = set()
    return grille


def propagation(filename):
    # lecture des sequences dans le fichier
    seq_r, seq_c = lecture_sequences(filename)
    # creation de la matrice
    mat = np.zeros((len(seq_r), len(seq_c)))
    # coloration de la grille
    res = coloration(mat, seq_r, seq_c)
    # affichage
    imshow(res, interpolation="nearest", cmap="Greys")
    show()

    return res


# -------------------------------------------

if __name__ == '__main__':
    import time

    for i in range(1):
        start = time.clock()
        propagation("instances/"+str(i)+".txt")
        end = time.clock() - start
        print "Temps exec - instance ", i, " : ", end