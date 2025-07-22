select round(count(distinct if(d=1,player_id,null))/count(distinct player_id),2) fraction
from(
    select player_id,datediff(event_date,min(event_date) over(partition by player_id)) d
    from Activity
)a;
