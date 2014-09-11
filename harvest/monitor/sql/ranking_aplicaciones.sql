SELECT SUM(spent_time), app_name
FROM gnome_launches
WHERE spent_time IS NOT NULL
AND spent_time > 0
AND app_name not in ( select app_name from gnome_alias where enabled=0)
GROUP BY app_name
ORDER BY SUM(spent_time) DESC
LIMIT 10;
