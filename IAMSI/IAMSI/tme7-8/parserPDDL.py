# -*- coding: utf-8 -*-
"""
VERSION 1 DU PARSEUR PDDL TO ASP
Premier essai - /!\ Code optimisable /!\
Hypothèse : PDDL typé
"""

import re
from pyparsing import OneOrMore, nestedExpr


def parseAction(elem):
    action = {"name": elem[1], \
                "parameters": [], \
                "pre": [], \
                "add": [], \
                "del": [] \
                      }
                      
    varfunc = lambda x: x[1:].upper() if x[0]=='?' else x               
                    
    for i in range(2, len(elem[2:])+1, 2):
        
        ## Parse parameters
        if elem[i] == ':parameters':
            tmp = elem[i+1]
            for i in range(0, len(tmp), 3):
                t = tmp[i+2]
                action["parameters"].append((tmp[i][1:].upper(), t))
                
        ## Parse preconditions
        elif elem[i] == ':precondition':
            tmp = elem[i+1]
            if tmp[0] == 'and':
                for p in tmp[1:]:
                    action["pre"].append(list(map(varfunc, p)))
            else:
                action["pre"].append(list(map(varfunc, tmp)))
                
        ## Parse effects
        elif elem[i] == ':effect':
            tmp = elem[i+1]
            if tmp[0] == 'and':
                for effect in tmp[1:]:
                    if effect[0] == 'not':
                        action["del"].append(list(map(varfunc, effect[1])))
                    else:
                        action["add"].append(list(map(varfunc, effect)))    
            else:
                if tmp[0] == 'not':
                    action["del"].append(list(map(varfunc, tmp[1])))
                else:
                    action["add"].append(list(map(varfunc, tmp[0])))
    
    return action
                

def parsePDDLDomain(filename):
    """ filename -> dictionnaire du fichier parsé
        Parseur pour un domaine PDDL
        Hypothèse : fichier PDDL bien constitué
    """
    #--------------------------------
    with open(filename, "r") as file:
        f = file.read()
    # remplace tous les \n et \t, excès d'espaces 
    # et commentaires par un espace
    elems = re.sub(r'(;;;.*\n)', " ", f)   
    # Transformation en tableau grace au parseur LISP
    elems = OneOrMore(nestedExpr()).parseString(elems)
    
    #--------------------------------
    preds, actions = [], []
    heriTypes = {}
    consts = {}
    name = str()
    
    #--------------------------------
    for elem in elems[0]:
        ### Domaine
        if elem[0] == 'domain':
            name = elem[1]
            
        ### Types            
        elif elem[0] == ':types':
            tmp = []
            for i, o in enumerate(elem[1:]):
                if o != '-':
                    if elem[i] != '-':
                        tmp.append(o)
                    else:
                        if o not in heriTypes:
                            heriTypes[o] = []
                        heriTypes[o].extend(tmp)
                        tmp = []
                        
        ### Prédicats
        elif elem[0] == ':predicates':
            for pred in elem[1:]:
                op = pred[0]
                params = []
                if len(pred) > 1:
                    # si definition de type alors len % 3 = 0
                    for i in range(1, len(pred[1:])+1, 3):
                        params.append((pred[i][1:].upper(), pred[i+2]))
                preds.append((op, params))
        ### Constantes
        elif elem[0] == ':constants':
            for i in range(1, len(elem[1:])+1, 3):
                t = elem[i+2]
                if t not in consts:
                    consts[t] = []
                consts[t].append(elem[i])
        
        ### Actions
        elif elem[0] == ':action':
            actions.append(parseAction(elem))
            
    #--------------------------------    
    return {"name": name, "types": heriTypes, "predicates":preds, \
    "actions":actions, "constants":consts}
    

def parsePDDLProblem(filename):
    """ filename -> dictionnaire du fichier parsé
        Parseur pour un problème PDDL
        Hypothèse : fichier PDDL bien constitué
    """
    #--------------------------------
    with open(filename, "r") as file:
        f = file.read()
    # remplace tous les \n et \t, excès d'espaces 
    # et commentaires par un espace
    elems = re.sub(r'(;;;.*\n)', " ", f)
    # Transformation en tableau grace au parseur LISP
    elems = OneOrMore(nestedExpr()).parseString(elems)
    
    #--------------------------------
    objs = {}
    init, goal = [], []
    name, domain = str(), str()
    
    #--------------------------------
    for elem in elems[0]:
        if elem[0] == 'problem':
            name = elem[1]
            
        elif elem[0] == ':domain':
            domain = elem[1]
            
        elif elem[0] == ':objects':
            tmp = []
            for i, o in enumerate(elem[1:]):
                if o != '-':
                    if elem[i] != '-':
                        tmp.append(o)
                    else:
                        if o not in objs:
                            objs[o] = []
                        objs[o].extend(tmp)
                        tmp = []
            
        elif elem[0] == ':init':
            init = elem[1:]
    
        elif elem[0] == ':goal':
            tmp = elem[1]
            if tmp[0] == 'and':
                goal = tmp[1:]
            else:
                goal = [tmp]
    
    #--------------------------------
    return {"name":name, "domain":domain, "objects":objs, \
            "init":init, "goal":goal}


def PDDLToASP(domainFile, problemFile):
    """ filename * filename -> str 
        Retourne un programme ASP à partir d'un domaine et un problème
        PDDL
    """
    
    d = parsePDDLDomain(domainFile)
    p = parsePDDLProblem(problemFile)
        
    #--------------------------------
    res = []
    ### Nom du domaine
    res.append("% Nom du domaine {}".format(d["name"]))
    ### Types - Héritage
    for k, v in d["types"].items():
        for t in v:
            res.append("{}(X) :- {}(X).".format(k, t))
    ### Prédicats
    res.append("% Déclaration des prédicats ({})".format(d["name"]))
    for pred in d["predicates"]:
        op = pred[0]
        if not pred[1]:
            res.append("pred({}).".format(op))
        else:
            var, types = [], []
            for pr in pred[1]:
                var.append(pr[0])
                types.append("{}({})".format(pr[1], pr[0]))
            var = ", ".join(var)
            types = ", ".join(types)
            
            res.append("pred({}({})) :- {}.".format(op ,var, types ))
            
    ### Actions
    res.append("% Déclaration des actions ({})".format(d["name"]))
    # Hypothèse : une action a forcément des paramètres
    for action in d["actions"]:
        # Declaration de l'action
        act = action["name"]
        
        params, types = [], []
        for par in action["parameters"]:
            params.append(par[0])
            types.append("{}({})".format(par[1], par[0]))
        params = ", ".join(params)
        types = ", ".join(types)
        
        res.append("action({}({})) :- {}.".format(act, params, types))
        # Déclaration des préconditions
        res.append("% préconditions")
        for pre in action["pre"]:
            op = pre[0]
            var = "({})".format(", ".join(pre[1:])) if pre[1:] else ""
            res.append("pre({}({}), {}{}) :- action({}({})).".format(act, params,\
                op, var, act, params))
        # Déclaration des effets
        res.append("% effects")
        for pre in action["del"]:
            op = pre[0]
            var = "({})".format(", ".join(pre[1:])) if pre[1:] else ""
            res.append("del({}({}), {}{}) :- action({}({})).".format(act, params,\
                op, var, act, params))
        for pre in action["add"]:
            op = pre[0]
            var = "({})".format(", ".join(pre[1:])) if pre[1:] else ""
            res.append("add({}({}), {}{}) :- action({}({})).".format(act, params,\
                op, var, act, params))
    
    ### Objets (problem) ou constantes (domain)
    res.append("% Déclaration des objets (problem) ou constantes (domain)")
    for k, v in d["constants"].items():
        tmp = ";".join(list(map(lambda v: v.lower(), v)))
        res.append("{}({}).".format(k, tmp))

    for k, v in p["objects"].items():
        tmp = ";".join(list(map(lambda v: v.lower(), v)))
        res.append("{}({}).".format(k, tmp))
        
    ### Initialisation
    res.append("% Etat initial")
    for init in p["init"]:
        tmp = "({})".format(", ".join(list(map(lambda v: v.lower(), init[1:])))) if len(init)>1 else ""
        res.append("init({}{}).".format(init[0], tmp))
    
    ### But
    res.append("% Etat final (but)")
    for but in p["goal"]:
        tmp = "({})".format(", ".join(list(map(lambda v: v.lower(), but[1:])))) if len(but)>1 else ""
        res.append("but({}{}).".format(but[0], tmp))

    return "\n".join(res)


if __name__ == '__main__':
    
    FILE_domain = "singe_bananes-domain.pddl"
    FILE_problem = "singe_bananes-problem.pddl"
    FILE_asp = "aspplan2.lp"

    res = PDDLToASP(FILE_domain, FILE_problem)
    print(res)
    #with open(FILE_asp, "w") as f:
    #    f.write(res)
    
