# Write your MySQL query statement below
WITH
  all_products AS (
    SELECT DISTINCT product_id
    FROM Products
  ),
  latest AS (
    SELECT product_id, MAX(change_date) AS change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
  )
SELECT
  a.product_id,
  COALESCE(p.new_price, 10) AS price
FROM all_products a
LEFT JOIN latest l
  ON a.product_id = l.product_id
LEFT JOIN Products p
  ON p.product_id = l.product_id
 AND p.change_date = l.change_date;