-- NOM: BOURMAUD
-- Prénom: Alexia

-- NOM: MARCHAL
-- Prénom: Louise

-- ==========================
--      TME Jointure
-- ========================== 


-- Préparation
-- ===========

-- construire la base contenant les tables J, C et F
@vider
purge recyclebin;
@baseJCF

@liste


-- schéma des tables
desc J
desc C
desc F
desc BigJoueur

COLUMN TABLE_NAME format A20
SELECT TABLE_NAME, blocks, num_rows 
FROM user_tables;

EXPLAIN plan FOR
SELECT * FROM F;
@p4


--afficher les cardinalités
select count(*) as nb_Joueurs from J;
select count(*) as nb_Clubs from C;
select count(*) as nb_Finances from F;
select count(*) as nb_BigJoueurs from BigJoueur;





-- =====================
-- Exercice préparatoire
-- =====================

explain plan for select * from J;
@p4
--J
--il y a 50 000 n-uplet
--cout d'acces 68

explain plan for select * from C;
@p4
--C
--il y a 5 000 n-uplet
--cout d'acces 7

explain plan for select * from F;
@p4
--F
--il y a 5 000 n-uplet
--cout d'acces 5

explain plan for select * from BigJoueur;
@p4
--il y a 50 000 n-uplets
--cout d'acces 13 798



-- ============================================
--    Exercice 1: Jointure entre 2 relations
-- ============================================

-- Question 1
--===========

explain plan for
  select J.licence, C.nom
  from J, C
  where J.cnum = C.cnum
  and salaire >10;
@p4
--r1 retourne la licence de chaque joueur ayant un salaire supérieur à 10 et le nom ce leur club
--   0
--   1*
--2     3*
--
--MAP<Int,String> map	 
--foreach( c: C.fullStream ()){
--	   map.put(c.num , c.nom)
--}
----foreach( j: J.fullStream ()){
--	   if(j.salaire>=10){
--	   	affichage(j.licence, map.get(j.num))
--}
--avec J est une TABLE
--     C est une TABLE
--     map est une MAP
--
--a)cout(J)=68
--  cout(C)=7
--  cout(C join J)= cout(J)+ cout(C) =75 or ici on observe que d'après oracle c'est 76, le 1 de différence est du au cout du cpu  pour construire la MAP
-- cout(filter(salaire)et J)= 68 car la cout du filtre est nul donc c'est juste le cout de J
--

--b)
explain plan for
SELECT /*+ ordered */ *
FROM C, BigJoueur j
WHERE j.cnum = c.cnum;
@p4

--cout 13805 =13798 (coutC) +7(cout BigAnnuaire)

explain plan for
SELECT /*+ ordered */ *
FROM  BigJoueur j, C
WHERE j.cnum = c.cnum;
@p4
-- cout 23370 !=13798+7 manque 9565
-- apparition d'une colonne TempSpc =192M pour le hash join
-- Ici on est dans un hachage externe d'ou l'apparition de cette colonne. L'ecriture de la map se fait dans TempSpc , le cout de la création de cette map est 192M*0.05=9600 env 9565

--c)
explain plan for
  select J.licence, C.nom
  from J, C
  where J.cnum = C.cnum
  and salaire >10;
@p4

explain plan for
  select J.licence, C.nom
  from J, C
  where J.cnum = C.cnum
  and salaire >100;
@p4

explain plan for
  select J.licence, C.nom
  from J, C
  where J.cnum = C.cnum
  and salaire >1000;
@p4

explain plan for
  select J.licence, C.nom
  from J, C
  where J.cnum = C.cnum
  and salaire >10000;
@p4

--On voit que le plan est toujours le même ainsi que le coùt (76). Il fait une jointure par hachage.
--SELECT STATEMENT
--	 HASH JOIN
--	      TABLE ACCESS FULL
--	      TABLE ACCESS FULL

--d)
explain plan for
SELECT /*+USE_NL(J,C)*/  J.licence, C.nom
FROM C, j
WHERE J.cnum = C.cnum
AND salaire < 10050;
@p4
-- oracle utilise une jointure par hachage
-- 4 table access full cost=7 ça signifi que 7 pages ont été lues.
-- 3 index range scan cost=2 oracle a lu deux pages d'index
-- 2 table access by index cost=52 oracle lit 52 pages grace aux index touvés en 3
-- 1 hash join cost=60 = 52+7+ 1   le 1  en plus est du au cout du cpu  pour construire la MAP
-- remarque en obligeant oracle a utiliser une boucle sur les index on observe que le cout est de 102


-- Question 2)
-- ===========

--a)

explain plan for
  select J.licence, C.nom
  from C, J
  where J.cnum = C.cnum
  and salaire < 10006;
@p4

-- foreach(iJ :IndexSalaire.GetRowIds(<10006)){
--	j=J.getTuple(iJ)
--	iC= IndexClub.GetRowIds(j.cnum)
--	c=C.getTuple(ic)
--	affiche(j.licence, c.nom
--}

-- oracle utilise une jointure par boucle avec index non placant (nested loops)
-- 4 index range scan sur I_J_SALAIRE , cost= 2, oracle lit une page d'index
-- 3 table access by index sur J, cost=8,  oracle accede au tuple correspondant aux index trouvés juste avant
--
-- 2 nested loops, cost =14, oracle fait une jointure par boucle, pour chaque rowid il cherche un tuple de C (3)
-- 5 INDEX UNIQUE SCAN recupere l'index du club grace a au cnum du joueur (env. jointure), oracle sait qu'il y aura qu'un seule index retourné (clé primaire) cout=0
-- 6 TABLE ACCESS BY INDEX recupere l'information du club grace a l'index trouve en 5, cout=1
-- 14=8(cout(J))+6(card(J):nb row)*1(card(C))

explain plan for
  select /*+ USE_HASH(C,J)*/  J.licence, C.nom
  from C, J
  where J.cnum = C.cnum
  and salaire < 10006;
@p4

-- Remarque si on force oracle  a utiliser une hash map le cout observé est de 16>14


--b)
explain plan for
SELECT /*+ USE_NL(J,C) */ J.licence, C.nom
FROM J, C
WHERE J.cnum = C.cnum
AND J.salaire > 10;
@p4


--		0
--		|
--		1
--	      /   \
--           2	   5
--	    / \
--        3    4

-- La table J est parcourue entierement une seule fois, la table C est parcourue pour chaque nouvel index trouvé.
-- L'index cnum utilisé est celui de la table J, il est utilisé dans la table C
-- Cout du plan = 50083= 68 (cout(J))+ 50000 (card(J)) * 1 (card(C))
-- ce plan est très couteux car il parcours J en entier et que pour chaque valeur j.Cnum il parcours C.

explain plan for
SELECT /*+ USE_NL(J,C) ordered*/ J.licence, C.nom
FROM C,J
WHERE J.cnum = C.cnum
AND J.salaire > 10;
@p4

--		0
--		|
--		1
--	      /   \
--	     2     5
--	   /   \
--	  3     4

-- La difference avec le plan précédent est qu'oracle parcourt en premier les club puis pour chaque club il cherche les joueurs qui en font partit. Cela est plus couteux car pour chaque club il y a plusieurs joueurs dedans et donc il faut faire plus d'acces à la table J.
-- cout = 55020 = 7 (cout(C))+ 5000(card(C)) *( 11 (card(J)) + cout CPU)

-- foreach(c :Club.fullScan()){
--	iJ= IndexJoueur.GetRowIds(c.cnum)
--	foreach(j : iJ){
--		  joueur=Joueur.getTuple(j)		  
--		  affiche(joueur.licence, c.nom)
--	}
--}


-- Question 3)
-- ===========
explain plan for
  select J.licence, C.division
  from C, J
  where J.cnum = C.cnum
  and C.nom in ('PSG', 'Barca');
@p4



-- Question 4)
-- ===========
explain plan for
  select J.licence, C.division
  from C, J
  where J.cnum = C.cnum
  and J.salaire between 10000 and 10001;
@p4





-- ============================================================
-- EXERCICE 2: Directives USE_NL et USE_HASH pour une jointure
-- ============================================================



-- Question 1
--===========

explain plan for
  select /*+ USE_NL(J,C) */ J.licence, C.nom
  from J, C
  where J.cnum = C.cnum
  and salaire >10;
@p4



-- Question 2)
-- ===========

explain plan for
  select /*+ USE_NL(J,C) */ J.licence, C.nom
  from C, J
  where J.cnum = C.cnum
  and salaire < 11000;
@p4


-- Question 3)
-- ===========

explain plan for
  select /*+ USE_HASH(J,C) */ J.licence, C.division
  from C, J
  where J.cnum = C.cnum
  and C.nom in ('PSG', 'Barca');
@p4

-- Question 4)
-- ===========
explain plan for
  select /*+ USE_HASH(J,C) */ J.licence, C.division
  from C, J
  where J.cnum = C.cnum
  and J.salaire between 10000 and 10001;
@p4






-- =====================================================
--   EXERCICE 3 : Ordre des jointures entre 3 relations 
-- =====================================================


-- ordre1 : CFJ
explain plan for
    select /*+ ORDERED */ C.nom, F.budget 
    from C, F, J
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4
--cout =81



-- ordre2 : CJF
explain plan for
    select /*+ ORDERED */ C.nom, F.budget 
    from C, J, F
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4
-- cout=81


-- ordre3 : FCJ
explain plan for
    select /*+ ORDERED */ C.nom, F.budget 
    from F, C, J
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4
--cout =82


-- ordre4 : FJC
explain plan for
    select /*+ ORDERED */ C.nom, F.budget 
    from F, J, C
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
--    where J.cnum = F.cnum and C.cnum = J.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4
--cout=79


-- ordre5 : JCF
explain plan for
    select /*+ ORDERED */ C.nom, F.budget 
    from J, C, F
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4
--cout 78


-- ordre6 : JFC
explain plan for
    select /*+ ORDERED */ C.nom, F.budget 
    from J, F, C
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4
--cout 78

-- 6 ordre possibles qui vont de 78 à 55000


-- SANS directive ORDERED
explain plan for
    select  C.nom, F.budget 
    from J, C, F
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4

-- si on ne spécifit pas l'ordre oracle trouve l'ordre le moins couteux


-- avec directive index(J I_J_salaire)

explain plan for
    select /*+ index(J I_J_salaire) */  C.nom, F.budget 
    from J, C, F
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4


-- avec directive  index(C I_C_division)

explain plan for
    select /*+ index(C I_C_division) */  C.nom, F.budget 
    from J, C, F
    where J.cnum = C.cnum and C.cnum = F.cnum and J.cnum = F.cnum
    and C.division=1 and J.salaire > 59000
    and J.sport = 'sport1';
@p4

