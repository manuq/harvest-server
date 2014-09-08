SELECT COUNT(*), is_sugar 
FROM sessions 
WHERE spent_time > 0 and spent_time/60/60 < 24
GROUP BY is_sugar;
