# Write your MySQL query statement below
select 
    p.product_id,
    round(sum(units*price)/sum(units),2) as average_price
from Prices p join unitsSold s
ON p.product_id = s.product_id 
AND s.purchase_date BETWEEN p.start_date AND p.end_date
group by product_id
