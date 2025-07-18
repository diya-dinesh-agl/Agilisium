SELECT LEFT(trans_date,7) as month,
country,COUNT(id) as trans_count,SUM(state = 'approved') as approved_count, 
SUM(amount) as trans_total_amount,
SUM((state='approved')*amount) AS approved_total_amount
FROM Transactions
group by month,country;
