-- TME Jointure
-- creation des relations de l'exercice J, C, F
-- ======================================

--show user

--drop table J;
--drop table C;
--drop table F;


-- ================ SCHEMA ============================

prompt creation des tables J, C, F 


create table C (  
  cnum number(10)  not null, 
  nom varchar2(30)  not null,
  division number(1)  not null, 
  ville varchar2(30),
  constraint I_C_cnum primary key(cnum)
);

create table F (  
  cnum number(10)  not null, 
  budget number(10)  not null,
  depense number(10),
  recette number(10),
  constraint I_F_cnum primary key(cnum)
);


create table J (
  licence number(10), 
  cnum number(10) not null, 
  prenom varchar2(30) not null, 
  salaire number(10)  not null, 
  sport varchar2(30)
);



--- ==================== DONNEES ================

-- definition de la procedure 
-- pour ajouter des tuples dans J,C et F

create or replace procedure ajouterJCF is
 prenom varchar2(30);
 n_salaire integer;
 n_club integer;
 n_sport integer;
 n_division integer;
--
begin
 DBMS_RANDOM.INITIALIZE(123456);
--
 FOR i in 1 .. 50000 LOOP
--
   prenom := 'pn' || i;
   n_club := abs(DBMS_RANDOM.RANDOM) mod 5000;
   n_salaire := abs(DBMS_RANDOM.RANDOM) mod 50000;
   n_sport := abs(DBMS_RANDOM.RANDOM) mod 200;
--
   insert into J values(i, n_club + 1, prenom, n_salaire + 10000, 'sport' || n_sport);
--
 END LOOP;
--
 FOR i in 1 .. 5000 LOOP
--
   n_division := abs(DBMS_RANDOM.RANDOM) mod 2;
--   
   insert into C values( i, 'nom' ||i, n_division + 1, 'ville');
   insert into F values( i, 1000, 10, 100);
--
 END LOOP;
--
 DBMS_RANDOM.TERMINATE;
 commit;
end;
/
sho err


-- remplir les relations:
prompt insertion des nuplets, patientez ...

begin
 ajouterJCF();
end;
/


-- ajouter la clé étrangère dans J 
alter table J add (constraint FK1 foreign key(cnum) references C);


-- ============ INDEX ========================
--drop index I_J_cnum;
--drop index I_J_salaire;
--drop index I_C_division;

create index I_J_cnum on J(cnum);
create index I_J_salaire on J(salaire);
create index I_C_division on C(division);

--create index I_C_cnum on C(cnum); deja defini avec la primary key
--create index I_F_cnum on F(cnum); deja defini avec la primary key



prompt analyse des tables J, C, F et les indes associées
@analyseJCF


-- synonyme vers une "grosse" table
--drop synonym BigJoueur;
create synonym BigJoueur for hubert.BigJoueur; 



prompt préparation terminée.


