%%%% Organisation de championnat %%%%

#const ne=3. % nb équipes participantes
#const ns=3. % nb semaines durée championnat
#const nj=(2*ns). % nb jours match
#const p_ext=50.
#const p_dom=40.

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

%% Nouvelles contraintes
%% pext% des matchs de chaque équipe à l'exterieur le dimanche

1{match(E2, E1, S, dimanche) : equipe(E1), equipe(E2), semaine(S)}lim :- lim=(p_ext*(ne-1)/100). 

%% pdom% des matchs de chaque équipe à domicile le dimanche

1{match(E1, E2, S, dimanche) : equipe(E1), equipe(E2), semaine(S)}lim :- lim=(p_dom*(ne-1)/100).

%% Aucune équipe ne joue (strictement) plus de deux matchs consécutifs à l'extérieur
% Impossible d'avoir une équipe qui joue le mercredi puis le dimanche a l'extérieur la même semaine
:- match(_, E1, S, mercredi), match(_, E1, S, dimanche), equipe(E1), semaine(S).

% Impossible d'avoir une équipe qui joue le dimanche puis le mercredi à l'extérieur sur deux semaines consécutives
:- match(_, E1, S1, dimanche), match(_, E1, S2, mercredi), equipe(E1), semaine(S1;S2), S2=S1+1.