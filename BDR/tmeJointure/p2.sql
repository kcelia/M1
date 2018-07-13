
set feedback off

select plan_table_output
from table(dbms_xplan.display('plan_table', null, 'basic +rows +predicate'));

delete plan_table;

set feedback on

