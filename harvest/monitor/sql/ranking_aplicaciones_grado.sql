SELECT SUM(spent_time), app_name
FROM (
  SELECT spent_time, app_name FROM tilo, gnome_launches
  WHERE tilo.grado = {{ grado }}
  AND tilo.serial_number LIKE gnome_launches.serial_number
) as gnome_launches_por_grado
WHERE spent_time IS NOT NULL
AND spent_time > 0
AND app_name not in ( select app_name from gnome_alias where enabled=0)
GROUP BY app_name
ORDER BY SUM(spent_time) DESC
LIMIT 10;
