SELECT e1.name FROM  Employee e1
where e1.id in (
    select e2.managerId FROM 
    Employee e2
    group by e2.managerId 
    having count(*) >= 5
)