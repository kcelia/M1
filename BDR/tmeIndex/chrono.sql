
-- Supplement au TME Index


-- acces à la table BigAnnuaire
create synonym BigAnnuaire for hubert.BigAnnuaire;

set timing off
set autotrace off
select count(*) from BigAnnuaire;




-- Chronomètre

-- durée d'une requête (moyenne mesurée pendant approx 2s)
declare
debut number; duree number; nbr number; a number;
begin
  debut := dbms_utility.get_time();
  nbr := 0; duree := 0;
  while duree < 2 loop
    nbr := nbr + 1;
    for j in (
               SELECT /*+ no_index(BigAnnuaire IndexAge)*/ min(cp)
               FROM BigAnnuaire 
               WHERE age <= 1
             )
    loop
      a := 0;
    end loop;
    duree := (dbms_utility.get_time() - debut) / 100;
  end loop;
  dbms_output.put_line('Une requête dure ' || round(duree * 1000 / nbr) || ' ms.');
  if(nbr > 1) then dbms_output.put_line('Moyenne mesurée sur ' || nbr || ' requêtes.'); end if;
end;
/


