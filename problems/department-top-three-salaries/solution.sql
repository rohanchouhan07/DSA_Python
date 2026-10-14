# Write your MySQL query statement below
with demo as (
    select 
        d.name as Department,
        e.name as Employee,
        Salary,
        dense_rank() over(partition by d.name order by salary desc) as rnk
    from Employee e join Department d on e.departmentId =d.id

)
select 
    Department ,
    Employee , 
    Salary 
from demo
where rnk <=3 
