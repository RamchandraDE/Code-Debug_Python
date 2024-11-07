WITH Total_sales (store_id,total_sales_per_store) AS 
		   (SELECT s.store_id, sum(cost) as total_sales_per_store
			FROM sales s
			GROUP BY s.store_id),
	  avg_sales (avg_sales_for_all_stores) as 
		(SELECT CAST(AVG(total_sales_per_store) AS INT) as avg_sales_for_all_stores
		FROM Total_sales)
SELECT *
FROM Total_sales ts
JOIN avg_sales  av
ON ts.total_sales_per_store > av.avg_sales_for_all_stores