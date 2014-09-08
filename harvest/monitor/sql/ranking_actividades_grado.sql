select duracion, IFNULL(activity_name, x.bundle_id) from (
SELECT SUM(spent_time) as duracion, bundle_id
FROM (
  SELECT spent_time, bundle_id FROM tilo, launches
  WHERE tilo.grado = {{ grado }}
  AND tilo.serial_number LIKE launches.serial_number
) launches_por_grado
WHERE spent_time IS NOT NULL
AND spent_time > 0 AND spent_time/60/60 < 24
GROUP BY bundle_id
ORDER BY SUM(spent_time) DESC
LIMIT 10
) x
LEFT JOIN (
SELECT bundle_id, activity_name FROM activities
) y
ON x.bundle_id = y.bundle_id;
