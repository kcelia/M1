%%%% Organisation de championnat %%%%

#const ne=3. % nb équipes participantes
#const ns=3. % nb semaines durée championnat
#const nj=(2*ns). % nb jours match

pos(1..nj).
jour(mercredi; dimanche).
semaine(1..ns).
equipe(1..ne).

%% Générer tous les matchs possibles entre les équipes
1{match(E1, E2, S, J) : semaine(S), jour(J)}1 :- equipe(E1), equipe(E2), E1!=E2.

%% Une equipe ne peut jouer qu'un seul match
% Impossible d'avoir la même équipe qui joue à domicile le même jour
:- match(E1, E2, S, J), match(E1, E3, S, J), equipe(E1;E2;E3), semaine(S), jour(J), E2!=E3.

% Impossible d'avoir la même équipe qui joue a domicile et à l'extérieur le même jour
:- match(E1, _, S, J), match(_, E1, S, J), equipe(E1), semaine(S), jour(J).

% Impossible d'avoir la même équipe qui joue à l'extérieur le même jour
:- match(E2, E1, S, J), match(E3, E1, S, J), equipe(E1;E2;E3), semaine(S), jour(J), E2!=E3.