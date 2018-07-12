
select c1.code , sum(c2.population)
from country c1, country c2, borders b, encompasses e
where (b.country1 = c1.code and b.country2  = c2.code) or (b.country1 = c1.code and b.country2  = c2.code) and e.country = c1.code  and e.continent = 'Europe'
group by c1.code;
