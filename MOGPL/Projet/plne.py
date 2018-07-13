# -*- coding: utf-8 -*-

from gurobipy import *
import numpy as np
import matplotlib.pyplot as plt
from dynamique import *
from time import clock


def resolution_PLNE(seq_r, seq_c, A=[], display=True):
    N, M = len(seq_r), len(seq_c)

    lignes = list(range(N))
    colonnes = list(range(M))
    
    m = Model("mogplex")     
    
    BLACK = 1  # case noire
    WHITE = -1  # case blanche
    IND = 0  # case indéterminée

    # Declaration et initialisation des variables de decision
    if A:
        x = []
        for i in lignes:
            tmp = []
            for j in colonnes:
                if A[i][j] == IND:
                    tmp.append(m.addVar(vtype=GRB.BINARY, name="x_%d%d" % (i, j)))
                elif A[i][j] == WHITE:
                    tmp.append(0)
                else:
                    tmp.append(1)
            x.append(tmp)

    else:
        x = [[m.addVar(vtype=GRB.BINARY, name="x_%d%d" % (i, j)) for j in colonnes] for i in lignes]
    y = []
    z = []


    for i in lignes:
        tmp_y, tmp_z = [], []
        for j in colonnes:
            tmp_2_y, tmp_2_z = [], []
            for t in range(len(seq_r[i])):
                if (j < sum(seq_r[i][:t]) + len(seq_r[i][:t])) or (j > M - (sum(seq_r[i][t:]) + len(seq_r[i][t+1:]))):
                    tmp_2_y.append(0)
                else:
                    tmp_2_y.append(m.addVar(vtype=GRB.BINARY, name="y_%d_%d%d" % (t+1, i, j)))
            for t in range(len(seq_c[j])):
                if (i < sum(seq_c[j][:t]) + len(seq_c[j][:t])) or (i > N - (sum(seq_c[j][t:]) + len(seq_c[j][t+1:]))):
                    tmp_2_z.append(0)
                else:
                    tmp_2_z.append(m.addVar(vtype=GRB.BINARY, name="z_%d_%d%d" % (t+1, i, j)))
            tmp_y.append(tmp_2_y)
            tmp_z.append(tmp_2_z)
        y.append(tmp_y)
        z.append(tmp_z)

    # Maj du modele pour integrer les nouvelles variables
    m.update()
    
    # Formulation de  la fonction objectif
    obj = LinExpr();
    obj = 0
    for x_i in x:
        for x_i_j in x_i:
            obj += x_i_j
    
    # Definition de l'objectif
    m.setObjective(obj,GRB.MINIMIZE) 
    
    # Definition des contraintes
    # Un bloc ne commence qu'à une seule case dans une ligne : somme des y_ijt = 1
    
    for i in lignes:
        for t in range(len(seq_r[i])):
            m.addConstr(quicksum(y[i][j][t] for j in colonnes) == 1, "Cons")

    for j in colonnes:
        for t in range(len(seq_c[j])):
            m.addConstr(quicksum(z[i][j][t] for i in lignes) == 1, "Cons")

    # ----------------------------------------------------------------
    # Dans chaque ligne, il y a autant de cases noires que la somme de la taille des blocs

    for i in lignes:
        m.addConstr(quicksum(seq_r[i][t] for t in range(len(seq_r[i]))) - quicksum(x[i][j] for j in colonnes) == 0, "Cons")
    for j in colonnes:
        m.addConstr(quicksum(seq_c[j][t] for t in range(len(seq_c[j]))) - quicksum(x[i][j] for i in lignes) == 0, "Cons")

    # ----------------------------------------------------------------
    # Si y_ijt = 1, alors la somme des x_ij des cases de j à j + st est égal à st * y_ijt
    
    for i in lignes:
        for t in range(len(seq_r[i])):
            for j in colonnes:
                m.addConstr(seq_r[i][t]*y[i][j][t] - quicksum(x[i][k] for k in colonnes[j:(j+seq_r[i][t])]) <= 0, "Cons")

    for j in colonnes:
        for t in range(len(seq_c[j])):
            for i in lignes:
                m.addConstr(seq_c[j][t]*z[i][j][t] - quicksum(x[k][j] for k in lignes[i:(i+seq_c[j][t])]) <= 0, "Cons")

    # ----------------------------------------------------------------
    # Si y_ijt = 1 alors les y_ijt des cases (i, 0) jusqu'à (i, j + st + 1) valent 0

    for i in lignes:
        for t in range(len(seq_r[i])-1):
            for j in colonnes:
                m.addConstr(y[i][j][t] + quicksum(y[i][k][t+1] for k in colonnes[:j + seq_r[i][t] + 1]) <= 1, "Cons")

    for j in colonnes:
        for t in range(len(seq_c[j])-1):
            for i in lignes:
                m.addConstr(z[i][j][t] + quicksum(z[k][j][t+1] for k in lignes[:i + seq_c[j][t] + 1]) <= 1, "Cons")

    # -----------------------------------------------------------------
    # x_ij est toujours superieur a y_ijt ou z_ijt
    
    for i in lignes:
        for t in range(len(seq_r[i])):
            for j in colonnes:
                m.addConstr(x[i][j] - y[i][j][t] >= 0, "Cons")

    for j in colonnes:
        for t in range(len(seq_c[j])):
            for i in lignes:
                m.addConstr(x[i][j] - z[i][j][t] >= 0, "Cons")
    
    # -----------------------------------------------------------------
    # Si y_ijt vaut 1 alors la variable x_i(j+st) vaut 0
    
    for i in lignes:
        for t in range(len(seq_r[i])):
            for j in colonnes:
                b = j + seq_r[i][t]
                if b < M:
                    m.addConstr(y[i][j][t] + x[i][b] <= 1, "Cons")

    for j in colonnes:
        for t in range(len(seq_c[j])):
            for i in lignes:
                b = i + seq_c[j][t]
                if b < N:
                    m.addConstr(z[i][j][t] + x[b][j] <= 1, "Cons")
    
    # ----------------------------------------------------
    # Le nombre de cases blanches est supérieur ou egal a la longueur de la sequence - 1
    
    for i in lignes:
        m.addConstr(M - quicksum(x[i][j] for j in colonnes) >= len(seq_r[i]) - 1, "Cons")

    for j in colonnes:
        m.addConstr(N - quicksum(x[i][j] for i in lignes) >= len(seq_c[j]) - 1, "Cons")
    
    # ----------------------------------------------------
    # Pour chaque ligne, la somme des y_ijt = nombre de blocs dans la séquenece associée

    for i in lignes:
        m.addConstr(quicksum(quicksum(y[i][j][t] for j in colonnes) for t in range(len(seq_r[i]))) == len(seq_r[i]), "Cons")

    for j in colonnes:
        m.addConstr(quicksum(quicksum(z[i][j][t] for i in lignes) for t in range(len(seq_c[j]))) == len(seq_c[j]), "Cons")
    
    # ---------------------------------------------------




    # Resolution
    m.optimize()

    print("")      
    print('Solution optimale:')
    print ("")
    print ('Valeur de la fonction objectif :', m.objVal)

    # Affichage matrice
    if display:
        aff_x = []
        for i, xi in enumerate(x):
            tmpx = []
            for j, xij in enumerate(xi):
                try:
                    tmpx.append(xij.x)
                except:
                    tmpx.append(xij)
            aff_x.append(tmpx)
        aff_x = np.array(aff_x)

        plt.imshow(aff_x, interpolation="nearest", cmap="Greys")
        plt.show()


def resolution_globale(filename, display=True):
    res, seq_r, seq_c = propagation(filename, False)
    resolution_PLNE(seq_r, seq_c, list(res), display)


if __name__ == '__main__':
    i = 16
    for i in range(i,i+1):
        seq_r, seq_c = lecture_sequences("instances/"+str(i)+".txt")
        #resolution_PLNE(seq_r, seq_c)
        start = clock()
        resolution_globale("instances/"+str(i)+".txt", False)
        end = clock() - start
        print("Temps exec - instance", i ,": ", end)