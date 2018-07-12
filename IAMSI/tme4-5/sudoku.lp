%%%% SUDOKU %%%%

valeur(1..9).
pos(0..8).

% Générer toutes les grilles possibles
1{case(I, J, V) : valeur(V)}1 :- pos(I), pos(J).

% Traduction dans le langage SMODELS les trois contraintes
% Contrainte 1 - Lignes
:- case(I, J1, V), case(I, J2, V), pos(I), pos(J1), pos(J2), valeur(V), J1!=J2. 

% Contrainte 2 - Colonnes
:- case(I1, J, V), case(I2, J, V), pos(I1), pos(I2), pos(J), valeur(V), I1!=I2. 

% Contrainte 3 - Chaque carré ne contient qu'un seul exemplaire de chaque numéro
:- case(I1, J1, V), case(I2, J2, V), pos(I1), pos(I2), pos(J1), pos(J2), valeur(V), I1/3==I2/3, J1/3==J2/3, 1{I1!=I2; J1!=J2}.


%%%%% Grille spécifiée dans l'énoncé %%%%%
case(0,1,7). 
case(0,3,6). 
case(0,5,3). 
case(0,7,1).
case(0,8,4). 
case(1,0,8).
case(1,4,9).
case(2,1,6).
case(2,2,3).
case(2,3,2).
case(2,4,1).
case(2,6,8).
case(3,4,3).
case(3,7,5).
case(3,8,9).
case(4,0,6).
case(4,3,9).
case(4,6,4).
case(4,8,1).
case(5,0,9).
case(5,1,2).
case(5,3,4).
case(5,5,1).
case(5,8,8).
case(6,1,5).
case(6,3,8).
case(6,8,3).
case(7,0,4).
case(7,2,1).
case(7,3,3).
case(7,4,6).
case(7,5,2).
case(7,6,7).
case(7,7,8).
case(8,0,3).
case(8,2,6).
case(8,3,1).
case(8,6,9).
case(8,8,2).

%%%% Resolution : une seule solution %%%%
%%% Resultat clingo %%%
% case(0,1,7) case(0,3,6) case(0,5,3) case(0,7,1) case(0,8,4) case(1,0,8) case(1,4,9) case(2,1,6) case(2,2,3) case(2,3,2) case(2,4,1) case(2,6,8) case(3,4,3) case(3,7,5) case(3,8,9) case(4,0,6) case(4,3,9) case(4,6,4) case(4,8,1) case(5,0,9) case(5,1,2) case(5,3,4) case(5,5,1) case(5,8,8) case(6,1,5) case(6,3,8) case(6,8,3) case(7,0,4) case(7,2,1) case(7,3,3) case(7,4,6) case(7,5,2) case(7,6,7) case(7,7,8) case(8,0,3) case(8,2,6) case(8,3,1) case(8,6,9) case(8,8,2) case(1,1,1) case(3,0,1) case(6,6,1) case(0,0,2) case(1,7,2) case(3,6,2) case(4,4,2) case(6,2,2) case(1,6,3) case(4,1,3) case(5,7,3) case(1,2,4) case(2,5,4) case(3,1,4) case(6,4,4) case(8,7,4) case(0,6,5) case(1,3,5) case(2,0,5) case(4,2,5) case(5,4,5) case(7,8,5) case(8,5,5) case(1,8,6) case(3,5,6) case(5,6,6) case(6,7,6) case(1,5,7) case(2,8,7) case(3,3,7) case(4,7,7) case(5,2,7) case(6,0,7) case(8,4,7) case(0,4,8) case(3,2,8) case(4,5,8) case(8,1,8) case(0,2,9) case(2,7,9) case(6,5,9) case(7,1,9)

%%% GRILLE %%%
% [[ 2.  7.  9.  6.  8.  3.  5.  1.  4.]
%  [ 8.  1.  4.  5.  9.  7.  3.  2.  6.]
%  [ 5.  6.  3.  2.  1.  4.  8.  9.  7.]
%  [ 1.  4.  8.  7.  3.  6.  2.  5.  9.]
%  [ 6.  3.  5.  9.  2.  8.  4.  7.  1.]
%  [ 9.  2.  7.  4.  5.  1.  6.  3.  8.]
%  [ 7.  5.  2.  8.  4.  9.  1.  6.  3.]
%  [ 4.  0.  1.  3.  6.  2.  7.  8.  5.]
%  [ 3.  8.  6.  1.  7.  5.  9.  4.  2.]]