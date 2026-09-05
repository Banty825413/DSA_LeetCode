# Write your MySQL query statement below
Select actor_id , director_id 
FROM ActorDirector
GROUP BY actor_id , director_id
having count(*) >= 3