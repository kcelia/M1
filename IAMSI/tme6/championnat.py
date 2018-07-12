# -*- coding: utf-8 -*-
import os
import sys

ne = 3
ns = 2
nj = 2*ns

# Jour pair : mercredi / impair : dimanche

#### Exercice 2 ####
# --------------------

# Question 1 
# nb_var = (nj - 1) * ne**2 + (ne - 1) * ne + (ne - 1) + 1
# nb_var = nj * ne**2 - ne**2 + ne**2 - ne + ne -1 + 1
nb_var = nj * ne**2

# QUestion 2
def codage(j, x, y, ne):
	return j*ne**2 + x*ne + y + 1

# Question 3
def decodage(k, ne):
	k -= 1
	j= k // ne**2
	x = k // ne % ne # = k % ne**2 // ne
	y = k % ne
	return j, x, y


#j, x, y = 7, 0, 1 
#print("Codage de", j, x, y)
#k = codage(j, x, y, ne)
#print("v_i =", k)
#j, x, y = decodage(k, ne)
#print("Decodage :", j, x, y)

#### Exercice 3 ####
# --------------------
# Question 1
def au_moins_un(variables):
    """ list(int) -> str
        Retourne la clause associée à la contrainte "au moins une variable est
        vraie"
    """
    return " ".join(str(i) for i in variables) + " 0\n"

# Test
#print("Au moins un :\n", au_moins_un([1,2,3,4,5,6]))
    
def au_plus_un(variables):
    """ list(int) -> str
        Retourne l'ensemble des clauses associée à le contrainte "au plus une
        variable est vraie"
    """
    clauses = []
    for i, var1 in enumerate(variables):
        for var2 in variables[i+1:]: # Eviter les répétitions de combinaison 
            clauses.append("{} {} 0\n".format(str(-var1), str(-var2)))
    return "".join(clauses)
    
# Test
#print("Au plus un :\n", au_plus_un([1,2,3]))

# Question 2
#1
"""
C1 : " chaque équipe ne peut jouer plus d'un match par jour"
Pour chaque jour j, pour chaque équipe x : Somme_y { m_jxy + m_jyx } <= 1
On prend en compte les matchs à domicile et les matchs en extérieur
"""

# Comptage
def comptage(clauses):
    """Retourne le nombre de contraintes générées par ne equipes en nj jours 
    """
    return len(clauses.split("\n"))-1
#2
def encoderC1(ne, nj):
    c1 = []
    for j in range(nj):
        for x in range(ne):
            var = []
            for y in range(ne):
                if x != y:
                    var.append(codage(j, x, y, ne))
                    var.append(codage(j, y, x, ne))
            c1.append(au_plus_un(var))
    return "".join(c1)

#print(comptage(encoderC1(ne, nj)))
#print("Codage de C1 :\n", encoderC1(ne, nj))            

#3
"""
Nombre de clauses (au_plus_un) : nb_var * (nb_var - 1)/2
Nombre de clauses (C1) : nj * ne * 2(ne)*2(ne-1)/2 = 180
Nous décidons de supprimer les clauses avec la même équipe
Nombre de clauses (C1) : nj * ne * 2(ne-1)*(2(ne-1) - 1)/2 = 72
"""          

#4
"""
C2 : "Sur la durée du championnat, chaque équipe doit rencontrer une fois 
l'ensemble des autres équipes"
Pour chaque paire d'équipes (x, y), Somme_j {m_jxy} = 1 et Somme_j {m_jyx} = 1
"""

#5
def encoderC2(ne, nj):
    c2 = []
    for x in range(ne):
        for y in range(ne):
            if x != y:
                var = []
                for j in range(nj):
                    var.append(codage(j, x, y, ne))
                c2.append(au_moins_un(var) + au_plus_un(var))
    return "".join(c2)

#6
#print(comptage(encoderC2(ne, nj)))
#print("Codage de C2 :\n", encoderC2(ne, nj))  
"""
Nombre de clauses (au_moins_un) : 1
Nombre de clauses (C2) : ne * (ne-1) * (nj*(nj-1)/2 + 1) = 42
"""
#7

# Contrainte : pas de match avec une équipe contre elle même
def encoderC3(ne, nj):
    c3 = []
    for j in range(nj):
        for x in range(ne):
            c3.append("{} 0\n".format(-codage(j, x, x, ne)))
    return "".join(c3)
    
    
def encoder(ne,nj):
    """ Retroune l'encadage de toutes les contraintes C1 et C2    
    """
    return "{}{}{}".format(encoderC3(ne, nj), encoderC1(ne,nj), encoderC2(ne,nj))

#print(nb_clauses)
#print("Encodage C1 et C2 :\n", encoder(ne,nj))


# Question 3
def genere_cnf(ne, nj):
    """ int * int ->
        Génère un fichier cnf modélisant le probleme du chamionnat
    """
    nb_var = nj*ne**2
    clauses = encoder(ne, nj)
    nb_clauses = comptage(encoder(ne, nj))
    
    with open("championnat.cnf", "w+") as f:
        f.write("p cnf {} {}\n".format(str(nb_var), str(nb_clauses)))
        f.write(clauses)

"""
glucose nous renvoie insatisfiable, car les contraintes de l'énoncé ne
permettent pas de résoudre le problème à ce stade.
Effectivement, avec trois équipes, chaque équipe devra jouer exactement 4 matchs
(2 fois contre chaque équipe). Par conséquent, elle devra jouer tous les jours.
Or les 2 premiers jours, la troisième équipe ne pourra pas jouer puisque les deux
premières s'affrontent. La troisième équipe ne pourra donc pas jouer tous ses matchs.

Nombre de matchs total : ne! / (ne - 2)!
On constate qu'il faut 6 jours pour que le problème soit solvable
"""

def solve_glucose(infile="championnat.cnf", outfile="tmp_c.txt"):
    os.system("./glucose_static -model {} > {}".format(infile, outfile))


# Question 4
def check_sat(filename="tmp_c.txt"):
    with open(filename, "r") as f:
        lines = f.read().split("\n")
    res = lines[-2].split()
    if res[0] == "s":
        return False
    else:
        return res[1:]
        
        
def decoder(ne, file_result, file_equipes=None):
    """ FILENAME * FILENAME -> str
        Retourne le planning du championnat à partir du résultat obtenu par le 
        solveur glucose dans le fichier file_result
        file_equipes (optionnel) : noms des équipes
    """
    res = check_sat(file_result)
    # Satisfiabilité    
    if res == False:
        print("INSATISFIABLE")
        return ""
        
    # Equipes
    equipes = list(range(ne))
    if file_equipes != None:
        with open(file_equipes, "r") as f:
            equipes = f.read().split("\n")
    
    # Planning
    aff = "------ PLANNING -------\n"
    matchs = []
    for var in res:
        if int(var) > 0:
            j, x, y = decodage(int(var), ne)
            matchs.append("Jour {} : {} vs {}".format(j, equipes[x], equipes[y]))
    return aff + "\n".join(matchs)

def affiche_planning(ne, nj):
    genere_cnf(ne, nj)
    solve_glucose()
    print(decoder(ne, "tmp_c.txt", "equipes.txt"))
    
#### Exercice 5 ####
# --------------------
p_ext = 50
p_dom = 40

# Question 1
"""
# 1 (a, b)
Pour une équipe :
Nombre de matchs à jouer (ext + dom) le dimanche:
nb_matchs_eq = 2(ne-1)
Nombre de matchs devant être joués à l'extérieur AU MOINS :
nb_matchs_ext = [nb_matchs_eq * p_ext/100]
Nombre de matchs devant être joués à domicile AU MOINS :
nb_matchs_dom = [nb_matchs_eq * p_dom/100]


Pour chaque équipe x :
Avec j tel que j%2 = 1 (dimanche)
Somme_j {Somme_y { m_jyx }} >= nb_matchs_ext
Soit :
Somme_j {Somme_y { not m_jyx }} <= nb_matchs_eq - nb_matchs_ext



"""


         
def main():
    # Paramètres programme
    if len(sys.argv) == 3:
        ne, nj = int(sys.argv[1]), int(sys.argv[2])
    else:
        ne, nj = 3, 6
        print("*** Planning pour ne=3 et nj=6 ***")
        print("*** Precisez ne et nj sinon ***")
    # Affichage du planning
    affiche_planning(ne, nj)

          
        

if __name__ == '__main__':
    main()






