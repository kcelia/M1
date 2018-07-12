# -*- coding: utf-8 -*-

from parserPDDL import PDDLToASP


def planASP(domainFile, problemFile, n):
    # Chargement du résultat des fichiers parsés
    parsedRes = PDDLToASP(domainFile, problemFile)
    
    res = []
    res.append("%Planificateur STRIPS en ASP")
    
    res.append("#const n={}.".format(n))
    res.append("time(0..n).\n")
    
    # Etat initial
    res.append("holds(P, 0) :- init(P).")
    # Préconditions
    res.append("1{perform(A, T) : action(A)} :- time(T), T!=n.")
    res.append(":- perform(A, T), not holds(P, T), pre(A, P), time(T), pred(P), action(A).")
    # Effets positifs
    res.append("holds(P, T+1) :- perform(A, T), add(A, P), time(T), pred(P), action(A).")
    # Inertie et effets négatifs
    res.append("holds(P, T+1) :- holds(P, T), not del(A, P), perform(A, T), time(T), pred(P), action(A).")
    # Choix d'action
    res.append(":- perform(A1, T), perform(A2, T), time(T), action(A1), action(A2), A1!=A2.")
    # Spécification du but
    res.append(":- not holds(P, n), but(P), pred(P).\n")
    # Test
    res.append("#show perform/2.")
    
    res = "\n".join(res)
    return "\n\n".join([parsedRes, res])



if __name__ == '__main__':
    FILE_domain = "singe_bananes-domain.pddl"
    FILE_problem = "singe_bananes-problem.pddl"
    FILE_asp = "aspplan2.lp"
    
    n = 4
    res = planASP(FILE_domain, FILE_problem, n)
    print(res)
    
    #with open(FILE_asp, "w") as f:
    #    f.write(res)