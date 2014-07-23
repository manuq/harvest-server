SELECT SUM(spent_time), app_name
FROM gnome_launches
WHERE spent_time IS NOT NULL
GROUP BY app_name
ORDER BY SUM(spent_time) DESC
LIMIT 10;
