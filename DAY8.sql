(SELECT u.name AS results FROM Users u
RIGHT JOIN MovieRating mr ON u.user_id = mr.user_id
GROUP BY u.name 
ORDER BY COUNT(mr.rating) DESC,u.name LIMIT 1)
UNION ALL
(SELECT m.title AS results FROM Movies m
LEFT JOIN MovieRating mr ON m.movie_id = mr.movie_id
WHERE MONTH(mr.created_at) = 02 AND YEAR(mr.created_at) = 2020
GROUP BY m.title
ORDER BY AVG(mr.rating) DESC, title ASC LIMIT 1);
