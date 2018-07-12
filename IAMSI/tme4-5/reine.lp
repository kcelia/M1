%%%% PROBLEME DES 8-REINES %%%%

#const n=8. % nombre de reines/taille de l'échiquier

%reine(1, 1).
%not reine(4, 4).

% Définition des positions (lignes et colonnes)
pos(1..n).

% Au maximum une reine par ligne
1{reine(I, J) : pos(J)}1 :- pos(I).

% Au maximum une reine par colonne / On ne peut avoir 2 reines sur une même colonne
:- 2{reine(I, J) : pos(I)}, pos(J).

% Au maximum une reine par diagonale / On ne peut avoir 2 reines sur la même diagonale
:- reine(I1, J1), reine(I2, J2), pos(I1), pos(J1), pos(I2), pos(J2), |J1-J2|==I1-I2, I1 > I2.



%%% 4 solutions du probleme avec reine(1, 1) %%%
%%% Solution 1 %%%
%% {reine(1,1), pos(1), pos(2), pos(3), pos(4), pos(5), pos(6), pos(7), pos(8),
%% reine(7,2), reine(5,3), reine(8,4), reine(2,5), reine(4,6), reine(6,7), reine(3,8) }
%%% Solution 2 %%%
%% {reine(1,1), pos(1), pos(2), pos(3), pos(4), pos(5), pos(6), pos(7), pos(8),
%% reine(6,2), reine(8,3), reine(3,4), reine(7,5), reine(4,6), reine(2,7), reine(5,8)}
%%% Solution 3 %%%
%% {reine(1,1), pos(1), pos(2), pos(3), pos(4), pos(5), pos(6), pos(7), pos(8),
%% reine(7,2), reine(4,3), reine(6,4), reine(8,5), reine(2,6), reine(5,7), reine(3,8)}
%%% Solution 4 %%%
%% {reine(1,1), pos(1), pos(2), pos(3), pos(4), pos(5), pos(6), pos(7), pos(8),
%% reine(5,2), reine(8,3), reine(6,4), reine(3,5), reine(7,6), reine(2,7), reine(4,8)}

%%% 84 solutions du problème avec aucune reine(4, 4) %%%

%%% Nb solutions avec différentes tailles d'échiquier %%%
%% 1 : 1 sol, 2 : 0 sol, 3 : 0 sol, 4 : 2 sol, 5 : 10 sol, 6 : 4 sol, 7 : 40 sol, 8 : 92 sol
