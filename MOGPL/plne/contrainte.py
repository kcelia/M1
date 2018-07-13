# -*- coding: utf-8 -*-

from gurobipy import *
import numpy as np
import matplotlib.pyplot as plt



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
    


def resolution(seq_r, seq_c):
    N, M = len(seq_r), len(seq_c)
    
    # Range of plants and warehouses
    """
    lignes = 0
    colonnes = 0
    
    # Matrice des contraintes
    
    
    # Second membre
    	    
    b = 0
    
    # Coefficients de la fonction objectif
    c = []
    """
    m = Model("mogplex")     
            
    # declaration variables de decision
    x = []
    y = []
    z = []
    
    #liste des variables x1,x2 de type continue, reelles
    for i in range(N):
        tmp_x = []
        tmp_y, tmp_z = [], []
        for j in range(M):
            tmp_2_y, tmp_2_z = [], []
            
            tmp_x.append(m.addVar(vtype=GRB.CONTINUOUS, lb=0, ub=1, name="x_%d%d" % (i+1, j+1)))
            for t in range(len(seq_r[i])):
                tmp_2_y.append(m.addVar(vtype=GRB.CONTINUOUS, lb=0, ub=1, name="y_%d_%d%d" % (t+1, i+1, j+1)))
            for t in range(len(seq_c[j])):
                tmp_2_z.append(m.addVar(vtype=GRB.CONTINUOUS, lb=0, ub=1, name="z_%d_%d%d" % (t+1, i+1, j+1)))
            tmp_y.append(tmp_2_y)
            tmp_z.append(tmp_2_z)
        x.append(tmp_x)
        y.append(tmp_y)
        z.append(tmp_z)
        
    # maj du modele pour integrer les nouvelles variables
    m.update()
    
    # formuler la fonction objectif
    obj = LinExpr();
    obj = 0
    for x_i in x:
        for x_i_j in x_i:
            obj += x_i_j
            
    # definition de l'objectif
    m.setObjective(obj,GRB.MAXIMIZE) 
    
    # Definition des contraintes
    
    for i in range(N):
        for t in range(len(seq_r[i])):
            m.addConstr(quicksum([y[i][j][t] for j in range(M)]) <= 1, "Contrainte 1.1 %d %d %d" % (i,j,t))
    
    for j in range(M):
        for t in range(len(seq_c[j])):
            m.addConstr(quicksum([z[i][j][t] for i in range(N)]) <= 1, "Contrainte 1.2 %d %d %d" % (i,j,t))
    
    
    for i in range(N):
        for t in range(len(seq_r[i])-1):
            m.addConstr(quicksum([y[i][j][t] + \
            quicksum([y[i][k][t+1] for k in range(j + seq_r[i][t])])\
            for j in range(M)]) <= 1, "Contrainte 2.1 %d %d %d" % (i,j,t))
    
    for j in range(M):
        for t in range(len(seq_c[j])-1):
            m.addConstr(quicksum([z[i][j][t] + \
            quicksum([z[k][j][t+1] for k in range(i + seq_c[j][t])])\
            for i in range(N)]) <= 1, "Contrainte 2.2 %d %d %d" % (i,j,t))
    
    for i in range(N):
        for t in range(len(seq_r[i])):
            for j in range(M):
                try:
                    m.addConstr(seq_r[i][t] * y[i][j][t] - quicksum(x[i][k] for k in range(j, j + seq_r[i][t] - 1)) <= 0,\
                 "Contrainte 3.1 %d %d %d" % (i,j,t))
                except Exception:
                    continue
    
    for j in range(M):
        for t in range(len(seq_c[j])):
            for i in range(N):
                m.addConstr(seq_c[j][t] * z[i][j][t] - quicksum(x[k][j] for k in range(i, i + seq_c[j][t] - 1)) <= 0,\
                 "Contrainte 3.2 %d %d %d" % (i,j,t))
    
    for i in range(N):
        m.addConstr(quicksum(seq_r[i][t] for t in range(len(seq_r[i]))) - quicksum(x[i][j] for j in range(M)) == 0 , "Cons")

    for j in range(M):
        m.addConstr(quicksum(seq_c[j][t] for t in range(len(seq_c[j]))) - quicksum(x[i][j] for i in range(N)) == 0 , "Cons")

    # Resolution
    m.optimize()

    print ""                
    print 'Solution optimale:'
    print ""
    print 'Valeur de la fonction objectif :', m.objVal

    #Affichage matrice
    aff_x = []
    for i, xi in enumerate(x):
        tmpx = []
        for j, xij in enumerate(xi):
            tmpx.append(xij.x)
        aff_x.append(tmpx)
    aff_x = np.array(aff_x)
    plt.imshow(aff_x, interpolation="nearest", cmap="Greys")
    plt.show()

#[[1,1], [2]], [[2], [1], [1]]
n, m = lecture_sequences("instances/0.txt")
resolution(n, m)
