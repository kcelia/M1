
set feedback off

select plan_table_output
from table(dbms_xplan.display('plan_table', null, 'basic'));

delete plan_table;

set feedback on
