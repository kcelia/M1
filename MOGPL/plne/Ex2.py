# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:27:27 2017

@author: 3309063
"""

import gurobipy as grb
import itertools as it
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
import time

def read_instance(path):
    f = open(path)
    s = []
    for line in f:
        if not line.startswith("#"):
            s.append([int(w) for w in line.split()])
        else:
            sl = s
            s = []
    sc = s

    return sl, sc

def init_vars(m, sl, sc):
    N = len(sl)
    M = len(sc)

    x = np.empty((N, M), dtype=object)

    for i, j in it.product(xrange(N), xrange(M)):
        x[i, j] = m.addVar(vtype=grb.GRB.INTEGER, lb=0, ub=1, name="x%d%d" % (i, j))

    y = np.empty((N,), dtype=object)

    for i, si in enumerate(sl):
        y[i] = np.empty((M, len(si)), dtype=object)
        right = M + 2 - sum(sit + 1 for sit in si)
        left = 0
        for t, sit in enumerate(si):
 #           for j in range(sum(si+1 for si in s[:t-1]), M - sum(si+1 for si in s[t-1:]) - 1):
            for j in xrange(left, right):
                y[i][j, t] = m.addVar(vtype=grb.GRB.INTEGER, lb=0, ub=1, name="y%d%d%d" % (i, j, t))
            right += (sit + 1)
            left += (sit + 1)

    z = np.empty((M,), dtype=object)

    for j, sj in enumerate(sc):
        z[j] = np.empty((N, len(sj)), dtype=object)
        right = N +2 - sum(sjt + 1 for sjt in sj)
        left = 0
        for t, sjt in enumerate(sj):
#            for i in range(sum(si+1 for si in s[:t-1]), N - sum(si+1 for si in s[t-1:]) -1 ):
            for i in xrange(left, right):
                z[j][i, t] = m.addVar(vtype=grb.GRB.INTEGER, lb=0, ub=1, name="z%d%d%d" % (i, j, t))
            right += (sjt + 1)
            left += (sjt + 1)

    obj = grb.LinExpr()
    obj = 0
    for i, j in it.product(xrange(len(sl)), xrange(len(sc))):
        obj += x[i, j]
    m.setObjective(obj, grb.GRB.MINIMIZE)

    m.update()

    return m, (x, y, z)

def add_constr(m, sl, sc, x, y, z):
    N = len(sl)
    M = len(sc)

    '''
    Dans chacune des boucles suivantes, left et right correspondent à une fenêtre où le bloc de l'itération courante
    peut être placé. cette fenêtre se décale vers la droite lorsqu'on regarde le bloc suivant
    '''

    #contraintes assurant que les cases suivants le début d'un bloc sont coloriés si elles doivent l'être
    for i, si in enumerate(sl):
        right = M + 2 - sum(sit + 1 for sit in si)
        left = 0
        for t, sit in enumerate(si):
            for j in xrange(left, right):
                m.addConstr(grb.quicksum(x[i, q] for q in xrange(j, j+sit)) >= (y[i][j, t] * sit))
            right += sit + 1
            left += sit + 1

    for j, sj in enumerate(sc):
        right = N + 2 - sum(sjt + 1 for sjt in sj)
        left = 0
        for t, sjt in enumerate(sj):
            for i in xrange(left, right):
                m.addConstr(grb.quicksum(x[q, j] for q in xrange(i, i+sjt)) >= (z[j][i, t] * sjt))
            right += sjt + 1
            left += sjt + 1

    for i, si in enumerate(sl):
        right = M + 2 - sum(sit + 1 for sit in si)
        left = 0
        for t, sit in enumerate(si):
            ct = grb.LinExpr()
            ct = 0
            for j in xrange(left, right):
                ct += y[i][j, t]
            m.addConstr(ct == 1)
            right += sit + 1
            left += sit + 1

    for j, sj in enumerate(sc):
        right = N + 2 - sum(sjt + 1 for sjt in sj)
        left = 0
        for t, sjt in enumerate(sj):
            ct = grb.LinExpr()
            ct = 0
            for i in xrange(left, right):
                ct += z[j][i, t]
            m.addConstr(ct == 1)
            right += sjt + 1
            left += sjt + 1

    #contraintes assurant que les blocs sont positionnés dans le bon ordre et ne se recouvrent pas
    for i, si in enumerate(sl):
        right = M + 2 - sum(sit + 1 for sit in si)
        left = 0
        for t, sit in enumerate(si[:-1]):
            for j in xrange(left, right):
                m.addConstr(grb.quicksum(y[i][q, t+1] for q in xrange(left + sit + 1, min(j + (sit + 1), right + sit + 1))) <= 1 - y[i][j, t])
            right += sit + 1
            left += sit + 1

    for j, sj in enumerate(sc):
        right = N + 2 - sum(sjt + 1 for sjt in sj)
        left = 0
        for t, sjt in enumerate(sj[:-1]):
            for i in xrange(left, right):
                m.addConstr(grb.quicksum(z[j][q, t+1] for q in xrange(left + sjt + 1, min(i + (sjt + 1), right + sit + 1))) <= 1 - z[j][i, t])
            right += sjt + 1
            left += sjt + 1

    m.update()

    return m

def add_extra_constr(model, sl, sc, x, y, z):
    N = len(sl)
    M = len(sc)

    for i, si in enumerate(sl):
        if len(si) <= 1:
            continue
        right = M + 2 - sum(sit + 1 for sit in si[1:])
        left = si[0] + 1
        for t, sit in zip(it.count(1), si[1:]):
            for j in xrange(left, right):
                model.addConstr(grb.quicksum(y[i][q, t-1] for q in xrange(j - sit - 1, min(j - sit - 1, right - sit - 1))) <= 1 - y[i][j, t])
            right += sit + 1
            left += sit + 1

    for j, sj in enumerate(sc):
        if len(sj) <= 1:
            continue
        right = N + 2 - sum(sjt + 1 for sjt in sj[1:])
        left = sj[0] + 1
        for t, sjt in zip(it.count(1), sj[1:]):
            for i in xrange(left, right):
                model.addConstr(grb.quicksum(z[j][q, t-1] for q in xrange(i - sjt - 1, min(i - sjt - 1, right - sjt - 1))) <= 1 - z[j][i, t])
            right += sjt + 1
            left += sjt + 1

    model.update()

    return model

def load_results(filename):
    return pkl.load(file(filename, 'rb'))

def array_solution(x):
    a = np.zeros(x.shape, dtype=int)
    for i, j in it.product(xrange(x.shape[0]), xrange(x.shape[1])):
        if x[i, j].x == 1.0:
            a[i, j] = 1
    return a

def affiche_solution(x):
    plt.figure()
    plt.imshow(array_solution(x), interpolation='nearest', cmap='gray_r')

def solve_plne(num_instance):
    sl, sc = read_instance("instances/%d.txt" % n)

    td = time.clock()
    m = grb.Model("mogplex")
    m, (x, y, z) = init_vars(m, sl, sc)
    m = add_constr(m, sl, sc, x, y, z)
    m = add_extra_constr(m, sl, sc, x, y, z)
    m.optimize()

    tf = time.clock()

    affiche_solution(x)
    plt.savefig('results/plne/t_instance_%d_%f.png'%(n, tf - td))

    return x

def solve_combined(num_instance):
    sl, sc = read_instance("instances/%d.txt" % n)

    td = time.clock()
    m = grb.Model("combined")
    m, (x, y, z) = init_vars(m, sl, sc)
    m = add_constr(m, sl, sc, x, y, z)

    B = load_results('results/combined/dyn_instance_%d.pkl' % n)

    add_constraints_from_results(B, m, x)

    m.optimize()

    tf = time.clock()

    affiche_solution(x)
    plt.savefig('results/combined/plne_instance_%d_%f.png'%(n, tf - td))

if __name__ == '__main__':
    plt.ioff()
    for n in range(0, 8):
        solve_plne(n)