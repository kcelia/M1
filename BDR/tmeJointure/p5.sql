
--desc plan_table

set feedback off

select plan_table_output
from table(dbms_xplan.display('plan_table', null, 'typical +projection'));

prompt 
prompt  Relation entre un noeud son parent:

select id, parent_id
from plan_table
where parent_id is not null
order by parent_id;


delete plan_table;

set feedback on


