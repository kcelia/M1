
-- analyser le contenu de la table Annuaire

set autotrace off
alter session set optimizer_mode = CHOOSE;

prompt analyse le contenu de la table Annuaire appartenant à :
show user

declare 
utilisateur varchar2(30);
begin
select sys_context('USERENV', 'SESSION_USER')
into utilisateur
from dual;
dbms_stats.gather_table_stats(utilisateur, 'J');
dbms_stats.gather_table_stats(utilisateur, 'C');
dbms_stats.gather_table_stats(utilisateur, 'F');
end;
/

prompt les tables analysées :
column table_name format A30
select table_name, global_stats as analysé from user_tables;

prompt les index analysés :
column index_name format A30
select index_name, global_stats as analysé from user_indexes;



