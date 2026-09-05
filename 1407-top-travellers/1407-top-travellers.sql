# Write your MySQL query statement below
SELECT u.name , IFNULL(t.distance,0) as travelled_distance
FROM Users u LEFT JOIN (SELECT user_id , SUM(IF(distance is null ,0,distance)) as distance from Rides
                     GROUP BY user_id 
                         ) as t On u.id = t.user_id 
ORDER BY travelled_distance desc , u.name asc 