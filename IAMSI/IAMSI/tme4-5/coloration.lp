%%%%% QUESTION DE COLORATION %%%%


%%% Définition des constantes

#const nbC=4. % nombre de couleurs
#const nbN=7. % nombre de noeuds

%%% Définition des couleurs et noeuds
couleur(1..nbC).
noeud(1..nbN).

%%% Définition des aretes (graphe de l'énoncé)
% Graphe non orienté :
% Une arête est définie par deux sommets x et y
arete(1,2).
arete(1,3).
arete(2,6).
arete(3,7).
arete(6,7).
arete(4,5).
arete(2,4).
arete(3,5).
arete(2,3).
arete(4,6).
arete(4,7).
arete(5,7).
arete(2,5).
arete(3,4).

% On génère les arêtes symetriques
arete(X, Y) :- arete(Y, X).

%%% Définition des contraintes
% On genere toutes les colorations possibles
1{coloration(X, C) : couleur(C)}1 :- noeud(X).

% Deux noeuds adjacents ne peuvent avoir la même couleur
:- coloration(X, C), coloration(Y, C), couleur(C), noeud(X), noeud(Y), arete(X, Y).

%%%% Resolution du probleme avec le graphe de l'énoncé %%%%
%% nombre de solutions : 96
%% Une solution :
% arete(1,2) arete(1,3) arete(2,6) arete(3,7) arete(6,7) arete(4,5) arete(2,4) arete(3,5) arete(2,3) arete(4,6) arete(4,7) arete(5,7) arete(2,5) arete(3,4) couleur(1) couleur(2) couleur(3) couleur(4) noeud(1) noeud(2) noeud(3) noeud(4) noeud(5) noeud(6) noeud(7) arete(2,1) arete(3,1) arete(6,2) arete(7,3) arete(7,6) arete(5,4) arete(4,2) arete(5,3) arete(3,2) arete(6,4) arete(7,4) arete(7,5) arete(5,2) arete(4,3) coloration(5,1) coloration(1,2) coloration(4,2) coloration(2,3) coloration(7,3) coloration(3,4) coloration(6,4)

%% Le graphe est 4-colorable mais pas 3-colorable
