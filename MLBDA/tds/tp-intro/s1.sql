-- MABD TP1 Prise en main de PL/SQL

-- --------------------
-- NOM KHERFALLAH
-- Prenom CELIA
-- -----------------------------------------------------

-- procedure S1
-- affiche le code source d'une méthode de l'utilisateur

create or replace procedure s1(nom in varchar2) is


-- cursor c is 


begin
   DBMS_OUTPUT.ENABLE (100000);


   dbms_output.put_line('code source de la méthode ' || nom || ' : '); 

end;

-- exécuter s1, pour afficher par exemple le code source de la procedure L1
select * from Country;

@liste
@vider

@mondial_synonym

--- requete 8
select c.code , sum(c.population)
from country c, borders b
where (c.code = b.country1 or c.code = b.country2) 
group by c.code;
--- verification 
select * from mondial.r8;

--- requete 9
---select continent from encompasses ;

select c.code , sum(c.population)
from country c ,  borders b, encompasses e
where c.code = e.country and e.continent = 'Europe'  and  (c.code = b.country1 or c.code = b.country2)
group by c.code ;

select * from mondial.r9;

 
select c.code, b.country1, b.country2
from country c , borders b 
where c.code = 'F' and   (c.code = b.country1 or c.code = b.country2)
group by c.code,b.country1, b.country2 ;
--- count(*), sum(c.population)


--- requete  12
--select unique(continent) from encompasses ;
---select e.country from encompasses e where e.continent= 'America';


select m.country, m.mountain
from geo_mountain m ,encompasses  e, mountain h
where e.continent = 'America' and
      e.country = m.country and
      m.mountain = h.name;
      --group by m.country;
      ---and
     --- h.height = ( select max(height) from mountain );
---select * from mondial.r12;
