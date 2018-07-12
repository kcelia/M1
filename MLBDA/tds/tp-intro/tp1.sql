-- MABD TP1 SQL avec la base MONDIAL


-- -------------------- binome -------------------------
-- NOM
-- Prenom

-- NOM
-- Prenom
-- -----------------------------------------------------

-- pour se connecter à oracle:
-- sqlplus E1234567/E1234567@oracle
-- remplacer E12345657 par la lettre E suivie de votre numéro de login

set sqlbl on
set linesize 150

prompt schema de la table Country
desc Country

prompt schema de la table City
desc City

prompt schema de la table IsMember
desc IsMember

prompt schema de la table City
desc City

-- pour afficher un nuplet entier sur une seule ligne
column name format A15
column capital format A15
column province format A20

-- Requete 0

select * from Country where name = 'France';

-- Requete 1
prompt 






-- Requete 2
prompt 
