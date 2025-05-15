select e.name from Employee e
JOIN Employee em ON e.id = em.managerId
GROUP BY e.id HAVING COUNT(e.id)>=5;
