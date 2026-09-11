# Write your MySQL query statement below
-- select d.unique_id,e.name 
-- from Employee as e left join EmployeeUNI as d 
-- on e.id=d.id


select
u.unique_id,
e.name
from Employees as e
left join EmployeeUNI as u
on e.id = u.id