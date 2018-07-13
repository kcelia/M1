#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:46:46 2017

@author: 3309063
"""
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
import time

def read_instance(path):
    with open(path) as f:
        s = []
        for line in f:
            if line.startswith("#"):
                sl = s
                s = []
            else:
                s.append(tuple([int(i) for i in line.split()]))
    return sl, s

def affiche_solution(x):
    plt.figure()
    plt.imshow(x, interpolation='nearest', cmap='gray_r')


#-------------------------------------
def T(j, s):
    #cas l = 0
    if len(s) == 0:
        return True
    #cas l > 0
    #cas j < sl - 1
    if j < s[-1] - 1:
        return False
    # cas j = sl - 1
    if j == s[-1] - 1:
        #cas bloc unique et espace libre
        if len(s) == 1:
            return True
        #cas multiples blocs
        return False
    #cas j >= sl - 1
    return T(j - (s[-1] + 1), s[:-1])

#------------------------------------
def add_memory(func):
    mem = dict()
    def func_wrapper(j, s, B):
        key = (j, s, tuple(B))
        try:
            return mem[key]
        except KeyError:
            r = mem[key] = func(j, s, B)
            return r
    return func_wrapper

@add_memory
def T2(j, s, B):
    #cas l = 0
    if len(s) == 0:
        #case noire indésirable
        if 1 in B:
            return False
        return True
    #cas j < sl - 1
    if j < s[-1] - 1:
        return False
    #cas j = sl - 1
    if j == s[-1] - 1:
        if len(s) == 1 and 0 not in B:
            return True
        return False
    # cas j > sl - 1
    if B[j] == 1:
        if B[j - s[-1]] != 1 and 0 not in B[j - (s[-1] - 1):]:
            return T2(j - (s[-1] + 1), s[:-1], B[: - (s[-1] + 1)])
        return False
    if B[j] == 0:
        return T2(j - 1, s, B[:-1])
    if B[j - s[-1]] != 1 and 0 not in B[j - (s[-1] - 1):]:
        return T2(j - (s[-1] + 1), s[:-1], B[: - (s[-1] + 1)]) or T2(j-1, s, B[:-1])
    return T2(j-1, s, B[:-1])


def propagate(sl, sc, B=None):
    nblig = len(sl)
    nbcol = len(sc)
    if B is None:
        B = np.ones((nblig, nbcol)) * -1

    def test_lig(lig):
        return T2(nbcol-1, sl[lig], B[lig, :])
    def test_col(col):
        return T2(nblig-1, sc[col], B[:, col])

    for lig in range(nblig):
        try:
            assert test_lig(lig)
        except AssertionError:
            print(sl[lig], B[lig, :])

    for col in range(nbcol):
        try:
            assert test_col(col)
        except AssertionError:
            print(sc[col], B[:, col])

    def test_case(i, j):
#        print("Testing", i, j)
        if B[i, j] != -1:
            return B[i, j]
        B[i, j] = 1
        bl, wh = 1, 1
        if not (test_lig(i) and test_col(j)):
            bl = 0
        B[i, j] = 0
        if not (test_lig(i) and test_col(j)):
            wh = 0

        if wh and bl:
            B[i, j] = -1
        elif bl:
            B[i, j] = 1
        elif wh:
            B[i, j] = 0
        else:
            print("Erreur pas de solution")

    ligs = set(range(nblig))
    cols = set(range(nbcol))

    while len(ligs) != 0:
        for i in ligs:
            for j in range(nbcol):
#                print(i, j)
#                print(B)
                if B[i, j] == -1:
                    test_case(i, j)
                    if B[i, j] != -1:
                        cols.add(j)
        ligs = set()
        for j in cols:
            for i in range(nblig):
#                print(i, j)
#                print(B)
                if B[i, j] == -1:
                    test_case(i, j)
                    if B[i, j] != -1:
                        ligs.add(i)
        cols = set()

    return B

def save_results(filename, B):
    pkl.dump(B, open(filename, 'wb'), protocol=2)
    
def solve_dynamique(num_instance):
    sl, sc = read_instance("instances/{}.txt".format(n))

    td = time.process_time()
    B = propagate(sl, sc)
    tf = time.process_time()
    
    affiche_solution(B)
    plt.savefig("results/prog_dynamique/instance_{}_{}.png".format(n, tf - td))

def solve_combined(num_instance):
    sl, sc = read_instance("instances/{}.txt".format(n))
    
    td = time.process_time()
    B = propagate(sl, sc)
    tf = time.process_time()
    
    affiche_solution(B)
    plt.savefig("results/combined/dyn_instance_{}_{}.png".format(n, tf - td))
    save_results("results/combined/dyn_instance_{}.pkl".format(n), B)    

if __name__ == '__main__':
    import cProfile

    p = cProfile.Profile()

    plt.ioff()
    
    for n in range(11, 17):
        solve_combined(n)
