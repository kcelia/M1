# -*- coding: utf-8 -*-

""" COMMANDE TERMINAL """
""" aspplan_min.py DOMAINEFILE PROBLEMFILE """

FILE_clingo = 'clingo-4.5.4-linux-x86_64/clingo'


from asp_strips import planASP
import sys
import os


def findMinPlan(domaineFile, problemFile, clingoFile):
    """ str -> int * str 
        Retourne n minimal et le plan minimal
    """
    
    n = 1
    ok = False
    aspPlan = planASP(domaineFile, problemFile, n)
    
    while not ok and n<50:
        ## On ne cherche qu'à modifier n
        ## dans le fichier résultat    
        aspPlan = aspPlan.split("\n")
        ind = list(map(lambda x: x.startswith("#const"),aspPlan)).index(True)
        aspPlan[ind] = "#const n={}.".format(n)
        aspPlan = "\n".join(aspPlan)
        
        # Ecriture sur fichier temporaire
        with open("tmp_plan.lp", "w") as f:
            f.write(aspPlan)
        # Lancement du programme
        os.system("{} tmp_plan.lp > tmp_planres.txt".format(clingoFile))
        
        # Lecture du resultat
        with open("tmp_planres.txt", "r") as f:
            resultat = f.read().split("\n")
        # 10 : nombre d'elements lorsque c'est insatisfiable ou erreur
        if len(resultat) > 10:
            answer = "\n".join(resultat[4].split(" "))
            return n, answer

        n += 1
        
        
def main():
    if len(sys.argv) > 2:
        FILE_domain = sys.argv[1]
        FILE_problem = sys.argv[2]
    else:
        FILE_domain = "singe_bananes-domain.pddl"
        FILE_problem = "singe_bananes-problem.pddl"
    
    n, res = findMinPlan(FILE_domain, FILE_problem, FILE_clingo)
    print("n_minimal =", n)
    print(res)
    

if __name__ == '__main__':
    main()
