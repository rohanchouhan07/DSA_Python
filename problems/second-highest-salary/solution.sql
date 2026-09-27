    -- select s.salary as  SecondHighestSalary
    -- from 
    --     (select *,
    --     dense_rank() over (order by salary) as second_height_salary
    --     from Employee) as s
    -- where second_height_salary=2
SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT salary, 
           DENSE_RANK() OVER (ORDER BY salary DESC) as rank_num
    FROM Employee
) a
WHERE rank_num = 2;