# Write your MySQL query statement below
select
    product_name,
    sum(unit) as unit 
from Products p left join orders o
on p.product_id=o.product_id
where extract(year_month from  o.order_date) =202002
group by o.product_id
having sum(unit) >=100