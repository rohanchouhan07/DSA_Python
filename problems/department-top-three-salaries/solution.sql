# Write your MySQL query statement below
select Department,Employee,Salary 
from (select 
    d.name as Department,
    e.name as Employee,
    Salary as Salary,
    dense_rank() over(partition by d.name order by salary desc) as drank
    from Employee e left join Department d
    on e.departmentId=d.id) r
where drank <=3
