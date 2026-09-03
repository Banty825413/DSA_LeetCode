# Write your MySQL query statement below
select c1.id ,c1.movie , c1.description ,c1.rating
from Cinema c1
where c1.id % 2 = 1 and c1.description != "boring"
order by rating desc