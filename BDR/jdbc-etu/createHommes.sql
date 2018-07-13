-- creation de la relation Annuaire

drop table Hommes;

create table Hommes(nom varchar(30), 
prenom varchar(30), 
age number(3), 
--adresse varchar(30), 
cp number(5), 
tel varchar(10)
);


-- definition de la procedure 
-- pour ajouter n tuples dans l'annuaire

create or replace procedure ajouterH(n number) is
 n_nom integer;
 n_prenom integer;
 n_age integer;
 n_cp integer;
 n_tel integer;

begin

 DBMS_RANDOM.INITIALIZE(123456);

 FOR i in 1 .. n LOOP

   n_nom := abs(DBMS_RANDOM.RANDOM) mod 100;
   n_prenom := abs(DBMS_RANDOM.RANDOM) mod 90;
   n_age := abs(DBMS_RANDOM.RANDOM) mod 50;
   n_cp := abs(DBMS_RANDOM.RANDOM) mod 990;
   n_tel := abs(DBMS_RANDOM.RANDOM) mod 900000000;

   insert into Hommes values( 
    'nom' || n_nom ,
    'prenom' || n_prenom,
    n_age + 1 , (n_cp*100) + 1000,
    '0' || (n_tel + 100000000)
   );
 END LOOP;
 DBMS_RANDOM.TERMINATE;
 update hommes set age=age+49;
 insert into Hommes values( 
    'nomHomme',
    'prenomHomme',
    2 , 75019,
    0144277000 
   );
 commit;
end;
/

sho err


-- remplir l'annuaire :
begin
 ajouterH(10000);
end;
/
