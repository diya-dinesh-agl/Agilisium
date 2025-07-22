SELECT ROUND(COUNT(DISTINCT IF(d=1,player_id,NULL)) / COUNT(DISTINCT player_id), 2) fraction
FROM (
  SELECT player_id, DATEDIFF(event_date, MIN(event_date) OVER(PARTITION BY player_id)) d
  FROM Activity
) a;
