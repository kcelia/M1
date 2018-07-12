# -*- coding: utf-8 -*-

#### Exercice 4 ####
# --------------------
from championnat import *
# Limite de temps 
import signal
import time


def find_min_j(ne):
    nj = 1
    while True:
        genere_cnf(ne, nj)
        solve_glucose()
        res = check_sat()
        if res != False:
            return nj
        nj += 1
         

def signal_handler(signum, frame):
    raise Exception("Time out!")


def optimize_nb_days():
    signal.signal(signal.SIGALRM, signal_handler)
    
    for ne in range(3,11):
        signal.alarm(30)   # (Ré)initialisation de l'alarme
        try:
            start = time.time()
            nj = find_min_j(ne)
            print("ne =", ne, ":", nj)
            end = time.time()
            print(end - start) 
        except Exception:
            print("ne =", ne, ":", "Time out!")

def main():
    optimize_nb_days()
    
"""    
ne = 3 : 6
ne = 4 : 6
ne = 5 : Time out!
ne = 6 : 10
ne = 7 : Time out!
ne = 8 : Time out!
ne = 9 : Time out!
"""   
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
