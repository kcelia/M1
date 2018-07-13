
-- TME index

-- usage:
-- @annuaire


 -- création de la relation Annuaire

purge recyclebin;

drop table Annuaire;

create table Annuaire(
  nom varchar(30), 
  prenom varchar(30), 
  age number(3) not null, 
  cp number(6) not null, 
  tel varchar(10) not null,
  profil varchar(1500) not null
  -- le telephone est unique:
  -- constraint UniqueTel unique(tel)
) nocache nologging;


drop table Ville;

create table Ville(
  ville varchar(30), 
  cp number(6) not null,
  population number(7) not null);

-- définition de la procedure 
-- pour ajouter n tuples dans l'annuaire

create or replace procedure ajouter(n number) is
 nom varchar(30);
 prenom varchar(30);
 age integer;
 cp integer;
 tel varchar(10);
 profil varchar(1500);
--
begin
 DBMS_RANDOM.INITIALIZE(1);
--
   FOR i in 1 .. n LOOP
     -- générer des valeurs aléatoires pour une personne
     nom := 'n' || i;
     prenom := 'pn' || i;
     age := 1 + abs(DBMS_RANDOM.RANDOM) mod 100;
     cp := (abs(DBMS_RANDOM.RANDOM) mod 1000 * 100) + 1000 ;
     tel := '0' || abs(DBMS_RANDOM.RANDOM) mod 900000000;
     profil := rpad('p' || abs(DBMS_RANDOM.RANDOM) mod 2000000, 1500, '.');
     --insérer une nouvelle personne
     insert into Annuaire values(nom, prenom, age, cp, tel, profil);
   END LOOP;
   -- valider les insertions
   commit;
   DBMS_RANDOM.TERMINATE;
end;
/
sho err



create or replace procedure ajoutervilles is
 ville varchar(30);
 cp integer;
 population integer;
--
begin
   DBMS_RANDOM.INITIALIZE(1);
   FOR i in 0 .. 999 LOOP
     -- générer des valeurs aléatoires pour une personne
     ville := 'n' || i;
     cp := 1000 + 100 * i;
     population := (1+ abs(DBMS_RANDOM.RANDOM) mod 1000) * 1000;
     --insérer une nouvelle personne
     insert into Ville values(ville, cp, population);
   END LOOP;
   -- valider les insertions
   commit;
   DBMS_RANDOM.TERMINATE;
end;
/
sho err




-- remplir l'annuaire avec 2000 personnes
begin
 ajouter(2000);
 ajoutervilles;
end;
/



-- remplir l'annuaire
--Créer les index sur les attributs age et cp :
create index IndexAge on Annuaire(age);
create index IndexCp on Annuaire(cp);

--create index IndexVilleCP on Ville(cp);


--statistiques sur l'Annuaire
@analyse



-- créer les synonymes pour les tables de grande taille
create synonym BigAnnuaire for hubert.BigAnnuaire; 
create synonym BigAnnuaireSimple for hubert.BigAnnuaireSimple;


prompt fin du ficher annuaire.sql
prompt
