# Write your MySQL query statement below
select id ,c1.movie , description ,rating
from Cinema c1
where id % 2 = 1 and description != "boring"
order by rating desc